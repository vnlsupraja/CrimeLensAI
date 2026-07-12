import logging
import traceback

from flask import jsonify, make_response

import zcatalyst_sdk

from config import (
    DATASET_DIR,
    TABLE_MAPPING
)

from csv_loader import CSVLoader
from datastore_helper import DataStoreHelper
from status_helper import StatusHelper
from logger import get_logger


# ----------------------------------------------------------
# LOGGER
# ----------------------------------------------------------

logger = get_logger()
logger.setLevel(logging.INFO)


# ----------------------------------------------------------
# MAIN HANDLER
# ----------------------------------------------------------

def handler(request):

    app = zcatalyst_sdk.initialize()

    csv_loader = CSVLoader(DATASET_DIR)

    datastore = DataStoreHelper(app)

    status = StatusHelper(app)

    logger.info("=" * 70)
    logger.info("CrimeLensAI Dataset Import Started")
    logger.info("=" * 70)

    summary = []

    try:

        for csv_file, table_name in TABLE_MAPPING.items():

            logger.info("")
            logger.info("-" * 70)
            logger.info(f"TABLE : {table_name}")
            logger.info("-" * 70)

            # ---------------------------------------
            # Skip already imported tables
            # ---------------------------------------

            existing_status = status.get_status(table_name)

            if existing_status and existing_status.get("status") == "completed":

                logger.info(
                    f"Skipping {table_name} "
                    "(Already Imported)"
                )

                summary.append({

                    "table": table_name,

                    "status": "Skipped",

                    "existing_status": existing_status.get("status")

                })

                continue

            # ---------------------------------------
            # Read CSV
            # ---------------------------------------

            logger.info(f"Reading {csv_file}")

            records = csv_loader.load(csv_file)

            logger.info(

                f"{len(records)} records loaded."

            )

            # ---------------------------------------
            # Import
            # ---------------------------------------

            inserted = datastore.insert_records(

                table_name,

                records

            )

            # ---------------------------------------
            # Update Import Status
            # ---------------------------------------

            status.mark_completed(

                table_name,

                inserted

            )

            summary.append({

                "table": table_name,

                "status": "Completed",

                "rows": inserted

            })

            logger.info(

                f"{table_name} completed."

            )

        logger.info("=" * 70)
        logger.info("ALL TABLES IMPORTED")
        logger.info("=" * 70)

        logger.info("")
        logger.info("=" * 70)
        logger.info("IMPORT SUMMARY")
        logger.info("=" * 70)

        for item in summary:
            logger.info(item)

        logger.info("=" * 70)

        return make_response(

            jsonify({

                "status": "success",

                "summary": summary

            }),

            200

        )

    except Exception as e:

        logger.error(str(e))

        logger.error(traceback.format_exc())

        try:

            status.mark_failed(

                table_name,

                str(e)

            )

        except Exception:

            pass

        return make_response(

            jsonify({

                "status": "failed",

                "table": table_name,

                "error": str(e)

            }),

            500

        )