#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from urllib import request


def send_test(webhook_url: str, message: str = "Test message from sales_data_quality_pipeline") -> int:
    payload = json.dumps({"content": message}).encode("utf-8")
    headers = {"Content-Type": "application/json", "User-Agent": "python-urllib/3"}
    req = request.Request(webhook_url, data=payload, headers=headers, method="POST")
    with request.urlopen(req, timeout=15) as resp:
        return resp.status


def main() -> int:
    webhook = os.getenv("DISCORD_WEBHOOK_URL")
    if len(sys.argv) > 1:
        webhook = sys.argv[1]

    if not webhook:
        print("No webhook URL provided. Set DISCORD_WEBHOOK_URL or pass it as an argument.")
        return 2

    try:
        status = send_test(webhook)
    except Exception as exc:
        print("Failed to send test webhook:", exc)
        return 1

    print("Discord webhook test status:", status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
