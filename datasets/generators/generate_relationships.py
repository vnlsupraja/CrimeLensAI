import os
import random
import pandas as pd

from datasets.config import (
    NUM_RELATIONSHIPS,
    OUTPUT_FOLDER
)

BASE_DIR = OUTPUT_FOLDER

RELATIONSHIP_TYPES = [
    "Associate",
    "Gang Member",
    "Family",
    "Business Partner",
    "Co-Offender",
    "Financial Link",
    "Known Contact"
]


def generate_dataset():

    criminals = pd.read_csv(
        os.path.join(BASE_DIR, "criminals.csv")
    )

    firs = pd.read_csv(
        os.path.join(BASE_DIR, "firs.csv")
    )

    relationships = []

    criminal_ids = criminals["criminal_id"].tolist()

    fir_lookup = (
        firs.groupby("criminal_id")["fir_id"]
        .apply(list)
        .to_dict()
    )

    print("Generating Criminal Relationships...")

    relationship_id = 1
    created_pairs = set()

    while relationship_id <= NUM_RELATIONSHIPS:

        source = random.choice(criminal_ids)
        target = random.choice(criminal_ids)

        if source == target:
            continue

        pair = tuple(sorted([source, target]))

        if pair in created_pairs:
            continue

        created_pairs.add(pair)

        source_firs = fir_lookup.get(source, [])
        target_firs = fir_lookup.get(target, [])

        common_firs = list(
            set(source_firs).intersection(target_firs)
        )

        relationship = {

            "relationship_id": f"REL{relationship_id:06d}",

            "source_criminal": source,

            "target_criminal": target,

            "relationship_type": random.choice(
                RELATIONSHIP_TYPES
            ),

            "shared_fir_count": len(common_firs),

            "strength_score": random.randint(1, 100),

            "active": random.choice(
                [True, True, True, False]
            )

        }

        relationships.append(relationship)

        relationship_id += 1

    df = pd.DataFrame(relationships)

    output_file = os.path.join(
        BASE_DIR,
        "crime_relationships.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print()

    print(df.head())

    print()

    print(
        f"Generated {len(df)} Criminal Relationships"
    )


if __name__ == "__main__":

    generate_dataset()