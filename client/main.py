import flet
from flet import *
from db import Database
from header import AppHeader
from form import AppForm
from data_table import AppDataTable

def main (page: Page):
    page.bgcolor = "#fdfdfd"
    page.padding = 20
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppForm(),
                Column(
                    scroll="hidden",
                    expand=True,
                    controls=[AppDataTable()]
                ),
            ],
        )
    )
    db = Database()
    db.load_data()
    page.update()

if __name__ == "__main__":
    flet.app(target=main, view=flet.AppView.WEB_BROWSER, port=5050)