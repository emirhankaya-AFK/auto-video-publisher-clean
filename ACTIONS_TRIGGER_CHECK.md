# First safe Actions trigger

This file was added to trigger the existing `public_sanity.yml` push workflow
on the clean public repository's `main` branch.

- Expected job: Python source syntax check only.
- No secrets, social posts, uploads or external account access.
- Existing private production repository remains untouched.
- The live publisher stays disabled pending the new Secrets, credential
  rotation and idempotency review.

If GitHub Actions records no run after this commit, the workflow registration
or repository/organization Actions settings require separate investigation.
