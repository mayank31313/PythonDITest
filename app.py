from time import time

from cndi.annotations import AppInitilizer, Autowired
from cndi.env import loadEnvFromFile, getContextEnvironment
from flask import Flask, jsonify
from paho.mqtt.client import Client


app = Flask(__name__)

STORE = dict(mqttClient=None)

@Autowired()
def setMqttClient(client: Client):
    STORE['mqttClient'] = client
    print(STORE)

@app.route("/event")
def triggerEvent():
    client = STORE['mqttClient']
    topic = getContextEnvironment("mqtt.topic")

    client.publish(topic, time())
    return jsonify(status="OK")


if __name__ == '__main__':
    loadEnvFromFile("config.yml")

    app_initiaizer = AppInitilizer()
    app_initiaizer.componentScan("beans")
    app_initiaizer.run()

    app.run("localhost", 5000)