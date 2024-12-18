import os
import logging
from datetime import datetime

## create the file with certain format of datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
## create the folder name logs in current directory thanks to getcwd()
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
## makes directory in given path and if exist skips as exist_ok=true
os.makedirs(log_path,exist_ok=True)

## combining both log path and LOG_FILE to get LOG_FILE_PATH
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

## took this code from documentation page
logging.basicConfig(
    ## file name is LOG_FILE_PATH
    filename=LOG_FILE_PATH,
    ## format as if we want to get in logging
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    ## This is the logging level as INFO 
    level=logging.INFO,
)

