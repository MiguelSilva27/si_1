import threading
import time
import os

import random 

from simulators import GPIOsim
import simulators.keyboard as keyboard

class WarehouseStandardControl:
    keyboard_listeners=[]
    GPIO : GPIOsim = None

    def __init__(self, gpioSim : GPIOsim):
        self.GPIO = gpioSim
    
    # OPERAÇÕES X
    def moveXRight(self):
        self.GPIO.output(30, self.GPIO.HIGH)
        self.GPIO.output(31, self.GPIO.LOW)

    def moveXLeft(self):
        self.GPIO.output(30, self.GPIO.LOW)
        self.GPIO.output(31, self.GPIO.HIGH)

    def stopX(self):
        self.GPIO.output(30, self.GPIO.LOW)
        self.GPIO.output(31, self.GPIO.LOW)

    def x_moving(self):
        if self.GPIO.input(30) == self.GPIO.HIGH:
            return 1
        if self.GPIO.input(31) == self.GPIO.HIGH:
            return -1
        return 0

    def x_is_at(self):
        if self.GPIO.input(1) == self.GPIO.LOW:
            return 1
        if self.GPIO.input(2) == self.GPIO.LOW:
            return 2
        if self.GPIO.input(3) == self.GPIO.LOW:
            return 3
        if self.GPIO.input(4) == self.GPIO.LOW:
            return 4
        if self.GPIO.input(5) == self.GPIO.LOW:
            return 5
        if self.GPIO.input(6) == self.GPIO.LOW:
            return 6
        if self.GPIO.input(7) == self.GPIO.LOW:
            return 7
        if self.GPIO.input(8) == self.GPIO.LOW:
            return 8
        if self.GPIO.input(9) == self.GPIO.LOW:
            return 9
        if self.GPIO.input(10) == self.GPIO.LOW:
            return 10
        return -1
    
    def goto_X(self, x):
        current_position = self.x_is_at()

        # msg = f"current_position_{current_position},desired_position:{x}"
        # print(msg)

        if(current_position < x):
            self.moveXRight()
        if(current_position > x):
            self.moveXLeft()

        delay_event = threading.Event()
        while(current_position != x):
            delay_event.wait(timeout=0.010)
            current_position = self.x_is_at()
        self.stopX()


    # OPERAÇÕES Y
    def moveYIn(self):
        self.GPIO.output(34, self.GPIO.HIGH)
        self.GPIO.output(35, self.GPIO.LOW)

    def moveYOut(self):
        self.GPIO.output(34, self.GPIO.LOW)
        self.GPIO.output(35, self.GPIO.HIGH)

    def stopY(self):
        self.GPIO.output(34, self.GPIO.LOW)
        self.GPIO.output(35, self.GPIO.LOW)

    def y_moving(self):
        if self.GPIO.input(34) == self.GPIO.HIGH:
            return 1
        if self.GPIO.input(35) == self.GPIO.HIGH:
            return -1
        return 0

    def y_is_at(self):
        if self.GPIO.input(21) == self.GPIO.LOW:
            return 1
        if self.GPIO.input(22) == self.GPIO.LOW:
            return 2
        if self.GPIO.input(23) == self.GPIO.LOW:
            return 3
        return -1
    
    def goto_Y(self, y):
        current_position = self.y_is_at()

        if(current_position < y):
            self.moveYIn()
        if(current_position > y):
            self.moveYOut()

        delay_event = threading.Event()
        while(current_position != y):
            delay_event.wait(timeout=0.010)
            current_position = self.y_is_at()
        self.stopY()


    # OPERAÇÕES Z
    def moveZUp(self):
        self.GPIO.output(32, self.GPIO.HIGH)
        self.GPIO.output(33, self.GPIO.LOW)

    def moveZDown(self):
        self.GPIO.output(32, self.GPIO.LOW)
        self.GPIO.output(33, self.GPIO.HIGH)

    def stopZ(self):
        self.GPIO.output(32, self.GPIO.LOW)
        self.GPIO.output(33, self.GPIO.LOW)

    def z_moving(self):
        if self.GPIO.input(32) == self.GPIO.HIGH:
            return 1
        if self.GPIO.input(33) == self.GPIO.HIGH:
            return -1
        return 0

    def z_is_at(self):
        if self.GPIO.input(11) == self.GPIO.LOW:
            return 1
        if self.GPIO.input(12) == self.GPIO.LOW:
            return 2
        if self.GPIO.input(13) == self.GPIO.LOW:
            return 3
        if self.GPIO.input(14) == self.GPIO.LOW:
            return 4
        if self.GPIO.input(15) == self.GPIO.LOW:
            return 5
        if self.GPIO.input(16) == self.GPIO.LOW: #pos 1_up
            return 1.5
        if self.GPIO.input(17) == self.GPIO.LOW: #pos 2_up
            return 2.5
        if self.GPIO.input(18) == self.GPIO.LOW: #pos 3_up
            return 3.5
        if self.GPIO.input(19) == self.GPIO.LOW: #pos 4_up
            return 4.5
        if self.GPIO.input(20) == self.GPIO.LOW: #pos 5_up
            return 5.5
        return -1
    
    def goto_Z(self, z):
        current_position = self.z_is_at()

        if(current_position < z):
            self.moveZUp()
        if(current_position > z):
            self.moveZDown()

        delay_event = threading.Event()
        while(current_position != z):
            delay_event.wait(timeout=0.010)
            current_position = self.z_is_at()
        self.stopZ()

    # OPERAÇÕES LS
    def moveLSIn(self):
        self.GPIO.output(36, self.GPIO.HIGH)
        self.GPIO.output(37, self.GPIO.LOW)

    def moveLSOut(self):
        self.GPIO.output(36, self.GPIO.LOW)
        self.GPIO.output(37, self.GPIO.HIGH)

    def stopLS(self):
        self.GPIO.output(36, self.GPIO.LOW)
        self.GPIO.output(37, self.GPIO.LOW)

    def ls_moving(self):
        if self.GPIO.input(36) == self.GPIO.HIGH:
            return 1
        if self.GPIO.input(37) == self.GPIO.HIGH:
            return -1
        return 0

    def ls_is_at(self):
        if self.GPIO.input(25) == self.GPIO.HIGH:
            return 1
        if self.GPIO.input(26) == self.GPIO.HIGH:
            return 2
        return -1
    
    def goto_LS(self, ls):
        current_position = self.ls_is_at()

        if(current_position < ls):
            self.moveLSIn()
        if(current_position > ls):
            self.moveLSOut()

        delay_event = threading.Event()
        while(current_position != ls):
            delay_event.wait(timeout=0.010)
            current_position = self.ls_is_at()
        self.stopLS()



    # OPERAÇÕES RS
    def moveRSIn(self):
        self.GPIO.output(38, self.GPIO.HIGH)
        self.GPIO.output(39, self.GPIO.LOW)

    def moveRSOut(self):
        self.GPIO.output(38, self.GPIO.LOW)
        self.GPIO.output(39, self.GPIO.HIGH)

    def stopRS(self):
        self.GPIO.output(38, self.GPIO.LOW)
        self.GPIO.output(39, self.GPIO.LOW)

    def rs_moving(self):
        if self.GPIO.input(38) == self.GPIO.HIGH:
            return 1
        if self.GPIO.input(39) == self.GPIO.HIGH:
            return -1
        return 0

    def rs_is_at(self):
        if self.GPIO.input(27) == self.GPIO.HIGH:
            return 1
        if self.GPIO.input(28) == self.GPIO.HIGH:
            return 2
        return -1
    
    def goto_RS(self, rs):
        current_position = self.rs_is_at()

        if(current_position < rs):
            self.moveRSIn()
        if(current_position > rs):
            self.moveRSOut()

        delay_event = threading.Event()
        while(current_position != rs):
            delay_event.wait(timeout=0.010)
            current_position = self.rs_is_at()
        self.stopRS()


    # MOVIMENTOS COMPLEXOS
    def goto_XZ(self, x, z):
        tx = threading.Thread(target=self.goto_X, args=(x,) )
        tz = threading.Thread(target=self.goto_Z, args=(z,) )
        tx.start()
        tz.start()
        tx.join()
        tz.join()

    # Tells whether the cage has a pallet returning true or false.
    def cage_has_pallet(self):
        if self.GPIO.input(24) == self.GPIO.HIGH:
            return True
        if self.GPIO.input(24) == self.GPIO.LOW:
            return False
        return -1

    # Test if the cage is at the lower position of any cell, returning true or false.
    def isAtLowerSensor(self):
        corrent_position = self.z_is_at()
        if corrent_position % 1 == 0:
           return True
        if corrent_position % 1 == 0.5:
            return False
        return -1
         

    # Test if the cage is at the upper position of any cell, returning true or false.
    def isAtUpperSensor(self):
        corrent_position = self.z_is_at()
        if corrent_position % 1 == 0.5:
           return True
        if corrent_position % 1 == 0:
            return False
        return -1

    # Moves the pallet from inside the cage into the current cell (xx,zz).
    def putInCell(self):
        if self.isAtLowerSensor():
            self.goto_Z(self.z_is_at()+0.5)
            self.goto_Y(3)
            self.goto_Z(self.z_is_at()-0.5)
            self.goto_Y(2)


    # Moves the pallet from the current cell (xx, zz) into the cage.
    def getFromCell(self):
        if self.isAtLowerSensor():
            self.goto_Y(3)
            self.goto_Z(self.z_is_at()+0.5)
            self.goto_Y(2)
            self.goto_Z(self.z_is_at()-0.5)

    # The cage must be at the position (1,1) already. The pallet must be at ls_is_at=2. 
    # In such a state, the method moves the pallet from the left station into the cage.
    def cageReceiveFromLeftStation(self):
        if self.x_is_at() == 1 and self.z_is_at() == 1 and self.ls_is_at() == 1 and not self.cage_has_pallet(): 
            self.goto_LS(2)
            self.goto_Y(1)
            self.goto_Z(1.5)
            self.goto_Y(2)
            self.goto_Z(1)

    #The cage must be at the position (10,1) already. The cage has a 
    # pallet. In such a state, the method moves the pallet from the cage into right station.
    def cageDisposeIntoRightStation(self):
        if self.x_is_at() == 10 and self.z_is_at() == 1 and self.cage_has_pallet(): 
            self.goto_Z(1.5)
            self.goto_Y(1)
            self.goto_Z(1)
            self.goto_Y(2)
            self.goto_RS(1)


    # Tira peça
    def takePartFromRS(self):
        self.GPIO.output(43, self.GPIO.HIGH)

    # Just activates a pin (see table) to create a new pallet in the left station.
    def FeedPartLeftStation(self):
        self.GPIO.output(40, self.GPIO.HIGH)
    
    # A continuous process illustrating all working together (seen later).
    def continuous_process(self):
        i=1

    def keyboard_control(self):
        print("ESC: exit program")
        print("a:left, s: stop all, d:right, w:up, z:down, p:inside, o:outside, ")

        delay_event = threading.Event()
        while True:
            try:
                # time.sleep(0.01)
                delay_event.wait(0.01)
                key = keyboard.get_key_pressed()
                if (key == chr(27)):
                    os._exit(0)
                if key != None:
                    print(key)
                    for keyboard_handler in self.keyboard_listeners:
                        keyboard_handler(key)

                match(key):
                    case 'd': self.moveXRight()
                    case 'a': self.moveXLeft()

                    case 'g': 
                        try:
                            xx = int(input("X="))
                        except ValueError:
                            xx = 5
                        if xx >=1 and xx<=10:
                            self.goto_X(xx)
                    case 'h': 
                        try:
                            yy = int(input("Y="))
                        except ValueError:
                            yy = 1
                        if yy >=1 and yy<=3:
                            self.goto_Y(yy)
                    case 'j': 
                        try:
                            zz = float(input("Z="))
                        except ValueError:
                            zz = 1.0
                        if zz >=1.0 and zz<=5.5:
                            self.goto_Z(zz)
                    
                    case 'k': 
                        try:
                            xx = int(input("X="))
                            zz = float(input("Z="))
                        except ValueError:
                            zz = 1.0
                            xx = 1
                        if (xx >= 1.0 and xx <= 10) and (zz >=1.0 and zz<=5.5):
                            self.goto_XZ(xx, zz)

                    case 'p': self.FeedPartLeftStation()
                    case 'i': self.cageReceiveFromLeftStation()
                    case 'o': self.cageDisposeIntoRightStation()
                    
                    case 'z': self.putInCell()
                    case 'x': self.getFromCell()
                    # case 'o': self.goto_LS(2)
                    case 's':
                        self.stopX()
                        self.stopY()
                        self.stopZ()
                    case 'f': os._exit(0)

            except Exception as e:
                # Code to handle any other exception
                print(f"An error occurred: {e}")
                os._exit(0)

    def start_controller(self):
        
        for i in range (1,30):
            self.GPIO.setup(i, self.GPIO.INPUT)

        self.GPIO.setup(30, self.GPIO.OUTPUT, self.GPIO.LOW) #move x right
        self.GPIO.setup(31, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(32, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(33, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(34, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(35, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(36, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(37, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(38, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(39, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(40, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(41, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(42, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        self.GPIO.setup(43, self.GPIO.OUTPUT, self.GPIO.LOW) #move x left
        ## inicir outros atuadores aqui:

        #keyboard control
        input_thread = threading.Thread(target=self.keyboard_control)
        input_thread.start()
