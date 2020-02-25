#!/usr/bin/env python3


from nornir import InitNornir
from nornir.core.filter import F

def my_task(task):
    print(f"==== {task.host} ==== {task.host['img']} ====  \n")
    #Order of the groups, sandXE has more groups, with set "img", first mentioned is used



nr = InitNornir(config_file="config.yaml")

onlyXE = nr.filter(F(groups__contains="xesandbox"))

onlyXE.run(task=my_task)


secretXE = nr.filter(F(groups__contains="xesandbox") & F(domain__contains="secret.local"))

secretXE.run(task=my_task)

#nr.filter(F(groups__contains="xesandbox") & F(domain__all=["secret.local", "xe.local"]))



nr.close_connections()