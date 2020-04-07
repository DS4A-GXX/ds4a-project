import os
import logging
import app.settings as settings
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
            sercodigo = row[0] if row[0] else "NULL"
            valdata = row[1] if row[1] else "NULL"
            valvalor = row[2] if row[2] else "NULL"
            nivnome = row[3] if row[3] else "NULL"
            tercodigo = row[4] if row[4] else "NULL"
            sql_statement = f"INSERT INTO EDA.IPEA (SERCODIGO,VALDATA,VALVALOR,NIVNOME,TERCODIGO,CREATED_ON) VALUES ('{sercodigo}','{valdata}',{valvalor},'{nivnome}','{tercodigo}', CURRENT_TIMESTAMP)"
            dao.execute(sql_statement)
            rows_loaded_in_file += 1
        rows_loaded += rows_loaded_in_file
        log.info(
            f"The file {data_location}/{ftl} was loaded with {rows_loaded_in_file}"
        )
        dao.commit()
    log.info(f"{rows_loaded} rows loaded in this batch")


def load_territorios():
    dao = BasicDAO()
    csv_file = f"{settings.DATA_DIR}/ipea/TERRITORIOS.csv"
    log.debug(f"Reading: {csv_file}")
    rows = read_csv(f"{csv_file}")
    log.debug(f"{len(rows)} rows read.")
    rows_loaded_in_file = 0
    for row in rows[1::]:
        nivnome = row[0] if row[0] else "NULL"
        tercodigo = row[1] if row[1] else "NULL"
        ternome = row[2] if row[2] else "NULL"
        ternomepadrao = row[3] if row[3] else "NULL"
        tercapital = row[4] if row[4] else "NULL"
        terarea = row[5] if row[5] else "NULL"
        nivamc = row[6] if row[6] else "NULL"
        nivnome = nivnome.replace("'", "")
        ternome = ternome.replace("'", "")
        ternomepadrao = ternomepadrao.replace("'", "")

        sql_statement = f"INSERT INTO eda.ipea_territorios(nivnome, tercodigo, ternome, ternomepadrao, tercapital, terarea, nivamc) VALUES ('{nivnome}', '{tercodigo}', '{ternome}', '{ternomepadrao}', {tercapital}, {terarea}, {nivamc});"
        dao.execute(sql_statement)
        rows_loaded_in_file += 1

    log.info(f"The file {csv_file} was loaded with {rows_loaded_in_file}")
    dao.commit()
