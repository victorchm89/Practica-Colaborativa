# ⚔️ Arsenal de un Analista: Uso Profesional de `curl`

Este proyecto técnico recoge el uso avanzado y realista de la herramienta `curl` en escenarios de análisis de vulnerabilidades web. Está orientado a analistas ofensivos, pentesters y profesionales que necesiten operar sin interfaces gráficas, integrando `curl` en sus flujos reales de análisis, automatización o scripting.

---

## 🎯 Objetivo

- Documentar un uso avanzado y eficaz de `curl` en tareas de enumeración, explotación y validación de vulnerabilidades web.
- Construir una referencia técnica útil para analistas del equipo o para formar parte de un portfolio profesional.
- Integrar ejemplos reales con capturas, comandos usados, casos explotados y resultados observables.

---

## 🧠 ¿Por qué `curl`?

`curl` es una herramienta crítica en análisis web, auditorías API y entornos donde no se puede depender de interfaces gráficas (Burp, Zap). Su versatilidad permite realizar desde pruebas de XSS o IDOR, hasta autenticaciones complejas, envío de cabeceras personalizadas, bypass de filtros o scripting automatizado.

Ventajas:
- ✅ Rápido, versátil y sin dependencias
- ✅ Ideal para scripting y automatización
- ✅ Funciona en entornos headless / remotos
- ✅ Permite total control de los headers, métodos, encoding y cuerpo

---

## 🧰 Herramientas incluidas

| Categoría           | Funcionalidad                         |
|---------------------|----------------------------------------|
| Curl (core)         | Peticiones GET, POST, PUT, DELETE      |
| Headers             | Manipulación avanzada de headers       |
| Cookies             | Autenticación manual, sesiones         |
| Fuzzing manual      | Bash + wordlists para bruteforce       |
| Upload              | Envío de ficheros, validación de tipo  |
| Debug               | Ver respuesta completa y headers       |
| Token handling      | JWT, API tokens en Authorization       |

---

## 📚 Contenido de este repositorio

- [`cheatsheets/curl-cheatsheet-avanzado.md`](cheatsheets/curl-cheatsheet-avanzado.md):  
  Comandos reales, explicaciones, flags avanzados.

- [`ejemplos/casos-practicos-con-curl.md`](ejemplos/casos-practicos-con-curl.md):  
  Casos de XSS, IDOR, login, uploads inseguros, documentados con capturas y comandos.

- `img/`:  
  Evidencias gráficas de explotación real.

- `flujo/`:  
  Diagrama de flujo de cómo integrar `curl` en una metodología ofensiva.

---

## 🔁 Diagrama de flujo profesional

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
|  Automatización Bash |
+----------------------+
