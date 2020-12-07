HE-GONG
=======

<p align="center">
  <img width="460" src="sings.jpg">
</p>

## File Structure
- __hardware__: code concerning the Raspberry Pi Zero's GPIO
- __model__: how the code will process *mosquitto* input
- __controller__: contains the `main` of the project; hooks the *hardware* and *model* together
- __test__: pytest tests for the rest of the repository

## Built With
- Python 3
    - [gpiozero](https://gpiozero.readthedocs.io/en/stable/)
    - [pytest](https://docs.pytest.org/en/stable/)
    - [paho-mqtt](https://pypi.org/project/paho-mqtt/)
