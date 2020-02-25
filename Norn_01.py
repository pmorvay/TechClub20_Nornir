#!/usr/bin/env python3


from nornir import InitNornir

def my_task(task):
    print(f"==== {task.host} ====  \n")



nr = InitNornir(config_file="config.yaml")

nr.run(task=my_task)
nr.close_connections()