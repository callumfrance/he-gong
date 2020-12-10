from hardware.viewpi import ViewPi
from model.slack_commands import *
from model.mqtt_commands import MqttCommands


def main():
    viewpi = ViewPi()
    mqttCommands = MqttCommands()


if __name__ == '__main__':
    main()
