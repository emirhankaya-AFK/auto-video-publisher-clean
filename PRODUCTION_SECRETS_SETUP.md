# GitHub Actions — production credentials (setup required)

This public repository has **no production secrets copied from the old private repo**. GitHub does not allow reading back old Actions Secret values. They cannot be migrated through the current ChatGPT GitHub connection. Never paste values into ChatGPT, PRs, workflows, issues or logs.

**Required before any rollout:** revoke/rotate the previously embedded Meta user token from the old private repository's history and issue fresh platform credentials.

Open [new repository Secrets](https://github.com/emirhankaya-AFK/auto-video-publisher-clean/settings/secrets/actions) and add only the credentials applicable to your active routes. Values MUST be supplied via encrypted Repository Secrets.

## Secret names referenced by previous publisher workflow

| Purpose | Exact secret name |
| --- | --- |
| Google Drive OAuth | `DRIVE_TOKEN_JSON` |
| Main Drive directory | `DRIVE_FOLDER_ID` |
| Gönle Düşen Drive directory | `GONLE_DUSEN_DRIVE_FOLDER_ID` |
| Daily Laugh Lab Drive directory | `DAILY_LAUGH_DRIVE_FOLDER_ID` |
| Film Drive directory (was embedded as an ID in a private workflow, should now be secret) | `FILM_DRIVE_FOLDER_ID` |
| YouTube channel 1 | `TOKEN_CHANNEL1_JSON` |
| YouTube channel 2 | `TOKEN_CHANNEL2_JSON` |
| Daily Laugh Lab YouTube | `TOKEN_DAILY_LAUGH_LAB_JSON` |
| Gönle Düşen YouTube | `TOKEN_GONLE_DUSEN_JSON` |
| Film YouTube diagnostics | `TOKEN_FILM_YOUTUBE_JSON` |
| Meta app/account configuration | `META_AUTH_JSON` |
| Meta access token | `META_ACCESS_TOKEN` |
| Optional NTFY endpoint | `NTFY_TOPIC_URL` |
| Optional NTFY topic | `NTFY_TOPIC` |
| Optional Threads account | `THREADS_ACCESS_TOKEN` |
| Optional Threads upload URL template | `PENGUEN_THREADS_VIDEO_URL_TEMPLATE` |

The exact active account-to-secret mappings and required scopes still need verification. Some secret names above are optional, depending on which account routes are enabled. The production publisher workflow is *not* yet installed in this public repository; adding secrets alone **will not** start videos.

## Required approval checks

1. New clean snapshot passes public, no-credential CI (real runner and steps).
2. New credential access/identity tests pass in read-only mode.
3. Previously leaked credentials are revoked; new credentials never appear in source or logs.
4. Original private schedules are disabled or otherwise prevented from running simultaneously before new live schedules are enabled.
5. Publication sequencing, Drive claim ledger, idempotency, and expected platform post IDs are independently verified.
6. Only then enable a reviewed production workflow and evaluate one normal scheduled run.

**Current state: source imported, live publisher disabled, real CI result not yet confirmed.**
