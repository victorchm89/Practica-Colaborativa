# Informe técnico de vulnerabilidades en binarios 

**Proyecto:**  
**Binario:**  
**Versión / hash:**  
**Analista:**  
**Fecha:**

## Resumen ejecutivo
- Severidad global (CVSS aprox.):
- Vulnerabilidades clave (con severidad):

## Entorno y metodología
- SO/herramientas (versiones) y flags de compilación.
- Flujo seguido: estático (Ghidra) + dinámico (gdb/pwndbg) + fuzzing (si aplica).
- **Nota:** No se incluyen evidencias; solo pasos, comandos y scripts.

## Hallazgos

### [ID-001] Título del hallazgo (Severidad)
**Descripción**  
Causa raíz y función/archivo.

**Ubicación**  
Función, offset/dirección (si aplica), fichero/línea.

**Cómo verificar (pasos y comandos)**  
1. Paso 1…  
2. Paso 2…  
3. Paso 3…

**Resultado esperado (texto)**  
- Ej.: “La ejecución alcanza `win()`” / “Crash en `memset` por tamaño negativo”.

**Mitigación**  
- Cambios de código y compilación defensiva.

---

### [ID-00X] Otro hallazgo (Severidad)
**Descripción** …  
**Ubicación** …  
**Cómo verificar** …  
**Resultado esperado** …  
**Mitigación** …

## Recomendaciones generales
- Compilar con:
```D_FORTIFY_SOURCE=2 -fstack-protector-strong -fPIE -pie -Wl,-z,relro,-z,now```
- Sustituir funciones inseguras; límites en `scanf/printf`; usar *sanitizers* en QA.

