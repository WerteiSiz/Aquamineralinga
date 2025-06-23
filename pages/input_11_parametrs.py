import COLORS
import import_module
import flet as ft
from flet import *


def input_11_parametrs_page(e):
        """страница с анализом проб"""
        page.controls.clear()
        # Настройка AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Входные параметры",color=COLORS["white"],size=44, italic=True),
            center_title=True,
            bgcolor=COLORS["dark_green"],
            toolbar_height=70
        )

        # Карточка с полями ввода
        input_card = ft.Card(
            content=ft.Container(
                content=ft.ResponsiveRow(
                    [
                        ft.Container(Aluminum_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(ammonium_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(iron_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(manganese_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(copper_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(nitrite_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(phenols_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(formaldehyde_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(phosphates_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(fluorides_input, padding=15, col={"sm": 12, "md": 4}),
                        ft.Container(chroma_input, padding=15, col={"sm": 12, "md": 4}),
                    ],
                    spacing=20,
                ),
                padding=20,
            ),
            elevation=5,
            color=COLORS["medium_green"],
            margin=ft.margin.only(bottom=30),
        )

        # Кнопки действий
        buttons_row = ft.Row(
            [
                ft.ElevatedButton(
                    text="Произвести расчёты",
                    color=COLORS["dark_green"],
                    icon=ft.Icons.CALCULATE,
                    style=btn_style,
                    width=200,
                    on_click=show_result_11_parametrs
                ),
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Сохранить в TXT",
                                icon=ft.Icons.TEXT_SNIPPET,
                                on_click=create_water_protocol_txt
                            ),
                            ft.PopupMenuItem(
                                text="Сохранить в Word",
                                icon=ft.Icons.DESCRIPTION,
                                on_click=create_water_protocol_word
                            ),
                            ft.PopupMenuItem(
                                text="Сохранить в Excel",
                                icon=ft.Icons.TABLE_CHART,
                                on_click=create_water_protocol_excel
                            ),
                        ],
                        icon=ft.Icons.SAVE,
                        tooltip="Выберите формат сохранения",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=12),
                            side=ft.BorderSide(1, COLORS["medium_green"]),
                            bgcolor=ft.Colors.WHITE,
                        )
                    ),
                    padding=10,
                    border_radius=12,
                    border=ft.border.all(1, COLORS["medium_green"]),
                    bgcolor=ft.Colors.WHITE,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30
        )

        # Добавляем элементы на страницу
        page.add(
            ft.Column(
                [
                    menubar,
                    input_card,
                    buttons_row,
                    save_message_container,
                    result_container
                ],
                spacing=20,
                expand=True,
            )
        )
        page.update()
    