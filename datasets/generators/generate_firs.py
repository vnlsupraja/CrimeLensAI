import os
import random
from datetime import datetime, timedelta

import pandas as pd

from datasets.config import NUM_FIRS, OUTPUT_FOLDER
from datasets.constants import CRIME_TYPES, STATUS, POLICE_STATIONS

BASE_DIR = OUTPUT_FOLDER


def random_datetime():
    """
    Generate a random date/time within the last 5 years.
    """
    start = datetime.now() - timedelta(days=5 * 365)
    end = datetime.now()

    delta = end - start

    random_seconds = random.randint(0, int(delta.total_seconds()))

    dt = start + timedelta(seconds=random_seconds)

    return dt


def load_data():

    criminals = pd.read_csv(
        os.path.join(BASE_DIR, "criminals.csv")
    )

    victims = pd.read_csv(
        os.path.join(BASE_DIR, "victims.csv")
    )

    stations = pd.read_csv(
        os.path.join(BASE_DIR, "police_stations.csv")
    )

    return criminals, victims, stations


def generate_dataset():

    criminals, victims, stations = load_data()

    firs = []

    print("Generating FIR Dataset...")

    for i in range(1, NUM_FIRS + 1):

        criminal = criminals.sample(1).iloc[0]

        # Prefer victims from the same district
        district_victims = victims[
            victims["district"] == criminal["district"]
        ]

        if len(district_victims) == 0:
            victim = victims.sample(1).iloc[0]
        else:
            victim = district_victims.sample(1).iloc[0]

        station_rows = stations[
            stations["district"] == criminal["district"]
        ]

        if len(station_rows) == 0:
            fallback_district = next(
                (d for d in POLICE_STATIONS if d == criminal["district"]),
                None
            )
            fallback_stations = POLICE_STATIONS.get(
                fallback_district,
                [
                    f"{criminal['district']} Town",
                    f"{criminal['district']} Rural",
                    f"{criminal['district']} East"
                ]
            )
            station_name = random.choice(fallback_stations)
            station = {
                "station_name": station_name,
                "officer_name": f"Inspector {station_name}"
            }
        else:
            station = station_rows.sample(1).iloc[0]

        incident_time = random_datetime()

        fir = {

            "fir_id": f"FIR{i:06d}",

            "crime_type": random.choice(CRIME_TYPES),

            "district": criminal["district"],

            "police_station": station["station_name"],

            "fir_date": incident_time.strftime("%Y-%m-%d"),

            "crime_time": incident_time.strftime("%H:%M:%S"),

            "status": random.choice(STATUS),

            "criminal_id": criminal["criminal_id"],

            "victim_id": victim["victim_id"],

            "investigating_officer": station["officer_name"]

        }

        firs.append(fir)

    df = pd.DataFrame(firs)

    output_file = os.path.join(
        BASE_DIR,
        "firs.csv"
    )

    df.to_csv(output_file, index=False)

    print(f"\nGenerated {len(df)} FIRs")

    print(df.head())


if __name__ == "__main__":

    generate_dataset()