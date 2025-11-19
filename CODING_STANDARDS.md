Coding Standards and Best Practices
1. Introduction
This document outlines the coding standards and best practices to be followed for all software development projects. The goal is to produce high-quality, clean, maintainable, and secure code. Adhering to these standards ensures consistency across the codebase, making it easier for developers to collaborate, onboard new team members, and manage projects long-term.

These guidelines are designed to be parseable by AI coding assistants like GitHub Copilot to help enforce consistency.

2. Naming Conventions
Clear and consistent naming is crucial for readability.

2.1. General Rules
Use descriptive and unambiguous names.

Avoid abbreviations and single-letter variable names (except for simple loop counters like i, j, k).

Use English for all names.

2.2. Language-Specific Conventions
JavaScript/TypeScript:

Variables and Functions: Use camelCase. Example: let userProfile;, function calculateTotal().

Classes and Components: Use PascalCase. Example: class UserAccount { ... }, function UserProfile() { ... }.

Constants: Use UPPER_SNAKE_CASE. Example: const MAX_CONNECTIONS = 100;.

Boolean Variables: Prefix with is, has, or should. Example: let isActive;, const hasPermission = true;.

// Good
const MAX_RETRIES = 3;
let currentUser = 'admin';
class DataProcessor {
  // ...
}
function hasValidSession() {
  return true;
}

Python:

Variables and Functions: Use snake_case. Example: user_profile, def calculate_total():.

Classes: Use PascalCase (CapWords). Example: class UserAccount:.

Constants: Use UPPER_SNAKE_CASE. Example: MAX_CONNECTIONS = 100.

# Good
MAX_RETRIES = 3
current_user = 'admin'
class DataProcessor:
    # ...
def has_valid_session():
    return True

3. Formatting and Style
Consistent formatting improves readability and reduces cognitive load. We use automated formatters to enforce style.

Tools:

JavaScript/TypeScript: Prettier

Python: Black

Line Length: Maximum 100 characters.

Indentation: Use 2 spaces for JS/TS/CSS, 4 spaces for Python. Do not use tabs.

Braces: Opening braces for blocks should be on the same line as the statement (if, function, etc.).

// Good
if (condition) {
  // statement
} else {
  // another statement
}

4. Comments
Comments should explain why something is done, not what is being done. The code itself should be self-documenting enough to explain the what.

Block Comments: Use for documenting modules, functions, and complex logic.

Inline Comments: Use sparingly to clarify a specific line of code that may not be obvious.

TODO Comments: Use // TODO: to mark areas that need future work. Include a description of what needs to be done.

# Explains the 'why'
# We have to manually set the user ID here because the legacy
# authentication system does not propagate it automatically.
user.id = get_legacy_id(user.email)

# BAD: Explains the 'what' (redundant)
# Increment the counter
counter += 1

5. Error Handling
Robust error handling is non-negotiable.

Fail Gracefully: Applications should handle errors gracefully without crashing.

Specific Exceptions: Catch specific exceptions rather than generic ones (e.g., catch FileNotFoundError instead of Exception).

Logging: Log errors with sufficient context (stack trace, request ID, user ID) to aid in debugging. Use appropriate log levels (ERROR, WARN, INFO, DEBUG).

User-Facing Messages: Do not expose raw error messages or stack traces to the end-user. Show a friendly, generic error message.

try {
  const data = await fetchData(url);
  processData(data);
} catch (error) {
  if (error instanceof NetworkError) {
    logger.error('Network failed for request', { url, error });
    // show user-friendly message
  } else {
    logger.error('An unexpected error occurred', { error });
    // show generic error message
  }
}

6. Testing
All new features and bug fixes must be accompanied by tests.

Unit Tests: Test individual functions and components in isolation. Aim for high test coverage of business logic.

Integration Tests: Test the interaction between different parts of the system (e.g., API and database).

Test Naming: Test descriptions should clearly state what is being tested. Use a "should do X when Y" format. Example: it('should return an error when the user is not authenticated').

CI/CD: All tests must pass in the Continuous Integration (CI) pipeline before code can be merged.

7. Security
Security is a primary concern at all stages of development.

Input Validation: Never trust user input. Sanitize and validate all data coming from external sources to prevent injection attacks (SQL, XSS).

Authentication & Authorization: Use strong, well-established libraries for authentication. Ensure proper authorization checks are performed for every request that accesses a protected resource.

Dependencies: Regularly scan for and update vulnerable dependencies using tools like npm audit or pip-audit.

Secrets Management: Never commit secrets (API keys, passwords, credentials) directly into the version control repository. Use environment variables and a secure secrets management system (e.g., AWS Secrets Manager, HashiCorp Vault).

8. Version Control (Git)
Follow these Git best practices to maintain a clean and understandable project history.

Branching:

main: Should always be stable and deployable. Direct commits are forbidden.

develop: The primary integration branch for features.

Feature Branches: Create new branches from develop for all new features and bug fixes. Use a descriptive naming convention, e.g., feature/user-authentication or fix/login-bug.

Commits:

Make small, atomic commits that represent a single logical change.

Write clear and concise commit messages. Follow the Conventional Commits specification.

Pull Requests (PRs):

All code changes must be submitted via a Pull Request.

PRs must be reviewed by at least one other developer.

PR descriptions should explain the "what" and "why" of the change. Link to relevant issue tickets.

All CI checks (linting, testing, etc.) must pass before a PR can be merged.
