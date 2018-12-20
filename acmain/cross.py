from toolbox import Debug
from claw import Claw
from statemachine import State, Transition, StateMachine
from drive import Drive

class Cross(object):

    self.turncount = 0

    drive = Drive()
    drive.turn(10) # hat noch keinen Effekt


    # wenn Farbe 'blau':
        # fahre bis Mitte
        # drehe um -90Grad auf der Stelle(links)
        # setze Richtung = 'links'
        # fahre langsam geradeaus
        # falls Farbe == 'weiß':
            # drehe um 180Grad
            # fahre geradeaus
            # falls Farbe == 'blue':
                # fahre geradeaus
                # falls Farbe == 'schwarz'
                    # first turn()
                    # folge Linie
                    # falls Hindernis:
                    # falls turncount == 1:
                    # search()
    # fahre zurück
    # drehe um 180 Grad
    # fahre geradeaus
    # falls Farbe == 'blau':
        # fahre bis Mitte
        # falls turncount = 2:
            # wenn Richtung == 'rechts'
            # drehe rechts um 90 Grad
            # elif Richtung == 'links'
            # drehe links um 90 Grad
        # folge Linie
        

    def firstTurn(self, sensorValues):
        Debug.print("Robo at Cross first Turn")
        self.turncount = 1

    def search(self):

        # stoppe motor
        self.minAbstand = self.sensIR.proximity
        # solange Abstand < Wert:
            # drehe nach rechts
            # falls (Abstand < minAbstand)
                # so lange wie (Abstand < minAbstand):
                    # minAbstand = Abstand
            # sonst:
                # drehe nach links
                # falls (Abstand < minAbstand):
                    # so lange wie (Abstand < minAbstand):
                        # minAbstand = Abstand
            # verringere Geschwindigkeit
            # fahre für 3 Sekunden
        # grab()
        # setze turncount = 2

    def grab():
        # öffne Greifarm
        # solange TouchButton = kein Signal:
            # fahre langsam auf Ball zu
        # wenn TouchButton == Signal:
            # Greifarm schließen