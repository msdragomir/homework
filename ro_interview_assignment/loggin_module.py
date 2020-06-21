import logging


def get_logger(logger_name, level):
    """
    Create logger with the specified name, configure the logger level
    and console handler
    """
    # Set logging level
    logging_level = getattr(logging, level, logging.NOTSET)

    # Create logger
    logger = logging.getLogger(logger_name)

    # Set logger level
    logger.setLevel(logging_level)

    # Configure console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging_level)

    # Create formatter and add it to the handler
    console_handler_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s - %(message)s')
    console_handler.setFormatter(console_handler_formatter)

    # Add the file handler to the logger
    logger.addHandler(console_handler)

    return logger
