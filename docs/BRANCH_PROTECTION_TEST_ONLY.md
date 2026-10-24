# Temporary branch-protection verification

This file is only for a **negative enforcement test**. It must never be merged.

The next relative link is intentionally invalid, so the repository's
`docs-integrity` required check should fail:

[Deliberately nonexistent target](./__branch-protection-test-must-not-exist-2026-10-24__.md)

Expected behavior: GitHub blocks merging the test pull request. After recording
the check status, close the PR without merging and remove the test branch.
