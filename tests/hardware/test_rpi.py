import pytest

from hardware.viewpi import ViewPi

@pytest.fixture
def viewpi():
    yield ViewPi()


class TestRpi:


    def test_class_build(self, viewpi):
        pass
