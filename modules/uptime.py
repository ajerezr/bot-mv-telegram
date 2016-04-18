# -*- coding: utf-8 -*-
import platform
import uptime
from datetime import timedelta
import time

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
	
	string="\U0001F4BB Running on "+uname[0]+" "+uname[2]+" "+uname[4]+"\n\U0000231B Machine Uptime: "+uptime_string+"\n\U0001F916 Bot uptime: "+bot_uptime
	
	return string
	