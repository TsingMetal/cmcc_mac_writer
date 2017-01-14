 ############################################################
# Config informations.                                        #
# Please note:                                                #
# 1, "'"(single quote) can't be removed from string values    #
# 2, all string values are CASE-SENSITIVE.                    #
# 3, program need to be restarted to make changes take effect #
 #############################################################


### host ip and port ###
HOST = '192.168.8.1'
PORT = 23             

### acount to login ###
USER   = 'root'         
PASSWD = 'taZz@01'    

### whether to show details of test  ###
### 1 to show, 0 to not. default 0   ###
VERBOSE = 0

### whether to clear screen after each test ###
### 1 to clear, 0 to not, default 0         ###
CLEAR_SCREEN = 1

### whether to log test infomation  ###
### 1 to log, 0 to not. default 0   ###
LOG = 0

### whether to verify macs ###
### 1 to verify, 0 to not  ###
CHECK_MAC = 0

### whether to reboot device after test ###
### 1 to reboot, 0 to not, default not  ###
AUTO_REBOOT = 0

### wlan mac writing commands ###
WLAN_COMMAND_1  = 'iwpriv ra0 e2p 04=%s\n'
WLAN_COMMAND_2  = 'iwpriv ra0 e2p 06=%s\n'
WLAN_COMMAND_3  = 'iwpriv ra0 e2p 08=%s\n'

### lan mac wrinting commands ###
LAN_COMMAND_1   = 'iwpriv ra0 e2p 28=%s\n'
LAN_COMMAND_2   = 'iwpriv ra0 e2p 2A=%s\n'
LAN_COMMAND_3   = 'iwpriv ra0 e2p 2C=%s\n'

### wan mac writing commands ###
WAN_COMMAND_1   = 'iwpriv ra0 e2p 2E=%s\n'
WAN_COMMAND_2   = 'iwpriv ra0 e2p 30=%s\n'
WAN_COMMAND_3   = 'iwpriv ra0 e2p 32=%s\n'

### sn writing commands ###
SN_COMMAND_1    = 'iwpriv ra0 e2p 150=%s\n'
SN_COMMAND_2    = 'iwpriv ra0 e2p 152=%s\n'
SN_COMMAND_3    = 'iwpriv ra0 e2p 154=%s\n'
SN_COMMAND_4    = 'iwpriv ra0 e2p 156=%s\n'
