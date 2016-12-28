import logging
import logging.config
import os

logging.config.fileConfig(os.getcwd().replace('/modules','')+'/log_config.ini')
