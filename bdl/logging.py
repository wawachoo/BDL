import logging

class Logger:
    """BDL logger facility.
    """

    def __init__(self, family, name):
        """Initializes the logger object.

        Arguments:
            family: The derived object family ('repository' or 'engine').
            name: The derived object name (ex: engine class basename).
        """
        self.logger = logging.getLogger("bdl.{}.{}".format(family, name))
        self.logger.addHandler(logging.NullHandler())
        self.name = name

    def __format_message(self, message):
        # return "{}".format(message)
        return message

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def debug(self, message):
        self.logger.debug(self.__format_message(message))

    def info(self, message):
        self.logger.info(self.__format_message(message))

    def warning(self, message):
        self.logger.warning(self.__format_message(message))

    def error(self, message):
        self.logger.error(self.__format_message(message))

    def critical(self, message):
        self.logger.critical(self.__format_message(message))
