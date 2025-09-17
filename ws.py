import threading
import time
import os

from simulators.GPIOsim import GPIOsim
import simulators.ws_server as webServer
import simulators.keyboard as keyboard

from WarehouseStandardControl import WarehouseStandardControl 

# http://localhost:8089/standard_storage/
if __name__ == "__main__":
    GPIO = GPIOsim()
    GPIO.setup(30, GPIO.OUTPUT, GPIO.LOW)  # move x right
    GPIO.setup(31, GPIO.OUTPUT, GPIO.LOW)  # move x left
    
    GPIO = GPIOsim()
    warehouseControl = WarehouseStandardControl(GPIO)
    warehouseControl.start_controller()

    # start web server for the simulator
    server_thread = threading.Thread(target=webServer.run_server, args=('localhost', 8089, GPIO))
    server_thread.start()

