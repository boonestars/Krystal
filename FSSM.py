import os
import sys
import subprocess
import time
from win32com.client import GetObject
import ctypes
from ConfigParser import NoOptionError, ConfigParser

PROCESS_TERMINATE = 1
PROC_NAME = "fivestars.exe"

config = ConfigParser()

class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp

class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[properties_section]\n'
    def readline(self):
        if self.sechead:
            try: return self.sechead
            finally: self.sechead = None
        else: return self.fp.readline()

def main():
	if count_of_processes() > foh_boh_status():
		terminate_processes()
	elif count_of_processes() == foh_boh_status()-1:
		terminate_processes()
	elif count_of_processes() < foh_boh_status()-1:
		terminate_processes()
	while (PROC_NAME in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]) and (count_of_processes() == foh_boh_status()):
           		time.sleep(10)
			if (PROC_NAME not in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]) or (count_of_processes() < foh_boh_status()):
				terminate_processes()
	terminate_processes()
	start()
	time.sleep(loading_time())
	main()

def foh_boh_status():
	try:
    		config.readfp(FakeSecHead(open('c:\\fivestars\config.ini')))
	except:
		sys.exit()

	try:
		config.get('plugins', 'auto_points') == "True"
		try:
			config.get('plugins', 'serial_port_monitor') == "True"
			auto_points = 1
		except NoOptionError:
			auto_points = 0
	except:
		auto_points = 0
		pass

	if (config.get('system','mode') == "master"):
		try:
			if (config.get('system','serve') == 'False'):
				processes = 1 + auto_points
			else:
				processes = 2 + auto_points
				return processes

		except NoOptionError:
			processes = 2 + auto_points
		return processes
	elif (config.get('system','mode') == "slave"):
		processes = 1 + auto_points
		return processes

def terminate_processes():
	instance_pid = GetObject('winmgmts:').ExecQuery("Select * from Win32_Process where Name = '%s'" % PROC_NAME)
	for i in instance_pid:
		handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, i.ProcessID)
		ctypes.windll.kernel32.TerminateProcess(handle, -1)
		ctypes.windll.kernel32.CloseHandle(handle)

def count_of_processes():
	running_processes = GetObject('winmgmts:').ExecQuery("Select * from Win32_Process where Name = 'fivestars.exe'").count
	return running_processes

def fs_exists():
	PROC_NAME in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]
	return

def start():
	subprocess.Popen(['c:\\fivestars\\fivestars.exe'])

def loading_time():
	try:
		timeout = int(config.get('system', 'process_restart_delay'))
	except NoOptionError:
		timeout = 20
	return timeout

if __name__ == '__main__':
    res = main()
    sys.exit(res)