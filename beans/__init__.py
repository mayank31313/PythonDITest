from cndi.annotations import Bean
from paho.mqtt.client import Client

@Bean()
def getMqttClient() -> Client:
    client = Client()
    client.connect("localhost", 1883)
    client.loop_start()
    return client