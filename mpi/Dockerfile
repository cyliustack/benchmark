FROM ubuntu:18.04

RUN apt update && apt install -y \
    wget \
    curl \
    vim \
    gcc \
    g++ \
    cmake \
    papi-tools \
    libpapi-dev \
    valgrind \
    strace \
    iperf \
    && rm -rf /var/lib/apt/lists/*


RUN apt update && apt install -y \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/cyliustack/scripts && \
    cp scripts/vimrc ~/.vimrc

COPY ./openmpi /opt/openmpi 

RUN adduser nathan && echo nathan:nathan | chpasswd
USER nathan
WORKDIR /home/nathan

ENV PATH=/opt/openmpi/bin:${PATH}

ENV LD_LIBRARY_PATH=/opt/openmpi/lib:${LD_LIBRARY_PATH}
