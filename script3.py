#!/usr/bin/env python3
"""
Script 3 – Mover: processing → out
Ogni 30 secondi sposta tutti i file presenti in ./processing
nella cartella ./out
"""

import os
import shutil
import time
from datetime import datetime
from pathlib import Path

PROCESSING_DIR = Path("./processing")
OUT_DIR        = Path("./out")
INTERVAL       = 30  # secondi


def log(msg: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}", flush=True)


def move_files() -> None:
    files = [f for f in PROCESSING_DIR.iterdir() if f.is_file()]

    if not files:
        log(f"Nessun file in '{PROCESSING_DIR}'. In attesa...")
        return

    log(f"Trovati {len(files)} file in '{PROCESSING_DIR}' – sposto in '{OUT_DIR}'...")

    moved  = 0
    errors = 0

    for src in files:
        dest = OUT_DIR / src.name

        # Gestisce collisioni di nome aggiungendo un suffisso timestamp
        if dest.exists():
            suffix = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            dest = OUT_DIR / f"{src.stem}_{suffix}{src.suffix}"

        try:
            shutil.move(str(src), str(dest))
            print(f"  ✔ Spostato: {src.name} → {OUT_DIR}", flush=True)
            moved += 1
        except OSError as e:
            print(f"  ✘ Errore nello spostamento di {src.name}: {e}", flush=True)
            errors += 1

    log(f"Completato – spostati: {moved}, errori: {errors}")


def main() -> None:
    PROCESSING_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    log(f"Script 3 avviato (intervallo: {INTERVAL}s)")
    log(f"Cartella sorgente    : {PROCESSING_DIR}")
    log(f"Cartella destinazione: {OUT_DIR}")
    print("-" * 62, flush=True)

    while True:
        try:
            move_files()
        except Exception as e:
            log(f"Errore imprevisto: {e}")

        print("-" * 62, flush=True)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()