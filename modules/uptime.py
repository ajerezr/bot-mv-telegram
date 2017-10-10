# -*- coding: utf-8 -*-
import platform
import uptime
from datetime import timedelta
import time
import subprocess
import os
import logging

logger = logging.getLogger(__name__)

def uptime_string(startup_time_in_seconds, last_error_time):
    # Machine info
    uname = platform.uname()
    uptime_seconds = uptime.uptime()
    # Delta uptime in human readable format
    uptime_message = str(timedelta(seconds=uptime_seconds))
    # Time now
    now = time.time()
    delta = now - startup_time_in_seconds
    bot_uptime = str(timedelta(seconds=int(delta)))
    
    # Make messsge
    message = ""
    message += "\U0001F4BB Running on " + uname[0] + " " + uname[2] + " " + uname[4] + "\n"
    message += "\U0000231B Machine Uptime: " + uptime_message + "\n"
    message += "\U0001F916 Bot uptime: " + bot_uptime + "\n"
    
    return message
