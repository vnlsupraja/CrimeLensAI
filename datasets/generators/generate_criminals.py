import os
import random
from faker import Faker
import pandas as pd

from datasets.config import NUM_CRIMINALS, OUTPUT_FOLDER
from datasets.constants import (
    DISTRICTS,
    OCCUPATIONS,
    GANGS,
    GENDERS,
    POLICE_STATIONS
)

fake = Faker("en_IN")


def calculate_risk(previous_cases, gang):
    """
    Calculate offender risk score.
    """

    score = 20

    score += previous_cases * 8

    if gang != "None":
        score += 20

    score += random.randint(0, 15)

    return min(score, 100)


def generate_criminal():
    """
    Generate one criminal record.
    """

    previous_cases = random.randint(0, 15)

    gang = random.choice(GANGS)

    district = random.choice(DISTRICTS)
    stations = POLICE_STATIONS.get(
        district,
        [
            f"{district} Town",
            f"{district} Rural",
            f"{district} East"
        ]
    )
    station = random.choice(stations)

    return {
        "criminal_id": "",

        "name": fake.name(),

        "age": random.randint(18, 65),

        "gender": random.choice(GENDERS),

        "occupation": random.choice(OCCUPATIONS),

        "gang": gang,

        "previous_cases": previous_cases,

        "risk_score": calculate_risk(previous_cases, gang),

        "phone": fake.phone_number(),

        "district": district,

        "police_station": station
    }


def generate_dataset():

    criminals = []

    print("Generating Criminal Dataset...")

    for i in range(1, NUM_CRIMINALS + 1):

        criminal = generate_criminal()

        criminal["criminal_id"] = f"CR{i:05d}"

        criminals.append(criminal)

    df = pd.DataFrame(criminals)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "criminals.csv"
    )

    df.to_csv(output_file, index=False)

    print(f"\nDataset Created Successfully")

    print(f"Rows : {len(df)}")

    print(f"Saved : {output_file}")

    print(df.head())


if __name__ == "__main__":
    generate_dataset()