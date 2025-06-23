def coordinates_page(e):
        """Страница ввода географических координат и описания места отбора проб"""
        page.controls.clear()

        # Настройка AppBar с иконкой
        page.appbar = ft.AppBar(
            title=ft.Row([
                ft.Icon(ft.Icons.LOCATION_ON, size=36),
                ft.Text(" Географическая локация", size=36, italic=True)
            ]),
            center_title=True,
            bgcolor=Colors["dark_green"],
            toolbar_height=80,
            color=Colors["white"]
        )

        # Информационная карточка
        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Инструкция по заполнению:",
                            size=18,
                            weight="bold",
                            color=Colors["dark_green"]),
                    ft.Text(
                        "1. Укажите точные координаты места отбора пробы\n"
                        "2. Добавьте описание местности и источника\n"
                        "3. Пронумеруйте точку отбора для идентификации\n"
                        "4. Данные сохранятся автоматически при вводе",
                        color=Colors["dark_green"]
                    )
                ]),
                padding=20
            ),
            color=Colors["light_green"],
            elevation=3,
            margin=ft.margin.only(bottom=20)
        )

        # Поля ввода с пояснениями
        coord_inputs = ft.ResponsiveRow(
            [
                ft.Column([
                    ft.Text("Широта (градусы):", color=Colors["white"]),
                    gradys_sh_input
                ], col={"sm": 12, "md": 3}, spacing=5),

                ft.Column([
                    ft.Text("Долгота (градусы):", color=Colors["white"]),
                    gradys_d_input
                ], col={"sm": 12, "md": 3}, spacing=5),

                ft.Column([
                    ft.Text("Описание места:", color=Colors["white"]),
                    description_input
                ], col={"sm": 12, "md": 3}, spacing=5),

                ft.Column([
                    ft.Text("Номер точки:", color=Colors["white"]),
                    number_of_point_input
                ], col={"sm": 12, "md": 3}, spacing=5),
            ],
            spacing=15,
        )

        # Карточка с полями ввода
        input_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Параметры локации:",
                            size=20,
                            weight="bold",
                            color=Colors["dark_green"]),
                    ft.Divider(height=10, color="transparent"),
                    coord_inputs,
                    ft.ElevatedButton(
                        "Показать на карте",
                        icon=ft.Icons.MAP,
                        style=ft.ButtonStyle(
                            bgcolor=Colors["medium_green"],
                            color=Colors["white"],
                            padding=20
                        ),
                        on_click=lambda _: webbrowser.open(
                            f"https://www.google.com/maps?q={gradys_sh_input.value},{gradys_d_input.value}")
                    )
                ]),
                padding=25
            ),
            elevation=8,
            color=Colors["white"],
            margin=ft.margin.only(bottom=30),
        )

        # Добавляем элементы на страницу
        page.add(
            ft.Column(
                [
                    menubar,
                    info_card,
                    input_card,
                    ft.Container(
                        content=ft.Text(
                            "Все координаты сохраняются в протокол анализа",
                            color=Colors["white"],
                            italic=True
                        ),
                        alignment=ft.alignment.center
                    )
                ],
                spacing=25,
                expand=True,
                scroll=ft.ScrollMode.AUTO
            )
        )
        page.update()