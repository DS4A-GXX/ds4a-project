import os
import logging
from utils.csv_utils import read_csv
from utils.db import BasicDAO

log = logging.getLogger(__name__)

data_extesions = ["csv", "CSV"]


def read_dir(data_location):
    csvs = [
        file
        for file in os.listdir(data_location)
        if any(file.endswith(ext) for ext in data_extesions)
    ]
    return csvs


def load(data_location):
    files_to_load = read_dir(data_location)
    dao = BasicDAO()
    files_loaded = 0
    rows_loaded = 0
    for ftl in files_to_load:
        files_loaded += 1
        log.debug(f"Reading: {data_location}/{ftl}")
        rows = read_csv(f"{data_location}/{ftl}")
        log.debug(f"{len(rows)} rows read.")
        rows_loaded_in_file = 0
        for row in rows[1::]:
            sql_statement = f"INSERT INTO EDA.IPEA (SERCODIGO,VALDATA,VALVALOR,NIVNOME,TERCODIGO,CREATED_ON) VALUES ('{row[0]}','{row[1]}',{row[2]},'{row[3]}','{row[4]}', CURRENT_TIMESTAMP)"
            dao.execute(sql_statement)
            rows_loaded_in_file += 1
        rows_loaded += rows_loaded_in_file
        log.info(
            f"The file {data_location}/{ftl} was loaded with {rows_loaded_in_file}"
        )
        dao.commit()
    log.info(f"{rows_loaded} rows loaded in this batch")
