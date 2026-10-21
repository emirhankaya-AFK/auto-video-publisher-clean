# Auto Video Publisher — public source snapshot

**Status: source migrated, live publishing disabled.** This is a clean public repository with independent Git history. Its code came from a limited, credential-screened snapshot of a private project. Prior private Git commits, production schedules, tokens, media, logs and manifests were not imported.

- Python source, dependency lockfile and regression tests are included.
- The only active workflow is `public_sanity.yml`, which checks Python syntax without accessing platform accounts.
- **There are no scheduled live publishing jobs or credentials in this public repository.**
- Reusing the code in production requires separate secret setup, history-token rotation, platform identity checks and duplicate-post protections.

See [PUBLIC_MIGRATION_STATUS.md](PUBLIC_MIGRATION_STATUS.md) for the remaining security and rollout checklist.

Never commit credentials, personal data, private NTFY URLs or token JSON files. The original repository must stay private.
