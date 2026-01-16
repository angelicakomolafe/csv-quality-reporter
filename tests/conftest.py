import sys
from pathlib import Path

# Add the repo root to PYTHONPATH so imports like `from src...` work in tests
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
