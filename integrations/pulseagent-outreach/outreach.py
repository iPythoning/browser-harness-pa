"""
PulseAgent outreach integration — routes parsed RFQs to the PA managed SDR pipeline.
"""

from __future__ import annotations

import json
import os
import urllib.request
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from parsers.inquiry_multilang import ParsedRFQ


PA_API_BASE = os.getenv("PA_API_BASE", "https://pulseagent.io/api")
PA_API_KEY = os.getenv("PA_API_KEY", "")
PA_PIPELINE_ID = os.getenv("PA_PIPELINE_ID", "")
PA_DRY_RUN = os.getenv("PA_DRY_RUN", "false").lower() == "true"


def submit_rfq(rfq: "ParsedRFQ") -> dict:
    """Submit a parsed RFQ to the PulseAgent outreach pipeline."""
    payload = {
        "pipeline_id": PA_PIPELINE_ID,
        "source": rfq.source_platform,
        "buyer": {
            "name": rfq.buyer_name,
            "company": rfq.buyer_company,
            "country": rfq.buyer_country,
            "email": rfq.buyer_email,
        },
        "rfq": {
            "subject": rfq.raw_subject,
            "body": rfq.raw_body,
            "language": rfq.detected_language,
            "quantity": rfq.quantity,
            "delivery_terms": rfq.delivery_terms,
            "product_keywords": rfq.product_keywords,
            "summary": rfq.normalized_summary,
        },
    }

    if PA_DRY_RUN:
        print(f"[DRY RUN] Would submit: {json.dumps(payload, ensure_ascii=False)[:300]}")
        return {"dry_run": True, "payload": payload}

    body = json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(
        f"{PA_API_BASE}/pipeline/ingest",
        data=body,
        headers={
            "Authorization": f"Bearer {PA_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    resp = urllib.request.urlopen(req, timeout=30).read().decode()
    return json.loads(resp)
