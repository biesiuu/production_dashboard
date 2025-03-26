import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta
import time
import paho.mqtt.client as mqtt
import json

fake = Faker()


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("oeetools/production")


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")


def generate_data():
    conn = sqlite3.connect('storage/development.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM machines WHERE active = 1")
    machines = cursor.fetchall()


    productions = []

    for machine in machines:
        event_at = datetime.now() - timedelta(minutes=random.randint(1, 5))
        good_part = random.choice([True, False])
        quantity = random.randint(0, 10) if good_part else random.randint(1, 2)


        cursor.execute("""
            INSERT INTO productions (event_at, machine_id, quantity, good_part, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (event_at, machine[0], quantity, good_part, datetime.now(), datetime.now()))


        production_data = {
            "event_at": event_at.strftime("%Y-%m-%d %H:%M:%S"),
            "machine_id": machine[0],
            "good_part": good_part,
            "quantity": quantity
        }
        productions.append(production_data)

    conn.commit()
    conn.close()

    return productions


def send_to_mqtt(data):
    #broker
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message


    client.connect("test.mosquitto.org", 1883, 60)

    client.loop_start()

    for production in data:
        print(f"Sending data: {production}")
        client.publish("oeetools/production", json.dumps(production))
        time.sleep(1)

    client.loop_stop()


def main():
    while True:
        #czas
        data = generate_data()
        send_to_mqtt(data)
        time.sleep(30)


if __name__ == "__main__":
    main()
