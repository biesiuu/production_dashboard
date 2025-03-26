import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta
import time

fake = Faker()


def generate_data():
    conn = sqlite3.connect('storage/development.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM machines WHERE active = 1")
    machines = cursor.fetchall()

    for machine in machines:
        event_at = datetime.now() - timedelta(minutes=random.randint(1, 5))
        good_part = random.choice([True, False])
        quantity = random.randint(0, 10) if good_part else random.randint(1, 2)


        cursor.execute("""
            INSERT INTO productions (event_at, machine_id, quantity, good_part, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (event_at, machine[0], quantity, good_part, datetime.now(), datetime.now()))

        conn.commit()

    conn.close()


if __name__ == "__main__":
    while True:
        generate_data()
        time.sleep(90 + random.randint(-60, 60))
