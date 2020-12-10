import pytest

from model.mqtt_commands import MqttCommands

@pytest.fixture
def mqttcomm():
    yield MqttCommands()


class TestMqttCommands:


    def test_class_build(mqttcomm):
        pass

    def test_on_connect(mqttcomm):
        pass

    def test_on_message(mqttcomm):
        pass
