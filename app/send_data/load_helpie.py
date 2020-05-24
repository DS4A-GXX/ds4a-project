import os
import base64
import logging
import app.settings as settings
from utils.csv_utils import read_csv, write_csv
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
    # dao = BasicDAO()
    files_loaded = 0
    rows_loaded = 0
    for ftl in files_to_load:
        files_loaded += 1
        log.debug(f"Reading: {data_location}/{ftl}")
        rows = read_csv(f"{data_location}/{ftl}")
        log.debug(f"{len(rows)} rows read.")
        rows_loaded_in_file = 0
        r = []
        for row in rows[1::]:
            row[3] = mask_cpf(row[3])
            r.append(row)
            rows_loaded_in_file += 1

        write_csv(r, r[0], "t8314.csv")
        rows_loaded += rows_loaded_in_file
        log.info(
            f"The file {data_location}/{ftl} was loaded with {rows_loaded_in_file}"
        )

    log.info(f"{rows_loaded} rows loaded in this batch")


def mask_cpf(cpf):
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    return encode(settings.MASK_KEY, cpf)


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
