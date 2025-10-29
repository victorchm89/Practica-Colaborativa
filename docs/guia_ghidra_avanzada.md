# Guía avanzada de Ghidra (paso a paso)

## Importación y análisis
- Proyecto **Non-Shared** → importar `lab/bins/*`.
- Activar: Decompiler, Strings, Stack Var Analyzer, Function ID, Demangler.
- Navegación: **Functions**, **Symbol Tree**, **Defined Strings**, secciones `.text/.plt/.got/.rodata`.

## Metodología
1. **Mapeo** de secciones y símbolos.
2. **Sinks**: `scanf/strcpy/memcpy/printf`.
3. **Datos de usuario**: `argv`, `stdin`, ficheros, env.
4. **Firmas**: corregir prototipos.
5. **Anotación**: hipótesis y decisiones.

## Scripting (Jython)
- `scripts/ghidra/scan_unsafe_calls.py` → llamadas peligrosas.
- `scripts/ghidra/find_user_input_sinks.py` → correlación source→sink.
- Uso: **Window → Script Manager** → ejecutar y revisar consola.

## Validación teórica (sin evidencias)
- BOF: offset + `win`.
- Format: `%p`/`%s`/`%n`.
- Integer: `-1`, `2^31`, etc.
