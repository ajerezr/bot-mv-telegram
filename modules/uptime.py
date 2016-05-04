# -*- coding: utf-8 -*-
import platform
import uptime
from datetime import timedelta
import time
import subprocess
import os

def memory_usage_ps():
    import subprocess
    out = subprocess.Popen(['ps', 'v', '-p', str(os.getpid())],stdout=subprocess.PIPE).communicate()[0].split(b'\n')
    vsz_index = out[0].split().index(b'RSS')
    mem = float(out[1].split()[vsz_index]) / 1024
    return "{0:.2f}".format(mem)

def uptime_string(startup_time_in_seconds):
	#Machine info
	uname = platform.uname()
	uptime_seconds = uptime.uptime()
	#Delta uptime in human readable format
	uptime_string = str(timedelta(seconds = uptime_seconds))
	#Time now
	now = time.time()
	delta = now-startup_time_in_seconds
	bot_uptime = str(timedelta(seconds=int(delta)))
	#Get memory usage with ps
	memory = memory_usage_ps()
	#Make messsge
	string=""
	string+="\U0001F4BB Running on "+uname[0]+" "+uname[2]+" "+uname[4]+"\n"
	string+="\U0000231B Machine Uptime: "+uptime_string+"\n"
	string+="\U0001F916 Bot uptime: "+bot_uptime+"\n"
	string+="\U0001F4CA Bot mem used: "+memory+"Mb"
	return string
