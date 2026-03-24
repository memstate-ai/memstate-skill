#!/usr/bin/env python3
"""
memstate_history.py — View version history for a keypath.

Usage:
  python3 memstate_history.py --project myapp --keypath auth.provider

Use the version numbers returned with memstate_get.py --at-revision N to time-travel.
"""
import argparse
import json
import os
import sys
import urllib.request

API_KEY = os.environ.get("MEMSTATE_API_KEY", "")
BASE_URL = "https://api.memstate.ai/api/v1"


def get_history(project_id=None, keypath=None):
    if not project_id or not keypath:
        print("Error: Both --project and --keypath are required", file=sys.stderr)
        return 1

    url = f"{BASE_URL}/memories/history"
    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json",
        "User-Agent": "memstate-skill/1.0",
    }

    data = {
        "project_id": project_id,
        "keypath": keypath,
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            print(json.dumps(result, indent=2))
            return 0
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - {e.read().decode('utf-8')}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="View version history for a keypath",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--project", required=True, help="Project ID")
    parser.add_argument("--keypath", required=True, help="Keypath to get history for")

    args = parser.parse_args()
    sys.exit(get_history(args.project, args.keypath))
