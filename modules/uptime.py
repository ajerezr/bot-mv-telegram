# -*- coding: utf-8 -*-
import platform
import uptime
from datetime import timedelta
import time
import subprocess
import os
import logging

logger = logging.getLogger(__name__)


def memory_usage_ps():
    out = subprocess.Popen(['ps', 'v', '-p', str(os.getpid())], stdout=subprocess.PIPE).communicate()[0].split(b'\n')
    vsz_index = out[0].split().index(b'RSS')
    mem = float(out[1].split()[vsz_index]) / 1024
    return "{0:.2f}".format(mem)


def uptime_string(startup_time_in_seconds, last_error_time):
    # Machine info
    try:
        uname = platform.uname()
        uptime_seconds = uptime.uptime()
    except Exception as e:
        logger.exception('machine info:',e)
    # Delta uptime in human readable format
    uptime_string = str(timedelta(seconds=uptime_seconds))
    # Time now
    now = time.time()
    delta = now - startup_time_in_seconds
    bot_uptime = str(timedelta(seconds=int(delta)))
    # Get memory usage with ps
    #try:
    #    memory = memory_usage_ps()
    #except Exception as e:
    #    logger.exception('memory_usage_ps():',e)
    
    # Make messsge
    string = ""
    string += "\U0001F4BB Running on " + uname[0] + " " + uname[2] + " " + uname[4] + "\n"
    string += "\U0000231B Machine Uptime: " + uptime_string + "\n"
    string += "\U0001F916 Bot uptime: " + bot_uptime + "\n"
    if memory:
        string += "\U0001F4CA Bot memory usage: " + memory + "MB"

    if last_error_time is not None:
        delta = now - last_error_time
        last_error = str(timedelta(seconds=int(delta)))
        string += "\n\U0001F480 " + last_error + " without casualties"

    return string
