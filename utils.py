import subprocess
from time import sleep
import random



def delayer():
    sleep(random.uniform(0.5, 4))

class CommandRunner():
    

    def __init__(self):
        pass
        

    
    def runCommand(self,newCommand):
        cmd = subprocess.check_output(newCommand,shell=True, universal_newlines=True)
        if( cmd == '' ):
            cmd = "No return value"

        print("Running command: "+ newCommand)
        print("Output: " + cmd)
        delayer()
        

    