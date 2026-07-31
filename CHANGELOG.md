# Changelog

All notable changes to this project will be documented in this file.

## [unreleased]

### <!-- 0 -->🚀 Features

- **ipc:** Split BH_RUNTIME_DIR (sock) from BH_TMP_DIR (logs/screenshots)
- **domain-skills:** Add browser-use-cloud (REST + cleanup-zombies)
- **domain-skills:** Add Vercel dashboard skill
- **domain-skills:** Add Vercel dashboard skill
- Add tasksquad.ai domain skills
- Add field-tested Flipkart shopping domain skill
- Discover Dia browser profile on macOS
- **helpers:** Add fill_input, wait_for_element, wait_for_network_idle
- Gate domain skills behind BH_DOMAIN_SKILLS env (default off)
- **_ipc:** BH_TMP_DIR overrides sock/port/pid/log + screenshot dir
- **doctor:** Show live browser connections and attached pages in run_doctor (#234)
- **helpers:** Add max_dim to capture_screenshot
- **domain-skills:** Add Substack scraping skill
- **cli:** Add --reload flag to restart the daemon (#200)
- **debug:** Add --debug-clicks mode with DPR-aware overlay (#189)
- Self-update CLI, release workflow, and fetch-use routing
- **domain-skills:** Add YouTube scraping skill
- **domain-skills:** Add facebook/ with groups and pages playbooks

### <!-- 1 -->🐛 Bug Fixes

- **ipc:** Set umask 0077 around AF_UNIX bind to avoid chmod TOCTOU
- **run:** Respect explicit CDP endpoint before cloud auto-bootstrap
- Verify daemon identity via IPC before signaling in restart_daemon
- **domain-skills/vercel:** Correct build log limit guidance
- **domain-skills/vercel:** Raise build log limit and document N lines guidance
- **daemon:** Fall back to DevToolsActivePort when BU_CDP_URL returns 404
- **daemon:** Add Brave Browser's Windows path to PROFILES discovery
- **fill_input:** Raise on missing element, add timeout param for SPA rendering
- Address copilot review — macOS Cmd+A, fixed visibility check, inflight tracking, stronger test
- Fix utf-8 encoding and document source_url in json schema

- write_text calls now pin encoding="utf-8" so non-ASCII transcripts
  don't depend on the locale default.
- share-export.md schema now lists source_url, matching what the script
  actually emits.
- **run:** Make cloud auto-bootstrap opt-in via BU_AUTOSPAWN
- **daemon:** Fall back to DevToolsActivePort ws path when /json/version 404s
- Auto-bootstrap cloud daemon on headless servers when BROWSER_USE_API_KEY is set
- Move shopify-admin skills to agent-workspace/domain-skills/
- **daemon:** Resolve WS via /json/version to avoid stale DevToolsActivePort path
- **daemon:** Report cdp_disconnected on stale CDP probe in connection_status
- **admin:** Catch SystemError raised by os.kill on Windows
- **_ipc:** Drop bu-<NAME> filename prefix when BH_TMP_DIR is set
- **_ipc:** Mkdir -p _TMP at module load so BH_TMP_DIR can point at a non-existent dir
- **_ipc:** Suppress empty python.exe console window on Windows daemon spawn
- **admin:** Route ensure_daemon CDP probe through ipc.connect (Windows)
- Prevent chrome://inspect tab flooding during setup (#232)
- **js:** Raise RuntimeError on JS evaluation errors instead of returning None (#230)
- **daemon:** Fire-and-forget mark-title eval so load events don't stall (#171)
- **deps:** Pin websockets==15.0.1 to unblock Chrome 147 CDP handshake
- Declare pillow dependency and use TemporaryDirectory in tests
- Remove contradictory body_html=null claims for paywalled posts
- **setup:** Retry Chrome handshake timeouts
- Disambiguate CDP handshake error between local Chrome and cloud remote
- **helpers:** Switch_tab accepts dict from current_tab()/list_tabs()
- **js:** Don't double-wrap IIFEs that contain return (#199)
- **js:** Auto-wrap top-level return expressions in an IIFE (#187)
- **run:** Exec scoping for comprehensions + sharpen click guidance (#133)
- **admin:** Ensure_daemon self-heals cold-start failures (#161)
- Don't flag updates when installed version is unknown
- **youtube/scraping:** Update stale age-restricted video docs
- **youtube/scraping:** Address code review findings
- Detect Chromium profiles on Linux
- **helpers:** New_tab(url) actually lands on url (#75)
- Fix tab indicator: re-enable Page + mark on session switch (#70)

The merged tab indicator only marked on Page.loadEventFired,
but Page events weren't enabled for new sessions created by
switch_tab(). Added Page.enable + immediate mark in set_session
handler so the 🟢 appears on every tab switch and survives
goto() navigation.

6/6 tests pass: new_tab, switch_tab, goto, click link,
cmd+click, switch back.

Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

### <!-- 10 -->📦 Miscellaneous

- Merge pull request #318 from browser-use/feat/runtime-dir-split

feat(ipc): split BH_RUNTIME_DIR (sock) from BH_TMP_DIR (logs/screenshots)
- Merge pull request #305 from hunnyboy1217/fix/current-tab-missing-target-id

current_tab: resolve attached target_id server-side via daemon meta
- Resolve attached target_id server-side via daemon meta
- Merge pull request #310 from browser-use/Alezander9-patch-2

Update VOUCHED.td
- Update VOUCHED.td
- Merge pull request #309 from browser-use/fix/ipc-socket-umask

fix(ipc): set umask 0077 around AF_UNIX bind to avoid chmod TOCTOU
- Merge pull request #308 from browser-use/Alezander9-patch-1

Update VOUCHED.td
- Update VOUCHED.td
- Merge pull request #263 from femto/add-chrome-canary-support

daemon: add Chrome Canary profile discovery
- Add Chrome Canary profile discovery on macOS and Windows
- Merge pull request #303 from song-swivel/song-swivel-patch-1

Undo #302
- Delete agent-workspace/domain-skills/mrm/analytics-reports.md

Remove
- Merge pull request #302 from song-swivel/domain-skill-freewheel-mrm

Add FreeWheel MRM analytics report skill
- Add FreeWheel MRM analytics report skill
- Merge pull request #301 from ComBba/feat/domain-skills-browser-use-cloud

feat(domain-skills): add browser-use-cloud (REST + cleanup-zombies)
- Also catch URLError so transient network failures don't abort the loop
- Merge pull request #300 from ComBba/fix/run-respect-explicit-cdp-endpoint

fix(run): respect explicit CDP endpoint before cloud auto-bootstrap
- Merge pull request #296 from browser-use/fix/switch-tab-enable-all-domains

fix(daemon): set_session must enable all four default domains, not just Page
- Run disable+enables in parallel; background cosmetic title prefix
- Filter by session_id; set_session: disable old Network
- Enable Page/DOM/Runtime/Network (parity with initial attach)
- Merge pull request #294 from browser-use/fix/restart-daemon-pid-reuse-safety

fix: verify daemon identity via IPC before signaling in restart_daemon
- Implement Windows path via GetProcessTimes
- Restore force-kill via process-start-time fingerprint + cap PID upper bound

Two more codex findings on ad39a95, both real:

1. _ipc.identify() accepted any positive int as pid, including values
   too large for C pid_t (typically signed 32-bit). os.kill(huge_pid, 0)
   then raises OverflowError, which propagates out of restart_daemon()
   before its cleanup runs. Bounded the accepted range to 0 < pid <
   2**31. Linux pid_max is also <2**22 in practice. Defense-in-depth:
   added OverflowError to the except lists wrapping the os.kill calls
   in restart_daemon, in case a different code path ever feeds it a
   too-large pid.

2. The daemon's serve() tears down the IPC socket BEFORE the daemon
   process actually exits — the daemon then runs slow cleanup work
   (notably stop_remote()'s 15s-timeout PATCH to api.browser-use.com
   to release a cloud browser). During that window identify() returns
   None even though the process is still our daemon, so the strict
   identify-only re-verification skipped SIGTERM and let the orphan
   keep running. The next bh invocation would then spawn a new daemon
   competing with the old one for the same Chrome.

   Fix: snapshot a process-start-time fingerprint at the top of
   restart_daemon, and accept it as a secondary identity signal in
   the SIGTERM gate. Two reads returning the same fingerprint means
   the PID still refers to the same process; a different fingerprint
   means PID reuse, in which case SIGTERM is skipped (preserving the
   protection from cubic's earlier finding). Implementation uses
   /proc/<pid>/stat field 22 on Linux and ps -o lstart= on macOS;
   on Windows / unsupported platforms the helper returns None and
   restart_daemon falls back to the strict identify-only check.

Tests in tests/unit/test_admin.py and tests/unit/test_ipc.py:
- restart_daemon SIGTERMs via start-time match when socket is gone
  (slow-shutdown recovery)
- restart_daemon skips SIGTERM when start-time has changed (PID
  reuse during the wait window)
- _process_start_time returns a stable fingerprint for the current
  process and None for invalid pids (None/0/negatives/non-int/dead)
- identify rejects oversized ints (covered via the bounded check)

Full suite: 75 passed.
- Harden ping/identify against non-positive pids and non-dict payloads

Two additional codex findings on 6d412c9:

1. _ipc.identify() accepted any int as pid, including 0 and negatives.
   On POSIX, os.kill(0, sig) signals every process in the calling
   process group, and os.kill(-1, sig) signals every process the
   caller can. A hostile or buggy daemon replying {pid: 0} or
   {pid: -1} would have turned restart_daemon() into a process-group
   kill. Restrict to pid > 0.

2. _ipc.ping() still did resp.get('pong') without a type check, so a
   list/scalar/null reply would raise AttributeError. The previous
   commit added that guard to identify() but left ping() bare. With
   the new daemon_alive fallback in restart_daemon() that now calls
   ping(), an unhandled raise here would abort restart before
   cleanup ran. Mirrored the identify() guards: isinstance(resp, dict)
   plus AttributeError in the except.

Tests in tests/unit/test_ipc.py now also cover:
- identify() rejects pid=0, pid=-1, pid=-42, pid=-99999
- ping() returns False for non-dict payloads (list/str/int/None)
- ping() requires pong is exactly True (rejects truthy non-True values)

Full suite: 71 passed.
- Identify(): reject bool pid and non-dict ping payloads

Two related cubic/codex findings on _ipc.identify():

1. isinstance(pid, int) accepts bool (since bool subclasses int in
   Python), so a hostile or buggy daemon replying {pid: True} would
   yield PID 1 and os.kill(1, SIGTERM) would target init on POSIX.
   Switched to type(pid) is int — strict same-type check, no subclass
   surprises.

2. request() returns whatever JSON the daemon sent, which can be a
   list, scalar, or None for a stale/hostile endpoint. resp.get(...)
   would then raise AttributeError, propagating out of identify() and
   crashing restart_daemon() before its cleanup runs. Added an
   isinstance(resp, dict) guard and AttributeError to the except.

Tests in new tests/unit/test_ipc.py cover both rejections plus the
happy path, the missing-pid path (pre-upgrade daemon), pong=False,
and several non-dict shapes (list, str, int, None). Full suite: 67
passed.
- Address cubic feedback: backward-compat ping fallback + re-verify before SIGTERM

Two issues raised on the initial commit:

1. Pre-upgrade daemons that don't include 'pid' in their ping reply made
   identify() return None, which short-circuited the entire shutdown
   path. The function would still delete the socket and pid file,
   orphaning the still-running daemon. Fix: keep daemon_pid (verified
   PID, used for signaling) separate from daemon_alive (any pong reply
   counts, falls back to ipc.ping for the alive check). Shutdown IPC
   is now sent whenever daemon_alive is true, regardless of whether
   we got a verifiable PID; SIGTERM still requires a verifiable PID.

2. A single identify() at the top didn't prevent PID reuse during
   the 15-second wait loop. If the daemon exited and the kernel
   reused its PID before the loop timed out, SIGTERM would land on
   the new owner. Fix: re-call identify() right before SIGTERM and
   only signal if it still returns the same PID we've been waiting
   on — any other state (None, different PID) means PID reuse is
   possible and we skip the kill.

Two new tests in tests/unit/test_admin.py lock in both:
- test_restart_daemon_sends_shutdown_to_pre_upgrade_daemon_without_pid_in_ping
- test_restart_daemon_skips_sigterm_if_pid_was_reused_during_wait

Existing tests updated to also stub ipc.ping. Full suite: 61 passed.
- Merge pull request #288 from teedonk/domain-skill/vercel

feat(domain-skills): add Vercel dashboard skill
- Merge pull request #292 from claytonlin1110/fix/bu-cdp-url-json-404-devtools-fallback

fix(daemon): fall back to DevToolsActivePort when BU_CDP_URL returns 404
- Bracket IPv6 hosts when building ws:// URL
- Merge pull request #281 from xajik/domain-skills/tasksquad.ai

feat: add tasksquad.ai domain skills
- Tasksquad domain skill: rename dir, replace fictional helper, fix compose snippet

- Move from top-level domain-skills/tasksquad.ai/ to the canonical
  agent-workspace/domain-skills/tasksquad-ai/ location, switching to
  kebab-case to match sibling dirs (booking-com, dev-to, archive-org).
- Replace find_text_coords(...) with self-contained inline Python
  helpers (_coords_by_text, _coords_by_selector) that wrap querySelector
  + getBoundingClientRect. find_text_coords does not exist in the
  harness or agent_helpers — every call site was a NameError waiting to
  happen.
- Fix the compose-task snippet: drop the dead subject_input = js(...)
  line, focus the subject input via _coords_by_selector before typing,
  and add a placeholder click for the agent dropdown item.
- Fix the polling-interval contradiction: the inbox section now defers
  to the gotchas, and the gotchas list the Free (5s) / Pro (2s) cadence
  in one place.
- Merge pull request #282 from abhay-0055/twitter-skill

Add posting.md in the x.com domain skill
- X posting skill: rename dir, add null guards to selectors

- Move agent-workspace/domain-skills/x.com/ to .../x/ to match repo
  convention (siblings use bare platform names like 'tiktok' / 'youtube'
  or kebab-case like 'booking-com'; nothing else uses a literal dot in
  a dir name).
- Guard the compose-textarea and post-button querySelector lookups so
  the snippet raises a clear RuntimeError if the elements aren't there
  yet, instead of throwing a confusing JS TypeError on
  el.getBoundingClientRect().
- Add posting.md in the x.com domain skill
- Merge pull request #283 from stian-a-johansen/SJ/agentlist-domain-skill

Add AgentList domain skill
- Add AgentList domain skill
- Merge pull request #285 from browser-use/feat/animated-banner

Animate README banner with ink-bleed SVG reveal
- Animate banner with ink-bleed SVG reveal
- Merge pull request #284 from DanielKeith/fix/brave-windows-discovery-path

fix(daemon): add Brave Browser's Windows path to PROFILES discovery
- Merge pull request #280 from browser-use/docs/canonical-browser-connection

docs: standardize harness docs against canonical browser connection reference
- Remove old --setup flag now that install.md is the source of truth
- Full proofread of install.md, fix small formatting issues
- Update setup guide to be clear, precise and accurate
- Remove information now redundant with new connection info block
- Add canonical browser connection notes to install.mc
- Merge pull request #157 from bilaldaqqah/skill/aa-checkout

domain-skills/aa: full checkout flow
- Move aa skill under agent-workspace/domain-skills/

Match the canonical location used by all other domain-skills. The
top-level domain-skills/ tree is not picked up by the harness's skill
loader.
- Checkout — deep-link URL, Angular shadow DOM, PAN-gated CVV mount
- Merge pull request #168 from iskyiskyisky/domain-skills/amazon-cart-orders

domain-skills: amazon — cart.md, orders.md
- Amazon — cart.md, orders.md
- Merge pull request #158 from bilaldaqqah/skill/alaska-checkout

domain-skills/alaska: full checkout flow
- Move alaska skill under agent-workspace/domain-skills/

Match the canonical location used by all other domain-skills. The
top-level domain-skills/ tree is not picked up by the harness's skill
loader.
- Checkout — Auro Design System + CyberSource OOPIF
- Merge pull request #179 from muqsitnawaz/skill/manus-perplexity

domain-skills: manus + perplexity — task workflows
- Move manus + perplexity skills under agent-workspace/domain-skills/

Match the canonical location used by all other domain-skills. The
top-level domain-skills/ tree is not picked up by the harness's skill
loader.
- Handle trailing-slash URLs in perplexity id extraction
- Address cubic round-2 review
- Review feedback + SKILL.md compliance fixes
- Manus + perplexity — task workflows
- Merge pull request #233 from NandiniMurali/domain-skill/flipkart-shopping

feat: add field-tested Flipkart shopping domain skill
- Move flipkart skill under agent-workspace/domain-skills/

Match the canonical location used by all other domain-skills. The
top-level domain-skills/ tree is not picked up by the harness's skill
loader.
- Merge pull request #249 from teotoplak/add-bigbang-hr-skill

Add bigbang-hr domain skill (checkout flow)
- Seed window.dataLayer before patching push so the interceptor works pre-GTM

If an agent runs the interceptor snippet before GTM has initialized,
window.dataLayer is undefined and .push.bind throws. Seeding with [] is
safe — GTM picks up a pre-existing array on init.
- Add bigbang-hr domain skill for checkout flow

Agent-generated skill covering Big Bang (bigbang.hr) checkout:
Vue/Nuxt form filling quirks, jQuery UI location autocomplete,
GTM dataLayer event patterns, and payment step selectors.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
- Merge pull request #279 from progremir/add-dia-browser-discovery

feat: discover Dia browser profile on macOS
- Merge pull request #258 from wdeveloper16/feat/spa-form-helpers

fix(helpers): add fill_input, wait_for_element, wait_for_network_idle
- Dispatch select-all without char event so Cmd/Ctrl+A actually fires
- **visible=True:** Prefer checkVisibility, fall back to computed style
- Merge pull request #259 from zhanning68-stack/domain-skills/cn-hotels

domain-skills: add ly.com, ctrip, wehotel (Chinese hotel sites)
- Address cubic feedback on cn-hotels skills

- ly-com: read Vue ref via stable .value with _rawValue fallback
  rather than the brittle internal _rawValue path.
- wehotel: ancestor walk now identifies the hotel-name anchor by
  identity/innerText instead of an href-based negation against text
  (查看详情 lives on the link body, not in href), which previously
  let the loop stop on the detail anchor itself.
- ctrip: raise an explicit error when the destination input or 搜索
  button isn't found, instead of dereferencing None and crashing
  with a confusing TypeError.
- Add ly.com, ctrip, wehotel (Chinese hotel sites)
- Merge pull request #267 from jamster/domain-skills/claude-ai-share-export

domain-skills: add claude-ai/share-export
- Add claude-ai/share-export
- Merge pull request #268 from vedantggwp/domain-skills/articulate-rise-code-blocks

domain-skills: articulate-rise — code blocks
- Move articulate-rise skill under agent-workspace/domain-skills/

Match the canonical location used by all other domain-skills.
- Articulate-rise — code blocks
- Add bilibili navigation and structure skill (#270)
- Add BOSS直聘 (zhipin.com) navigation, job search, and chat skills (#271)
- Merge pull request #277 from browser-use/fix/respect-bu-cdp-ws

fix(run): make cloud auto-bootstrap opt-in via BU_AUTOSPAWN
- Merge pull request #276 from browser-use/feat/win-ipc-ping-token

harden Windows IPC: ping handshake, token auth, atomic port file
- Harden Windows IPC: ping handshake, token auth, atomic port file

Three improvements to the cross-platform IPC layer, lifted from #104:

- meta:'ping' handshake replaces bare TCP connect in daemon_alive() and already_running(). A connect-only check on Windows can succeed against an unrelated process that grabbed our ephemeral port after a daemon crash; the ping/pong response confirms the listener is actually our daemon.

- Per-daemon random token (secrets.token_hex(32)) gates every request on Windows. AF_UNIX + chmod 600 is the boundary on POSIX, but TCP loopback has no chmod-equivalent; without a token any local process could connect and issue CDP commands.

- Atomic .port write (write .port.tmp, os.replace) so a concurrent reader never sees a half-written file.

Adds rohitdutt108 to VOUCHED.td.

Co-authored-by: Rohit Dutt <rohit.dutt@iyc.ishafoundation.org>
- Merge pull request #275 from browser-use/docs/domain-skills-readme-section

docs: add concise Domain skills section to README
- Merge pull request #274 from browser-use/feat/opt-in-domain-skills

Gate domain skills behind BH_DOMAIN_SKILLS env (default off)
- Soften skill-toggle wording; drop redundant =0 test
- Merge pull request #273 from browser-use/docs/add-vouched

docs: add VOUCHED.td (vouch list)
- Add VOUCHED.td seeded with two recent contributors
- Merge pull request #272 from browser-use/docs/issue-templates

docs: add issue templates; route questions to Discussions
- Add issue templates and route questions to Discussions

bug-report.yml: 4 required fields plus a 4-box preflight (searched issues, ran --doctor, read install.md, this is a bug not a question/FR/cloud issue). feature-request.yml: 3 required fields plus a 2-box preflight. config.yml disables blank issues and links to Discussions Q&A and install.md.
- Merge pull request #269 from browser-use/docs/add-agents-md

docs: add AGENTS.md
- List agent-workspace contents; clarify SKILL.md scope
- Merge pull request #265 from molesza/fix/chrome147-default-profile-cdp-fallback

fix(daemon): fall back to DevToolsActivePort ws path when /json/version 404s
- Inline 404 fallback; drop saw_http_404 flag

Same behavior matrix: HTTPError 404 with a ws_path returns the file's ws URL immediately; 404 without ws_path or any other error keeps polling until the 30s deadline. Removes the flag, the break, the post-loop check, and shrinks the explanatory comment.
- Merge pull request #266 from shaunandrewjackson1977/fix/headless-cloud-auto-bootstrap

fix: auto-bootstrap cloud daemon on headless servers when BROWSER_USE_API_KEY is set
- Probe /json/version instead of bare TCP; trim redundant gate tests

Cubic flagged that the original socket.create_connection probe matches any process on 9222/9223, not just Chrome. Mirror daemon.py's fallback by hitting /json/version, so a stale or unrelated listener does not skip the cloud bootstrap.

Drop the three boolean-table tests that mocked every collaborator and re-asserted the literal if-condition. Add a focused test for _local_chrome_listening that covers the false-positive case directly.
- Merge pull request #261 from browser-use/fix/shopify-admin-skills-location

fix: move shopify-admin skills to agent-workspace/domain-skills/
- Merge pull request #260 from Alezander9/fix/stale-devtools-active-port

fix(daemon): ignore stale DevToolsActivePort path; resolve WS via /json/version
- Merge pull request #256 from browser-use/docs/install-profile-sync-c-flag

docs: replace remaining heredoc examples with -c flag
- Merge pull request #255 from browser-use/docs/readme-operator-framing-rebase

docs: lead README with first-buyer job (rebased from #170)
- Merge pull request #254 from browser-use/fix/connection-status-error-on-cdp-failure

fix(daemon): report error on stale CDP in connection_status
- Add Xiaohongshu scraping skill (web search, sorting, and note-opening) (#246)
- KB FAQs, embedded apps, Polaris inputs (#247)
- Fix remote browser cleanup when daemon startup fails (#251)

* Fix remote startup cleanup

* Fix cloud browser cleanup on startup interruption
- Merge pull request #245 from browser-use/add-comet-arc-profiles

daemon: discover DevToolsActivePort in Comet and Arc profiles on macOS
- Discover DevToolsActivePort in Comet and Arc profiles on macOS
- Merge pull request #241 from cryptoshrine/fix/windows-os-kill-systemerror

fix(admin): catch SystemError raised by os.kill on Windows
- Merge pull request #244 from browser-use/fix/bh-tmp-dir-short-filenames

fix(_ipc): drop bu-<NAME> filename prefix when BH_TMP_DIR is set
- Merge pull request #243 from browser-use/fix/ipc-tmp-dir-mkdir

fix(_ipc): mkdir -p _TMP at module load
- Merge pull request #242 from browser-use/claude/slack-session-sdKmR

Rename skill command from /browser-harness to /browser
- Rename skill command from /browser-harness to /browser

Shortens the invocation to a cleaner /browser command.

https://claude.ai/code/session_014BWe8AkViicHviYPP843t5
- Merge pull request #240 from browser-use/fix/ensure-daemon-windows-probe

fix(admin): route ensure_daemon CDP probe through ipc.connect (Windows)
- Merge pull request #225 from browser-use/fix/windows-ipc

Windows support: route IPC through ipc.py (TCP on Windows, AF_UNIX on POSIX)
- Use /tmp on POSIX to stay under AF_UNIX sun_path limit

tempfile.gettempdir() on macOS returns /var/folders/xx/yy.../T/ (~49 chars).
Combined with bu-{64-char-name}.sock that exceeds the 104-byte sun_path
limit on macOS (108 on Linux), causing daemon startup to fail.

Pre-PR upstream hardcoded /tmp; this restores that for POSIX. Windows is
unaffected (uses TCP, not AF_UNIX).
- Slim ipc.py and rename to _ipc.py to signal internal

Cut ipc.py from 127 to 68 lines (-46%) by removing restated docstrings and
keeping only load-bearing inline comments (path-traversal guard, uv-Python
AF_UNIX gating, Windows .port-file role). Same logic, same call sites.

Rename ipc -> _ipc per Python convention for internal modules. The IPC
plumbing is only called by daemon/admin/helpers; agents reading helpers.py
should not be pulled into transport details. Callers do 'import _ipc as ipc'
so internal ipc.foo references stay unchanged.
- Merge remote-tracking branch 'origin/main' into fix/windows-ipc

# Conflicts:
#	SKILL.md
#	admin.py
#	helpers.py
- Address PR review (cubic): docs, serve-task crash detection, name sanitization

- daemon.py:1, SKILL.md:151 — docstring/diagram said named pipe on Windows;
  the implementation is TCP loopback. Updated.
- daemon.py:209 — if ipc.serve() crashes (e.g. bind failure), the prior
  shutdown path could miss it and leave the daemon waiting forever on
  d.stop without a listening endpoint. Now race serve_task and stop.wait()
  via asyncio.wait(FIRST_COMPLETED): if serve finishes first it must have
  raised, so await it to surface the exception. Cleanup cancels both tasks
  unconditionally.
- ipc.py:45 — BU_NAME flowed straight into f-strings building filesystem
  paths, allowing path traversal outside tempdir. Validate via
  ^[A-Za-z0-9_-]{1,64}$ in a single _check() helper that all path
  builders (log_path/pid_path/port_path/_sock_path) call. Bad names raise
  ValueError early with a clear message.
- Windows support: route IPC through ipc.py (TCP on Windows, AF_UNIX on POSIX)

The harness was Linux/macOS-only because daemon IPC hardcoded AF_UNIX sockets
at /tmp/bu-*.sock paths and asyncio.start_unix_server, all of which are
unavailable or invalid on Windows. Worse, uv-managed Python on Windows
(python-build-standalone) ships without socket.AF_UNIX entirely (#124).

New ipc.py centralizes the platform fork:
  - POSIX: AF_UNIX socket at <tempdir>/bu-<NAME>.sock (chmod 0600), unchanged
    semantics from the prior /tmp-hardcoded path.
  - Windows: TCP loopback on 127.0.0.1:<ephemeral>, with the chosen port
    written to <tempdir>/bu-<NAME>.port so clients can find the daemon.
    Uses asyncio.start_server (stdlib, no obscure APIs, no third-party deps).

Path discipline: log/pid/port files all sit under tempfile.gettempdir() so
they land in /tmp on Linux, $TMPDIR on macOS, %TEMP% on Windows. helpers.py
screenshot() default also moves from /tmp/shot.png to tempfile.gettempdir().

subprocess detach uses start_new_session=True on POSIX and
DETACHED_PROCESS|CREATE_NEW_PROCESS_GROUP on Windows via ipc.spawn_kwargs().

run.py reconfigures stdout to UTF-8 on Windows so print(page_info()) doesn't
UnicodeEncodeError on the 🟢 marker that helpers prepend to tab titles
(#124 item 4). cp1252 (PowerShell default) can't encode it.

Verified end-to-end on Windows 11 with Chrome remote debugging:
  - daemon spawns, allocates port, writes .port file
  - goto + page_info + screenshot round-trip through TCP loopback
  - restart_daemon cleans up .port and .pid

POSIX path is logically equivalent to the prior code (same AF_UNIX call,
same socket-file semantics, same chmod 0600), routed through ipc.py.

Closes #124 items 1, 2, 4. Item 3 (Chrome 147 user-data-dir) is a separate
concern not addressed here.
- Merge pull request #221 from browser-use/feat/screenshot-max-dim

feat(helpers): add max_dim to capture_screenshot
- Merge branch 'main' into feat/screenshot-max-dim
- Merge pull request #209 from everlastconsulting/loom-folder-enumeration

domain-skills/loom: library folder enumeration
- Library folder enumeration
- Merge pull request #214 from samtucker/add-bu-cdp-url

daemon: add BU_CDP_URL for HTTP DevTools endpoint resolution
- Add BU_CDP_URL for HTTP DevTools endpoint resolution
- Merge pull request #173 from drichman1-maker/fix/macos-brave-and-port-fallback

Add macOS Brave profile path + port-9222/9223 CDP probe fallback
- Add macOS Brave profile path + port-9222/9223 CDP probe fallback

Two small fixes in daemon.py for macOS users running Brave (or any
Chromium variant launched with --remote-debugging-port):

1. PROFILES list was missing the macOS path for Brave
   (~/Library/Application Support/BraveSoftware/Brave-Browser).
   The Linux Flatpak path was the only Brave entry, so macOS Brave
   users got "DevToolsActivePort not found" even after enabling
   remote debugging.

2. When Chromium is launched with an explicit --remote-debugging-port
   flag, the DevToolsActivePort file is not always written to the
   profile dir. CDP is fully live, but get_ws_url() can't find it.
   Added a final fallback that probes 127.0.0.1:9222 and :9223 via
   /json/version and uses the returned webSocketDebuggerUrl. The
   loop is gated to the standard debugging ports and only runs after
   the existing profile-dir scan fails, so it doesn't interfere with
   the normal sticky-checkbox flow.

Both changes are additive — no existing behavior is altered.
- Merge pull request #211 from hobostay/fix/missing-c-argument-validation

Fix IndexError when -c flag is passed without code argument
- Fix IndexError when -c flag is passed without code argument

Running `browser-harness -c` without a code argument crashed with an
unhandled IndexError at `exec(args[1])`. Added a length check to
produce a proper usage message instead.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
- Merge pull request #172 from mvanhorn/fix/106-websockets-pin-chrome-147

fix(deps): pin websockets==15.0.1 to unblock Chrome 147 CDP handshake
- Merge pull request #217 from sontianye/feat/substack-domain-skill

feat(domain-skills): add Substack scraping skill
- Merge pull request #218 from NandiniMurali/domain-skill/expedia

Add Expedia domain skill: hotel search automation
- Add Expedia domain skill: hotel search automation

Covers URL-based search (dates, destination, travellers), traveller widget
JS interaction, child age dropdowns, and price filter usage. Documents that
the date picker is unreliable with coordinate clicks and should be bypassed
via URL parameters.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
- Merge pull request #204 from browser-use/fix/chrome-handshake-timeout

fix(setup): retry Chrome handshake timeouts
- Merge pull request #121 from mvanhorn/fix/108-cdp-handshake-error-message

fix: disambiguate CDP handshake error between local Chrome and cloud remote
- Merge pull request #176 from iskyiskyisky/domain-skills/gmail-compose

domain-skills: gmail — compose.md
- Gmail — compose.md
- Merge pull request #202 from anandvc/fix/switch-tab-accept-dict

fix(helpers): switch_tab accepts dict from current_tab()/list_tabs()
- Merge pull request #197 from YiannisDermitzakis/youtube/watch-page-hydration-note

docs(youtube): document watch-page DOM hydration wait
- Merge pull request #184 from b00833647-cmd/feat/imdb-domain-skill

domain-skills/imdb: charts, search, and More Like This
- Charts, search, and More Like This
- Merge pull request #194 from ambeidetic/domain-skills/polymarket

domain-skills: add Polymarket scraping skill
- Add Polymarket scraping skill
- Merge pull request #190 from browser-use/cursor/update-readme-footer-links-19e8

Update README footer Bitter Lesson and Skills links
- Update README bitter lesson and skills footer links

Co-authored-by: Luka Secilmis <lukasec@users.noreply.github.com>
- Merge pull request #178 from browser-use/refactor/remove-playwright-name-overlap

refactor: rename goto/click/screenshot to avoid Playwright name overlap
- Merge pull request #177 from browser-use/docs/remove-bold-formatting

docs(SKILL.md): remove bold formatting
- Linkedin — invitation-manager.md (#149)
- Merge pull request #131 from browser-use/feat/versioning-and-fetch-use

feat: self-update CLI and fetch-use routing
- Merge pull request #137 from sontianye/feat/youtube-domain-skill

feat(domain-skills): add YouTube scraping skill
- Merge pull request #138 from browser-use/readme-free-remote-stealth

readme: name stealth, proxies, and captcha solving in free remote browsers
- Name stealth, proxies, and captcha solving in free remote browsers
- Merge pull request #141 from opensesamenext1-netizen/fix/flatpak-browser-profiles

Support Flatpak browser profile paths
- Support Flatpak browser profile paths
- Merge pull request #130 from robertguss/add-reddit-and-medium-hydration-skills

domain-skills: reddit + medium article hydration
- Article body via DOM (logged-in fallback)
- Reddit — shreddit-* DOM extraction and JSON API
- Merge pull request #116 from johnmarktaylor91/docs/centilebrain-domain-skill

docs(skill): centilebrain — generate normative z-scores
- Merge pull request #103 from forrest-motz/docs/github-form-actions

domain-skills/github: repo actions (star, watch) via form.submit()
- Repo actions (star, watch) via form.submit()
- Merge pull request #101 from harrisboatworks/feat/facebook-domain-skill

domain-skills: add facebook/ (groups + pages)
- Merge pull request #99 from trwpang/narrow/trello-boards-and-lists-589ffe

trello: boards-and-lists
- Boards-and-lists (via narrow)
- Merge pull request #105 from SybrenGL/fix/linux-chromium-devtoolsactiveport

fix: detect Chromium profiles on Linux
- Framer — web editor (#98)
- Explain why stop_remote_daemon calls restart_daemon (#97)
- Stop_remote_daemon helper, skill updates from sub-agent testing (#96)
- Atlas — my.recruitwithatlas.com (#94)
- Paginate list_cloud_profiles; expose profile-use v1.0.4 sync flags (#93)
- Python API for remote browsers, profiles, and local-profile sync (#84)
- Merge pull request #92 from browser-use/pin-deps

pyproject: pin dependencies and commit uv.lock
- Pin direct dependencies to exact versions
- Merge pull request #86 from browser-use/feat/domain-skills-batch18

Add domain skills: World Bank, REST Countries, NASA, Wayback Machine, arXiv bulk
- Add batch 18 domain skills: World Bank, REST Countries, NASA, Wayback Machine, arXiv bulk
- Merge pull request #73 from browser-use/feat/domain-skills-batch11

Add domain skills: PubMed, CrossRef, OpenAlex, FRED, MusicBrainz
- Add browser-harness validated domain skills for batch 11

PubMed/NCBI (ESearch→ESummary/EFetch pipeline; count is string; ELink broken 2026; CollectiveName branch),
CrossRef (title/container-title always lists; abstract has JATS XML tags; type=proceedings-article not conference-paper),
OpenAlex (abstract_inverted_index reconstruction; cursor >10K pages; group_by not group-by; concepts deprecated use topics),
FRED (fredgraph.csv timeouts headlessly; API needs free key; BLS/WorldBank/AlphaVantage as keyless alternatives),
MusicBrainz (Mozilla/5.0 gets 403; recording length in ms; CAA front flag vs types array differ).
- Surface remote browser liveUrl and tell agents to share it (#83)
- Make PATH invocation and new_tab-at-session-start unmissable (#77)
- Error-driven decision tree, drop unconditional chrome://inspect (#74)
- Merge pull request #71 from browser-use/readme-contributing-section

readme: add contributing section inviting domain-skill PRs
- Add contributing section inviting domain-skill PRs
- Merge pull request #47 from browser-use/feat/domain-skills-batch3

Add domain skills: ArXiv, Craigslist, Stack Overflow, npm/PyPI, Zillow
- Add browser-harness validated domain skills for batch 3

ArXiv (comma-separated id_list), Craigslist (cl-static-search-result),
Stack Overflow API (filter=withbody), npm/PyPI registries, Zillow
(NEXT_DATA extraction + Redfin fallback).
- Merge pull request #49 from browser-use/feat/domain-skills-batch4

Add domain skills: Booking.com, Eventbrite, Etsy, eBay, CoinGecko
- Add Booking.com domain skill (AWS WAF; sitemap + GraphQL schema + browser CDP)
- Add browser-harness validated domain skills for batch 4 (partial)

Eventbrite (JSON-LD ItemList, __NEXT_DATA__ for detail; public API needs auth),
Etsy (DataDome blocks http_get; browser CDP + official API v3 with free key),
CoinGecko (free API, sleep 5s between calls; /coins/list for IDs not symbols),
eBay (http_get works until rate limit; JSON-LD Product schema on detail pages).
- Add green dot indicator for agent-controlled tab (#69)

* try WS handshake once, not 12 times

Each retry created a new CDPClient which opened a new WebSocket
connection, triggering Chrome's "Allow debugging" dialog again.
12 retries = 12 stacked popups the user has to dismiss.

Now tries once. If it fails, tells the user to click Allow and
retry — no popup spam.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* add tab title indicator for agent-controlled tab

Prepends 🟢 to the page title on switch_tab() so the user can
see which tab the agent controls. Unmarks the previous tab first
so only one tab is marked at a time.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

---------

Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
- Add Microsoft Edge support (#63)

* Add Microsoft Edge support

Edge is Chromium, so the daemon's CDP bootstrap works unchanged once it
knows where Edge's DevToolsActivePort lives. This adds the macOS, Linux,
and Windows Edge profile paths to the discovery list, plus a one-line
note in install.md clarifying that `chrome://inspect/#remote-debugging`
and the rest of the setup flow apply to Edge too.

* Edge Beta/Dev/Canary, drop Edge from main README

Cover the non-stable Edge channels on macOS, Linux, and Windows so
users on insider builds don't fall through to 'DevToolsActivePort not
found'. Edge SxS (Side-by-Side) is Canary's install dir on Windows.

Keep README's Chrome-only pitch; Edge stays documented in install.md
where setup details belong.

* install.md: move Edge note to bottom, one line

Top-of-section carve-out distracts from the Chrome bootstrap steps.
A one-liner in the cold-start reminders is enough for users who need it.

---------

Co-authored-by: MagMueller <mamagnus00@gmail.com>
- Create LICENSE (#68)
- Try WS handshake once, not 12 times (#67)

Each retry created a new CDPClient which opened a new WebSocket
connection, triggering Chrome's "Allow debugging" dialog again.
12 retries = 12 stacked popups the user has to dismiss.

Now tries once. If it fails, tells the user to click Allow and
retry — no popup spam.

Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
- Add 5s timeout on domain enable calls, add nuclear recovery gotcha (#66)

daemon.py: Page/DOM/Runtime/Network.enable calls now have a 5s
timeout. Previously they could hang indefinitely on heavy pages
(TikTok FYP), preventing the daemon from reaching its socket
listener.

SKILL.md: added one gotcha for when restart_daemon() itself hangs
(kill Chrome entirely and reconnect).

Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
- Surface pending native dialog (#65)
- Update section title from 'Remote browsers' to 'Free remote browsers' (#64)
- Merge pull request #50 from browser-use/feat/domain-skills-batch5

Add domain skills: SEC EDGAR, Coursera, Goodreads, DuckDuckGo, TrustPilot
- Add Goodreads domain skill (http_get works; __NEXT_DATA__ Apollo state + JSON-LD)
- Add browser-harness validated domain skills for batch 5 (partial)

Coursera (public API no auth, q=search is POST-only/405 on GET),
DuckDuckGo (Instant Answer API, skip_disambig=1 essential, widget answers unusable),
SEC EDGAR (company UA required for www.sec.gov; 10 req/s; XBRL frames for cross-company),
TrustPilot (http_get works; __NEXT_DATA__ has reviews; 10-page cap per filter).
- Merge pull request #55 from browser-use/feat/domain-skills-batch10

Add domain skills: Wellfound, G2, Capterra, TradingView, Macrotrends
- Add browser-harness validated domain skills for batch 10

Wellfound (DataDome + Cloudflare dual stack; browser CDP resolves silently; Rails not Next.js),
G2 (DataDome blocks all http_get; browser CDP; schema.org microdata stable; data.g2.com API needs vendor key),
Capterra (ClaudeBot UA returns Markdown not HTML; Chrome UA gets Cloudflare 403),
TradingView (scanner.tradingview.com POST open; symbol-search needs Origin header; data.tradingview.com dead),
Macrotrends (iframe PHP endpoints bypass main page; stock OHLCV direct; Referer required for economic API).
- Add browser-harness validated domain skills for batch 9

CoinMarketCap (internal data-api/v3 fully open, no auth; 25 calls no rate limit),
Quora (full Chrome UA required; push() payloads double-encoded JSON; 3 SSR answers only),
Itch.io (http_get works; game cards via CSS selectors; RSS feeds exist),
Steam (appdetails single appid only; price in cents; ISteamApps/GetAppList dead in 2026),
HowLongToBeat (two-step token flow /api/find/init then POST; comp_* in seconds not hours).
- Add browser-harness validated domain skills for batch 8

Letterboxd (http_get works on film pages; JSON-LD CDATA gotcha; API needs OAuth),
Gutenberg (Gutendex REST API; text via /cache/epub/; .opf is 404, use .rdf),
Metacritic (internal backend API key in HTML; Nuxt __NUXT_DATA__ not __NEXT_DATA__),
RAWG (API needs key; window.CLIENT_PARAMS in HTML has full game data without key),
OpenLibrary (full free API; missing cover = 43-byte GIF not 404; description dual type).
- Add browser-harness validated domain skills for batch 7

Glassdoor (Cloudflare managed challenge; browser only; __NEXT_DATA__ + DOM fallbacks),
Medium (?format=json strips XSSI prefix; GraphQL /_/graphql no auth; RSS 10-item cap),
SoundCloud (oEmbed no-auth; __sc_hydration apiClient.id as client_id; API v2 with pagination),
Genius (OS token in UA bypasses 403; internal /api/songs no auth; strip first lyrics div header),
Dev.to (public REST API; burst limit 6 req then 429/1s; listings empty without auth).
- Add browser-harness validated domain skills for batch 6

Walmart (http_get works; bare Mozilla/5.0 UA bypasses PerimeterX; __NEXT_DATA__ via id= regex not type=),
Spotify (oEmbed no-auth; embed __NEXT_DATA__ has full trackList; anonymous token burns 22h Retry-After),
Weather (wttr.in format=j1; Open-Meteo current+hourly+daily; NWS two-call flow),
OpenStreetMap (Nominatim lat/lon are strings; Overpass bbox order differs from Nominatim; POST required),
Archive.org (Wayback availability API degraded; CDX sort=closest reliable; /search?output=json returns HTML).
- Merge pull request #62 from browser-use/readme-free-remote-browser

readme: promote free remote browser tier
- Promote free remote browser tier
- Reframe post-task ritual as "Always contribute back" (#61)
- [codex] Clarify README code size section (#56)

* Clarify README code size section

* Rename README setup heading
- Fix daemon attaching to invisible omnibox popup (#60)

* fix daemon attaching to invisible omnibox popup on fresh Chrome

When Chrome opens fresh, the only page targets are chrome://
internal pages and the omnibox popup (1px invisible viewport).
The daemon's attach_first_page() fell back to the popup, making
all subsequent work invisible to the user.

Fix: when no real pages exist, create an about:blank tab via
Target.createTarget instead of attaching to the omnibox popup.

Tested configurations:
- Fresh start with no real tabs → creates about:blank (1112x817)
- Navigate without AppleScript → works, tab visible
- Recovery from stale socket → auto-reconnects
- Chrome restart from scratch → creates about:blank

Also adds interaction-skills/connection.md documenting the
omnibox popup problem and startup sequence.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* add connection skill reference to main SKILL.md

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

---------

Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
- Remove extra spacing (#59)
- Better readme (#58)
- Merge pull request #46 from browser-use/feat/domain-skills-validated

Replace drafted skills with browser-harness validated versions
- Replace drafted skills with browser-harness validated versions

Ran actual browser-harness sessions against each site and rewrote
the skill files from live test findings. Key corrections:

GitHub: wait(2) after wait_for_load() for React hydration; search API
  separate 10 req/min limit; search/code needs auth (401 unauthed)

HackerNews: athing also matches comment rows (use 'athing submission');
  job posts break naive score-zip; html.unescape() required for titles

Amazon: .zg-item-immersion gone from Best Sellers; #priceblock_ourprice
  returns null (legacy); review count selector collides with cross-sell
  widget — use [aria-label*='ratings'] instead

News: The Verge is Atom not RSS (namespace dict required); Reuters
  hard-blocks http_get with 403 even with User-Agent; BBC shows no
  consent banner from US IP; parallel fetch is 4.3x faster (0.16s vs 0.70s)

ProductHunt: goto() ERR_ABORTED — always use new_tab(); /posts/ URLs
  don't exist (it's /products/); homepage has 30 fixed items no lazy load;
  [data-test^='post-item-'] is the correct card selector
- Add more spacing between README sections (#44)
- Merge pull request #43 from browser-use/feat/domain-skills-batch1

Add domain skills: GitHub, HN, Product Hunt, Amazon, News, Job Boards
- Add domain skills for 6 public, no-login-required sites

- github/scraping.md: GitHub API + trending page patterns, rate limiting
- hackernews/scraping.md: http_get + Algolia API for search/filtering
- producthunt/scraping.md: React SPA browser scraping + GraphQL token approach
- amazon/product-search.md: ASIN extraction, price parsing, CAPTCHA handling
- news-aggregation/multi-source.md: RSS-first approach, parallel fetch, consent banners
- job-boards/indeed-glassdoor.md: URL construction, job key extraction, salary normalization

All skills derived from real user task patterns. No credentials or sensitive data included.
- [codex] Add domain skill name helper (#42)

* Add domain skill name helper

* Inline domain skill lookup in goto
- [codex] Refine domain skill guidance (#41)

* Refine domain skill guidance

* Drop unintended skill regressions
- [codex] Document domain-skill PR ritual (#39)

* Document domain-skill PR ritual

* Tighten domain-skill PR wording

* Expand shared domain-skill guidance
- Add thetechgeeks domain-skill for Ubiquiti AU pricing (#40)

Captures three learnings from a real run that mis-reported $3,080 AUD for
a UACC-Rack-12U-Wall (real AU street ~$420-630): Tech Geeks is Shopify so
use /products/<handle>.js for canonical price and SKU; its .js `available`
flag is unreliable so cross-check the DOM for sold-out markers; and
sold-out pages there carry stale/junk prices that must never enter a
final table without a second-source sanity check.

Co-authored-by: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
- Emphasize screenshots for verification and exploration (#38)
- Trim JS-heavy guidance from SKILL (#37)
- Remove default ensure_real_tab from docs (#36)
- [codex] Rename CLI to browser-harness run (#35)

* Rename CLI to browser-harness run

* Simplify browser-harness CLI
- Top-load browser harness usage guidance (#33)

* Top-load browser harness usage guidance

* Refine skill fast-start copy
- Print usage hint when bh is run on a TTY (#34)

A bare `bh` invocation blocks forever on sys.stdin.read(). Detect a TTY
stdin and exit with a one-line usage hint instead, so the failure mode
is obvious.

Co-authored-by: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
- Tighten install durability and restart guidance (#32)
- Refine README structure section (#31)
- [codex] Refresh remote debugging screenshot (#30)

* Trim README setup copy

* Refresh remote debugging screenshot
- Trim README setup copy (#29)
- Add remote debugging setup image (#28)
- Tighten install cold-start guidance (#27)
- Document daemon reuse during setup (#26)
- Simplify helper surface (#23)

* Simplify helper surface

* Trim common module and restore dispatch key
- Clean up install bootstrap flow (#25)
- Clarify Chrome remote debugging bootstrap (#22)
- Compress README setup prompt (#21)
- Split install and runtime docs (#20)

* Split install and runtime docs

* Refine install skill prompts
- Changed name
- Clarify Chrome profile setup flow (#18)

* Clarify Chrome profile setup flow

* Refine Chrome setup decision flow
- Tighten README setup prompt (#19)
- [codex] Make setup work from anywhere (#17)

* Make setup work from anywhere

* Rename launcher to bh

* Remove extra helper commands

* Document global skill setup
- Add spacing between README sections (#16)
- Defer README setup to skill (#15)
- Add global bu launcher and shared skill guidance (#14)
- Simplify skill setup flow (#12)
- Update README tagline (#13)
- Merge pull request #11 from browser-use/magnus/readme-how-it-works-lines

[codex] Clarify README title and how-it-works section
- Tighten README how-it-works bullets
- Tighten README line count wording
- Clarify README how-it-works section
- Merge pull request #10 from browser-use/magnus/rewrite-readme-for-humans

[codex] Rewrite README for human setup flow
- Reduce README to one example task
- Refine README setup and examples
- Refine setup prompt in README
- Tighten README to prompt-first flow
- Expand README: setup prompt, features, line counts

- rename "example prompt" → "setup prompt"; coding agent handles clone,
  uv sync, opens chrome://inspect on macOS, walks user through the
  allow-debugging checkbox, verifies connection, navigates to the repo,
  then offers the first task (star the repo)
- setup prompt explicitly tells the agent to read SKILL.md end-to-end first
- add Features section: raw CDP + editable helpers, Browser Use cloud
  for parallel sub-agents (each gets its own live URL), iframe/shadow
  passthrough, http_get bulk fallback
- how-it-works now shows line counts (~580 total) to show how small it is

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
- Rewrite README for human setup flow
- Merge pull request #9 from browser-use/magnus/remove-python-version-and-lock

[codex] Remove Python version and uv lock files
- Remove python version and uv lock
- Merge pull request #8 from browser-use/magnus/merge-skill-and-agents

[codex] Merge AGENTS guidance into SKILL
- Merge AGENTS into SKILL
- Merge pull request #7 from browser-use/magnus/interaction-skill-misc

[codex] Add misc interaction skill stubs
- Add misc interaction skill stubs
- Merge pull request #5 from browser-use/magnus/interaction-skill-scaffolds

[codex] Scaffold interaction skill notes
- Restore scaffold notes except uploads
- Tighten interaction skill scaffolds
- Scaffold interaction skill notes
- Merge pull request #4 from browser-use/magnus/tab-interaction-notes

[codex] Document tab control and visible ordering
- Trim AGENTS tab-order note
- Default list_tabs to include chrome pages
- Document tab control and visible ordering
- Merge pull request #3 from browser-use/skills-structure

Add interaction-skills and domain-skills structure
- Add interaction-skills and domain-skills structure

Two skill categories, pure markdown, no Python files:

- interaction-skills/ — generic browser patterns (dialogs, inputs, etc.)
  Flat .md files. Agent reads the relevant one before a task.

- domain-skills/ — per-site playbooks (tiktok/, linkedin/, etc.)
  Flat .md files per action (upload, schedule, post).
  Subfolders for large domains when needed.

Starting with:
- interaction-skills/dialogs.md — CDP vs JS dialog handling
- domain-skills/tiktok/upload.md — full upload flow with gotchas
- Placeholder folders for linkedin, spreadshirt, salesforce

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
- Add remote browser support (Browser Use cloud) + multi-daemon + rename to bu (#1)

* add remote browser support via Browser Use cloud + multi-daemon

HARNESLESS_NAME suffixes socket/pid/log — daemons are independent, no
supervisor. start_remote_daemon() creates a Browser Use cloud browser and
launches a daemon attached to it; kill_daemon() stops both. Local Chrome
path is unchanged.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

* rename env vars to BU_ prefix (shorter, less noisy in tool calls)

HARNESLESS_NAME → BU_NAME
HARNESLESS_CDP_WS → BU_CDP_WS
HARNESLESS_REMOTE_BROWSER_ID → BU_BROWSER_ID

Socket/pid/log files keep the harnesless- prefix on disk so they're
recognizable in /tmp. BROWSER_USE_API_KEY unchanged (external convention).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

* rename project from harnesless to bu

Socket/pid/log paths now /tmp/bu-<name>.{sock,pid,log}. pyproject package
name updated, uv.lock regenerated. Slash command now /bu.

Note: the repo directory itself is still named harnesless on disk. Rename
manually (mv harnesless bu) so the absolute paths in docs line up.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

---------

Co-authored-by: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
- Prune eval-specific helpers; keep primitives + document gotchas

Previous commit added fill_form / mui_select_first / is_success which are
eval-harness logic, not harnesless primitives (task-specific defaults like
"dumbledore"/"Harry Potter", MUI-only shim). Per AGENTS.md — "could the LLM
rewrite this from scratch after reading it once" — the LLM should pick field
values + the submit strategy per-task, not inherit eval defaults.

Removed: fill_form, _FILL_JS, mui_select_first, is_success (~100 lines)
Kept: dispatch_key, upload_file, capture_dialogs/dialogs (universal needs)

Insights from the eval captured as gotchas in SKILL.md instead:
- React controlled inputs need native-setter + input event
- Radios/checkboxes: el.click() over el.checked=true for React
- MUI / UI-library overlays: real CDP click, not JS .click()
- CDP char event ≠ DOM keypress for special keys → dispatch_key
- Same-origin iframes: contentDocument walk, not CDP targets
- Shadow DOM: querySelector doesn't pierce, walk .shadowRoot
- Form success signals vary: element / alert / body text

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
- Self-managing daemon + document post-task self-improvement ritual

Connection management (addresses "shit ton of daemons" problem):
- Socket is the lock. Daemon refuses to start if another is already
  listening (5-line check).
- PID file at /tmp/harnesless.pid written on start, removed on exit.
- ensure_daemon() / kill_daemon() / daemon_alive() helpers.
- run.py auto-calls ensure_daemon() before exec — users never manage
  the daemon manually.
- kill_daemon uses PID file (robust) instead of pkill pattern matching
  (was silently missing because the process command line didn't contain
  the "harnesless/" prefix).

Post-task ritual added to SKILL.md: after every browser task, extract
ONE generalizable friction point and make the simplest possible
improvement (2-line helper, one-line gotcha, recipe correction).
This is how the harness sharpens itself over time.

Verified end-to-end: kill_daemon → 0 processes + files cleaned → next
run.py → auto-starts exactly one daemon. Second `uv run daemon.py`
exits with "daemon already running" message instead of racing.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
- Handle stale sessions + add iframe support (Azure billing admin task)

Observed friction during an Azure portal task:
- Daemon's default session went stale (user closed the attached tab),
  which broke every subsequent call including browser-level Target.*.
- new_tab() had been removed in the previous simplification pass but
  was needed to recover.
- Azure portal renders blade panels in iframes; js() on the main page
  returned nothing for picker contents.

Changes:
- daemon: browser-level Target.* calls now bypass self.session entirely
  (so a stale session doesn't poison them). On "Session with given id
  not found" for session-scoped calls, clear + re-attach + retry once.
  Merged start() and the new recovery path into attach_first_page().
- helpers: add new_tab(); js() accepts target_id for iframe queries;
  iframe_target(substr) to find blade iframes; ensure_real_tab() now
  resilient to stale-session exceptions.
- SKILL.md: one-line note on iframe-site workflow.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
- Drop 14 unused helpers, compress daemon, tighten docs
- Initial commit: harnesless — LLM-first browser control via CDP

Three-process architecture: daemon.py holds one persistent CDP WebSocket
to the user's running Chrome (via chrome://inspect), short-lived run.py
processes talk to it over a Unix socket, helpers.py is the transparent
layer the LLM reads and edits at will.

Philosophy: no CLI, no fixed API surface. The LLM writes Python blocks
against ~13 tiny helpers (cdp, click, type_text, screenshot, get_dom,
etc.) and edits helpers.py on the fly when a pattern repeats. Coordinate
clicks default because they pass through iframes/shadow DOM/cross-origin
at the compositor level.

Uses cdp-use internally for send_raw only (ignores its 36k lines of
typed wrappers — raw CDP strings tokenize better than typed calls).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

### <!-- 3 -->🔧 Refactoring

- **js:** Proper return-statement parsing, unserializable value decoding, unified eval helpers (#231)
- Move to src layout, agent-workspace, and fix SKILL.md invocation format (#229)
- **tests:** Reorganize into tests/unit and tests/integration (#228)
- **run:** Replace heredoc stdin with -c flag (#188)
- Rename goto/click/screenshot to avoid Playwright name overlap

### <!-- 4 -->📝 Documentation

- Standardize harness docs against canonical browser connection reference
- Add concise Domain skills section to README
- Add AGENTS.md with repo orientation for coding agents
- Replace remaining heredoc examples with -c flag
- Lead README with first-buyer job
- **youtube:** Document watch-page DOM hydration wait
- Move setup/maintenance content from SKILL.md to install.md (#186)
- **SKILL.md:** Remove inline backticks; fix install.md goto_url rename (#185)
- **SKILL.md:** Remove bold formatting
- **skill:** Centilebrain -- generate normative z-scores
- Point onboarding fast-start at docs.browser-use.com (#118)
- Agent offers to star the repo as a demo, asks first (#95)

### <!-- 7 -->🏗️ Chores

- Remove release workflow
- **release:** Drop PyPI publish step


