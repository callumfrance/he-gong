import gpiozero
from time import sleep

class ViewPi:

    # TODO incorporate into a mutator for the self.strikeState
    STATES = {'idle', 'active', 'reset'}

    # Time in seconds a component ignores changes in state after an inital change
    BOUNCE_TIME = 0.05

    def __init__(self,
            contactSwitch=[2,3],
            ledVolume=4,
            potVolume=17,
            dcMotor=[18,23,24],
            muteSwitch=25,
            ):
        self.contactSwitch = [gpiozero.Button(contactSwitch[0], bounce_time=self.BOUNCE_TIME), 
                gpiozero.Button(contactSwitch[1], bounce_time=self.BOUNCE_TIME)]
        self.ledVolume = gpiozero.PWMLED(ledVolume)
        self.potVolume = gpiozero.AnalogInputDevice(potVolume)
        self.dcMotor = [ gpiozero.Motor(dcMotor[0], dcMotor[1], pwm=False), 
                gpiozero.PWMOutputDevice(dcMotor[2]) ]
        self.muteSwitch = gpiozero.Button(muteSwitch, bounce_time=self.BOUNCE_TIME)
        
        self.volumeLevel = 0
        self.strikeState = 'idle'

    @property
    def strikeState(self):
        return self._strikeState

    @strikeState.setter
    def strikeState(self, in_strike_state):
        if (in_strike_state in self.STATES):
            self._strikeState = in_strike_state
        else:
            raise ValueError("strikeState not permitted to be ", in_strike_state)

    def volume_loop(self):
        if (self.muteSwitch.is_pressed() == False):
            self.volumeLevel = self.potVolume.value() # check if this is [-1, 1] or [0, 1]
        elif (self.volumeLevel != 0):
            self.volumeLevel = 0

        self.ledVolume.value = self.volumeLevel
        self.dcMotor[1].value = self.volumeLevel

    def state_idle(self):
        if self.dcMotor[0].is_active():
            self.dcMotor[0].stop()

    def state_active(self):
        if (self.contactSwitch[0].is_pressed()):
            self.strikeState = 'reset'
        elif (self.volumeLevel > 0):
            self.dcMotor[0].forward()

    def state_reset(self):
        if (self.contactSwitch[1].is_pressed()):
            self.strikeState = 'idle'
        else:
            self.dcMotor[0].backward()
