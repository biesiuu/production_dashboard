import sqlite3
import random
import time
from faker import Faker

fake = Faker()

def generate_data():
    conn = sqlite3.connect('db/development.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM machines WHERE active = 1")
    machines = cursor.fetchall()

    for machine in machines:
        good_part = random.random() < 0.9
        quantity = random.randint(0, 10) if good_part else random.randint(1, 2)
        event_at = fake.date_time_this_month()

        cursor.execute('''
            INSERT INTO productions (event_at, machine_id, quantity, good_part)
            VALUES (?, ?, ?, ?)
        ''', (event_at, machine[0], quantity, good_part))

    conn.commit()
    conn.close()

while True:
    generate_data()
    time.sleep(90 + random.randint(-60, 60))
