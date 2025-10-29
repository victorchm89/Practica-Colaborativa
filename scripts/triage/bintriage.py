#!/usr/bin/env python3
"""
Resumen express de binarios: pasos/metadatos que revisar.
Uso: python3 scripts/triage/bintriage.py lab/bins/bof lab/bins/fmt ...
(muestra QUÉ revisar)
"""
import sys

KEY_STRINGS = ["win", "Introduce", "Nombre", "%s", "%p", "%n"]

def main():
    bins = sys.argv[1:]
    if not bins:
        print("Uso: bintriage.py <ruta_bin> ...")
        sys.exit(1)
    for b in bins:
        print("="*60)
        print(f"[+] Binario: {b}")
        print("[i] Metadatos: ejecutar ->")
        print(f"    file {b}")
        print(f"    readelf -a {b} | less")
        print(f"    checksec --file={b}")
        print("[i] Strings a buscar:", KEY_STRINGS)
        print("[i] En Ghidra: sinks, XREFs, prototipos, .plt/.got")
        print("-"*60)

if __name__ == "__main__":
    main()
