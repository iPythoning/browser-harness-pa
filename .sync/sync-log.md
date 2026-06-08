# browser-harness-pa sync log

## 2026-05-07T00:00:00Z — First-run initialization
- Upstream browser-use/browser-harness: **no stable releases / no git tags** (pyproject v0.1.0, no GitHub release published)
- Action: initialized .sync state, bootstrapped PA scaffold
- PA selectors: created (alibaba, mic, globalsources, linkedin)
- PA parsers: created (inquiry-multilang.py + .ts)
- PA integrations: created (pulseagent-outreach)
- Blog en: n/a (no release)
- Blog zh: n/a (no release)
- WeChat: n/a (queue empty)
- Next: monitor for first upstream stable tag → full workflow runs

## 2026-05-25T00:00:00Z — Weekly digest 2026-W22
- Commits: 7
- PRs merged: 5 (#314 QBO PDF export, #337 close_tab, #338 HubSpot webhooks, #380 stale skills cleanup, #381 Firecrawl removal)
- Top picks: close_tab() CDP helper, QBO blob PDF export, Firecrawl vendor-neutral cleanup, React-Select click strategy, domain-skills dir consolidation
- PA selectors: ok (no breaking changes; CDP blob export opportunity noted)
- Blog en: https://pulseagent.io/en/blog/browser-harness-weekly-digest-2026-w22
- Blog zh: https://pulseagent.io/en/blog/browser-harness-weekly-digest-2026-w22-zh
- WeChat: queued (API error: invalid appsecret 40125)

## 2026-05-29T00:00:00Z — Queue drain attempt (2026-W22, already digested)
- Week already digested: yes
- Drain attempt: 2026-W22 zh → POST /api/wechat/publish → 403 Forbidden
- WeChat: still queued (403 — check API key / WeChat OAuth token expiry)
- Action needed: verify pulseagent.io WeChat integration credentials

## 2026-06-01T00:00:00Z — Weekly digest 2026-W23
- Commits: 0
- PRs merged: 0
- Top picks: n/a
- PA selectors: ok (no upstream changes)
- Blog en: n/a
- Blog zh: n/a
- WeChat: queued (W22 still pending — API 403)
- Note: no upstream activity in browser-use/browser-harness since 2026-05-25

## 2026-06-08T14:30:00Z — Weekly digest 2026-W24
- Commits: 0 (last merged commit: 2026-05-20, PR #314 QBO report export skill)
- PRs merged: 0
- Closed PRs (no merge): #193 docs README refresh, #403 Brevo domain skill (withdrawn), #402 BH_NO_ACTIVATE switch_tab (withdrawn), #404 removed duplicate
- Open PRs in pipeline: #412 JPEG screenshot helper, #411 reddit voice docs, #410 Polish tax portal skill, #409 #407 testfol.io backtester, #406 Allow-dialog race docs, #405 SG grocery skills, #401 Robinhood MCP, #400 mermaid.live skill, #399 Chinese locale request, #398 Google Trends+Reddit fix
- Top picks: n/a (no merges)
- PA selectors: ok — no breaking upstream changes; fork stable
- Blog en: n/a
- Blog zh: n/a
- WeChat: W22 still queued — Cloudflare 1010 block (IP or token); W24 no-activity skip
- Note: upstream in review pause since 2026-05-20; community PRs accumulating (412+)
