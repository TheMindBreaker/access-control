import sqlite3 as sl
import datetime
import os.path as path
import utils.general as general
import uuid

con = sl.connect("qr_codes.db")

def setup():
    with con:
        sql = '''
            CREATE TABLE qr_codes (
            qr_code varchar(255) DEFAULT NULL,
            red_id int(11) DEFAULT NULL,
            valid_from datetime DEFAULT current_timestamp,
            valid_to datetime DEFAULT NULL,
            status tinyint(4) DEFAULT 1,
            type tinyint(4) DEFAULT 0
            )'''
        con.execute(sql)
        con.commit()

def check_for_new():
    if general.check_connection():
        print("All OK")

def insert_new():
    with con:
        currentDateTime = datetime.datetime.now()
        uid = uuid.uuid4().hex
        sql = '''INSERT INTO qr_codes(qr_code, valid_from, type) VALUES (?,?,?)'''
        con.execute(sql, (uid,currentDateTime, 1))
        con.commit()

        
def print_all():
    with con:
        sql = "SELECT * FROM qr_codes"
        search = con.execute(sql)
        for row in search:
            print(row)

