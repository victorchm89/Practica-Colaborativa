#@category Audit/Unsafe
# Marca llamadas peligrosas (strcpy/scanf sin ancho/memcpy...) y printf-like para revisión manual.

from ghidra.program.model.symbol import RefType

UNSAFE = {"gets","strcpy","strcat","sprintf","vsprintf","scanf","sscanf","memcpy","strncpy"}

listing = currentProgram.getListing()
fm = currentProgram.getFunctionManager()

def is_printf_like(name):
    return "printf" in name

for f in fm.getFunctions(True):
    for ins in listing.getInstructions(f.getBody(), True):
        for r in ins.getReferencesFrom():
            if r.getReferenceType() == RefType.UNCONDITIONAL_CALL:
                dest = getFunctionAt(r.getToAddress())
                if not dest:
                    continue
                name = dest.getName()
                if name in UNSAFE:
                    print(f"[UNSAFE] {f.getName()} -> {name} @ {ins.getMinAddress()}")
                elif is_printf_like(name):
                    print(f"[FMT?] Revisar formato en {f.getName()} @ {ins.getMinAddress()}")
