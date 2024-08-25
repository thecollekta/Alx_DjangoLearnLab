# Security Testing Results

## CSRF Protection

- All forms were tested for CSRF protection. Forms without valid CSRF tokens resulted in a `403 Forbidden` response, confirming that CSRF protection is correctly enforced.

## XSS Protection

- Input fields and URL parameters were tested for XSS vulnerabilities. All scripts were sanitized or rendered as plain text, indicating that XSS protection is effective.

## SQL Injection Protection

- Search fields were tested using sqlmap for SQL injection vulnerabilities. No vulnerabilities were detected, confirming that queries are properly parameterized.

## CSP Testing

- The Content Security Policy (CSP) was verified in the browser’s developer tools. The policy was correctly enforced, and only allowed domains were used for loading content.

# Security Configuration Documentation

## HTTPS and Redirects

- `SECURE_SSL_REDIRECT` is set to `True` to redirect all HTTP requests to HTTPS.
- `SECURE_HSTS_SECONDS` is set to `31536000` seconds (1 year) to enforce HTTPS for a long duration.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS` and `SECURE_HSTS_PRELOAD` are both set to `True` to include all subdomains and allow HSTS preload.

## Secure Cookies

- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` are set to `True` to ensure cookies are only sent over HTTPS.

## Secure Headers

- `X_FRAME_OPTIONS` is set to `'DENY'` to prevent framing of the site.
- `SECURE_CONTENT_TYPE_NOSNIFF` and `SECURE_BROWSER_XSS_FILTER` are both set to `True` to enhance security against content-type sniffing and XSS attacks.
