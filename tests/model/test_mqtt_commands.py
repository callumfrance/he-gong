import pytest

from model/mqtt_commands.py import MqttCommands

@pytest.fixture
def mqttcomm():
    yield MqttCommands()


class TestMqttCommands:


    def test_class_build(mqttcomm):
        pass
