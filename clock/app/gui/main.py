from datetime import tzinfo
import time
from typing import Literal
import flet as ft
from clock.logger import (
    app_logger,
    flet_logger,
    flet_core_logger,
    configure_present_loggers,
    RichConsoleHandler,
    logging,
)
from clock.api import DateTime


class TimePiece(ft.UserControl):
    logger = app_logger.getChild("app.gui")

    def __init__(
        self,
        show: Literal["time", "date", "datetime", "timedate"],
        tz: tzinfo | None = None,
    ):
        super().__init__()
        self.class_name = f"[{self.__class__.__name__}@flet]"
        self.logger.info(f"{self.class_name} Initialized the Control")

        self.show: (
            Literal["time"]
            | Literal["date"]
            | Literal["datetime"]
            | Literal["timedate"]
        ) = show

        self.time_text = ft.Text(
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
            font_family="digital",
            size=60,
        )
        self.date_text = ft.Text(
            theme_style=ft.TextThemeStyle.DISPLAY_SMALL,
            font_family="digital",
            size=50,
        )
        self._date_time_text: list[ft.Control] = [
            self.time_text,
            self.date_text,
        ]

        # logging informations:
        self.logger.debug(f"{self.class_name} Time Zone: {tz}")
        self.logger.debug(f"{self.class_name} Information to show: {show}")

    def _set_up(self):
        self.logger.info(f"{self.class_name} Configuring the `Control`")
        match self.show:
            case "time":
                self.logger.debug(f"{self.class_name} Shows only the Time info")
                self._date_time_text = [self.time_text]

            case "date":
                self.logger.debug(f"{self.class_name} Shows only the Date info")
                self._date_time_text = [self.date_text]

            case "datetime":
                self.logger.debug(f"{self.class_name} Shows the date and then the time")
                self._date_time_text = [self.date_text, self.time_text]

            case "timedate":
                self.logger.debug(f"{self.class_name} Shows the time and then the date")
                self._date_time_text = [self.time_text, self.date_text]

        self._date_time_text = self._date_time_text

    def update_time(self, time: str):
        self.logger.debug(f"{self.class_name} Updating the time to {time}")
        self.time_text.value = time
        self.update()

    def update_date(self, date: str):
        self.logger.debug(f"{self.class_name} Updating the date to {date}")
        self.date_text.value = date
        self.update()

    def update_date_and_time(self, date: str, time: str):
        self.logger.debug(
            f"{self.class_name} Updating the date and time to {date} & {time}"
        )
        self.update_date(date)
        self.update_time(time)

    def build(self):
        self._set_up()
        self.logger.info(f"{self.class_name} Building the UserControl")
        self.logger.debug(f"{self.class_name} Proceeding to render the Time Piece")
        return ft.Container(
            content=ft.Column(
                controls=self._date_time_text,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )


def setup_loggers():
    for logger in [app_logger, flet_core_logger, flet_logger]:
        logger.setLevel(logging.DEBUG)

    configure_present_loggers(
        loggers=[app_logger, flet_core_logger, flet_logger],
        handlers=[RichConsoleHandler(level=app_logger.level)],
    )


def main(page: ft.Page):
    setup_loggers()
    page.title = "Clock"
    page.fonts = {
        "digital": "/home/lucifer/projects/py_stuffs/clock/clock/app/gui/assets/fonts/Technology.ttf",
        "digital-bold-italic": "/home/lucifer/projects/py_stuffs/clock/clock/app/gui/assets/fonts/Technology-BoldItalic.ttf",
    }
    page.theme = ft.Theme(
        color_scheme_seed="#DAE300",
    )

    def theme_changer(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        theme_switcher.icon = (
            ft.icons.LIGHT_MODE
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.icons.DARK_MODE
        )
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT

    theme_switcher = ft.IconButton(
        icon=ft.icons.LIGHT_MODE, on_click=theme_changer, tooltip="Switch Theme Mode"
    )
    info_button = ft.IconButton(
        icon=ft.icons.INFO,
        on_click=lambda e: page.show_dialog(info_dialog),
        tooltip="About",
    )

    info_dialog = ft.AlertDialog(
        title=ft.Text("About", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        content=ft.Text(
            "Simple Clock, made by Lucifer516-sudoer with 💝",
            theme_style=ft.TextThemeStyle.LABEL_MEDIUM,
            size=20,
        ),
    )

    page.appbar = ft.AppBar(
        title=ft.Text(
            value="Clock",
            style=ft.TextStyle(font_family="digital-bold-italic"),
            size=50,
        ),
        color=ft.colors.BLUE_ACCENT_700,
        elevation=50,
        leading=ft.Icon(name=ft.icons.ALARM, size=40),
        actions=[theme_switcher, info_button],
    )

    dt = DateTime()
    time_piece = TimePiece(show="timedate")
    time_piece.time_text.color = ft.colors.BLUE
    time_piece.date_text.color = ft.colors.AMBER

    page.add(time_piece)
    page.update()

    previous_time = ""
    previous_date = ""

    try:
        while True:
            current_time = dt.get_time(format="hh:mm:ss A")
            current_date = dt.get_date(format="DD MMM, YYYY")

            if current_time != previous_time:
                time_piece.update_time(current_time)
                previous_time = current_time
            if current_date != previous_date:
                time_piece.update_date(current_date)
                previous_date = current_date

            time.sleep(1)  # Throttle the loop to avoid excessive CPU usage
    except Exception as e:
        app_logger.error(f"[main@flet] An error occurred in the main loop: {e}")
    finally:
        app_logger.info("[main@flet] Clock app terminated")


def run(method=main):
    ft.app(
        target=main,
        assets_dir="/home/lucifer/projects/py_stuffs/clock/clock/app/gui/assets",
    )


if __name__ == "__main__":
    run()
