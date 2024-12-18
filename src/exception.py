import sys ## sys support the error logs to have particular details apart from customized output
from src.logger import logging

## Method define to get error message and error details in self.error_message "This method took from the documentation"
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

## created a custome exception to get the desired error message
class CustomException(Exception):
    ## defined __init__ to initialize the error messeging
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)

    def __str__(self):
        return self.error_message