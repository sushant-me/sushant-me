<div align="center">

# Sushant Poudel

**AI security engineer — I find where agent tool boundaries leak, then close them.**

Kathmandu, Nepal · [sushant.poudel2028@gmail.com](mailto:sushant.poudel2028@gmail.com) · [LinkedIn](https://linkedin.com/in/sushant-poudel2028) · [sushantpoudel2028.com.np](https://sushantpoudel2028.com.np)

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
| **Merged into `google/go-github`** — release-asset uploads are rejected when the upload URL's host differs from the configured host; approved by maintainer `gmlewis` with the full CI matrix green | [PR #4556](https://github.com/google/go-github/pull/4556) |
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
- [**reputation**](https://github.com/sushant-me/reputation) — the claims-verification repository described above.

## Tools, at their current release

- [agentbound](https://github.com/sushant-me/agentbound) — [v0.1.9](https://github.com/sushant-me/agentbound/releases/tag/v0.1.9) · tool-boundary bugs in agent frameworks (Python, TypeScript, YAML)
- [mcp-nameguard](https://github.com/sushant-me/mcp-nameguard) — [v0.4.7](https://github.com/sushant-me/mcp-nameguard/releases/tag/v0.4.7) · MCP tool names against the ones frameworks reserve
- [trajectorycheck](https://github.com/sushant-me/trajectorycheck) — [v0.1.2](https://github.com/sushant-me/trajectorycheck/releases/tag/v0.1.2) · grades whole agent trajectories, with a deliberately broken agent as a control

---

<div align="center">
<sub>Computer Engineering, Nepal Engineering College (final year) · previously AI Engineer, Atmos SoftTech · two-time Hult Prize 1st Runner-Up · Aspire Leaders Global Finalist</sub>
</div>
