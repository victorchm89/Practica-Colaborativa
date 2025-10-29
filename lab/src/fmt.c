#include <stdio.h>

int main() {
    char name[64];
    setvbuf(stdout, NULL, _IONBF, 0);
    puts("Nombre:");
    fgets(name, sizeof(name), stdin);
    printf(name); // VULN: formato no constante
    return 0;
}
