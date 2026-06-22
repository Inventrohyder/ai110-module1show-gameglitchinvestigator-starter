# Branch Protection Rules

Branch protection rules are enforced on the `main` branch to maintain code quality and test passing status:

1. **Strict Status Checks**: Pull requests must pass the following status checks before merging:
   - `test` (GitHub Actions workflow running unit tests)
   - `Trunk Check` (GitHub Actions workflow checking code linting and formatting)
2. **No Force Pushing**: Force pushing to `main` is disabled for all users.
3. **No Branch Deletions**: Deleting the `main` branch is disabled.
