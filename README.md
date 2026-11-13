<div align="center">

<img src="https://raw.githubusercontent.com/sushant-me/sushant-me/main/assets/banner.svg" alt="Sushant Poudel — AI security engineer. I find where agent tool boundaries leak, then close them." width="100%" />

**AI security engineer — I find where agent tool boundaries leak, then close them.**

Bhaktapur, Nepal · open to security-engineering and AI-security work, remote or on-site

[sushantpoudel2028.com.np](https://sushantpoudel2028.com.np) · [Writing](https://sushantpoudel2028.com.np/writing) · [Publications](https://sushantpoudel2028.com.np/publications) · [Press](https://sushantpoudel2028.com.np/press) · [LinkedIn](https://www.linkedin.com/in/sushant-poudel2028/) · [sushant.poudel2028@gmail.com](mailto:sushant.poudel2028@gmail.com)

**[What I do, and how to work with me →](https://sushant-me.github.io/hire/)**

</div>

---

## Receipts

Chosen because each one can be checked from the link next to it.

1. **A merged security fix in `google/go-github`.** [#4556](https://github.com/google/go-github/pull/4556) stopped a release-asset upload from being sent to a host the client never configured. A maintainer generalised the rule the next day in [#4564](https://github.com/google/go-github/pull/4564) — *"send credentials only to configured origins"* — and merged [#4579](https://github.com/google/go-github/pull/4579), which puts `Sushant Poudel` in [AUTHORS](https://github.com/google/go-github/blob/master/AUTHORS) on `master` and in the [`v93.0.0` release notes](https://github.com/google/go-github/releases/tag/v93.0.0).

2. **A bug filed, confirmed by the maintainer, and fixed the same night.** `google/osv-scanner` compiles `nameIsRegex` overrides by string concatenation, so a top-level alternation escapes the documented `^pattern$` anchors and silently drops packages from a vulnerability scan: [#3120](https://github.com/google/osv-scanner/issues/3120). The maintainer replied *"what you have pointed out is true"* and merged his own fix, [#3121](https://github.com/google/osv-scanner/pull/3121), hours later.

3. **Memory-safety findings with standalone reproducers.** Five open issues in `google/s2geometry` — a NULL dereference ([#674](https://github.com/google/s2geometry/issues/674)), an out-of-bounds read ([#676](https://github.com/google/s2geometry/issues/676)), a heap-buffer-overflow ([#678](https://github.com/google/s2geometry/issues/678)), a 16 GiB allocation from a **117-byte** input ([#677](https://github.com/google/s2geometry/issues/677)) and a 2.4 GiB allocation from a **28-byte** input ([#679](https://github.com/google/s2geometry/issues/679)) — plus two hardening PRs ([#681](https://github.com/google/s2geometry/pull/681), [#682](https://github.com/google/s2geometry/pull/682)). A heap-buffer-overflow **write** in `pnggroup/libpng` ([#935](https://github.com/pnggroup/libpng/issues/935)), reproduced under AddressSanitizer on 1.6.60 and 1.8.0; stated limit: caller-triggered, not reachable from crafted PNG bytes. And an OSS-Fuzz harness in `google/libphonenumber` that was asserting **0.00%** coverage of the code it targeted — the corrected harness measures **93.05%** locally ([#4079](https://github.com/google/libphonenumber/pull/4079), open).

4. **Four published security advisories** against my own tools — one high, three medium, each found, fixed and written up: [policygate](https://github.com/sushant-me/policygate/security/advisories/GHSA-qwvv-fcmm-r3j2) — a newline stepped around a `deny` glob, an authorisation bypass in the gate itself; [mcp-nameguard](https://github.com/sushant-me/mcp-nameguard/security/advisories/GHSA-wcqw-86xv-w95q) — an unbounded server reply let a hostile MCP server exhaust the scanner inspecting it; [agentbound](https://github.com/sushant-me/agentbound/security/advisories/GHSA-mffv-hhg5-mm33) — the masker blanked one-line strings and hid real findings; [mcpaudit](https://github.com/sushant-me/mcpaudit/security/advisories/GHSA-62f4-h552-54wc) — invisible-character ranges covered 16 of 256 variation selectors.

5. **HackingHub — Elite, 21,785 XP, 61% of the platform conquered, 1 gold / 4 silver / 3 bronze medals**, #7 on the all-time global leaderboard. [Profile](https://app.hackinghub.io/p/nofear976) · [leaderboard API](https://api.hackinghub.io/leaderboard?type=previous)

6. **NullOrigin CTF 2026 — grand finalist, rank #2.** Certificate `NO-2026-GF-229CF4` verifies at [creds.cyberhx.com/verify](https://creds.cyberhx.com/verify); the event ran a 12-hour qualifier and a 12-hour final, with 50 finalist teams selected from 3,500+.

7. **A paper with a DOI** — *Edge-Native Semantic Firewall for Autonomous LLM Agents: A Structured Chain-of-Thought Verification Framework*, Proceedings of ICICSET 2026, published 2 October 2026: [10.65091/icicset.v3i1.75](https://doi.org/10.65091/icicset.v3i1.75).

<details>
<summary><b>Other merged upstream work — breadth, if you want it</b></summary>

- `open-telemetry/opentelemetry-go` — two merged (OTLP log-exporter env-var case handling, [#9230](https://github.com/open-telemetry/opentelemetry-go/pull/9230); module version reporting, [#9232](https://github.com/open-telemetry/opentelemetry-go/pull/9232)), one open ([#9231](https://github.com/open-telemetry/opentelemetry-go/pull/9231)).
- `google/adk-python` — the framework now refuses its reserved `set_model_response` tool name ([commit `cc5d516`](https://github.com/google/adk-python/commit/cc5d5164faf520b9f30ca7edf18a5751df419fc0), 2 Oct 2026). `google/adk-go` — two merged ([#1679](https://github.com/google/adk-go/pull/1679), [#1711](https://github.com/google/adk-go/pull/1711)), one open ([#1606](https://github.com/google/adk-go/pull/1606)).
- `trailofbits/skills` — two merged ([#346](https://github.com/trailofbits/skills/pull/346), [#347](https://github.com/trailofbits/skills/pull/347)); `trailofbits/it-depends` — one merged ([#254](https://github.com/trailofbits/it-depends/pull/254)).
- `sisaku-security/sisakulint` — a docs fix merged ([#655](https://github.com/sisaku-security/sisakulint/pull/655)); three issues from an audit of its AI-action rules remain open ([#646](https://github.com/sisaku-security/sisakulint/issues/646), [#647](https://github.com/sisaku-security/sisakulint/issues/647), [#648](https://github.com/sisaku-security/sisakulint/issues/648)) after the maintainer reproduced the finding independently.
- `elementalsouls/Claude-BugHunter` — routing fix merged ([#81](https://github.com/elementalsouls/Claude-BugHunter/pull/81)): 22 of its 58 `hunt-*` skills had no mapping and could never be selected.

</details>

## What I do

**Agent and MCP security.** Detectors, audits and fail-closed gates for the boundary where an agent's tool declarations become executed actions — [agentbound](https://github.com/sushant-me/agentbound), [mcpaudit](https://github.com/sushant-me/mcpaudit), [policygate](https://github.com/sushant-me/policygate), [trajectorycheck](https://github.com/sushant-me/trajectorycheck), and the [labelled corpus](https://github.com/sushant-me/tool-boundary-corpus) that keeps their precision numbers honest.

**Memory safety and fuzzing.** ASan/UBSan triage, harness engineering, and upstream reports with reproducers — libpng, s2geometry, libphonenumber's dead OSS-Fuzz harness, OpenTelemetry-Go.

**Full-stack and offline-first builds.** Next.js/TypeScript and Flutter products for infrastructure that is not reliable: two years as an AI engineer at Atmos SoftTech (Mar 2024 – Mar 2026) building production ML, agent pipelines and offline inference. [meshdoc](https://github.com/sushant-me/meshdoc) is the current one, in Rust.

Background: Computer Engineering student at Nepal Engineering College, Bhaktapur.

## Selected work

- **[agentbound](https://github.com/sushant-me/agentbound)** · Python, ships as a GitHub Action · static detection of agent tool-boundary bugs across Python, TypeScript, JavaScript, Go, Java and Actions workflows. Precision measured, not claimed: **0.79 → 1.00** across a 14-framework survey, and **0.94** once two more frameworks were added in v0.1.16 — every false positive, the rule that removed it and the four mechanisms behind them are in [SURVEY.md](https://github.com/sushant-me/agentbound/blob/master/SURVEY.md). Its [advisory](https://github.com/sushant-me/agentbound/security/advisories/GHSA-mffv-hhg5-mm33) fixed a masker that was hiding a real finding.
- **[mcpaudit](https://github.com/sushant-me/mcpaudit)** · Python · audits an MCP server's tool declarations before you connect, then pins them in a lock file — a description that changes after approval is reported as the tool-poisoning shape it is.
- **[policygate](https://github.com/sushant-me/policygate)** · Python · a fail-closed gate for agent tool calls: the model may deny or escalate but **cannot authorise**, a failing evaluator falls through to refusal, and every decision lands in a hash-chained audit log. Its high-severity advisory was an authorisation bypass I found in my own gate.
- **[trajectorycheck](https://github.com/sushant-me/trajectorycheck)** · Python · grades whole agent trajectories — tool calls, arguments, side effects, injected instructions — with a deliberately broken agent as a control.
- **[tool-boundary-corpus](https://github.com/sushant-me/tool-boundary-corpus)** · Python · 24 labelled tool-boundary cases and a detector-agnostic harness, so a precision number can be re-measured instead of trusted.
- **[Edge-Native Semantic Firewall](https://github.com/sushant-me/Edge-Native_Semantic_Firewall_)** · Python · the paper's artifact: 600-scenario corpus, raw model outputs, and a result that contradicted the hypothesis — JSON-constrained output *without* a reasoning field approved **46.2%** of policy-blocked proposals, against 17.2% free-form.
- **[meshdoc](https://github.com/sushant-me/meshdoc)** · Rust · offline-first, end-to-end-encrypted collaboration for teams without reliable connectivity.
- **[reputation](https://github.com/sushant-me/reputation)** · Python · every claim I make about my own work, its public source, and the weekly check that turns red when one stops being true.

Six tools on one page, with install lines and Action snippets: [sushant-me.github.io/tooling](https://sushant-me.github.io/tooling/).

## Publications and writing

- **DOI paper** — ICICSET 2026 proceedings, 2 October 2026: [10.65091/icicset.v3i1.75](https://doi.org/10.65091/icicset.v3i1.75)
- **Two abstracts** in the [AICSE 2026 abstract book](https://eemc.edu.np/public/aicse/abstract.pdf) (printed pp. 32–33): Google's Open Knowledge Format for multi-agent threat intelligence, and Wi-Fi sensing attack vectors.
- **ORCID** [0009-0008-7732-3269](https://orcid.org/0009-0008-7732-3269) · all nine papers on [sushantpoudel2028.com.np/publications](https://sushantpoudel2028.com.np/publications)
- **Writing, if you want the method rather than the claim:**
  - [My own benchmark said 1.000. Real code said 0.14.](https://sushantpoudel2028.com.np/writing/my-benchmark-said-1000-real-code-said-014)
  - [Structured output made my safety evaluator less safe](https://sushantpoudel2028.com.np/writing/structured-output-made-it-less-safe)
  - [The check that could not see what it was checking](https://sushantpoudel2028.com.np/writing/the-check-that-could-not-see-what-it-was-checking)
  - [A number nothing recomputes](https://sushantpoudel2028.com.np/writing/a-number-nothing-recomputes)

## Work with me

I take on work where the deliverable can be checked: **MCP server and agent-tool-boundary audits**, threat models of an agent's action surface, memory-safety and fuzzing reviews of the C/C++ underneath, and full-stack builds where connectivity is not a given.

**[Hire page →](https://sushantpoudel2028.com.np/hire)** · **[CV (PDF) →](https://sushantpoudel2028.com.np/cv)** · [sushant.poudel2028@gmail.com](mailto:sushant.poudel2028@gmail.com) · [LinkedIn](https://www.linkedin.com/in/sushant-poudel2028/) · [Press and author page](https://sushantpoudel2028.com.np/press)

<div align="center">
<sub>Every claim above links to the thing that proves it, and where a claim has a limit the limit is in the sentence. The subset that is machine-checked every week lives in <a href="https://github.com/sushant-me/reputation">reputation</a>. Work that cannot be linked — private bug-bounty reports, unpublished audits — is deliberately not listed here.</sub>
</div>
