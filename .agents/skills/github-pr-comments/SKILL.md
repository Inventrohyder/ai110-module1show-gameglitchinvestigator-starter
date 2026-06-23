---
name: github-pr-comments
description: Extract and process GitHub Pull Request reviews and inline comment threads.
---

# Github PR Comments Skill

Use this skill to access and process Pull Request reviews and inline/thread comments from a GitHub repository, handling credentials and API fallbacks correctly.

## Retrieving Comments

There are two main methods to retrieve comments depending on authentication context.

### Method 1: Using Github CLI (`gh`)

If the environment has a valid GitHub token (check status with `gh auth status`), use the CLI for direct integration:

1. **View General PR Description & Conversation**:
   ```sh
   gh pr view <pr_number> --comments
   ```
2. **List PR Comments using API**:
   ```sh
   gh api repos/<owner>/<repo>/pulls/<pr_number>/comments
   ```

### Method 2: Public API Fallback (Using `curl`)

If `gh` credentials are unauthorized (e.g. `HTTP 401: Bad credentials`), use unauthenticated GET requests to the public GitHub REST API:

1. **Fetch Reviews and Summaries**:

   ```sh
   curl -s "https://api.github.com/repos/<owner>/<repo>/pulls/<pr_number>/reviews"
   ```

   _Check for review items with non-empty `body` fields and `state: "COMMENTED"` or `"CHANGES_REQUESTED"`._

2. **Fetch Inline Comments (Diff Thread Discussions)**:
   ```sh
   curl -s "https://api.github.com/repos/<owner>/<repo>/pulls/<pr_number>/comments"
   ```
   _This returns a list of comments, each containing:_
   - `"path"`: The file containing the comment (e.g., `.trunk/trunk.yaml`).
   - `"body"`: The text of the comment.
   - `"diff_hunk"`: The context surrounding the commented line.
   - `"line"` or `"original_line"`: The line number in the file.
   - `"node_id"`: Unique identifier for the comment thread (e.g. `PRRC_kwDOS4I49s7OSFtE`).

## Parsing Comments to Action Items

1. Find the target file using `"path"`.
2. Locate the line specified by `"line"` or `"original_line"`.
3. Match the `"body"` comment text with the file content to extract the exact issue.
4. Create a task plan mapping out:
   - The file path.
   - The exact line comment.
   - The required correction.
