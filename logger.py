import logging

def logger(): 
    logging.basicConfig(
        filename="C:\\Users\\DELL\\Desktop\\Python Projects\\weather_client\\log_database.log",
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H-%M-%S"
    )
    return logging.getLogger('log_database')

tracker = logger()