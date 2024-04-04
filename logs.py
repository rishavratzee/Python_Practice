import logging
# import logging.config
# logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
# we can log into five different levels

# logging.debug('this is a debug message')
# logging.info('this is a info message')
# logging.warning('this is a warning message')
# logging.error('this is a error message')
# logging.critical('this is a critical message')


#import logHelper

#logHandler


logger = logging.getLogger(__name__)

#create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# #level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a warning')
# logger.error('this is an error')


# try:
#     a=[1,2,3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)

# import traceback

# try:
#     a=[1,2,3]
#     val = a[4]
# except:
#     logging.error('the error is %s', traceback.format_exc())


#rotating file handler to keep the log file small

from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler('app.log',maxBytes=2000,backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello world!')
