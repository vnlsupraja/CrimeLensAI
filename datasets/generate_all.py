"""
Master Dataset Generator
CrimeLens AI
"""

import os
import shutil
from pathlib import Path

from datasets.config import OUTPUT_FOLDER
from datasets.generators.generate_police_stations import generate_dataset as generate_police
from datasets.generators.generate_criminals import generate_dataset as generate_criminals
from datasets.generators.generate_victims import generate_dataset as generate_victims
from datasets.generators.generate_firs import generate_dataset as generate_firs
from datasets.generators.generate_transactions import generate_dataset as generate_transactions
from datasets.generators.generate_relationships import generate_dataset as generate_relationships
from datasets.generators.generate_demographics import generate_dataset as generate_demographics
import random
import numpy as np
from faker import Faker

random.seed(42)
np.random.seed(42)
Faker.seed(42)

OUTPUT_FOLDER = Path(OUTPUT_FOLDER)


def clean_output_folder():
    """
    Delete previously generated CSV files.
    """

    if OUTPUT_FOLDER.exists():

        for file in OUTPUT_FOLDER.glob("*.csv"):
            file.unlink()

    else:
        OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


def main():

    print("=" * 60)
    print("CrimeLens AI Dataset Generator")
    print("=" * 60)

    clean_output_folder()

    print("\nStep 1 : Police Stations")
    generate_police()

    print("\nStep 2 : Criminals")
    generate_criminals()

    print("\nStep 3 : Victims")
    generate_victims()

    print("\nStep 4 : FIRs")
    generate_firs()

    print("\nStep 5 : Transactions")
    generate_transactions()

    print("\nStep 6 : Relationships")
    generate_relationships()

    print("\nStep 7 : Demographics")
    generate_demographics()

    print("\n" + "=" * 60)
    print("Dataset Generation Completed Successfully")
    print("=" * 60)

    print("\nGenerated Files:")

    for file in OUTPUT_FOLDER.glob("*.csv"):

        print(f"✔ {file.name}")


if __name__ == "__main__":
    main()