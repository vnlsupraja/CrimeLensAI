import os
import random
import pandas as pd

from datasets.config import (
    NUM_TRANSACTIONS,
    OUTPUT_FOLDER
)

BASE_DIR = OUTPUT_FOLDER


def random_account():

    return f"AC{random.randint(1000000000,9999999999)}"


def random_amount():

    return round(random.uniform(500,500000),2)


def generate_dataset():

    firs = pd.read_csv(
        os.path.join(BASE_DIR,"firs.csv")
    )

    criminals = pd.read_csv(
        os.path.join(BASE_DIR,"criminals.csv")
    )

    transactions=[]

    print("Generating Transactions...")

    for i in range(1,NUM_TRANSACTIONS+1):

        fir=firs.sample(1).iloc[0]

        criminal=criminals[
            criminals["criminal_id"]==
            fir["criminal_id"]
        ].iloc[0]

        amount=random_amount()

        suspicious=False

        if amount>250000:

            suspicious=True

        transaction={

            "transaction_id":f"TR{i:07d}",

            "fir_id":fir["fir_id"],

            "criminal_id":criminal["criminal_id"],

            "from_account":random_account(),

            "to_account":random_account(),

            "amount":amount,

            "transaction_type":random.choice([

                "UPI",

                "NEFT",

                "RTGS",

                "Cash",

                "IMPS"

            ]),

            "suspicious":suspicious

        }

        transactions.append(transaction)

    df=pd.DataFrame(transactions)

    output_file=os.path.join(

        BASE_DIR,

        "transactions.csv"

    )

    df.to_csv(

        output_file,

        index=False

    )

    print(df.head())

    print(f"\nGenerated {len(df)} Transactions")


if __name__=="__main__":

    generate_dataset()