def location_page(e):
        """
        Страница описания места отбора проб воды
        """
        # Очищаем страницу перед построением
        page.controls.clear()

        # Создаем AppBar с иконкой
        app_bar = ft.AppBar(
            title=ft.Row([
                ft.Icon(ft.Icons.PIN_DROP, size=36),
                ft.Text(" Описание места отбора проб", size=36, italic=True)
            ]),
            center_title=True,
            bgcolor=Colors["dark_green"],
            toolbar_height=80,
            color=Colors["white"]
        )
        page.appbar = app_bar

        # Создаем информационную карточку
        info_card = _create_info_card()

        # Создаем карточку с полями ввода
        input_card = _create_input_card()

        # Добавляем элементы на страницу
        page.add(
            ft.Column(
                [
                    menubar,
                    info_card,
                    input_card,
                    _create_footer_notification()
                ],
                spacing=25,
                expand=True,
                scroll=ft.ScrollMode.AUTO
            )
        )
        page.update()
