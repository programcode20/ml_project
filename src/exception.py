
import sys
from logger import logger

def error_message_detail(error, error_detail: sys):  # function to format detailed error info, error:actual error msg,error_detail:expected to be sys, so we can access sys.exc_info()
    _, _, exc_tb = error_detail.exc_info()  # returns 3 things exception type,exception value,exception traceback

    file_name = exc_tb.tb_frame.f_code.co_filename  # from the traceback extract python file name

    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{str(error)}]"
    )

    return error_message


class CustomException(Exception):  # custom exception
    def __init__(self, error_message, error_detail: sys):  #constructor: to initialize the object when it is created
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)  # calls the above function and stores the detailed error message

    def __str__(self):  # controls what gets printed
        return self.error_message  #returns custom formatted error message



