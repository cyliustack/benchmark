#!/usr/bin/env python3
import subprocess
import os 

if __name__ == '__main__':
    input_dir = 'input'
    openmpi = 'openmpi-4.0.2' 
    if not os.path.exists( openmpi + '.tar.bz2' ):
        subprocess.call('wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.2.tar.bz2', shell=True)

    subprocess.call('tar xvf %s.tar.bz2 ' % (openmpi), shell=True, stdout=subprocess.DEVNULL) 
    subprocess.call('cd %s && mkdir -p build && cd build && ../configure --prefix=$(pwd)/../../openmpi && make -j4 && make install' % (openmpi), shell=True, stdout=subprocess.DEVNULL) 
    subprocess.call('mkdir -p %s' % (input_dir) , shell=True) 
    subprocess.call('docker build --network host -t mpitest .', shell=True, stderr=subprocess.DEVNULL) 
