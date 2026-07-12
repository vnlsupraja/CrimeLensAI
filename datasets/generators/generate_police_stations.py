import os
import random
import pandas as pd

from datasets.config import OUTPUT_FOLDER
from datasets.constants import DISTRICTS, POLICE_STATIONS


def generate_dataset():

    stations = []

    station_counter = 1

    for district in DISTRICTS:

        if district in POLICE_STATIONS:

            station_list = POLICE_STATIONS[district]

        else:

            station_list = [
                f"{district} Town",
                f"{district} Rural",
                f"{district} East"
            ]

        for station in station_list:

            stations.append({

                "station_id": f"PS{station_counter:04d}",

                "station_name": station,

                "district": district,

                "officer_name": f"Inspector {station}",

                "contact_number": f"080-{random.randint(20000000,99999999)}"

            })

            station_counter += 1

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    df = pd.DataFrame(stations)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "police_stations.csv"
    )

    df.to_csv(output_file, index=False)

    print(df.head())

    print(f"\nGenerated {len(df)} police stations")


if __name__ == "__main__":

    generate_dataset()