from toolbox import Debug
from claw import Claw
from statemachine import State, Transition, StateMachine
from drive import Drive

class Cross(object):

    self.turncount = 0

    drive = Drive()
    drive.turn(10) # hat noch keinen Effekt
    drive.steerPair.on_for_degrees()

    if nchan.sensColor.calibrate_blue():
        # fahre bis Mitte
        self.turn(90)
        Richtung = 'links'
        self.speed = Config.data['pid']['fast']['speed_min'] # Geschwindigkeit verringern
        self.run()
        if nchan.sensColor.calibrate_white():
            turn(180)
            # fahre geradeaus
            if nchan.sensColor.calibrate_blue():
                # fahre geradeaus
                if nchan.sensColor.calibrate_black():
                    firstTurn(self)
                    self.run()
                    # falls Hindernis:
                    if turncount == 1:
                    # search()
        
    # fahre zurück
    turn(180)
    # fahre geradeaus
    if nchan.sensColor.calibrate_blue():
        # fahre bis Mitte
        if turncount == 2:
            if Richtung == 'rechts':
                turn(90) # drehe rechts um 90 Grad
            elif Richtung == 'links'
                turn(-90) # drehe links um 90 Grad
    self.fsm.transition("crossSecondsTurn")
        

    def firstTurn(self, sensorValues):
        Debug.print("Robo at Cross first Turn")
        self.turncount = 1

    def search(self):

        brake()
        self.minAbstand = self.sensIR.proximity
        while(Abstand < Wert):
            turn(90) # drehe nach rechts
            if(Abstand < minAbstand):
                while(Abstand < minAbstand):
                    minAbstand = Abstand
            elif:
                turn(-90) # drehe nach links
                if(Abstand < minAbstand):
                    while(Abstand < minAbstand):
                        minAbstand = Abstand
            # verringere Geschwindigkeit
            # fahre für 3 Sekunden
        # grab()
        turncount = 2

    def grab():
        self.releaseClaw()
        while sensTouch.is_pressed
            self.run()
        if sensTouch.is_pressed:
            self.closeClaw()