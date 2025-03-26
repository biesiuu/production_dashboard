import sqlite3
import json
import time
from datetime import datetime, timedelta

#pliki
DB_PATH = "storage/development.sqlite3"
JSON_FILE = "results.json"
CHECK_INTERVAL = 300  # 5 minut

def fetch_productions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    #czas
    last_24h = datetime.now() - timedelta(hours=24)
    last_5min = datetime.now() - timedelta(minutes=5)

    cursor.execute("""
        SELECT event_at, machine_id, good_part, quantity 
        FROM productions 
        WHERE event_at >= ?
    """, (last_24h.strftime("%Y-%m-%d %H:%M:%S"),))

    rows = cursor.fetchall()
    conn.close()

    productions = []
    for row in rows:
        event_at = row[0].split(".")[0]
        event_time = datetime.strptime(event_at, "%Y-%m-%d %H:%M:%S")

        if event_time >= last_5min:
            productions.append({
                "event_at": event_at,
                "machine_id": row[1],
                "good_part": bool(row[2]),
                "quantity": row[3]
            })

    return {"productions": productions}

def save_to_json(data):
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

def main():
    while True:
        data = fetch_productions()
        save_to_json(data)
        print(f"Zapisano {len(data['productions'])} rekordów do {JSON_FILE}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
