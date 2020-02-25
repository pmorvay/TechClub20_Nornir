#!/usr/bin/env python3


from pprint import pprint
from colorama import Fore
from datetime import datetime

from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.filter import F
from ro



#export NET_TEXTFSM=/Users/pmorvay/Documents/Cisco/Devnet/misc/nornir/ntc-templates/templates



def get_commands(task, commands):
    for command in commands:
        result = task.run(task=netmiko_send_command, command_string=command, use_genie=True)
        #print(f"==== {result[0].result} ====\n")


#https://nornir.readthedocs.io/en/latest/plugins/tasks/networking.html


nr = InitNornir(config_file="config.yaml")

onlyXE = nr.filter(F(groups__contains="xesandbox"))

#london_devices = nr.filter(F(groups__contains="London"))
result = onlyXE.run(task=get_commands, commands=["show int desc", ])
print_result(result)
nr.close_connections()