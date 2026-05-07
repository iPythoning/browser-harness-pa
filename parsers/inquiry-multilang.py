"""
Multilanguage RFQ (Request for Quotation) parser for PulseAgent external-trade SDR.
Normalizes inquiry payloads from Alibaba, Made-in-China, and Global Sources into a
canonical RFQ schema regardless of source language.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional


CURRENCY_SYMBOLS = {"$": "USD", "€": "EUR", "£": "GBP", "¥": "CNY", "₹": "INR"}

QUANTITY_PATTERN = re.compile(
    r"(\d[\d,\.]*)\s*(pcs?|pieces?|units?|sets?|卡|套|件|个|台|箱|cbm|m³|kg|tons?|mt)",
    re.IGNORECASE,
)

LANGUAGE_HINTS = {
    "zh": ["询价", "采购", "报价", "数量", "规格", "最小起订", "交货期"],
    "es": ["cotización", "precio", "cantidad", "unidades", "proveedor"],
    "ar": ["عرض سعر", "كمية", "مورد", "طلب"],
    "pt": ["cotação", "fornecedor", "quantidade", "preço"],
    "ru": ["запрос", "цена", "количество", "поставщик"],
}


@dataclass
class ParsedRFQ:
    source_platform: str          # 'alibaba' | 'mic' | 'globalsources' | 'linkedin'
    raw_subject: str
    raw_body: str
    detected_language: str        # ISO-639-1 code or 'en'
    buyer_name: Optional[str] = None
    buyer_company: Optional[str] = None
    buyer_country: Optional[str] = None
    buyer_email: Optional[str] = None
    product_keywords: list[str] = field(default_factory=list)
    quantity: Optional[str] = None
    target_price: Optional[str] = None
    delivery_terms: Optional[str] = None  # FOB / CIF / EXW etc.
    normalized_summary: str = ""          # EN summary for CRM ingestion


def detect_language(text: str) -> str:
    for lang, hints in LANGUAGE_HINTS.items():
        if any(h in text for h in hints):
            return lang
    return "en"


def extract_quantity(text: str) -> Optional[str]:
    m = QUANTITY_PATTERN.search(text)
    return f"{m.group(1)} {m.group(2)}" if m else None


def extract_delivery_terms(text: str) -> Optional[str]:
    m = re.search(r"\b(FOB|CIF|EXW|DDP|FCA|CPT|CFR)\b", text, re.IGNORECASE)
    return m.group(0).upper() if m else None


def parse_rfq(
    platform: str,
    subject: str,
    body: str,
    buyer_name: Optional[str] = None,
    buyer_company: Optional[str] = None,
    buyer_country: Optional[str] = None,
    buyer_email: Optional[str] = None,
) -> ParsedRFQ:
    combined = f"{subject} {body}"
    lang = detect_language(combined)

    rfq = ParsedRFQ(
        source_platform=platform,
        raw_subject=subject,
        raw_body=body,
        detected_language=lang,
        buyer_name=buyer_name,
        buyer_company=buyer_company,
        buyer_country=buyer_country,
        buyer_email=buyer_email,
        quantity=extract_quantity(combined),
        delivery_terms=extract_delivery_terms(combined),
    )

    # Minimal product keyword extraction: nouns longer than 3 chars not in stop-words
    stop = {"for", "the", "and", "with", "from", "that", "this", "want", "need",
            "please", "send", "price", "quote", "about", "some", "have"}
    words = re.findall(r"[a-zA-Z]{4,}", combined.lower())
    rfq.product_keywords = list(dict.fromkeys(w for w in words if w not in stop))[:8]

    rfq.normalized_summary = (
        f"[{platform.upper()}] {buyer_country or 'Unknown'} buyer"
        + (f" ({buyer_company})" if buyer_company else "")
        + f" — qty: {rfq.quantity or 'n/a'}"
        + f", terms: {rfq.delivery_terms or 'n/a'}"
        + f", lang: {lang}"
        + f" | {subject[:120]}"
    )
    return rfq
