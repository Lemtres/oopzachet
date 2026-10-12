import flet as ft


class Converter:

    KM_TO_MILES = 1.61
    KG_TO_POUNDS = 0.453

    @staticmethod
    def km_to_miles(value: float) -> float:
        return value / Converter.KM_TO_MILES

    @staticmethod
    def miles_to_km(value: float) -> float:
        return value * Converter.KM_TO_MILES

    @staticmethod
    def celsius_to_fahrenheit(value: float) -> float:
        return value * 1.8 + 32

    @staticmethod
    def fahrenheit_to_celsius(value: float) -> float:
        return (value - 32) / 1.8

    @staticmethod
    def kg_to_pounds(value: float) -> float:
        return value / Converter.KG_TO_POUNDS

    @staticmethod
    def pounds_to_kg(value: float) -> float:
        return value * Converter.KG_TO_POUNDS

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
            value = float(e.control.value)
            kilo.value = f"{Converter.miles_to_km(value):.2f}"

    def m(e: ft.Event[ft.TextField]):
            value = float(e.control.value)
            mile.value = f"{Converter.km_to_miles(value):.2f}"


    def oC(e: ft.Event[ft.TextField]):
            value = float(e.control.value)
            cels.value = f"{Converter.fahrenheit_to_celsius(value):.2f}"

    def oF(e: ft.Event[ft.TextField]):
            value = float(e.control.value)
            far.value = f"{Converter.celsius_to_fahrenheit(value):.2f}"


    def kg(e: ft.Event[ft.TextField]):
            value = float(e.control.value)
            kilogram.value = f"{Converter.pounds_to_kg(value):.2f}"

    def lbs(e: ft.Event[ft.TextField]):
            value = float(e.control.value)
            pound.value = f"{Converter.kg_to_pounds(value):.2f}"

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
                                                input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9.]*$",
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
                                                input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9.]*$",
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
                                                input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9.]*$",
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