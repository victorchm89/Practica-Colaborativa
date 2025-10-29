# Guía práctica avanzada: análisis de vulnerabilidades en binarios con **Ghidra** 

> **Objetivo:** Guiar a alguien sin experiencia previa en Ghidra para auditar binarios ELF (Linux) y diseñar PoCs. 

---

## Estructura del repositorio (navegación rápida)

Archivo | Contenido | Enfoque
---|---|---
`README.md` | Introducción, requisitos y visión general | Presentación
`docs/cheatsheet_ghidra.md` | Atajos/comandos clave de Ghidra/gdb | Referencia rápida
`docs/flujo_trabajo_binario.md` | Procedimiento end-to-end (estático + dinámico + fuzzing) | Método
`docs/guia_ghidra_avanzada.md` | Ghidra a fondo: análisis, XREFs, patching, scripting | Guía extendida
`docs/ejemplos.md` | Casos prácticos: BOF, Format String, Integer Overflow (pasos + resultado esperado) | Prácticas
`docs/checklist.md` | Lista de verificación profesional (sin evidencias) | Control de calidad
`docs/report_template.md` | Plantilla de informe de hallazgos (sin evidencias) | Entrega

---

## 1) Requisitos y preparación

**SO recomendado:** Ubuntu/Debian x86_64

```bash
sudo apt update
sudo apt install -y build-essential python3 python3-venv git gdb \
                    python3-pip file binutils checksec radare2 ropper

# (Opcional) pwndbg
git clone https://github.com/pwndbg/pwndbg.git
cd pwndbg && ./setup.sh && cd ..

# Python venv + pwntools
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pwntools

# (Opcional) AFL++
sudo apt install -y afl++

# Ghidra: instalar (Java 17+); añadir ejecutable a PATH.

Si compilas 32-bit en 64-bit: sudo apt install gcc-multilib.

2) Compilar binarios de laboratorio
cd lab && make
file bins/bof bins/fmt bins/int
checksec --file=./bins/bof
checksec --file=./bins/fmt
checksec --file=./bins/int


Resultado esperado (texto, sin evidencias): se generan bof, fmt, int en lab/bins/, con mitigaciones relajadas al compilar bof y fmt.

3) Flujo de trabajo estático en Ghidra (resumen)

Proyecto Non-Shared → importar lab/bins/bof, fmt, int.

Activar: Decompiler, String References, Stack Variable Analyzer, Function ID.

Explorar secciones .text/.plt/.got/.rodata y funciones main, vuln, win.

Decompilar y anotar sinks (scanf/strcpy/memcpy/printf).

XREFs y Strings → localizar rutas y mensajes clave.

Ajustar prototipos si es necesario; patch de instrucciones (opcional, para validar hipótesis).

4) Dinámico + explotación teórica (sin evidencias)
BOF (lab/bins/bof)
1) gdb/pwndbg: `pattern create 200`; ejecutar y enviar patrón.
2) Crash → `pattern find $rsp` → offset.
3) Dirección de `win()` (símbolo/Ghidra).
4) Ajustar `scripts/exploit/bof_exploit.py` con `offset` + `win`.
**Resultado esperado:** salto a `win()`.

Format String (lab/bins/fmt)
1) Enviar `%p %p %p %p` para leaks teóricos.
2) Identificar índice del argumento controlado; considerar `%n` si procede.
**Resultado esperado:** leak de direcciones y/o escritura controlada (si RELRO lo permite).

Integer Overflow (lab/bins/int)
1) Probar `./int -1` y `./int 2147483648`.
2) Explicar efecto de signo/cast en `malloc/memset` con Ghidra.
**Resultado esperado:** comportamiento indefinido/crash por tamaño inválido.

5) Fuzzing opcional con AFL++
cd lab
make clean
CC=afl-cc CFLAGS='-O0 -g' make bof fmt int

mkdir -p afl_inputs afl_outputs
echo "AAAA" > afl_inputs/in.txt
afl-fuzz -i afl_inputs -o afl_outputs -- ./bins/fmt


Resultado esperado: nuevas entradas/crashes en afl_outputs/ (no subir evidencias).

6) Recursos

Cheatsheet: docs/cheatsheet_ghidra.md

Flujo completo: docs/flujo_trabajo_binario.md

Guía Ghidra avanzada: docs/guia_ghidra_avanzada.md

Casos prácticos: docs/ejemplos.md

Checklist: docs/checklist.md

Plantilla informe: docs/report_template.md

7) Licencia y aviso legal

Licencia MIT (ver LICENSE).
