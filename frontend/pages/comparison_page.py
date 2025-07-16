
def comparison_page(e):
        """Страница сравнения 2 проб с индикаторами ± по ПДК"""
        page.controls.clear()

        # Настройка AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Сравнение проб", color=ft.Colors.WHITE, size=44, italic=True),
            center_title=True,
            bgcolor=Colors["dark_green"],
            toolbar_height=70
        )

        # Загрузка сохраненных проб
        samples = load_samples()

        # Выпадающие списки для выбора 2 проб
        sample1_dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(str(s["id"]), f"Проба {s['id']}") for s in samples],
            label="Выберите пробу 1",
            width=300,
        )

        sample2_dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(str(s["id"]), f"Проба {s['id']}") for s in samples],
            label="Выберите пробу 2",
            width=300,
        )

        # Таблица сравнения
        comparison_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Параметр", weight="bold")),
                ft.DataColumn(ft.Text("Проба 1", weight="bold")),
                ft.DataColumn(ft.Text("Проба 2", weight="bold")),
                ft.DataColumn(ft.Text("ПДК", weight="bold")),
                ft.DataColumn(ft.Text("Сравнение", weight="bold")),
            ],
            rows=[],
            border=ft.border.all(1, Colors["medium_green"]),
            border_radius=10,
        )

        # Функция обновления таблицы
        def update_table(e):
            if not sample1_dropdown.value or not sample2_dropdown.value:
                return

            # Получаем данные выбранных проб
            sample1 = next((s for s in samples if str(s["id"]) == sample1_dropdown.value), None)
            sample2 = next((s for s in samples if str(s["id"]) == sample2_dropdown.value), None)

            if not sample1 or not sample2:
                return

            # ПДК значений
            pdk_values = {
                "Железо": 3.0,
                "Алюминий": 1.0,
                "Магний": 0.2,
                "Марганец": 0.1,
                "Медь": 1.0,
                "Нитриты": 3.3,
                "Фенолы": 0.001,
                "Формальдегид": 0.05,
                "Фосфаты": 3.5,
                "Фториды": 1.5,
                "Хром": 0.05
            }

            # Создаем строки таблицы
            rows = []
            parameters = [
                ("Железо", "iron"),
                ("Алюминий", "aluminum"),
                ("Магний", "magnesium"),
                ("Марганец", "manganese"),
                ("Медь", "copper"),
                ("Нитриты", "nitrite"),
                ("Фенолы", "phenols"),
                ("Формальдегид", "formaldehyde"),
                ("Фосфаты", "phosphates"),
                ("Фториды", "fluorides"),
                ("Хром", "chroma")
            ]

            for param_name, param_key in parameters:
                value1 = sample1.get(param_key, 0)
                value2 = sample2.get(param_key, 0)
                pdk = pdk_values.get(param_name, 0)

                # Определяем статус по ПДК
                status1 = "+" if value1 <= pdk else "-"
                status2 = "+" if value2 <= pdk else "-"

                # Цвета для статусов
                color1 = Colors["green"] if status1 == "+" else Colors["red"]
                color2 = Colors["green"] if status2 == "+" else Colors["red"]

                rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(param_name)),
                            ft.DataCell(ft.Text(f"{value1:.3f}")),
                            ft.DataCell(ft.Text(f"{value2:.3f}")),
                            ft.DataCell(ft.Text(f"{pdk:.3f}")),
                            ft.DataCell(
                                ft.Row([
                                    ft.Text(status1, color=color1, size=20),
                                    ft.Text("/", size=20),
                                    ft.Text(status2, color=color2, size=20)
                                ])
                            ),
                        ],
                        color=Colors["light_green_50"] if len(rows) % 2 else ft.Colors.WHITE
                    )
                )

            comparison_table.rows = rows
            page.update()

        # Привязываем обновление таблицы к выбору проб
        sample1_dropdown.on_change = update_table
        sample2_dropdown.on_change = update_table

        # Основной интерфейс
        page.add(
            ft.Column(
                [
                    menubar,
                    ft.Row(
                        [sample1_dropdown, sample2_dropdown],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=50
                    ),
                    ft.Container(
                        content=comparison_table,
                        padding=20,
                        margin=ft.margin.only(top=20),
                        border_radius=10,
                        bgcolor=ft.Colors.WHITE,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors.GREY_300,
                        )
                    )
                ],
                spacing=20,
                expand=True,
                scroll=ft.ScrollMode.AUTO
            )
        )
        page.update()
def load_samples():
        """Функция для загрузки сохраненных проб из файла или базы данных"""
        # Здесь должна быть реализация загрузки данных
        # Временные данные для примера
        return [
            {"id": 1, "iron": 1.0, "aluminum": 1.0, "magnesium": 1.0, "manganese": 0.5,
             "copper": 0.3, "nitrite": 2.0, "phenols": 0.0005, "formaldehyde": 0.03,
             "phosphates": 2.5, "fluorides": 1.0, "chroma": 0.02},
            {"id": 2, "iron": 5.0, "aluminum": 5.0, "magnesium": 5.0, "manganese": 1.2,
             "copper": 1.5, "nitrite": 4.0, "phenols": 0.002, "formaldehyde": 0.07,
             "phosphates": 4.0, "fluorides": 2.0, "chroma": 0.08},
            # Добавьте другие пробы по мере необходимости
        ]