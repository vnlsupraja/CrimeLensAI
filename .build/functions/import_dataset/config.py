
import os
from pathlib import Path

# ------------------------------------------------------------------
# DATASET CONFIGURATION
# ------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent


def _resolve_dataset_dir():
    candidates = [Path.cwd(), BASE_DIR]
    candidates.extend(BASE_DIR.parents)

    for candidate in candidates:
        for possible_dir in (
            candidate / "datasets" / "output",
            candidate / "functions" / "import_dataset" / "datasets",
        ):
            if possible_dir.exists():
                return str(possible_dir.resolve())

    return str((BASE_DIR / ".." / ".." / "datasets" / "output").resolve())


DATASET_DIR = _resolve_dataset_dir()

# ------------------------------------------------------------------
# IMPORT CONFIGURATION
# ------------------------------------------------------------------

BATCH_SIZE = 100

MAX_RETRIES = 3

RETRY_DELAY = 2

# ------------------------------------------------------------------
# TABLE MAPPING
# ------------------------------------------------------------------

TABLE_MAPPING = {

    "criminals.csv": "criminals",

    "victims.csv": "victims",

    "police_stations.csv": "police_stations",

    "firs.csv": "firs",

    "transactions.csv": "transactions",
    "crime_relationships.csv": "crime_relationships",
    "demographics.csv": "demographics"

}