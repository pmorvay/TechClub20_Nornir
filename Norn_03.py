#!/usr/bin/env python3


from pprint import pprint
from colorama import Fore
from datetime import datetime

from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.core.filter import F

#Configure device

#export NET_TEXTFSM=/Users/pmorvay/Documents/Cisco/Devnet/misc/nornir/ntc-templates/templates


#https://nornir.readthedocs.io/en/latest/plugins/tasks/networking.html


nr = InitNornir(config_file="config.yaml")

onlyXE = nr.filter(F(groups__contains="xesandbox"))

result = onlyXE.run(task=netmiko_send_config, config_commands=["int loo 123", "description created by nornir"])

#result = onlyXE.run(task=netmiko_send_config, config_commands=["no int loo 123"])

print_result(result)
nr.close_connections()