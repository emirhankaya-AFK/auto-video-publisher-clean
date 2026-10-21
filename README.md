# Auto Video Publisher — clean public source

This repository is a **new, history-free source snapshot** of a private video-publishing project.

**Live publishing is disabled until separately verified.** The private original, its historical commits, personal data, accounts, tokens, and production workflow schedules must not be copied here. This project uses third-party APIs; GitHub Actions becoming available does not prove that those platforms are connected or that scheduled posts are running.

## Security

- Never commit API keys, Meta/YouTube/Google access tokens, OAuth JSON, NTFY topics or signed URLs.
- Previously embedded Meta credentials in the old private repository must be revoked/rotated before connecting live accounts.
- Review and scan source before publishing; pattern scanning is not a guarantee that all private information is absent.
- Use new GitHub Actions Secrets, never GitHub workflow parameters, logs, comments or issues, for credentials.
- Only add live publishing workflows after tests, permissions and duplicate-publishing safety are verified.

## Current operational state

- Code migration: in progress.
- GitHub Actions: not yet verified.
- Live production: **NOT ENABLED**.
- Existing private repository remains unchanged.

GitHub's standard hosted runners for public projects can have free usage; artifact storage, external platforms and other services may have separate costs or limits.
