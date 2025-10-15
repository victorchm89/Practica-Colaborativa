# Arsenal de un Analista – Uso Profesional de Burp Suite

Este proyecto documenta el uso profesional y real de **Burp Suite** como herramienta principal en el análisis y explotación de vulnerabilidades web.

Incluye flujos de trabajo, cheatsheets, capturas reales y ejemplos prácticos. Está orientado a servir como documentación interna de un equipo de análisis o como portfolio profesional.

---

## Estructura del recurso

- `cheatsheets/` → Guía avanzada de uso de Burp Suite.
- `ejemplos/` → Casos reales (XSS, IDOR, errores backend).
- `img/` → Capturas de pantalla reales de análisis.
- `flujo/` → Diagrama visual de análisis con Burp.

---

## Casos reales incluidos

- Análisis de flujo de registro vulnerable
- Explotación de IDOR en perfiles
- Evaluación del backend con errores en subida de ficheros

🔗 [Ver los casos prácticos](ejemplos/burp-xss-idor.md)

---

## Cheatsheet de Burp Suite

Una guía técnica y ofensiva con funcionalidades avanzadas para uso real.

🔗 [Accede a la cheatsheet](cheatsheets/burp-suite-avanzado.md)

---

## Diagrama de flujo del análisis

```plaintext
+-------------------------+
|  Enumeración inicial    |
+-----------+-------------+
            |
        +---v---+
        | Proxy |
        +---+---+
            |
    +-------v--------+
    | Scope Filtering |
    +-------+--------+
            |
        +---v----+
        |Repeater|
        +---+----+
            |
        +---v----+
        |Intruder|
        +---+----+
            |
        +---v----+
        |Comparer|
        +---+----+
            |
        +---v-------------------+
        | Extensiones (Autorize |
        | Logger++, Hackvertor) |
        +-----------------------+

