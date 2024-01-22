from flet import *
from controls import add_to_control_reference, return_control_reference

control_map = return_control_reference()

class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def app_header_instance(self):
        add_to_control_reference("AppHeader", self) 
    
    def app_header_brand(self):
        return Container(content=Text("Каталог запасных частей",size=15))
    
    def app_header_seach(self):
        return Container(
            width=320,
            bgcolor="white10",
            border_radius=6,
            opacity=1,
            animate_opacity=320,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=17, opacity=0.85),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        color="white",
                        hint_text="Поиск",
                        on_change=lambda e: self.filter_data_table(e),
                    )
                ]
            )
        )
    
    def app_header_avatar(self):
        return Container(content=IconButton(icons.DIRECTIONS_CAR))
    
    def show_search_bar(self,e):
        if e.data == 'true':
            self.controls[0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
        else:
            self.controls[0].content.controls[1].content.controls[1].value = ""
            self.controls [0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
    
    def filter_data_table(self, e):
        for key, value in control_map.items():
            if key == "AppDataTable":
                if len(value.controls[0].controls[0].rows) != 0:
                    for data in value.controls[0].controls[0].rows[:]:
                        if e.data.lower() in data.cells[2].content.controls[0].value.lower():
                            data.visible = True
                            data.update()
                        else:
                            data.visible = False
                            data.update()

    def build(self):
        self.app_header_instance()
        return Container(
            expand=True,
            on_hover=lambda e: self.show_search_bar(e),
            height=60,
            bgcolor="#FF1300",
            border_radius=border_radius.only(top_left=15,top_right=15),
            padding=padding.only(left=15,right=15),
            content=Row(
                expand=True, 
                alignment=MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    self.app_header_brand(),
                    self.app_header_seach(),
                    self.app_header_avatar(),
                    ]
            ),
        )