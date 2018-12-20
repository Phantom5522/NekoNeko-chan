from toolbox import Debug
from toolbox import Debug
from claw import Claw
from statemachine import State, Transition, StateMachine
from cross import Cross
from drive import Drive

class Cross(object):

    self.turncount = 0

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
        # setze turncount = 2
