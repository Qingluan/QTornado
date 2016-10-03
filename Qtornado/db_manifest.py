from Qtornado.log import LogControl
from Qtornado.db import *

LogControl.LOG_LEVEL |= LogControl.INFO

def get_tables(tables_obj):
    for k in tables_obj.__dict__:
        if not k.startswith("_"):
            yield k, getattr(tables_obj, k)


class DbManifest():
    
    def __init__(self, db_connect_cmd, tables):
        con = dict([e.split("=") for e in db_connect_cmd.replace('"','').split(',')])
        self.handle = SqlEngine(**con)
        self.tables = tables

    def db_created(self):
        for name, table in get_tables(self.tables):
            if isinstance(table, dict):
                LogControl.info(self.handle.create(name, **table))

    def db_update(self):
        for name, table in get_tables(self.tables):
            try:
                self.handle.alter(name, **table)
            except Exception as e:
                LogControl.err(name)
                LogControl.err(e)

    def db_drop(self, name):
        self.handle.drop_table(name)
        LogControl.info("delete table ", name)

        