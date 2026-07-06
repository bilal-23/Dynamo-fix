The file `/app/access.log` contains an Apache-style HTTP access log. Parse it and produce a JSON summary report at `/app/report.json`.

The report must be a single JSON object with exactly these keys:

- `total_requests` — integer, the total number of log lines (each line is one request).
- `unique_ips` — integer, the number of distinct client IP addresses.
- `top_path` — string, the request path (e.g. `/index.html`) that appears most often.

Success criteria:

1. `/app/report.json` exists and is valid JSON.
2. `total_requests` equals the exact number of requests in the log.
3. `unique_ips` equals the exact number of distinct source IPs in the log.
4. `top_path` equals the request path with the highest frequency.
