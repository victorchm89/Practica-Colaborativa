CC=gcc
CFLAGS=-O0 -g
LDFLAGS=
BINS_DIR=./bins

all: prep bof fmt int

prep:
	mkdir -p $(BINS_DIR)

# Versiones vulnerables (laboratorio)
bof: src/bof.c
	$(CC) $(CFLAGS) -fno-stack-protector -z execstack -no-pie -o $(BINS_DIR)/bof $<

fmt: src/fmt.c
	$(CC) $(CFLAGS) -fno-stack-protector -no-pie -o $(BINS_DIR)/fmt $<

int: src/int.c
	$(CC) $(CFLAGS) -o $(BINS_DIR)/int $<

secure: prep
	$(CC) -O2 -g -D_FORTIFY_SOURCE=2 -fstack-protector-strong -fPIE \
	      src/*.c -Wl,-z,relro,-z,now -pie -o $(BINS_DIR)/secure_app

clean:
	rm -rf $(BINS_DIR)
