from telnetlib import Telnet
from time import sleep

from config import *


class MacParser:

    def parse_mac(self, mac):
        '''
        divide the mac string into three subgroups evenly,
        then swap each group's first two elements and last two elements.
        '''
        for i in range(3):
            sub_mac = mac[i*4 : i*4+4]
            temp = sub_mac
            sub_mac  = temp[2 : 4]
            sub_mac += temp[0 : 2]
            yield sub_mac

    def parse_sn(self, sn):
        '''
        divide sn into 4 sub groups evenly
        '''
        for i in range(4):
            sub_sn = sn[i*4 : i*4+4]
            yield sub_sn


class MacWriter(Telnet, MacParser):
    
    def __init__(self, host='192.168.8.1',
                       port=23,
                       user='root',
                       passwd='taZz@01',
                       timeout=10):
        Telnet.__init__(self)
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.timeout=timeout

    def login(self): 
        try:
            self.open(self.host)
        except:
            return False

        try:
            self.read_until(b'login: ')
            self.write(self.user.encode('ascii') + b'\n')
            self.read_until(b'Password: ')
            self.write(self.passwd.encode('ascii') + b'\n')
        except:
            return False
        
        return True

    def write_wlan_mac(self, mac):
        result = self.parse_mac(mac)
        self.write((WLAN_COMMAND_1 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((WLAN_COMMAND_2 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((WLAN_COMMAND_3 % next(result)).encode('ascii'))
        sleep(0.2)

    def write_lan_mac(self, mac):
        result = self.parse_mac(mac)
        self.write((LAN_COMMAND_1 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((LAN_COMMAND_2 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((LAN_COMMAND_3 % next(result)).encode('ascii'))
        sleep(0.2)

    def write_wan_mac(self, mac):
        result = self.parse_mac(mac)
        self.write((WAN_COMMAND_1 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((WAN_COMMAND_2 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((WAN_COMMAND_3 % next(result)).encode('ascii'))
        sleep(0.2)

    def write_sn(self, sn):
        result = self.parse_sn(sn)
        self.write((SN_COMMAND_1 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((SN_COMMAND_2 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((SN_COMMAND_3 % next(result)).encode('ascii'))
        sleep(0.2)
        self.write((SN_COMMAND_4 % next(result)).encode('ascii'))
        sleep(0.2)

        self.write(b'. / LoadDefault\n')

    def reboot(self):
        # the 2 'if' blocks should be placed in main
        if VERBOSE or LOG:      
            self.read_until(b'\r\n\r\n\r\n') # remove newlines
            text = self.read_until(b'Default').decode()
            if VERBOSE:
                print('\n' + '*' * 16 + 'SHELL VIEW' + '*' * 16 + '\n')
                print(text)
                print('\n' + '*' * 42 + '\n')
                print('\nwait...')
                sleep(3)
            self.write(b'reboot\n')
            return text
        
        if AUTO_REBOOT:
            self.write(b'reboot\n')
        else:
            self.write(b'exit\n')
            self.close()
