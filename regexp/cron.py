#!/usr/bin/python
# -*-coding: utf-8 -*-
import re
import sys

cronTasks="""
0 * * * * wget -O - -q http://www.example.com/cron.php
0 * * * * wget -O - -q http://www.example.com/cron.php
0 * * * * wget -O - -q http://www.example.com/cron.php
"""
task = "wget  - -q http://www.example.com/cron.php -O"

#(crontab -l ; echo "0 * * * * wget -O - -q http://www.example.com/cron.php") | crontab 

def format_task(task):
    args_pat = '(\-\S+\s+(?:[^\-]\S*\s*)?)+'
    t = re.sub("\s+", " ", task)
    command = re.findall("^\s*(\S+)\s*",t)
    ar = re.findall(args_pat,t)
    if not not command: #commando no nulo []                                          
        return (command[0],ar)
    return None

def cleanCronTasks(cronTasksStr):
    tasksCleaned = re.sub("^\s*(\S\s+){5}", "", cronTasks,0,re.MULTILINE)
    tasksArray = re.split("\n",tasksCleaned)
    return tasksArray

def existsTaskElem(myTask_elem,tasks_elems):
    exists = True
    for t in tasks_elems:
        if myTask_elem[0]==t[0]:
            if len(myTask_elem[1])==len(t[1]):
                for t_arg in myTask_elem[1]:
                    if t_arg in t[1]:pass
                    else: exists = False

    return exists


tasksArray = cleanCronTasks(cronTasks)

myTask_elem = format_task(task)

tasks_elems = []

for t in tasksArray:
    tc = format_task(t)
    if tc: tasks_elems.append(tc)

for t_e in tasks_elems:
    print t_e


print existsTaskElem(myTask_elem,tasks_elems)

