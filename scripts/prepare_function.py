"""
Copies generated CSV files into the Catalyst Function folder.

Run:

python scripts/prepare_function.py
"""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent

SOURCE = ROOT / "datasets" / "output"

DESTINATION = (
    ROOT
    / "functions"
    / "import_dataset"
    / "datasets"
)

FILES = [
    "criminals.csv",
    "victims.csv",
    "police_stations.csv",
    "firs.csv",
    "transactions.csv",
    "crime_relationships.csv",
    "demographics.csv"
]


def main():

    DESTINATION.mkdir(
        parents=True,
        exist_ok=True
    )

    print("=" * 60)
    print("Preparing Catalyst Function Dataset")
    print("=" * 60)

    copied = 0

    for file in FILES:

        src = SOURCE / file
        dst = DESTINATION / file

        if not src.exists():
            print(f"[ERROR] Missing {file}")
            continue

        shutil.copy2(src, dst)

        copied += 1

        print(f"[OK] {file}")

    print()

    print(f"{copied}/{len(FILES)} files copied.")

    print("\nDone.")


if __name__ == "__main__":
    main()