import logging

# FILE DETAILS WHERE LOGS WILL BE SAVED

# asctime -> Time Format
# levelname -> Warning, Error, Critical, Info, ...
logging.basicConfig(filename="Logs.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%y-%m-%d %h:%M:%S')

k = 100
logging.info("Starting Division")
try:
    for i in range(0, 2):
        k = k / i;

except:
    logging.error("Division By Zero")

