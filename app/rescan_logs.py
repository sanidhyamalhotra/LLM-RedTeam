"""
Re-scan historical conversation logs with the current detection logic.
--------------------------------------------------------------------------
Detection rules improve over time (e.g. the whitespace-normalization
fix added after Attack #9 was found to bypass the original filter).
Old rows in the database were logged with whatever detection logic
existed AT THE TIME, so their secret_leaked flag can become stale
once detection improves.

This script re-reads every stored raw model_response and recomputes
secret_leaked using the current guardrails.contains_secret() logic,
then updates the row. Run this any time detection logic changes, so
historical stats and the dashboard reflect an accurate picture rather
than outdated flags.

Usage:
    cd app
    python rescan_logs.py
"""

import sqlite3
import os
import guardrails

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "logs", "conversations.db")


def rescan():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("SELECT id, model_response, secret_leaked FROM conversations").fetchall()

    updated_count = 0
    for row in rows:
        correct_flag = int(guardrails.contains_secret(row["model_response"]))
        if correct_flag != row["secret_leaked"]:
            conn.execute(
                "UPDATE conversations SET secret_leaked = ? WHERE id = ?",
                (correct_flag, row["id"])
            )
            updated_count += 1
            print(f"Row {row['id']}: secret_leaked corrected "
                  f"{row['secret_leaked']} -> {correct_flag}")

    conn.commit()
    conn.close()

    print(f"\nDone. {updated_count} of {len(rows)} rows corrected.")


if __name__ == "__main__":
    rescan()