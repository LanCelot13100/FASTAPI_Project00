import logging


def setup_logger():
    logger = logging.getLogger("my_app")
    logger.setLevel(logging.DEBUG)

    # Creating console processer
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Declaring the format of logs
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    # Adding the processer to the logger
    logger.addHandler(ch)

    return logger


logger = setup_logger()
