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



class NumberField(ft.TextField):
    def __init__(self, label, on_submit_handler):
        super().__init__(
            label=label,
            input_filter=ft.InputFilter(
                allow=True,
                regex_string=r"^[-0-9.]*$",
                replacement_string="",
            ),
            on_submit=on_submit_handler,
        )

    def parse(self):
            return float(self.value)



class ConverterPanel(ft.Container):
    def __init__(self, page, left_label, right_label):
        self._page = page
        self.left_label = left_label
        self.right_label = right_label

        self.left_field = NumberField(left_label, self._on_left)
        self.right_result = ft.Text(value="")
        self.right_field = NumberField(right_label, self._on_right)
        self.left_result = ft.Text(value="")

        row = ft.Row(
            controls=[
                self.left_field,
                ft.Text(f"{right_label}:"),
                self.right_result,
                self.right_field,
                ft.Text(f"{left_label}:"),
                self.left_result,
            ]
        )

        super().__init__(
            width=520,
            padding=10,
            border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
            border_radius=10,
            alignment=ft.Alignment.CENTER,
            content=row,
        )

    def _show(self, target, value):
        target.value = "Ошибка" if value is None else f"{value:.2f}"
        self._page.update()

    def _on_left(self, e):
        v = self.left_field.parse()
        self._show(self.right_result, None if v is None else self.left_to_right(v))

    def _on_right(self, e):
        v = self.right_field.parse()
        self._show(self.left_result, None if v is None else self.right_to_left(v))

    def left_to_right(self, v): raise NotImplementedError
    def right_to_left(self, v): raise NotImplementedError



class KmMilesPanel(ConverterPanel):
    def __init__(self, page):
        super().__init__(page, left_label="Miles", right_label="Kilometers")

    def left_to_right(self, v):
        return Converter.miles_to_km(v)

    def right_to_left(self, v):
        return Converter.km_to_miles(v)


class CelsiusFahrenheitPanel(ConverterPanel):
    def __init__(self, page):
        super().__init__(page, left_label="Fahrenheit", right_label="Celsius")

    def left_to_right(self, v):
        return Converter.f_to_c(v)

    def right_to_left(self, v):
        return Converter.c_to_f(v)


class KgPoundPanel(ConverterPanel):
    def __init__(self, page):
        super().__init__(page, left_label="Pound", right_label="Kilogram")

    def left_to_right(self, v):
        return Converter.lbs_to_kg(v)

    def right_to_left(self, v):
        return Converter.kg_to_lbs(v)



class ThemeSwitcher(ft.Switch):
    def __init__(self, page):
        super().__init__(
            label="Light ThemeMode",
            on_change=self._on_change,
        )
        self._page = page
        self._page.theme_mode = ft.ThemeMode.DARK

    def _on_change(self, e):
        if e.control.value:
            self._page.theme_mode = ft.ThemeMode.LIGHT
            self.label = "Light ThemeMode"
        else:
            self._page.theme_mode = ft.ThemeMode.DARK
            self.label = "Dark ThemeMode"
        self._page.update()



class ConverterTabs(ft.Tabs):
    PANELS = [
        ("Kilometers <-> Miles", ft.Icons.ADD_ROAD, KmMilesPanel),
        ("Celsius <-> Fahrenheit", ft.Icons.CLOUD, CelsiusFahrenheitPanel),
        ("Kilogram <-> Pound", ft.Icons.SCALE, KgPoundPanel),
    ]

    def __init__(self, page):
        self._page = page

        tabs = [ft.Tab(label=label, icon=icon) for label, icon, _ in self.PANELS]
        panels = [cls(page) for _, _, cls in self.PANELS]

        column = ft.Column(
            expand=True,
            controls=[
                ft.TabBar(tabs=tabs),
                ft.TabBarView(expand=True, controls=panels),
                ThemeSwitcher(page),
            ],
        )

        super().__init__(
            selected_index=0,
            length=len(self.PANELS),
            expand=True,
            content=column,
        )



class ConverterApp:
    def __init__(self, page):
        self.page = page
        self.page.title = "Converter"
        self.page.add(
            ft.SafeArea(
                expand=True,
                content=ConverterTabs(self.page),
            )
        )

def main(page: ft.Page):
    ConverterApp(page)

if __name__ == "__main__":
    ft.run(main)