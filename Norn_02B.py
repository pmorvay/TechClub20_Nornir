#!/usr/bin/env python3


from pprint import pprint
from colorama import Fore
from datetime import datetime

from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.filter import F

#Parse output - Genie

#Config_Backup
#execute + save output


#export NET_TEXTFSM=/Users/pmorvay/Documents/Cisco/Devnet/misc/nornir/ntc-templates/templates



def get_commands(task, commands):
    dt = datetime.now()
    with open(f"outputs/{task.host.name}-{dt}.txt", "w") as output_file:
        for command in commands:
            result = task.run(task=netmiko_send_command, command_string=command, use_genie=True)
            output_file.write(f"==== {command} ==== \n {result.result} \n")

#https://nornir.readthedocs.io/en/latest/plugins/tasks/networking.html


nr = InitNornir(config_file="config.yaml")

onlyXE = nr.filter(F(groups__contains="xesandbox"))

result = onlyXE.run(task=get_commands, commands=["show cdp nei", "show version", ])
print_result(result)
nr.close_connections()