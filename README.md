# url-health-monitor

Lightweight command-line URL uptime checker. Reads a list of URLs from a YAML
config and reports HTTP status + latency for each.

## Usage

    python check.py config.yml

## Config format

```yaml
urls:
  - https://example.com
  - https://github.com
timeout: 10
```

## Dependencies

See `requirements.txt`.