# import libs

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

log_filepath = os.path.join(log_dir,"running_log.log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level = logging.INFO,
    format= logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath), # it is used to show the message in file 
        logging.StreamHandler(sys.stdout) # it is used to show the message in terminal
    ]
)


logger = logging.getLogger("mlProjectLogger")