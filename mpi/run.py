#!/usr/bin/env python3
import subprocess
import os 

if __name__ == '__main__':
    command = 'docker run -it -u 1000:1000 -v $(pwd)/input:/input --privileged --network host --rm -v $(pwd)/..:/home/nathan mpitest bash'
    subprocess.call(command, shell=True, stderr=subprocess.DEVNULL) 
