#@category Audit/Taint
# Heurística simple: marca funciones con posibles 'sources' y 'sinks' cercanos.

SOURCES = {"gets","fgets","read","scanf"}
SINKS   = {"printf","sprintf","memcpy","strcpy","system"}

fm = currentProgram.getFunctionManager()
for f in fm.getFunctions(True):
    used_src = False; used_sink = False
    for x in getReferencesTo(f.getEntryPoint()):
        caller = getFunctionContaining(x.getFromAddress())
        if not caller:
            continue
        if caller.getName() in SOURCES:
            used_src = True
        if caller.getName() in SINKS:
            used_sink = True
    if used_src and used_sink:
        print(f"[FLOW] Posible flujo SOURCE→SINK en {f.getName()} @ {f.getEntryPoint()}")
