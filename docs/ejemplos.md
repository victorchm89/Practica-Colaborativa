# Casos prácticos 

## Caso 1 — Ret2win (BOF) en `bof`
**Pasos**
1. `gdb lab/bins/bof` → `pattern create 200`; ejecutar y enviar patrón.
2. Crash → `pattern find $rsp` → offset.
3. Ubicar `win` (símbolo/Ghidra).
4. Ajustar `scripts/exploit/bof_exploit.py`.
**Resultado esperado:** salto a `win()`.

## Caso 2 — Format string en `fmt`
**Pasos**
1. Enviar `%p %p %p %p`.
2. Identificar índice del argumento; considerar `%n`.
**Resultado esperado:** leaks y/o escritura controlada (si procede).

## Caso 3 — Integer overflow/sign en `int`
**Pasos**
1. Probar `./int -1` y `./int 2147483648`.
2. Explicar en Ghidra cómo llega el tamaño inválido a `memset`.
**Resultado esperado:** comportamiento indefinido/crash por tamaño inválido.
