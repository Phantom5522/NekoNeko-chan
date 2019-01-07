from toolbox import Debug

class Cross(object):

    drive = Drive()
    drive.turn(10) # hat noch keinen Effekt
    drive.steerPair.on_for_degrees()

    if nchan.sensColor.calibrate_blue():
        if c== blue:
            clawOpen()
            turn(right)
        self.fsm.transition("checkNextExit")
        while c== white:
        turn(skip)
        UpdateTTE

        if b==black:
            distance = 0
            self.fsm.transition("findBall")

        if ball == 1:
            self.fsm.transition("followLine")
            
            elif IRevent:
                self.fsm.transition("approachBall")
                if e == TS:
                    claw lose()
                    turn(180)
                    self.fsm.transition("backToCross")
            elif distance > thr:
                turn(180)
                TTE = 1
                self.fsm.transition("backToCross")

        if c == blue and ball == 1 and TTE == 2:
            self.fsm.transition("exit")
        elif C == blue and ball == 1 TTE:
            turn(left)
            self.fsm.transition("exit")
        elif c == blue:
            turn(right)
            self.fsm.transition("checkNext")



self.fsm.states["checkNextExit"] = State("checkNextExit")
        self.fsm.states["checkNextExit"].addFunc(self.drive.followLine, self.sensValues)

self.fsm.states["findBall"] = State("findBall")
        self.fsm.states["findBall"].addFunc(self.drive.followLine, self.sensValues)

self.fsm.states["backToCross"] = State("backToCross")
        self.fsm.states["backToCross"].addFunc(self.drive.followLine, self.sensValues)

self.fsm.states["approachBall"] = State("approachBall")
        self.fsm.states["approachBall"].addFunc(self.drive.followLine'''slow''', self.sensValues)

self.fsm.states["exit"] = State("exit")
        self.fsm.states["exit"].addFunc(self.drive.followLine, self.sensValues)

def pickFollow:
	#fahre auf Mitte
	# drehe um 90 Grad nach rechts
	#fahre geradeaus
	#falls Farbe == “weiß”:
		#state["sackgasse"]
	#elif Farbe == “Schwarz”:
		#state[“search”]

self.fsm.states["sackgasse"] = State(self.cross.crossingTurn)

def turn:
	#drehe um 180 Grad
	#state["crossing"]

self.fsm.states["searching"] = State(self.cross.searchObject)

def searchObject:
	#while Sensoren kein Signal:
		#fahre Distanz
		#state[“Strecke”]+
	state[“Ball”]

self.fsm.states["strecke"] = State(self.cross.weiterFahrt)

def weiterFahrt:
	#if Ball == True:
		#folgeLinie()
	#else:
		#drehe um 180 Grad
		#fahre, bis Farbe == „Blau“
		#state[„crossing“]

    def searchBall(self):

        brake()
        self.minAbstand = self.sensIR.proximity
        while(Abstand > Wert):
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

    def grabBall():
        self.releaseClaw()
        while sensTouch.is_pressed
            self.run()
        if sensTouch.is_pressed:
            self.closeClaw()
    def firstTurn(self, sensorValues):
        Debug.print("Robo at Cross first Turn")
