# Arsenal de un Analista: Uso Profesional de `curl`

Este recurso técnico muestra cómo usar `curl` de forma avanzada para analizar, automatizar y explotar vulnerabilidades web desde terminal. Se incluyen casos reales, comandos útiles y un flujo de trabajo profesional orientado a analistas ofensivos.

---

## Contenido

- Cheatsheet avanzada de uso de `curl` → `cheatsheets/curl-cheatsheet-avanzado.md`
- Casos reales documentados → `ejemplos/casos-practicos-con-curl.md`
- Capturas de pantalla con resultados reales → `img/`
- Diagrama de flujo de uso profesional de `curl` → `flujo/`

---

## ¿Por qué `curl`?

- Herramienta clave en pentesting real
- Permite testear XSS, IDOR, CSRF, inyecciones, bypasses
- 100% compatible con scripts y automatización
- No depende de GUI: ideal para entornos headless

---

## Flujo profesional de análisis con `curl`

```plaintext
+----------------------+
|  Recolección inicial |
+----------------------+
          ↓
+----------------------+
|  Petición GET simple |
+----------------------+
          ↓
+----------------------+
|  Petición POST / Auth|
+----------------------+
          ↓
+----------------------+
|  Manipulación Headers|
+----------------------+
          ↓
+----------------------+
|  Fuzzing con wordlist|
+----------------------+
          ↓
+----------------------+
|  Scripts automatizados|
+----------------------+
