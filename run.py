import subprocess
import sys
from pathlib import Path
from rich import print as bprint

if __name__ == "__main__":
    try:
        src_path = Path(__file__).parent / "src"
        subprocess.run(
            [sys.executable, "main.py"], cwd=str(src_path), check=True
        )
    except KeyboardInterrupt:
        bprint("\n[green][SAIDA][/] Adeus!\n")
