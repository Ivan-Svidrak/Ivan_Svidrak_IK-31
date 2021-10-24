import datetime
import sys
import logging
log = logging.getLogger()

def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime

def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def EvenOdd(bool):
    for i in range(0,101):
        if bool and i % 2 == 0:
            print(i)
        elif not bool and i%2 != 0:
            print(i)

def error(x,y):
    try:
        a = x/y
        log.info("Програма виконалась")
        return a
    except Exception as ERROR:
        log.error("Помилка")