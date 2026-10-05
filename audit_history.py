import json
import os
from datetime import datetime

HISTORY_FILE = os.path.join("data", "audit_history.json")


def save_audit(audit_data):
    os.makedirs("data", exist_ok=True)

    history = load_history()

    audit_data["saved_at"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    history.append(audit_data)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    except (json.JSONDecodeError, OSError):
        return []