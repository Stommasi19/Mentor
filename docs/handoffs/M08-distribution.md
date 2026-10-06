# M08 — distribute the verified product

Status: Final phase; implementation has not started.
Depends on local behavior, code quality, and portability evidence from M01–M07.
Scope: [Roadmap](../ROADMAP.md#final-phase--distribution).
Criteria: [T14](../TESTING.md#criteria), plus regression checks of the core and
each supported adapter.

## Before and after

Before: Mentor works locally with a neutral core, verified development hooks,
manual/adaptive coaching behavior, and recorded language/model/host coverage.
After: other users can discover, install, configure, update, and remove a package
whose supported behavior is documented and tested.

## Implementation

1. Review the actual local evidence and compatibility matrix. Resolve material
   defects; identify experimental or unsupported combinations explicitly.
2. Wrap the canonical core for the supported hosts. Keep model/host configuration
   in adapters and avoid divergent copies of policy or workflow instructions.
3. Add the required plugin manifests and marketplace/catalog entries here.
   For Codex, follow the current supported packaging/discovery schema at this
   milestone, rather than treating the earlier development-hook setup as an
   installed-plugin test.
4. Test discovery, installation, hook review/trust, automatic context delivery,
   preferences, updates/cache refresh, disabling, and removal in a clean
   environment. Recheck actual generated code/comments and a mentoring scenario.
5. Document prerequisites, tested language/model/provider/host combinations,
   controls, local data location, troubleshooting, limitations, and useful examples.
   Verify source attribution, redistribution terms, and required notices.
6. Prepare release assets and a reproducible demonstration from real evidence.
   Publish only when explicitly requested; preparing this handoff does not publish.

Public installation is the output of this final phase. The M01–M04 local
milestones do not depend on marketplace discovery or distributable packaging.

## Acceptance

- [ ] T14: a clean environment can discover/install the intended package through
  the supported mechanism, and actual hook delivery works after required trust.
- [ ] Update/disable/remove behavior and preference handling are documented and
  exercised; no private toolkit or author-machine dependency is required.
- [ ] Core code-quality, comments/docs, and coaching scenarios still satisfy
  their applicable criteria through the installed distribution.
- [ ] Compatibility claims identify actual tested combinations and limitations.
- [ ] Source notices, usage documentation, and demonstration match the shipped
  behavior; no synthetic-human-learning or universal-support claim is invented.
- [ ] Any external publication has its own explicit authorization and recorded result.

## Handback

Report package/version, verified installation and hook evidence, supported
combinations, code-quality examples, update/removal results, known limitations,
and publication state. Keep the existing local evidence alongside distribution
results so installation success cannot substitute for product quality.
