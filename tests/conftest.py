import sys
from pathlib import Path

# Add repository root so `import src.*` works
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
