# Checklist de análisis de binarios 

## Metadatos y mitigaciones
- [ ] `file`, `readelf -a`, `ldd`, `checksec` (NX, PIE, RELRO, Canary).
- [ ] Arquitectura/ABI/endianness, 32/64-bit.
- [ ] Secciones inusuales; símbolos (¿strippeados?).

## Superficie de entrada
- [ ] `argv`, `stdin`, ficheros, red, variables de entorno.
- [ ] Validaciones de tamaño/longitud/formato.

## Sinks prioritarios
- [ ] `str*`, `mem*`, `scanf/printf` (anchos), `system/popen`, `dlopen/dlsym`.
- [ ] Punteros a función / vtables / callbacks.

## Vulnerabilidades comunes
- [ ] BOF (stack/heap), off-by-one, OOB R/W.
- [ ] Format string (leak/write).
- [ ] Integer overflow/sign/truncation.
- [ ] UAF/Double free.
- [ ] Race/TOCTOU (tmpfiles).

## Explotación (teórica)
- [ ] Leaks posibles (stack, libc, PIE).
- [ ] Rutas ROP/ret2libc; gadgets.
- [ ] Regiones escribibles (GOT/.data/heap) y cómo validarlas.

## Documentación mínima por hallazgo
- [ ] **Descripción** (causa raíz y ubicación).
- [ ] **Cómo verificar** (pasos/comandos; sin salidas).
- [ ] **Script/PoC** (ruta en `scripts/` si aplica).
- [ ] **Resultado esperado** (1–2 líneas).
- [ ] **Mitigación** (código/flags/proceso).
