import os
import random
import pandas as pd

from datasets.config import OUTPUT_FOLDER
from datasets.constants import DISTRICTS

BASE_DIR = OUTPUT_FOLDER


def generate_dataset():

    demographics = []

    print("Generating Demographics Dataset...")

    for district in DISTRICTS:

        population = random.randint(800000, 12000000)

        literacy = round(random.uniform(62, 96), 2)

        unemployment = round(random.uniform(1.5, 12.0), 2)

        poverty = round(random.uniform(5.0, 35.0), 2)

        urbanization = round(random.uniform(20.0, 95.0), 2)

        migration = round(random.uniform(1.0, 15.0), 2)

        demographics.append({

            "district": district,

            "population": population,

            "literacy_rate": literacy,

            "unemployment_rate": unemployment,

            "poverty_index": poverty,

            "urbanization_rate": urbanization,

            "migration_rate": migration

        })

    df = pd.DataFrame(demographics)

    output_file = os.path.join(
        BASE_DIR,
        "demographics.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print()

    print(df.head())

    print()

    print(
        f"Generated {len(df)} District Records"
    )


if __name__ == "__main__":

    generate_dataset()