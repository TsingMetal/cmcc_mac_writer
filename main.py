import os
import sys
from time import sleep

from mac_writer import MacWriter
from db_connector import DBConnector
from config import *


writer = MacWriter()
db_connector = DBConnector()

PASS = True
FAIL = False

sn = ''
macs = ['', '', '']

tested = 1


def main():
    
    while True:
        cleanup()     # clear screen before test

        while True:
            start()
            
            input_sn()

            if check_sn_mac() == FAIL:
                end()
                break

            if check_login() == FAIL:
                end()
                break

            write_macs()

            if update_db() == FAIL:
                end()
                break

            reboot()

            end()

            break


def start():
    global tested
    print("\n\nTEST STARTING...\tNO. %s" % tested)
    print("\n(input 'exit' to end program)\t")
    tested += 1


def input_sn():
    global sn
    sn = input("Input sn\t:")
    sn = sn.strip()

    if sn.lower().strip() == 'exit':
        print("\nprogram ending...")
        sleep(2)
        sys.exit(0)
    while len(sn) != 16:
        sn = input("Wrong sn!\nInput again\t:")
        sn = sn.strip()


def check_login():
    print("\nconnecting to host...")
    for i in range(10):
        if writer.login():
            print("connect OK\nlogin OK")
            return PASS
        else:
            print("retry+" + str(i+1))
            sleep(1)
    print("\nconnect to host FAIL\n\nTEST FAILED!")
    sleep(3)
    return FAIL


def check_sn_mac():
    record = db_connector.get_record(sn)
    if record == None:
        print("sn %s NOT FOUND!" % sn)
        sleep(3)
        return FAIL
    elif record[-1] == 'used':
        print("sn %s already USED!" % sn)
        sleep(3)
        return FAIL
    print("%s found, sn OK" % sn)

    if CHECK_MAC:
        get_macs()
        print("\nchecking mac...")
        if len(set(macs)) != 3:
            print("INVALID macs! please check.")
            return FAIL
            sleep(3)
        elif record[2] != macs[0]:
            print("wlan_mac %s NOT MATCH db mac! %s" 
                    % (macs[0], record[2]))
            sleep(3)
            return FAIL
        elif record[3] != macs[1]:
            print("lan_mac %s NOT MATCH db mac! %s"
                    % (macs[1], record[2]))
            return FAIL
            sleep(3)
        elif record[4] != macs[2]:
            print("wan_mac %s NOT MATCH db mac! %s"
                    % (macs[2], record[4]))
            return FAIL
            sleep(3)
    else:
        macs[0] = record[2]
        macs[1] = record[3]
        macs[2] = record[4]

    print("check sn and macs OK")
    sleep(0.5)
    return PASS


def write_macs():
    wlan_mac = macs[0]
    lan_mac  = macs[1]
    wan_mac  = macs[2]

    print('\n' + '-' * 16, 'SN & MAC', '-' * 16, '')
    print("SN      \t=>\t%s" % sn)
    print("WLAN_MAC\t=>\t%s" % wlan_mac)
    print("LAN_MAC \t=>\t%s" % lan_mac)
    print("WAN_MAC \t=>\t%s" % wan_mac)
    print('-' * 42)

    write_wlan_mac(wlan_mac)
    write_lan_mac(lan_mac)
    write_wan_mac(wan_mac)
    write_sn(sn)


def update_db():
    print("\nupdating database...")
    if db_connector.update(sn, 'used'):
        return PASS
        sleep(0.5)
    else:
        return FAIL


def log():
    pass


def reboot():
    text = writer.reboot()
    if LOG and text != None:
        logger.log(text)
    print("\nreset OK")
    sleep(0.5)


def end():
    print("\n\nTEST ENDING...")
    print("\ntest will restart in 3 secs")
    sleep(1)
    print("\n2")
    sleep(1)
    print("\n1")
    sleep(1)
    print("\n0")
    sleep(2)
    cleanup()


def input_mac(prompt):
    mac = input("\nInput " + prompt + "\t:")
    while len(mac) != 12:
        mac = input("Wrong mac!\nInput again\t:")
    return mac.strip().upper()


def get_macs():
    macs[0] = input_mac('wlan_mac')
    macs[1] = input_mac('lan_mac')
    macs[2] = input_mac('wan_mac')


def verify_macs(macs):
    return PASS


def write_wlan_mac(mac):
    print("\nwriting wlan_mac...")
    writer.write_wlan_mac(mac)
    print("write wlan_mac OK")
    sleep(0.5)


def write_lan_mac(mac):
    print("\nwriting lan_mac...")
    writer.write_lan_mac(mac)
    print("write lan mac OK")
    sleep(0.5)


def write_wan_mac(mac):
    print("\nwriting wan_mac...")
    writer.write_wan_mac(mac)
    print("write wan mac OK")
    sleep(0.5)


def write_sn(sn):
    print("\nwriting sn...") 
    writer.write_sn(sn)
    print("write sn OK")
    sleep(0.5)


def cleanup():
    global sn
    global macs
    sn = ''
    macs = ['', '', '']
    clear_screen()


def clear_screen():
    if CLEAR_SCREEN:
        if sys.platform == 'linux':
            os.system('clear')
        elif sys.platform == 'win32':
            os.system('cls')
        else: #for unkown platform
            pass



if __name__ == '__main__':
    main()
