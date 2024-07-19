"""
Contains Date and Time Related stuffs
Usage:
>>> dt = Datetime()
>>> dt.get_time_data()
>>> dt.get_date_data()
"""

from dataclasses import asdict, dataclass, field
from datetime import date, time, tzinfo

from arrow import Arrow

from clock.logger import app_logger


@dataclass
class TimeData:
    """Contains Time related datum"""

    hour: str | None = field(default=None)
    minute: str | None = field(default=None)
    second: str | None = field(default=None)
    sub_second: str | None = field(default=None)
    session: str | None = field(default=None)

    def asdict(self):
        return asdict(self)


@dataclass
class DateData:
    """Contains Date related datum"""

    day: str | None = field(default=None)
    month: str | None = field(default=None)
    year: str | None = field(default=None)

    def asdict(self):
        return asdict(self)


class DateTime:
    """A naive implementation of the `arrow` module, with logging facility"""

    def __init__(self, tz: tzinfo | None = None) -> None:
        self.logger = app_logger.getChild("api")
        self._tz = tz

        self.class_name = f"[{self.__class__.__name__}]"

        self.logger.info(
            f"{self.class_name} Initialized the Date and Time handling API"
        )
        self.logger.debug(f"{self.class_name} Time Zone: {self.tz}")
        self.logger.info(f"{self.class_name} Proceeding to return time and date")

    @property
    def date_time(self) -> Arrow:
        """
        Returns an `Arrow` object representing the current date and time, with the time zone if provided

        Supported Tokens to be used when formatting, please refer to the documentation of the arrow module:
            Year Related:
                YYYY, YY

            Month Related:
                MMMM, MMM, MM, M

            Day of Year:
                DDDD ( with zero padding )
                DDD ( without zero padding )

            Day of Month:
                DD   ( with zero padding )
                D ( without zero padding )
                Do (1st, 2nd, 3rd … 30th, 31st)

            Day of Week:
                dddd (Monday, Tuesday, Wednesday …)
                ddd (Mon, Tue, Wed …)
                d (1, 2, 3 … 6, 7)

            ISO week date:
                W (2011-W05-4, 2019-W17)

            Hour:
                HH (00, 01, 02 … 23, 24)
                H (0, 1, 2 … 23, 24)
                hh (01, 02, 03 … 11, 12)
                h (1, 2, 3 … 11, 12)

            AM / PM:
                A (AM, PM, am, pm )
                a (am, pm )

            Minute:
                mm (00, 01, 02 … 58, 59)
                m (0, 1, 2 … 58, 59)

            Second:
                ss (00, 01, 02 … 58, 59)
                s (0, 1, 2 … 58, 59)

            Sub-second
                S… (0, 02, 003, 000006, 123123123123…)

            Timezone:
                ZZZ (Asia/Baku, Europe/Warsaw, GMT … )
                ZZ (-07:00, -06:00 … +06:00, +07:00, +08, Z)
                Z (-0700, -0600 … +0600, +0700, +08, Z)

            Seconds Timestamp:
                X (1381685817, 1381685817.915482 …)

            ms or µs Timestamp:
                x (1569980330813, 1569980330813221)
        """
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

        # def get_time_hour(self, time: Arrow | None = None) -> int:
        #     """Returns the hour of the given time object as an integer"""
        #     self.logger.debug(f"{self.class_name} Returning the hour of the time")
        #     if not isinstance(time, Arrow):
        #         self.logger.debug(
        #             f"{self.class_name} Not provided a Arrow object to retrieve data, using current time object"
        #         )
        #         return self.time.hour
        #     else:
        #         self.logger.debug(
        #             f"{self.class_name} Retrieving hour info from the `Arrow` object"
        #         )
        #         return time.time().hour

        # def get_time_minute(self, time: Arrow | None = None) -> int:
        #     """Returns the minute of the given time object as an integer"""
        #     self.logger.debug(f"{self.class_name} Returning the minute of the time")
        #     if not isinstance(time, Arrow):
        #         self.logger.debug(
        #             f"{self.class_name} Not provided a Arrow object to retrieve data, using current time object"
        #         )
        #         return self.time.minute
        #     else:
        #         self.logger.debug(
        #             f"{self.class_name} Retrieving minute info from the `Arrow` object"
        #         )
        #         return time.time().minute

        # def get_time_second(self, time: Arrow | None = None) -> int:
        #     """Returns the second of the given time object as an integer"""
        #     self.logger.debug(f"{self.class_name} Returning the second of the time")
        #     if not isinstance(time, Arrow):
        #         self.logger.debug(
        #             f"{self.class_name} Not provided a Arrow object to retrieve data, using current time object"
        #         )
        #         return self.time.second
        #     else:
        #         self.logger.debug(
        #             f"{self.class_name} Retrieving second info from the `Arrow` object"
        #         )
        #         return time.time().second

        # def get_time_subsecond(self, time: Arrow) -> int:
        #     """Returns the subsecond, (a single digit of the sub second) of the given time object as an integer"""
        #     self.logger.debug(f"{self.class_name} Returning the sub-second of the time")
        #     self.logger.debug(
        #         f"{self.class_name} Retrieving sub-second info from the `Arrow` object"
        #     )
        #     return int(time.format("S"))

        # def get_time_session(self, time: Arrow) -> str:
        """Returns the session of the given time object as an string in Upper case"""
        self.logger.debug(f"{self.class_name} Returning the session of the time")
        self.logger.debug(
            f"{self.class_name} Retrieving session info from the `Arrow` object"
        )
        return time.format("A")

    def get_time_data(self, time: Arrow | None = None) -> TimeData:
        self.logger.info(f"{self.class_name} Getting Time Data")

        if time is None:
            self.logger.debug(
                f"{self.class_name} time object is not supplied, returning the current time data"
            )
            time = self.date_time
            data = TimeData(
                hour=time.format("hh"),
                minute=time.format("mm"),
                second=time.format("ss"),
                sub_second=f"{time.format("S")}",
                session=time.format("A"),
            )

            self.logger.info(f"{self.class_name} Returning time data")
            self.logger.debug(f"{self.class_name} Returning data:\n{data.asdict()}")

            return data

        else:
            self.logger.debug(
                f"{self.class_name} time object supplied, stripping time data from the object"
            )

            data = TimeData(
                hour=time.format("hh"),
                minute=time.format("mm"),
                second=time.format("ss"),
                sub_second=f"{time.format("S"):02}",
                session=time.format("A"),
            )

            self.logger.info(f"{self.class_name} Returning time data")
            self.logger.debug(f"{self.class_name} Returning data:\n{data.asdict()}")

            return data

    def get_date_data(self, date: Arrow | None = None) -> DateData:
        self.logger.info(f"{self.class_name} Getting Date Data")

        if date is None:
            self.logger.debug(
                f"{self.class_name} date object is not supplied, returning the current date data"
            )

            date = self.date_time
            data = DateData(
                day=date.format("DD"),
                month=date.format("MMM"),
                year=date.format("YYYY"),
            )

            self.logger.info(f"{self.class_name} Returning time data")
            self.logger.debug(f"{self.class_name} Returning data:\n{data.asdict()}")

            return data

        else:
            self.logger.debug(
                f"{self.class_name} date object supplied, stripping date data from the object"
            )

            data = DateData(
                day=date.format("DD"),
                month=date.format("MMM"),
                year=date.format("YYYY"),
            )

            self.logger.info(f"{self.class_name} Returning time data")
            self.logger.debug(f"{self.class_name} Returning data:\n{data.asdict()}")

            return data
