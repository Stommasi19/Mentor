# M01 — readable-code core and local hook prototype

Status: Ready for an implementation request; implementation has not started.
Scope: [Local implementation plan](../IMPLEMENTATION-PLAN.md).
Criteria: [T01–T05, T12, and T13 architecture](../TESTING.md#criteria).
Current baseline: `main` at `42bc70c7d66c24ef54592a151c97488bbeb38a76`.
Account for these planning revisions before creating an implementation branch.

## Before and after

Before: planning documents only.
After: a neutral core produces correct, readable, maintainable, appropriately
commented code in a controlled C# case, and a local development hook automatically
delivers that same policy in a fresh agent session. Both outcomes are required.
Marketplace discovery and other-user packaging are final M08.

## Implementation order

1. Write original `core/policy.md`. Keep behavior independent of coding language,
   model/vendor, and host APIs. Follow the target project's idioms. Require
   descriptive names, traceable flow, useful boundaries, comments explaining
   intent/non-obvious rules, accurate public-contract documentation, and necessary
   checks. Separate those code standards from optional coaching. Honor explicit
   ownership, demonstration/takeover, and project implementation agreements.
2. Create the small [C# fixture](../TESTING.md#reusable-fixture), S01 task/response
   cards, and independent behavioral checks. C# is only the first test case;
   Python can implement utility scripts without defining the learner's language.
3. Run fresh baseline and policy-supplied experiments on the same starting task
   and settings. Inspect the actual resulting code, comments, and docs; record
   concrete T04 strengths/defects and checks. Label these policy experiments.
   Revise and rerun failures; do not infer improvement when baseline already passes.
4. Add a thin `adapters/codex/` development hook using the host-supported
   SessionStart lifecycle and output contract. Host schemas/roles stay here.
   Resolve the shared core independently of session working directory and quote
   paths. Missing core fails visibly. Keep injected context concise.
5. Configure that local hook through a supported development configuration in
   a disposable external workspace and use the host's normal review/trust flow.
   Start a fresh session without pasted policy or a manual skill invocation;
   capture actual hook execution/context evidence and repeat S01 through it.
6. Immediately run real-entry output/resource-failure checks and applicable
   lifecycle/interaction/code checks. Document reproduction of local experiments
   and development-hook tests, versions/settings, and results.

No plugin manifest, marketplace/catalog entry, other-user installation, or release
asset in this slice. Persistent controls are M02; deeper neutral workflows are
M03/M04. No evidence ledger or full reactive actor runner yet.

## Immediate acceptance

- [ ] T04 first: independent C# checks pass; an annotated review shows descriptive
  names, understandable flow, appropriate boundaries, and needed comments/docs
  in the generated code. Teaching chat prose does not replace code documentation.
- [ ] T12: baseline/core comparison records settings, starting code, actual diff/
  comments, check results, and limitations without invented improvement claims.
- [ ] T13 architecture: canonical instructions contain no model/vendor API or
  target-language default; C#/host specifics are in fixture/adapter.
- [ ] T02: real adapter entry emits valid host output with shared core from
  another directory; missing core fails visibly. No exact-prose snapshots.
- [ ] T01 required: actual local hook executes and delivers context automatically
  in a fresh external host session; disabled/untrusted hook supplies none.
  Handler-only or policy-only tests cannot satisfy this criterion.
- [ ] T03: record startup and exercised resume/clear/compact separately; retain
  explicit session preferences, and mark unexercised events pending.
- [ ] T05: meaningful conditional learner participation and requested takeover
  lead to complete checked work; agent-implements project agreements respected.
- [ ] README/status reflect only implemented, tested behavior and limitations.

Use Python's standard library for utility/contract checks where chosen. Record
actual Python/.NET/host/model versions and the real C# check command. Run
`python3 -m unittest discover -s tests -v` once checks exist and `git diff --check`.
Verify native hook configuration against the actual host. No marketplace commands
or silent trust edits are needed. C# success is not proof of all-language/model
compatibility; broader coverage is M05.

## Handback and learning checkpoint

Show generated code, useful comments/docs, behavioral checks, concrete readability
review, and actual hook delivery evidence. Explain the neutral-core/host-adapter
boundary and diagnose a hook that emits correct JSON but never reaches the model.
Separate code quality, coaching conduct, and unaided comprehension observations.
Report failed/pending criteria and the next correction before marking M01 complete.

References: [Design](../DESIGN.md),
[verification](../TESTING.md), [Codex hooks](https://learn.chatgpt.com/docs/hooks).
