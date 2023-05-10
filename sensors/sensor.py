import sys
import paho.mqtt.publish as publish
import random
import json
import time

# Set the MQTT broker host and port
mqtt_host = "mosquitto"
mqtt_port = 1883

# Define the MQTT topic
mqtt_topic = "sensors/temperature"

# Get the sensor ID from the command line arguments
if len(sys.argv) < 2:
    print("Please provide a sensor ID as an argument")
    sys.exit(1)
sensor_id = sys.argv[1]

while(True):

    # Generate a random temperature value between 18 and 32
    temperature = random.randint(18, 32)

    # Create a dictionary containing the temperature value and sensor ID
    data = {"temperature": temperature, "sensor_id": sensor_id}
    print(data)

    # Convert the dictionary to a JSON string
    payload = json.dumps(data)

    # Publish the data to the MQTT topic
    publish.single(mqtt_topic, payload=payload, hostname=mqtt_host, port=mqtt_port)

    time.sleep(1)
