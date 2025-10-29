#include <stdio.h>

void win() {
    puts("WIN: control alcanzado");
}

void vuln() {
    char buf[64];
    puts("Introduce tu nombre:");
    scanf("%s", buf); // VULN: sin anchura -> overflow si input > 63 bytes
    printf("Hola %s\n", buf);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
