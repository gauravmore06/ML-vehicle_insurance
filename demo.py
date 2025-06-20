# from src.logger import logging

# logging.info("this a simple info message")

# Exception
from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1+'z'

except Exception as e:
    logging.info(e)
    raise MyException(e, sys)