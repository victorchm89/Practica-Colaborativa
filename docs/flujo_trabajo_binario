# Flujo de trabajo profesional (binarios ELF) — SIN EVIDENCIAS

## 1) Preparación
- Compilar: `cd lab && make`.
- Ver mitigaciones: `checksec --file=lab/bins/bof` (y `fmt`, `int`).

## 2) Estático en Ghidra
1. Importar binarios.
2. Activar analizadores recomendados.
3. Localizar funciones relevantes y *sinks*.
4. Anotar hipótesis (comentarios, renombres) y XREFs.
5. (Opcional) Patching temporal.

## 3) Hipótesis de explotación
- **BOF**: offset de retorno + dirección de `win`.
- **Format**: leaks con `%p`, escritura con `%n` (si aplica).
- **Integer**: inputs negativos/grandes.

## 4) Dinámico (pasos/comandos)
- Patrón cíclico, cálculo de offset, dirección de gadgets/símbolos.
- PoCs en `scripts/exploit` (describir **resultado esperado**).

## 5) (Opcional) Fuzzing
- Instrumentar con `afl-cc`, lanzar `afl-fuzz`, triage.

## 6) Cierre
- Rellenar `docs/report_template.md`.
- Pasar `docs/checklist.md`.
