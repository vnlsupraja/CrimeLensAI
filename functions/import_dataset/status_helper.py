from datetime import datetime

from constants import (
    IMPORT_STATUS_TABLE,
    SUCCESS,
    FAILED
)


class StatusHelper:

    def __init__(self, app):

        self.table = app.datastore().table(
            IMPORT_STATUS_TABLE
        )

    def get_all_status(self):
        """
        Returns all status records.
        """

        try:

            rows = self.table.get_rows()

            if rows is None:
                return []

            return rows

        except Exception:

            return []

    def get_status(
        self,
        table_name
    ):
        """
        Return the latest import status for a table, if any.
        """

        rows = self.get_all_status()

        for row in rows:

            if row.get("table_name") == table_name:
                return row

        return None

    def mark_completed(
        self,
        table_name,
        rows_imported
    ):

        self.table.insert_row({

            "table_name": table_name,

            "status": SUCCESS,

            "rows_imported": rows_imported,

            "imported_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        })

    def mark_failed(
        self,
        table_name,
        message
    ):

        self.table.insert_row({

            "table_name": table_name,

            "status": FAILED,

            "rows_imported": 0,

            "imported_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "error_message": str(message)

        })