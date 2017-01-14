import os
import sqlite3


def create_sn_mac_db():
    '''
    create a sqlite database for sn and mac.
    this module is one-off.
    it could be removed once the datas had been stored.
    however it is kept for reuse in case of adding new data.
    '''
    conn = sqlite3.connect('sn.db') # database name 'sn.db' 
    curs = conn.cursor()

    curs.execute(       # table name 'sn'
        '''
        CREATE TABLE sn (           
            id          INTEGER,
            sn          TEXT        PRIMARY KEY,
            wlan_mac    TEXT,
            lan_mac     TEXT,
            wan_mac     TEXT,
            status      TEXT
        )
        '''
    )

    query = 'INSERT INTO sn VALUES (?,?,?,?,?,?)'

    sn_data = open('sn.csv', 'r') 
    for line in sn_data.readlines():
        line = line.rstrip()        # remove '\n' at the end
        print(line)
        lst = line.split('\t') 
        curs.execute(query, lst)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    if os.path.exists('sn.db'):
        print('daba already created')
    else:
        create_sn_mac_db()
