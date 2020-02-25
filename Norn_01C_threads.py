#!/usr/bin/env python3


from nornir import InitNornir


def my_task(task):
    print(f"==== {task.host} ==== {task.host['img']} ====  \n")
    #Order of the groups, sandXE has more groups, with set "img", first mentioned is used



nr = InitNornir(config_file="config.yaml")

nr.run(task=my_task)
nr.close_connections()