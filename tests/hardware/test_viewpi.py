import pytest

from hardware.viewpi import ViewPi

@pytest.fixture
def viewpi():
    """ Ensure that the pin values are mocked here so that running the test
    does not actually trigger a connected RPi if there is one
    """
    yield ViewPi()


class TestRpi:


    @staticmethod
    def test_states(viewpi):
        viewpi.strikeState = 'reset'
        assert viewpi.dcMotor[0].is_active == False
        assert viewpi.dcMotor[1].is_active == True

        viewpi.strikeState = 'active'
        assert viewpi.dcMotor[0].is_active == True
        assert viewpi.dcMotor[1].is_active == False

        viewpi.strikeState = 'idle'
        assert viewpi.dcMotor[0].is_active == False
        assert viewpi.dcMotor[1].is_active == False

    @staticmethod
    def test_volume_control(viewpi):
        assert viewpi.muteSwitch == 0
        assert viewpi.current_volume == 1.0

        viewpi.muteSwitch = 1
        assert viewpi.current_volume == 0.0
