# Public migration status — 2026-10-21

Source: private `emirhankaya-AFK/auto-video-publisher` master `107c623f4dc15e72f1ecdf31c470b84a025a35a1`.

This is a **new independent Git history**, not a fork or mirror. An allowlist imported 78 Python/config/test files. Files were scanned for common credential patterns; two test-only NTFY URL literals were replaced with inert fixtures. A pattern scan is not a complete security audit.

**Production: disabled.** Old scheduling and credentialed workflows are deliberately absent. `.github/workflows/public_sanity.yml` only compiles Python source; it does not import production modules, use secrets, call external APIs or publish videos.

## Before any live use

1. Revoke/rotate previously embedded Meta tokens in the old private repository history. Never publish the private repository itself or copy its Git history.
2. Do an independent sensitive-data review; replace or remove any remaining confidential identifiers.
3. Recreate all required YouTube, Meta, Google Drive and notification values in **this public repository's Actions Secrets**, never in code, logs or chat. The ChatGPT GitHub connector cannot set those Secrets.
4. Independently validate account identities, access scopes, daily schedule, Drive claims, duplicate protection and rollback before enabling any publishing job.
5. For real publishing, add a separate reviewed workflow using appropriate `secrets.*` references; public PRs must not be allowed to execute untrusted code with production secrets.
6. Validate nonzero job steps for CI; then verify genuine normal scheduled platform post IDs plus delivery reports. Syntax success by itself is **not** proof of live operation.

The original private repository and all existing automation jobs remain untouched.
