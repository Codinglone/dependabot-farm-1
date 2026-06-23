import sys
import time

import requests
import yaml


def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f) or {}


def check_url(url, timeout=10):
    start = time.time()
    try:
        resp = requests.get(url, timeout=timeout)
        ms = int((time.time() - start) * 1000)
        return url, resp.status_code, ms, None
    except Exception as exc:
        ms = int((time.time() - start) * 1000)
        return url, None, ms, str(exc)


def main(config_path="config.yml"):
    cfg = load_config(config_path)
    timeout = cfg.get("timeout", 10)
    exit_code = 0
    for url in cfg.get("urls", []):
        url, status, ms, err = check_url(url, timeout)
        if err:
            print(f"FAIL  {url}  {ms}ms  {err}")
            exit_code = 1
        else:
            print(f"OK    {url}  {status}  {ms}ms")
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "config.yml"))
