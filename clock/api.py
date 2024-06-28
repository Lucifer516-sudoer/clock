from datetime import date, time, tzinfo
from clock.logger import app_logger
from arrow import Arrow


class DateTime:
    """A naive implementation of the `arrow` module, with logging facility"""

    def __init__(self, tz: tzinfo | None = None) -> None:
        self.logger = app_logger.getChild("api")
        self._tz = tz

        self.class_name = f"[{self.__class__.__name__}]"

        self.logger.info(
            f"{self.class_name} Initialized the Date and Time handling API"
        )
        self.logger.info(f"{self.class_name} Proceeding to render time and date")

    @property
    def date_time(self) -> Arrow:
        self.logger.debug(f"{self.class_name} Returning Arrow object (tz={self.tz}) ")
        return Arrow.now(tzinfo=self.tz)

    @property
    def time(self) -> time:
        return self.date_time.time()

    @property
    def date(self) -> date:
        return self.date_time.date()

    @property
    def tz(self) -> tzinfo | None:
        return self._tz

    def set_timezone(self, tz: tzinfo) -> tzinfo | None:
        """Sets the Time zone info for the `Arrow` object"""
        self.logger.info(f"{self.class_name} Updating the Time Zone Info")
        self.logger.debug(f"{self.class_name} Existing TimeZone: {self.time.tzname}")
        self._tz = tz
        self.logger.debug(f"{self.class_name} New TimeZone: {self.time.tzname}")
        self.logger.info(f"{self.class_name} Updated the Time Zone Info")
        return self.tz

    def get_time(self, format: str = "HH:mm:ss") -> str:
        """Returns the string representation of the current time, with the given format. Refer to the `Arrow` module's documentation for the formatting options"""
        self.logger.debug(f"{self.class_name} Returning current time as string")
        return self.date_time.format(format)

    def get_date(self, format: str = "DD/MM/YYYY") -> str:
        """Returns the string representation of the current date, with the given format. Refer to the `Arrow` module's documentation for the formatting options"""
        self.logger.debug(f"{self.class_name} Returning current date as string")
        return self.date_time.format(format)
