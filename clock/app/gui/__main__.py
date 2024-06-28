"""This is an special script that is called automatically when we run the command `python -m clock.app.gui`"""

if __name__ == "__main__":
    from clock.app.gui.main import run

    run()
