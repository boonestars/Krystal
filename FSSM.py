import os
import sys
import subprocess
import time
from win32com.client import GetObject
import ctypes

PROCESS_TERMINATE = 1
PROC_NAME = "fivestars.exe"

import json

with open('c:\\git\\falco-cef\\app\\config.json') as data_file:
    config = json.load(data_file)


def main():
    print 'start'
    if count_of_processes() != foh_boh_status():
        print 'count of proc != foh boh status'
        terminate_processes()

    while (PROC_NAME in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]) and (count_of_processes() == foh_boh_status()):
            time.sleep(10)
            if (PROC_NAME not in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]):
                print 'proc no in tasklist'
                if (count_of_processes() < foh_boh_status()):
                    print 'count < foh boh status'
                    terminate_processes()
    terminate_processes()
    start()
    time.sleep(loading_time())
    main()

def foh_boh_status():
    # import pdb
    # pdb.set_trace()
    print config['plugins']['receipt'].keys()
    if (config['plugins']['auto_points']['feature']) and (config['plugins']['receipt']['com_monitor']['spmc_installed'] == 'monitoring'):
        print 'spmc monitoring'
        auto_points = 1
    else:
        print 'spmc not monitoring'
        auto_points = 0

    if config['system']['mode'] == "slave":
        print 'fivestars setup as slave'
        processes_running = 1 + auto_points
    elif (config['system']['mode'] == "master") and not (config['system']['serve']):
        processes_running = 1 + auto_points
    else:
        processes_running = 2 + auto_points

    print "processes_running: ", processes_running
    return processes_running

def terminate_processes():
    instance_pid = GetObject('winmgmts:').ExecQuery("Select * from Win32_Process where Name = '%s'" % PROC_NAME)
    for i in instance_pid:
        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, i.ProcessID)
        ctypes.windll.kernel32.TerminateProcess(handle, -1)
        ctypes.windll.kernel32.CloseHandle(handle)

def count_of_processes():
    running_processes = GetObject('winmgmts:').ExecQuery("Select * from Win32_Process where Name = 'fivestars.exe'").count
    print 'running_processes: ', running_processes
    return running_processes

def fs_exists():
    PROC_NAME in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]
    return

def start():
    subprocess.Popen(['c:\\fivestars\\fivestars.exe'])

def loading_time():
    try:
        print 'loadig time method'
        timeout = config['system']['service_manager']['process_restart_delay']
    except:
        print 'except loading time method'
        timeout = 20
    return timeout

if __name__ == '__main__':
    res = main()
    # sys.exit(res)
