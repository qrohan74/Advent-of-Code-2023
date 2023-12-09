class Logger:
    """
    A class for logging purposes

    This class should be used like a singleton, most of its methods are static methods.
    """
    ERROR = 1
    WARNING = 2
    INFO = 3
    DEBUG = 4
    SPAM = 5

    level = INFO

    def __init__(self, level=INFO):
        """
        Logger creation
        Default level is info
        """
        Logger.level = level

    @classmethod
    def set_level(cls, level):
        """
        set the level of the logger
        """
        Logger.level = level

    @staticmethod
    def log(msg, level):
        """
        log a message into the standard output
        """
        if level <= Logger.level:
            print('%s - %s' % (Logger._level2str(level).rjust(10, ' '), msg))

    @staticmethod
    def error(msg):
        """
        log a message into the standard output
        """
        Logger.log(msg, Logger.INFO)

    @staticmethod
    def warning(msg):
        """
        log a warning message into the standard output
        """
        Logger.log(msg, Logger.WARNING)

    @staticmethod
    def info(msg):
        """
        log an info message into the standard output
        """
        Logger.log(msg, Logger.INFO)

    @staticmethod
    def debug(msg):
        """
        log a debug message into the standard output
        """
        Logger.log(msg, Logger.DEBUG)

    @staticmethod
    def spam(msg):
        """
        log a spam message into the standard output
        """
        Logger.log(msg, Logger.SPAM)

    @staticmethod
    def _level2str(level):
        """
        convert a logging level to string
        """
        if level == Logger.INFO:
            return 'INFO'
        if level == Logger.WARNING:
            return 'WARNING'
        if level == Logger.INFO:
            return 'INFO'
        if level == Logger.DEBUG:
            return 'DEBUG'
        if level == Logger.SPAM:
            return 'SPAM'
