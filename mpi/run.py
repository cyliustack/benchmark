#!/usr/bin/env python3
import subprocess
import os 

if __name__ == '__main__':
    command = 'docker run -it -v $(pwd)/input:/input -v $(pwd)/..:/home/nathan --privileged --network host --rm  mpitest bash'
    subprocess.call(command, shell=True, stderr=subprocess.DEVNULL) 
