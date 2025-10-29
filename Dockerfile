# Entorno de laboratorio reproducible 
FROM ubuntu:22.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential python3 python3-pip python3-venv git gdb file binutils \
    checksec radare2 afl++ ropper && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY . /workspace
RUN make -C lab

CMD ["/bin/bash"]
