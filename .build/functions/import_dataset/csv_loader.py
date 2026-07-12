import os
import pandas as pd


class CSVLoader:

    def __init__(self, dataset_folder):

        self.dataset_folder = dataset_folder

    def load(self, filename):

        filepath = os.path.abspath(
            os.path.join(
                self.dataset_folder,
                filename
            )
        )

        if not os.path.exists(filepath):
            raise FileNotFoundError(
                f"CSV file not found: {filepath}"
            )

        df = pd.read_csv(filepath)

        df = df.fillna("")

        records = df.to_dict("records")

        if records:
            print(f"\n{filename} headers:")
            print(records[0].keys())
        else:
            print(f"\n{filename} has no records.")

        return records