# Security Testing Results

## CSRF Protection

- All forms were tested for CSRF protection. Forms without valid CSRF tokens resulted in a `403 Forbidden` response, confirming that CSRF protection is correctly enforced.

## XSS Protection

- Input fields and URL parameters were tested for XSS vulnerabilities. All scripts were sanitized or rendered as plain text, indicating that XSS protection is effective.

## SQL Injection Protection

- Search fields were tested using sqlmap for SQL injection vulnerabilities. No vulnerabilities were detected, confirming that queries are properly parameterized.

## CSP Testing

- The Content Security Policy (CSP) was verified in the browser’s developer tools. The policy was correctly enforced, and only allowed domains were used for loading content.
