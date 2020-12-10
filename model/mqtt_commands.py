import paho.mqtt.client as mqtt

(CONNECT_HOST, CONNECT_PORT, CONNECT_KEEPALIVE) = \
    ("mqtt.eclipse.org", 1883, 60)

SUBSCRIBE_TOPIC = ""

class MqttCommands:
    """Class to handle MQTT logic

    See https://pypi.org/project/paho-mqtt/#usage-and-api
    """


    def __init__(self):
        self.client = mqtt.Client()

    def make_connection(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(CONNECT_HOST, CONNECT_PORT, CONNECT_KEEPALIVE)
        # check to find a way to keep persistent with being a blocking method call
        # self.client.loop_forever()

    def on_connect(self, userdata, flags, rc):
        self.client.subscribe(SUBSCRIBE_TOPIC)

    def on_message(userdata, msg):
        print(msg.topic + " " + str(msg.payload))
