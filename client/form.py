from flet import *
from controls import add_to_control_reference
from btn import return_form_button, return_sort_button

class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    def app_form_input_instance(self):
        add_to_control_reference("AppForm", self)

    def app_form_input_field(self, name:str, expand:int):
        return Container(
            expand=expand, 
            height=45, 
            bgcolor="#ebebeb", 
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(value=name, size=9, color="black", weight="bold"),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                    )
                ]
            )
        )
    
    def build(self):
        self.app_form_input_instance()
        return Container(
            expand=True, 
            height=190, 
            bgcolor="white10", 
            border=border.all(1, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True, 
                controls=[
                    Row(
                        controls=[
                            self.app_form_input_field("Марка и модель", 1),
                            self.app_form_input_field("Номер по каталогу", 1),
                            self.app_form_input_field("Описание", 1),
                        ],
                    ),
                    Divider(height=1, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            return_sort_button(),
                            return_form_button()
                        ]
                    )
                ]
            ),   
        )