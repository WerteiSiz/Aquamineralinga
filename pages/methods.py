def methods_page(e):
        page.scroll = "adaptive"
        page.controls.clear()

        # Загрузка кастомной иконки волонтерского центра
        volunteer_icon = ft.Image(
            src=r"C:\Users\wertei siz\Dropbox\ПК\Downloads\вц.png",
            width=65,
            height=65,
            fit=ft.ImageFit.CONTAIN,
        )

        # Стилизованный AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Инструкция по работе с Aquaminerale",
                          color=ft.Colors.WHITE,
                          size=28,
                          weight="w600",
                          font_family="RobotoSlab"),
            center_title=True,
            bgcolor=Colors["dark_green"],
            toolbar_height=80,
        )

        # Основное содержимое
        content = ft.Column(
            spacing=15,
            scroll="adaptive",
            controls=[
                # Блок цели программы
                ft.Container(
                    content=ft.Column([
                        ft.Text("Цель программы",
                                size=24,
                                color=Colors["dark_green"],
                                weight="w600"),
                        ft.Text(
                            "Анализ природной воды, расчет индекса УКИЗВ (Удельный Комбинаторный Индекс Загрязненности Воды), "
                            "классификация качества воды и генерация отчетов по ГОСТ в полевых условиях.",
                            size=16,
                            text_align="justify"
                        ),
                    ], spacing=10),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Шаг 1 - Запуск
                ft.Container(
                    content=ft.Column([
                        ft.Text("1. Запуск и знакомство",
                                size=22,
                                color=Colors["dark_green"],
                                weight="w600"),
                        ft.Text("Главный экран:", size=18, weight="w500"),
                        ft.Markdown(
                            "- Откройте приложение Aquaminerale\n"
                            "- На главном экране вы увидите описание возможностей:\n"
                            "  • Анализ 11+ параметров воды (Алюминий, Железо, Марганец и др.)\n"
                            "  • Автоматический расчет УКИЗВ и классификация воды\n"
                            "  • Генерация отчетов в 3 форматах (PDF, Excel, TXT)\n"
                            "  • Привязка проб к географическим координатам"
                        )
                    ], spacing=8),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Шаг 2 - Ввод данных
                ft.Container(
                    content=ft.Column([
                        ft.Text("2. Ввод данных пробы",
                                size=22,
                                color=Colors["dark_green"],
                                weight="w600"),
                        ft.Text("Экран 'Входные параметры':", size=18, weight="w500"),
                        ft.Markdown(
                            "- Перейдите в раздел для ввода результатов анализа воды\n"
                            "- Введите концентрации показателей в соответствующие поля\n"
                            "- **Важно:** используйте единицы измерения мг/л!\n"
                            "- Сверяйтесь с экраном «Нормативы» для точных названий и ПДК"
                        )
                    ], spacing=8),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Шаг 3 - Геолокация
                ft.Container(
                    content=ft.Column([
                        ft.Text("3. Внесение местоположения",
                                size=22,
                                color=Colors["dark_green"],
                                weight="w600"),
                        ft.Text("Вкладки «Географическая локация» и «Описание места»:", size=18, weight="w500"),
                        ft.Markdown(
                            "- Укажите координаты точки отбора (широта/долгота в градусах)\n"
                            "- Задайте уникальный номер точки\n"
                            "- Детально опишите место отбора (пример: «Родник в Центральном парке...»)\n"
                            "- Укажите метод отбора пробы (если требуется)\n"
                            "- Прикрепите фотографии места отбора"
                        )
                    ], spacing=8),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Шаг 4 - Расчет УКИЗВ
                ft.Container(
                    content=ft.Column([
                        ft.Text("4. Расчёт УКИЗВ и анализ",
                                size=22,
                                color=Colors["dark_green"],
                                weight="w600"),
                        ft.Text("Экран «Расчет УКИЗВ»:", size=18, weight="w500"),
                        ft.Markdown(
                            "- Нажмите кнопку «Рассчитать УКИЗВ»\n"
                            "- Программа автоматически:\n"
                            "  • Сравнит данные с нормативами ПДК\n"
                            "  • Рассчитает индекс УКИЗВ\n"
                            "  • Определит класс качества воды\n"
                            "  • Выявит показатели с превышением ПДК"
                        )
                    ], spacing=8),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Шаг 5 - Нормативы
                ft.Container(
                    content=ft.Column([
                        ft.Text("5. Просмотр нормативов",
                                size=22,
                                color=Colors["dark_green"],
                                weight="w600"),
                        ft.Text("Вкладка «Нормативы»:", size=18, weight="w500"),
                        ft.Markdown(
                            "- Таблица с контролируемыми показателями\n"
                            "- Типичные диапазоны концентраций\n"
                            "- Предельно Допустимые Концентрации (ПДК)\n"
                            "- Параметры для приборов (длины волн и др.)"
                        )
                    ], spacing=8),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Шаг 6 - Отчеты
                ft.Container(
                    content=ft.Column([
                        ft.Text("6. Генерация отчета",
                                size=22,
                                color=Colors["dark_green"],
                                weight="w600"),
                        ft.Text("Главный экран / Результаты:", size=18, weight="w500"),
                        ft.Markdown(
                            "- Выберите формат отчета (PDF/Excel/TXT)\n"
                            "- Нажмите «Сохранить отчёт»\n"
                            "- **Ключевая функция:** отчеты формируются по ГОСТ Р 51932-2000\n"
                            "- В Excel-формате выделяются параметры с отклонением от ПДК"
                        )
                    ], spacing=8),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_100,
                ),

                # Важные замечания
                ft.Container(
                    content=ft.Column([
                        ft.Text("Важные замечания",
                                size=22,
                                color=Colors["dark_red"],
                                weight="w600"),
                        ft.Markdown(
                            "**Описание места:** Детально описывайте место отбора пробы!\n"
                            "**Координаты:** Всегда указывайте точные широту/долготу\n"
                            "**Сохранение:** Не забывайте экспортировать итоговые отчеты"
                        )
                    ], spacing=8),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.GREY_200,
                    border=ft.border.all(1, Colors["dark_red"])
                ),

                # Чек-лист
                ft.Container(
                    content=ft.Column([
                        ft.Text("Краткий чек-лист",
                                size=22,
                                color=Colors["dark_green"],
                                weight="w600"),
                        ft.Markdown(
                            "1. Запустите Aquaminerale\n"
                            "2. Введите концентрации показателей (мг/л)\n"
                            "3. Укажите координаты (широта/долгота)\n"
                            "4. Детально опишите место отбора\n"
                            "5. Нажмите «Рассчитать УКИЗВ»\n"
                            "6. Сгенерируйте и сохраните отчет"
                        )
                    ], spacing=8),
                    padding=15,
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

        # Правильное добавление элементов на страницу
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