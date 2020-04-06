#!/usr/bin/python
import logging
import psycopg2
import app.settings as settings

log = logging.getLogger(__name__)


class BasicDAO:
    def __init__(self):
        """ Connect to the PostgreSQL database server """
        self.conn = None
        try:

            # connect to the PostgreSQL server
            self.conn = psycopg2.connect(
                user=settings.db_user,
                password=settings.db_pass,
                host=settings.db_host,
                port=settings.db_port,
                database=settings.db_name,
            )

            log.info(f"Connected to [{settings.db_host}]")

        except Exception as error:
            log.error(error)

    def execute(self, statement):
        log.debug(f"execute: {statement}")
        try:
            cur = self.conn.cursor()
            resp = cur.execute(statement)
            cur.close()
            return resp

        except Exception as error:
            log.error(error)

    def commit(self):
        log.debug("commit()")
        self.conn.commit()

    def query(self, query):
        log.debug(f"query:{query}")
        try:
            qry = self.conn.cursor()
            qry.execute(query)
            return qry.fetchall()
        except Exception as error:
            log.error(error)

    def disconnect(self):
        try:
            self.conn.close()
        except Exception as error:
            log.error(error)
