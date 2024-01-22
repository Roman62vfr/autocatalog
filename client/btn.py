from flet import *
from controls import return_control_reference
from db import Database

control_map = return_control_reference()

def update_text(e):
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

def get_input_data(e):
    for key, value in control_map.items():
        if key == "AppForm":
            data = []
            for user_input in value.controls[0].content.controls[0].controls[:]:
                data.append(user_input.content.controls[1].value)
            db = Database()
            db.write(data)
            db.load_data()

def sort_by_name(e):
    db = Database()
    db.load_data("num")

def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor="#FF1300",
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,
                    ),
                    Text(
                        "Добавить запись",
                        size=11,
                        weight="bold",
                    )
                ]
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=220,
        )
    )

def return_sort_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: sort_by_name(e),
            bgcolor="#FF1300",
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.SORT,
                        size=12,
                    ),
                    Text(
                        "Отсортировать по номеру",
                        size=11,
                        weight="bold",
                    )
                ]
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=220,
        )
    )