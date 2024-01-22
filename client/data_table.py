from flet import *
from controls import add_to_control_reference

class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()

    def app_data_table_reference(self):
        add_to_control_reference("AppDataTable", self)

    def build(self):
        self.app_data_table_reference()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    columns=[
                        DataColumn(
                            Text("ID", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Модель авто", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Номер по каталогу", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Описание", size=12, color="black", weight="bold")
                        ),
                    ],
                    rows=[],
                )
            ],
        )