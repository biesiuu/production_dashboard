import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("oeetools/production")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

def send_to_mqtt(data):
    #broker
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message


    client.connect("test.mosquitto.org", 1883, 60)


    client.loop_start()


    while True:

        client.publish("oeetools/production", json.dumps(data))
        print("Data sent:", data)
        #czas
        time.sleep(5)

    client.loop_stop()

def main():
    data = {
        "productions": [
            {
                "event_at": "2025-03-07 11:22:33",
                "machine_id": 1,
                "good_part": True,
                "quantity": 10
            }
        ]
    }
    send_to_mqtt(data)

if __name__ == "__main__":
    main()
