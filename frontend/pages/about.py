def about_page(e):
        page.scroll = "adaptive"
        page.controls.clear()

        # Логотип проекта и иконка волонтерского центра
        project_logo = ft.Image(
            src=r"C:\Users\wertei siz\Dropbox\ПК\Downloads\вц.png",
            width=120,
            height=120,
            fit=ft.ImageFit.CONTAIN,
        )

        volunteer_icon = ft.Image(
            src=r"C:\Users\wertei siz\Dropbox\ПК\Downloads\вц.png",
            width=65,
            height=65,
            fit=ft.ImageFit.CONTAIN,
        )

        # Стилизованный AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("О нас",
                          color=ft.Colors.WHITE,
                          size=32,
                          weight="w600",
                          font_family="RobotoSlab"),
            center_title=True,
            bgcolor=Colors["dark_green"],
            toolbar_height=80,
        )

        # Основное содержимое
        content = ft.Column(
            spacing=20,
            scroll="adaptive",
            controls=[
                # Блок с логотипом и миссией
                ft.Container(
                    content=ft.Column([
                        ft.Row([project_logo], alignment="center"),
                        ft.Text("Наша миссия",
                                size=26,
                                color=Colors["dark_green"],
                                weight="w600",
                                text_align="center"),
                        ft.Text(
                            "Автоматизация расчетов водопотребления и комплексный анализ данных "
                            "для эффективного мониторинга водных ресурсов.",
                            size=18,
                            text_align="center",
                            color=ft.Colors.BLACK87,
                        ),
                    ], spacing=15),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Блок цели проекта
                ft.Container(
                    content=ft.Column([
                        ft.Text("Цель проекта",
                                size=26,
                                color=Colors["dark_green"],
                                weight="w600",
                                text_align="center"),
                        ft.Text(
                            "Разработка программного обеспечения для:\n"
                            "• Автоматизации расчетов водопотребления\n"
                            "• Анализа гидрологических данных\n"
                            "• Мониторинга качества воды\n"
                            "• Генерации отчетов по стандартам ГОСТ",
                            size=18,
                            text_align="justify",
                        ),
                    ], spacing=15),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Блок функционала
                ft.Container(
                    content=ft.Column([
                        ft.Text("Функционал",
                                size=26,
                                color=Colors["dark_green"],
                                weight="w600",
                                text_align="center"),
                        ft.Text(
                            "Инструменты для специалистов:\n"
                            "• Для экологов: анализ загрязнений и качества воды\n"
                            "• Для гидрологов: расчет водопотребления и баланса\n"
                            "• Для полевых исследований: мобильный сбор данных\n"
                            "• Для аналитиков: визуализация и отчетность",
                            size=18,
                            text_align="justify",
                        ),
                    ], spacing=15),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Блок разработчиков
                ft.Container(
                    content=ft.Column([
                        ft.Text("Команда разработчиков",
                                size=26,
                                color=Colors["dark_green"],
                                weight="w600",
                                text_align="center"),


                        # я
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.PERSON),
                            title=ft.Text("Благославова Инга Дмитриевна"),
                            subtitle=ft.Text("Фуллстек-разработчик,\nengablagoslavova@yandex.ru"),
                        ),
                        # я
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.PERSON),
                            title=ft.Text("Лавреньтев Артём Александрович"),
                            subtitle=ft.Text("Научный руководитель,\nlavrentiev@yandex.ru"),
                        ),
                    ], spacing=15),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Блок преимуществ
                ft.Container(
                    content=ft.Column([
                        ft.Text("Преимущества",
                                size=26,
                                color=Colors["dark_green"],
                                weight="w600",
                                text_align="center"),
                        ft.Text(
                            "• Автоматизация рутинных расчетов\n"
                            "• Точный анализ данных\n"
                            "• Работа в полевых условиях\n"
                            "• Соответствие ГОСТ\n"
                            "• Удобный интерфейс для специалистов",
                            size=18,
                            text_align="justify",
                        ),
                    ], spacing=15),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Кнопки действий
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Row([
                                volunteer_icon,
                                ft.Text(" Волонтерский центр", size=16),
                            ],
                                alignment="center",
                                spacing=10),
                            color=Colors["dark_green"],
                            bgcolor=Colors["white"],
                            height=50,
                            width=250,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                padding=10,
                            ),
                            on_click=open_url,
                        ),
                        ft.ElevatedButton(
                            content=ft.Row([
                                ft.Icon(ft.Icons.SCHOOL, size=20),
                                ft.Text(" СНО РТУ МИРЭА", size=16, color=ft.Colors.WHITE),
                            ],
                                alignment="center",
                                spacing=10),
                            color=ft.Colors.WHITE,
                            bgcolor=Colors["medium_blue"],
                            height=50,
                            width=250,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                padding=10,
                            ),
                            on_click=open_url1,
                        ),
                    ],
                    alignment="center",
                    spacing=30,
                ),
            ],
        )

        # Добавление элементов на страницу
        page.add(
            ft.Column(
                controls=[
                    menubar,
                    ft.Container(
                        content=content,
                        padding=20
                    )
                ],
                spacing=0,
                expand=True
            )
        )
        #перевод на СНО и Волонтёрский центр
def open_url(e):
        url = "https://vcrtumirea.ru"  # вц
        webbrowser.open(url)
def open_url1(e):
        url = "https://vk.com/mirea_sno?ysclid=m9r49jnbat498182103"  # сно
        webbrowser.open(url)
