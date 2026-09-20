<div align="center">

# Sushant Poudel

**AI security engineer — I find where agent tool boundaries leak, then close them.**

Kathmandu, Nepal · [sushant.poudel2028@gmail.com](mailto:sushant.poudel2028@gmail.com) · [LinkedIn](https://linkedin.com/in/sushant-poudel2028) · [sushantpoudel2028.com.np](https://sushantpoudel2028.com.np) · **[Work with me →](https://sushant-me.github.io/hire/)**

[![claims: verified](https://github.com/sushant-me/reputation/actions/workflows/verify.yml/badge.svg)](https://github.com/sushant-me/reputation)
[![HackingHub #1](https://img.shields.io/badge/HackingHub-Q3%202026%20%231-0d6b5f?style=flat-square)](https://app.hackinghub.io/p/nofear976)

</div>

Every number on this page is re-checked against its public source once a week by
[**sushant-me/reputation**](https://github.com/sushant-me/reputation) — a repository that lists each
claim I make, names where it came from, and turns red the moment one stops being true. That badge is
the result of that check, not decoration.

---

## Receipts

| what | where it can be checked |
|---|---|
| **Rank #1, HackingHub Q3 2026** global leaderboard — 116 flags, 11,860 XP, 2 silver + 1 bronze award (next account: 97 flags) | [public leaderboard API](https://api.hackinghub.io/leaderboard) |
| **Security patch authored, merged, then generalised into `google/go-github`** — my [#4556](https://github.com/google/go-github/pull/4556) refused a release-asset upload whose URL pointed off-host; maintainer `gmlewis` replaced it the next day with the broader [#4564](https://github.com/google/go-github/pull/4564) — *"credentials are sent only to configured origins"* — which is what master implements today and which carries the commit *"Address feedback from sushant-me"* | [#4556](https://github.com/google/go-github/pull/4556) · [#4564](https://github.com/google/go-github/pull/4564) |
| **Five memory-safety issues in `google/s2geometry`** — a NULL dereference on the library's documented traversal path, an out-of-bounds read, a 16 GiB allocation from a 5-byte header, and a **2.4 GiB allocation reachable from a 28-byte input** | [#674](https://github.com/google/s2geometry/issues/674) · [#676](https://github.com/google/s2geometry/issues/676) · [#677](https://github.com/google/s2geometry/issues/677) · [#678](https://github.com/google/s2geometry/issues/678) · [#679](https://github.com/google/s2geometry/issues/679) |
| **Two hardening PRs under review** in `google/s2geometry`, split at the maintainer's request | [#681](https://github.com/google/s2geometry/pull/681) · [#682](https://github.com/google/s2geometry/pull/682) |
| **MCP tool shadowing** — framework-reserved tool names a server tool can occupy; fixes open against three of Google's agent frameworks | [adk-go #1606](https://github.com/google/adk-go/pull/1606) · [adk-java #1515](https://github.com/google/adk-java/pull/1515) · [adk-python #7145](https://github.com/google/adk-python/pull/7145) |
| **An OSS-Fuzz harness that was testing nothing** — `google/libphonenumber`'s as-you-type formatter asserted **0.00% line coverage** of the code it targeted; the corrected harness reaches **93%** | [PR #4079](https://github.com/google/libphonenumber/pull/4079) |
| **Two IEEE papers accepted** — *Edge-Native Semantic Firewall for Autonomous LLM Agents* (to be presented at NCIT, camera-ready in progress) and *PREBAS: Preemptive Bandwidth Scaling for WebRTC in LEO Satellite Networks* (2026 IEEE RTC, Chicago) | [paper, code and raw model outputs](https://github.com/sushant-me/Edge-Native_Semantic_Firewall_) |

---

## What I actually work on

**Agent safety you can measure.** An autonomous agent that *executes* actions sits outside
role-based access control, which authenticates an identity and says nothing about whether an action
should happen. My current paper asks whether a small, locally served model can be that missing
verification layer — 600 policy scenarios per condition on a 3.8B model inside a 4.2 GiB VRAM budget,
no cloud inference. The headline result is the one that contradicted my own hypothesis: **constraining
output to JSON without a reasoning field made the evaluator less safe, not more** (46.2% unsafe
accepts against 17.2% unconstrained), and the paper reports the residual failures rather than rounding
them away.

**Tooling for the bug class I keep finding.** [agentbound](https://github.com/sushant-me/agentbound)
statically detects tool-boundary bugs in agent frameworks; [mcp-nameguard](https://github.com/sushant-me/mcp-nameguard)
checks an MCP server's tool names against the ones frameworks reserve for themselves;
[trajectorycheck](https://github.com/sushant-me/trajectorycheck) grades whole agent trajectories —
tool calls, arguments, side effects and injected instructions — with a deliberately broken agent as a
control.

**The systems those agents stand on.** Fuzzing and harness engineering, memory-safety triage under
ASan/UBSan, and the ordinary C++ that decides whether an agent's world model can be crashed by 28
bytes.

**Building for places where infrastructure is unreliable.** Two years as an AI engineer (Atmos
SoftTech) and an internship as technical lead: offline-first inference, a Wi-Fi CSI life-detection
prototype that works through rubble without cameras, and an offline payment wallet.

---

## Selected work

- [**beyond-attention**](https://github.com/sushant-me/beyond-attention) — a selective state-space model (Mamba/S6) implemented from scratch in NumPy, published with the results that *don't* flatter it: a scalar register still ties the agent on the arithmetic tasks, and the SSM is the weaker model past its training length.
- [**Edge-Native Semantic Firewall**](https://github.com/sushant-me/Edge-Native_Semantic_Firewall_) — paper, 600-scenario corpus, raw model outputs, camera-ready, and reproducibility checks that can fail.
- [**policygate**](https://github.com/sushant-me/policygate) — a fail-closed policy gate for agent tool calls, written
  because of a measurement: my paper found a locally served 3.8B model approving **23.5%** of the
  proposals the policy would have blocked. In the library a model can deny or escalate and **cannot
  authorise** an uncovered action, a failing evaluator falls through to a refusal, and every decision
  lands in a hash-chained audit log. Ships adapters for MCP servers, LangChain-style tools
  and provider function calls, so gating a call needs no new dependency. Disabling either
  invariant fails three tests; disabling both fails six.
- [**mcpaudit**](https://github.com/sushant-me/mcpaudit) — audits an MCP server's tool
  declarations before you connect: reserved-name collisions, instruction-shaped text,
  invisible Unicode **with the tag-block payload decoded**, look-alike names, destructive
  tools declaring `readOnlyHint`. Pins the declarations in a lock file, so a description
  that changes after you approve it is reported as the tool-poisoning shape it is.
- [**tool-boundary-corpus**](https://github.com/sushant-me/tool-boundary-corpus) — a labelled
  corpus of 18 agent tool-boundary cases and a detector-agnostic harness, because a claim about
  a scanner is worth little without precision and recall. Measured: my `mcpaudit` at
  **P=1.000 R=1.000** on the tool-list cases and **P=1.000 R=1.000** on the code cases. That second
  number started at 0.750: the corpus found a false positive in `agentbound` (a pattern inside a
  string bound to a name, which its comment-stripping did not cover), I fixed it in v0.1.10, and
  the same harness re-measured the improvement. Adding the guard that pins which build a score
  came from turned up a third defect — [v0.1.11](https://github.com/sushant-me/agentbound/releases/tag/v0.1.11)
  corrects a release that reported the wrong version. The corpus is self-authored, and says so in
  every report.
- [**reputation**](https://github.com/sushant-me/reputation) — the claims-verification repository described above.

## Writing

- [**A benchmark found a bug in my own detector**](https://github.com/sushant-me/writeups/blob/main/2026-09-21-a-benchmark-found-a-bug-in-my-own-detector.md) — I built a labelled corpus to stop making unmeasured claims and it found a false positive in my own scanner: precision **0.750 → 1.000**, with the failing case named in CI rather than deleted. The benchmark was wrong twice before the detector was, the harness assumed its author's output format, and the guard added for the fix surfaced a third defect — a release that reported the wrong version. Three defects, one shape: a number nothing checked.
- [**Structured output made my safety evaluator less safe**](https://github.com/sushant-me/writeups/blob/main/2026-09-20-structured-output-made-it-less-safe.md) — the counter-intuitive result from my paper: JSON-constrained output *without* a reasoning field approved **46.2%** of proposals the policy would have blocked, against **17.2%** for free-form, and it was 5.5× faster — the trade a team picks under a latency budget. Includes the parts that hurt: the best arm still approved 6 of 208 irreversible hard denials.
- [**A sample agent security review**](https://github.com/sushant-me/agent-review-sample) — a deliberately vulnerable agent I wrote, and the deliverable I would return for it: four findings (tool shadowing, a fail-open confirmation gate, indirect prompt injection, path traversal) with reproductions, fixes, and a section stating what was *not* tested. `python3 demo.py` reproduces all four.
- [**The crash that wasn't**](https://github.com/sushant-me/writeups/blob/main/2026-09-19-the-crash-that-wasnt.md) — a memory-safety test that passed locally and segfaulted in CI, the AddressSanitizer trace that showed my patch fixed the wrong bug, and the pull request I closed on myself afterwards. *"A passing memory-safety test proves almost nothing unless it runs under a sanitizer."*

## Tools, at their current release

- [agentbound](https://github.com/sushant-me/agentbound) — [v0.1.11](https://github.com/sushant-me/agentbound/releases/tag/v0.1.11) · tool-boundary bugs in agent frameworks (Python, TypeScript, YAML)
- [mcp-nameguard](https://github.com/sushant-me/mcp-nameguard) — [v0.4.7](https://github.com/sushant-me/mcp-nameguard/releases/tag/v0.4.7) · MCP tool names against the ones frameworks reserve
- [trajectorycheck](https://github.com/sushant-me/trajectorycheck) — [v0.1.2](https://github.com/sushant-me/trajectorycheck/releases/tag/v0.1.2) · grades whole agent trajectories, with a deliberately broken agent as a control

---

<div align="center">
<sub>Computer Engineering, Nepal Engineering College (final year) · previously AI Engineer, Atmos SoftTech · two-time Hult Prize 1st Runner-Up · Aspire Leaders Global Finalist</sub>
</div>
