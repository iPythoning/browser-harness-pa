/**
 * Multilanguage RFQ parser — TypeScript counterpart to inquiry-multilang.py.
 * Used by the PA browser-harness integration layer when running in Node/Deno contexts.
 */

export type Platform = "alibaba" | "mic" | "globalsources" | "linkedin";

export interface ParsedRFQ {
  sourcePlatform: Platform;
  rawSubject: string;
  rawBody: string;
  detectedLanguage: string;
  buyerName?: string;
  buyerCompany?: string;
  buyerCountry?: string;
  buyerEmail?: string;
  productKeywords: string[];
  quantity?: string;
  deliveryTerms?: string;
  normalizedSummary: string;
}

const LANGUAGE_HINTS: Record<string, string[]> = {
  zh: ["询价", "采购", "报价", "数量", "规格", "最小起订", "交货期"],
  es: ["cotización", "precio", "cantidad", "unidades", "proveedor"],
  ar: ["عرض سعر", "كمية", "مورد", "طلب"],
  pt: ["cotação", "fornecedor", "quantidade", "preço"],
  ru: ["запрос", "цена", "количество", "поставщик"],
};

const QUANTITY_RE =
  /(\d[\d,.]*)\s*(pcs?|pieces?|units?|sets?|套|件|个|台|箱|cbm|m³|kg|tons?|mt)/i;
const DELIVERY_TERMS_RE = /\b(FOB|CIF|EXW|DDP|FCA|CPT|CFR)\b/i;

const STOP_WORDS = new Set([
  "for", "the", "and", "with", "from", "that", "this",
  "want", "need", "please", "send", "price", "quote", "about", "some", "have",
]);

function detectLanguage(text: string): string {
  for (const [lang, hints] of Object.entries(LANGUAGE_HINTS)) {
    if (hints.some((h) => text.includes(h))) return lang;
  }
  return "en";
}

function extractQuantity(text: string): string | undefined {
  const m = text.match(QUANTITY_RE);
  return m ? `${m[1]} ${m[2]}` : undefined;
}

function extractDeliveryTerms(text: string): string | undefined {
  const m = text.match(DELIVERY_TERMS_RE);
  return m ? m[0].toUpperCase() : undefined;
}

export function parseRFQ(params: {
  platform: Platform;
  subject: string;
  body: string;
  buyerName?: string;
  buyerCompany?: string;
  buyerCountry?: string;
  buyerEmail?: string;
}): ParsedRFQ {
  const { platform, subject, body, buyerName, buyerCompany, buyerCountry, buyerEmail } = params;
  const combined = `${subject} ${body}`;
  const lang = detectLanguage(combined);

  const words = (combined.toLowerCase().match(/[a-z]{4,}/g) ?? []);
  const productKeywords = [...new Set(words.filter((w) => !STOP_WORDS.has(w)))].slice(0, 8);

  const quantity = extractQuantity(combined);
  const deliveryTerms = extractDeliveryTerms(combined);

  const normalizedSummary =
    `[${platform.toUpperCase()}] ${buyerCountry ?? "Unknown"} buyer` +
    (buyerCompany ? ` (${buyerCompany})` : "") +
    ` — qty: ${quantity ?? "n/a"}, terms: ${deliveryTerms ?? "n/a"}, lang: ${lang}` +
    ` | ${subject.slice(0, 120)}`;

  return {
    sourcePlatform: platform,
    rawSubject: subject,
    rawBody: body,
    detectedLanguage: lang,
    buyerName,
    buyerCompany,
    buyerCountry,
    buyerEmail,
    productKeywords,
    quantity,
    deliveryTerms,
    normalizedSummary,
  };
}
