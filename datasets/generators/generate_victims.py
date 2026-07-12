import os
import random
from faker import Faker
import pandas as pd

from datasets.config import (
    NUM_VICTIMS,
    OUTPUT_FOLDER
)

from datasets.constants import (
    DISTRICTS,
    OCCUPATIONS,
    GENDERS,
    EDUCATION,
    POLICE_STATIONS
)

fake = Faker("en_IN")


def generate_victim():

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

        "victim_id": "",

        "name": fake.name(),

        "age": random.randint(18, 70),

        "gender": random.choice(GENDERS),

        "occupation": random.choice(OCCUPATIONS),

        "education": random.choice(EDUCATION),

        "income": random.randint(150000, 1200000),

        "district": district,

        "police_station": station,

        "phone": fake.phone_number(),

        "address": fake.address().replace("\n", ", ")

    }


def generate_dataset():

    victims = []

    print("Generating Victim Dataset...")

    for i in range(1, NUM_VICTIMS + 1):

        victim = generate_victim()

        victim["victim_id"] = f"VI{i:05d}"

        victims.append(victim)

    df = pd.DataFrame(victims)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "victims.csv"
    )

    df.to_csv(output_file, index=False)

    print(f"\nDataset Created Successfully")

    print(f"Rows : {len(df)}")

    print(f"Saved : {output_file}")

    print(df.head())


if __name__ == "__main__":
    generate_dataset()