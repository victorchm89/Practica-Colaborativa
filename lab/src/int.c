#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int process(int len) {
    // VULN: no valida signo/overflow; conversión implícita hacia size_t
    char *buf = (char*)malloc(len);
    if (!buf) return -1;
    memset(buf, 'A', len);
    printf("Procesado %d bytes\n", len);
    free(buf);
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        puts("Uso: ./int <len>");
        return 1;
    }
    int len = atoi(argv[1]);
    return process(len);
}
