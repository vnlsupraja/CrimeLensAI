import time
import logging

from config import (
    BATCH_SIZE,
    MAX_RETRIES,
    RETRY_DELAY
)


logger = logging.getLogger()


class DataStoreHelper:

    def __init__(self, app):

        self.datastore = app.datastore()

    def insert_records(
        self,
        table_name,
        records
    ):

        table = self.datastore.table(table_name)

        total_records = len(records)

        inserted = 0

        logger.info(
            f"Starting import into {table_name}"
        )

        logger.info(
            f"Total Records : {total_records}"
        )

        for start in range(
            0,
            total_records,
            BATCH_SIZE
        ):

            end = min(
                start + BATCH_SIZE,
                total_records
            )

            batch = records[start:end]

            success = False

            retry = 0

            while (
                retry < MAX_RETRIES
                and not success
            ):

                try:

                    table.insert_rows(batch)

                    inserted += len(batch)

                    logger.info(
                        f"{table_name}: "
                        f"{inserted}/{total_records}"
                    )

                    success = True

                except Exception as ex:

                    retry += 1

                    logger.warning(

                        f"Retry {retry}/"
                        f"{MAX_RETRIES}"

                    )

                    logger.warning(str(ex))

                    if retry < MAX_RETRIES:

                        wait = RETRY_DELAY * retry
                        logger.warning(
                            f"Waiting {wait} seconds..."
                        )
                        time.sleep(wait)


            if not success:

                logger.error(
                    f"Batch Failed "
                    f"{start}-{end}"
                )

                raise Exception(

                    f"Unable to import "

                    f"{table_name}"

                )

        logger.info(

            f"{table_name} "

            f"completed."

        )

        return inserted