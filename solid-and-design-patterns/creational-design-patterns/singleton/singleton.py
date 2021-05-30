class SingletonObject:

    class __SingletonObject:
        """
        A file-based message logger with the following properties
        Attributes:
        file_name: a string representing the full path of the log file to which
        this logger will write its messages
        """

        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

        def __init__(self, file_name):
            """Return a Logger object whose file_name is *file_name*"""
            self.file_name = file_name

        def _write_log(self, level, msg):
            """Writes a message to the file_name for a specific Logger instance"""
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, level, msg):
            self._write_log("CRITICAL", msg)

        # the rest of the class definition will follow here, as per the previous logging script
        def error(self, level, msg):
            self._write_log("ERROR", msg)

        def warn(self, level, msg):
            self._write_log("WARN", msg)

        def info(self, level, msg):
            self._write_log("INFO", msg)

        def debug(self, level, msg):
            self._write_log("DEBUG", msg)

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
