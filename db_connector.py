import sqlite3
import sys
from time import sleep


class DBConnector:

    def __init__(self):
        try:
            self.conn = sqlite3.connect('sn.db')
            self.curs = self.conn.cursor()
            print("\nconnect database OK")
        except:
            print("\nCAN'T connect to database!")
            print("\nplease check")
            print("\nprogram will exit in 3 secs")
            sleep(3)
            sys.exit(1)

    def get_record(self, sn):
        self.curs.execute("SELECT * FROM sn WHERE sn='%s'" % sn)
        record = self.curs.fetchone()
        #print(record)
        return record

    def update(self, sn, status):
        self.curs.execute("UPDATE sn SET status='%s' \
                WHERE sn='%s'" % (status, sn))
        self.conn.commit() # changes need to be made by calling commit()!

        self.curs.execute("SELECT STATUS FROM sn WHERE sn='%s'" % sn)
        result = self.curs.fetchone()
        if result[0] == status:
            print("update database OK")
            return True
        else:
            print("update database FAILED!")
            return False
