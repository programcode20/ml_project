import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log" #creates a timestamped log file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #creates the logs folder path in the current directory
os.makedirs(logs_path,exist_ok=True)  #creates the folder if it doesn’t exist

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #combines folder + file name

logging.basicConfig(  #configures where and how logs are written
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,
)

logger= logging.getLogger()