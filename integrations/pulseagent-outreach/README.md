# PulseAgent Outreach Integration

Connects browser-harness-pa scraped RFQ data to the PulseAgent managed SDR pipeline.

## Data flow

```
browser-harness-pa (scrape)
  → parsers/inquiry-multilang.{py,ts}  (normalize)
    → integrations/pulseagent-outreach  (route to CRM + reply drafting)
      → pulseagent.io managed outreach queue
```

## Files

| File | Purpose |
|------|---------|
| `outreach.py` | Main entry: POST normalized RFQ to PA pipeline API |
| `reply-templates/` | Jinja2/Handlebars templates per platform × language |
| `config.example.json` | Required env/config keys |

## Config keys

```
PA_API_KEY          — PulseAgent pipeline API key
PA_PIPELINE_ID      — target outreach pipeline UUID
PA_REPLY_LANG       — default reply language (en / zh / es / auto)
PA_DRY_RUN          — set "true" to preview without sending
```
