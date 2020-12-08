import gpiozero


class ViewPi:


    STATES = {'idle', 'active', 'reset'}

    # Time in seconds a component ignores changes in state after an inital change
    BOUNCE_TIME = 0.05

    def __init__(self,
            contactSwitch=[2,3],
            ledVolume=4,
            potVolume=17,
            motorDirection=[18,23,24],
            muteSwitch=25,
            ):
        self.contactSwitch = [gpiozero.Button(contactSwitch[0], bounce_time=self.BOUNCE_TIME), 
                gpiozero.Button(contactSwitch[1], bounce_time=self.BOUNCE_TIME)]
        self.ledVolume = gpiozero.PWMLED(ledVolume)
        self.potVolume = gpiozero.MCP3008(channel=potVolume)

        # TODO program motorDirection[2] for PWM speed control
        # see L298N motor driver documentation for details
        self.motorDirection = [ gpiozero.Motor(motorDirection[0], motorDirection[1], pwm=False), 
                gpiozero.PWMOutputDevice(motorDirection[2]) ]
        self.muteSwitch = gpiozero.Button(muteSwitch, bounce_time=self.BOUNCE_TIME)
        
        self.strikeState = 'idle'

    @property
    def strikeState(self):
        return self._strikeState

    def current_volume(self):
        vol = 0
        if (self.muteSwitch.value == 0):
            vol = 0
        elif (self.potVolume.value):
            vol = self.potVolume.value # assume [0, 1] and not [-1, 1]

        self.ledVolume = vol

        return vol

################################################################################
# State Management
################################################################################
# Probably need to redo these to make them blocking calls idk at this point
    @strikeState.setter
    def strikeState(self, in_strike_state):
        if (in_strike_state in self.STATES):
            self._strikeState = in_strike_state
            if self._strikeState == 'idle':
                self.state_idle()
            elif self._strikeState == 'active':
                self.state_active()
            elif self._strikeState == 'reset':
                self.state_reset()
        else:
            raise ValueError("strikeState not permitted to be ", in_strike_state)

    def state_idle(self):
        if self.motorDirection[0].is_active():
            self.motorDirection[0].stop()

    def state_active(self):
        if (self.contactSwitch[0].value == 1):
            self.strikeState = 'reset'
        elif (self.current_volume != 0):
            self.motorDirection[0].forward()

    def state_reset(self):
        if (self.contactSwitch[1].value == 1):
            self.strikeState = 'idle'
        else:
            self.motorDirection[0].backward()
