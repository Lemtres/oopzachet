import flet as ft

def main(page: ft.Page):
    page.title = "converter"
#Смена темы
    def handle_switch_change(e: ft.Event[ft.Switch]):
        page.theme_mode = ft.ThemeMode.LIGHT if e.control.value else ft.ThemeMode.DARK
        e.control.label = (
            "Light ThemeMode"
            if page.theme_mode == ft.ThemeMode.LIGHT
            else "Dark ThemeMode"
        )
#Формулы перевода
    def km(e: ft.Event[ft.TextField]):
        km = float(e.control.value)
        km *= 1.61
        kilo.value = km

    def m(e: ft.Event[ft.TextField]):
        m = float(e.control.value)
        m /= 1.61
        mile.value = m

    def oC(e: ft.Event[ft.TextField]):
        oC = float(e.control.value)
        oC -= 32
        oC *= 0.55
        cels.value = oC

    def oF(e: ft.Event[ft.TextField]):
        oF = float(e.control.value)
        oF *= 1.8
        oF += 32
        far.value = oF

    def kg(e: ft.Event[ft.TextField]):
        kg = float(e.control.value)
        kg *= 0.453
        kilogram.value = kg

    def lbs(e: ft.Event[ft.TextField]):
        lbs = float(e.control.value)
        lbs /= 0.453
        pound.value = lbs
#Изначальная тема
    page.theme_mode = ft.ThemeMode.DARK

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Tabs(
                selected_index=0,
                length=3,
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[
                        ft.TabBar(
                            tabs=[
                                ft.Tab(label="kilometers<->miles", icon=ft.Icons.ADD_ROAD,),
                                ft.Tab(label="Celsius<->Fahrenheit", icon=ft.Icons.CLOUD),
                                ft.Tab(label="Kilogram<->Pound", icon=ft.Icons.SCALE),
                            ]
                        ),
                        ft.TabBarView(
                            expand=True,
                            controls=[
                                ft.Container(
                                    width=480,
                                    padding=10,
                                    border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
                                    border_radius=10,
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Row(
                                        controls=[
                                            ft.TextField(
                                                label="mile",
                                                input_filter=ft.InputFilter(allow=True,
                                                                            regex_string=r"^[0-9.]*$",
                                                                            replacement_string=""
                                                                            ),
                                                key="handling_change_textfield",
                                                on_submit=km,
                                            ),
                                            ft.Text("Kilometers:"),
                                            kilo := ft.Text(),
                                            ft.TextField(
                                                label="kilometer",
                                                input_filter=ft.InputFilter(allow=True,
                                                                            regex_string=r"^[0-9.]*$",
                                                                            replacement_string=""),
                                                key="handling_change_textfield",
                                                on_submit=m,
                                            ),
                                            ft.Text("Miles:"),
                                            mile := ft.Text(),
                                        ]
                                    ),


                                ),
                                ft.Container(
                                    width=480,
                                    padding=10,
                                    border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
                                    border_radius=10,
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Row(
                                        controls=[
                                            ft.TextField(
                                                label="Fahrenheit",
                                                input_filter=ft.InputFilter(allow=True,
                                                                            regex_string=r"^[0-9.]*$",
                                                                            replacement_string=""
                                                                            ),
                                                key="handling_change_textfield",
                                                on_submit=oC,
                                            ),
                                            ft.Text("Celsius:"),
                                            cels := ft.Text(),
                                            ft.TextField(
                                                label="Celsius",
                                                input_filter=ft.InputFilter(allow=True,
                                                                            regex_string=r"^[0-9.]*$",
                                                                            replacement_string=""),
                                                key="handling_change_textfield",
                                                on_submit=oF,
                                            ),
                                            ft.Text("Fahrenheit:"),
                                            far := ft.Text(),
                                        ]
                                    ),

                                ),
                                ft.Container(
                                    width=480,
                                    padding=10,
                                    border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
                                    border_radius=10,
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Row(
                                        controls=[
                                            ft.TextField(
                                                label="Pound",
                                                input_filter=ft.InputFilter(allow=True,
                                                                            regex_string=r"^[0-9.]*$",
                                                                            replacement_string=""
                                                                            ),
                                                key="handling_change_textfield",
                                                on_submit=kg,
                                            ),
                                            ft.Text("Kilogram:"),
                                            kilogram := ft.Text(),
                                            ft.TextField(
                                                label="Kilogram",
                                                input_filter=ft.InputFilter(allow=True,
                                                                            regex_string=r"^[0-9.]*$",
                                                                            replacement_string=""),
                                                key="handling_change_textfield",
                                                on_submit=lbs,
                                            ),
                                            ft.Text("Pound:"),
                                            pound := ft.Text(),
                                        ]
                                    ),

                                ),
                            ],
                        ),
                        ft.Switch(
                            key="theme_mode_switch",
                            label="Light ThemeMode",
                            on_change=handle_switch_change,
                        ),
                    ],
                ),
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)