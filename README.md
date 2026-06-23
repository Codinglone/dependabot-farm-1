# url-health-monitor

Lightweight command-line URL uptime checker. Reads a list of URLs from a YAML
config and reports HTTP status + latency for each.

## Usage

```bash
python check.py config.yml
```

Sample `config.yml` is included. Output:

```
OK    https://example.com  200  120ms
FAIL  https://down.example  5000ms  ...
```

Exit code is `1` if any URL failed, `0` otherwise.

## Config format

```yaml
urls:
  - https://example.com
  - https://github.com
timeout: 10
```

## Dependencies

See `requirements.txt`.
