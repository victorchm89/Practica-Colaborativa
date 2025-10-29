
---

```markdown
# Cheatsheet Ghidra + gdb/pwndbg 

## Ghidra — básico útil
- Importar binario → activar: **Decompiler**, **Strings**, **Stack Var Analyzer**, **Function ID**.
- Vistas: **Symbol Tree**, **Functions**, **Defined Strings**, **Program Trees**.
- Acciones:
  - XREFs: clic símbolo → **References**.
  - Renombrar: `L` / *Edit Function Signature*.
  - Comentarios: **EOL** / **Plate** (anotar hipótesis).
  - Patching: *Instruction Patch* (NOPs / forzar ramas).

## Patrones mínimos a buscar
- **BOF**: `scanf("%s", buf)` sin ancho, `strcpy/strcat`, `memcpy` con len controlable.
- **Format string**: `printf(user_input)` → `%p/%s` (leak), `%n` (write).
- **Integer overflow/sign**: tamaños, `int` vs `size_t`, multiplicaciones de tamaño.
- **UAF/Double free**: rutas de error, ownership.
- **Mitigaciones**: NX→ROP; PIE→leaks; RELRO parcial→GOT escribible; Canary→leak.

## gdb + pwndbg — imprescindibles
- Patrón: `pattern create 200` → crash → `pattern find $rsp` (`$eip` en 32-bit).
- Memoria: `vmmap`, `telescope $rsp`.
- Símbolos: `info functions`, `b main`, `ni/si`, `c`.
- ROP rápido: `ropper --file ./bin --search "ret"`.

## Auxiliares
- ELF/mitigaciones: `file`, `readelf -a`, `ldd`, `checksec --file`.
