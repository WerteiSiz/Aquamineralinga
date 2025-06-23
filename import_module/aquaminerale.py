# Импорты из папки COLORS
from COLORS import Colors
from COLORS import import_module

# Импорты из папки pages
from pages import about as about_pages
from pages import coordinates_page
from pages import comparison_page
from pages import input_11_parametrs_page
from pages import location
class ThemeManager:
    def __init__(self):
        self.light_theme = {
            "primary": "#0c7054",  # medium_green
            "secondary": "#0b362c",  # dark_green
            "background": "#feebc8",  # молочный
            "surface": "#ffffff",  # white
            "on_primary": "#ffffff",  # white
            "on_surface": "#0b362c",  # dark_green
        }
        self.dark_theme = {
            "primary": "#1da668",  # light_green
            "secondary": "#0c7054",  # medium_green
            "background": "#0b362c",  # dark_green
            "surface": "#1a3a32",  # темнее dark_green
            "on_primary": "#ffffff",  # white
            "on_surface": "#feebc8",  # молочный
        }
        self.is_dark = False
        self.colors = self.light_theme

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.colors = self.dark_theme if self.is_dark else self.light_theme
        return self.colors

def main(page: ft.Page):
    COLORS = {
        "medium_green": "#0c7054",
        "dark_green": "#0b362c",
        "Fon": "#feebc8",  # Молочный
        "light_green": "#1da668",  # Огранка всего
        "white": "#ffffff",
        "medium_blue": "#0f81f1"
    }
    Colors = {
        "dark_green": "#2E7D32",
        "medium_green": "#388E3C",
        "light_green_50": "#E8F5E9",
        "green": "#4CAF50",
        "red": "#F44336",
        "medium_green": "#0c7054",
        "dark_green": "#0b362c",
        "Fon": "#feebc8",  # Молочный
        "light_green": "#1da668",  # Огранка всего
        "white": "#ffffff",
        "medium_blue": "#0f81f1",
        "dark_red": "#7C0A02",
    }
    # Глобальные переменные
    substances_data = []
    result_container = ft.Column()
    save_message_container = ft.Column()
    menubar = ft.Column()  # Заглушка для меню

    # Стиль для кнопок
    global btn_style
    btn_style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=12),
        padding=18,
        side=ft.BorderSide(1, Colors["medium_green"]),
        bgcolor=ft.Colors.WHITE,
        overlay_color=ft.Colors.TRANSPARENT
    )
    page.title = "Aquaminerale"
    page.bgcolor = Colors["Fon"]
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO  # Включение автоматической прокрутки
    page.auto_scroll = True  # Автоматическая прокрутка при добавлении новых элементовз

    page.appbar = ft.AppBar(
        title=ft.Text("Aquaminerale", color=Colors["white"],size=48,italic=True),
        bgcolor=Colors["dark_green"],
        center_title=True,
        toolbar_height=70
    )
    def create_input_field(label):
        return ft.TextField(
            label=label,
            border_color=Colors["medium_green"],
            border_radius=10,
            border_width=1.5,
            bgcolor=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=Colors["dark_green"]),
            color=Colors["dark_green"],  # Цвет вводимого текста
            width=300
        )

    # Основные данные
    gradys_d_input = create_input_field("Долгота (°):")
    gradys_sh_input = create_input_field("Широта (°):")
    location_input = create_input_field("Место:")
    description_input = create_input_field("Описание локации:")
    number_of_point_input = create_input_field("Номер точки:")

    # Органолептические показатели
    transparency_input = create_input_field("Прозрачность:")
    color_input = create_input_field("Цвет:")
    sediment_input = create_input_field("Осадок:")
    taste_odor_input = create_input_field("Вкус и запах:")
    chroma_input = create_input_field("Цветность (°):")

    # Химические показатели
    Aluminum_input = create_input_field("Алюминий (Al+2) (мг/л):")
    ammonium_input = create_input_field("Аммоний (мг/л):")
    iron_input = create_input_field("Железо общее (мг/л):")
    manganese_input = create_input_field("Марганец (мг/л):")
    copper_input = create_input_field("Медь (мг/л):")
    nitrite_input = create_input_field("Нитрит (мг/л):")
    phenols_input = create_input_field("Фенолы (мг/л):")
    formaldehyde_input = create_input_field("Формальдегид (мг/л):")
    phosphates_input = create_input_field("Фосфаты (мг/л):")
    fluorides_input = create_input_field("Фториды (мг/л):")

    # Заключение
    conclusion_result_input = create_input_field("Результаты анализа:")
    conclusion_recommendations_input = create_input_field("Рекомендации:")
    conclusion_is_safe_input = create_input_field("Пригодность (пригодна/не пригодна):")
    conclusion_purpose_input = create_input_field("Для каких целей:")

    # Для отчёта
    substance_name_input = create_input_field("Название показателя:")
    pdk_input = create_input_field("ПДК (норматив):")
    total_samples_input = create_input_field("Общее количество проб:")
    exceed_samples_input = create_input_field("Количество проб с превышением:", )

    #Показ результатов и тд

    def show_save_message(message, is_error=False):
        """Показывает красивое сообщение о сохранении"""
        save_message.value = message
        save_message.color = ft.Colors.WHITE if is_error else Colors["light_green"]
        save_message_container.visible = True
        page.update()
        # Автоматическое скрытие сообщения через 3 секунды
        def hide_message():
            save_message_container.visible = False
            page.update()
        import threading
        timer = threading.Timer(3.0, hide_message)
        timer.start()

    # Функции сохранения
    def create_water_protocol(
            gradys_d_input, gradys_sh_input, location_input, description_input,
           number_of_point_input, Aluminum_input, ammonium_input, iron_input,
            manganese_input, copper_input, nitrite_input, phenols_input,
            formaldehyde_input, phosphates_input, fluorides_input, chroma_input,
            filename="water_analysis.docx"
    ):
        doc = Document()

        # --- Настройка стилей ---
        style = doc.styles["Normal"]
        style.font.name = "Times New Roman"
        style.font.size = Pt(12)
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")

        # --- Заголовок протокола ---
        title = doc.add_paragraph("Протокол полного химического анализа воды")
        title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        title.runs[0].bold = True
        title.runs[0].font.size = Pt(14)

        # --- Основная информация ---
        doc.add_paragraph(f"№ {number_of_point_input} от «{datetime.now().strftime('%d.%m.%Y')}» г.")
        doc.add_paragraph(f"Местоположение источника: {location_input}")
        doc.add_paragraph(f"Координаты: Широта {gradys_sh_input}°, Долгота {gradys_d_input}°")
        doc.add_paragraph(f"Дата отбора: {datetime.now().strftime('%d.%m.%Y')}")

        # --- Описание водоёма ---
        doc.add_paragraph("\nОписание водоёма:", style='Heading 2')
        doc.add_paragraph(description_input)

        # --- Органолептические показатели ---
        doc.add_paragraph("\nОрганолептические показатели:", style='Heading 2')
        doc.add_paragraph(f"Цветность: {chroma_input}°")

        # --- Химические показатели ---
        doc.add_paragraph("\nХимические показатели:", style='Heading 2')

        chem_data = [
            ("Алюминий (Al+2)", Aluminum_input),
            ("Аммоний", ammonium_input),
            ("Железо общее", iron_input),
            ("Марганец", manganese_input),
            ("Медь", copper_input),
            ("Нитрит", nitrite_input),
            ("Фенолы", phenols_input),
            ("Формальдегид", formaldehyde_input),
            ("Фосфаты", phosphates_input),
            ("Фториды", fluorides_input)
        ]

        table = doc.add_table(rows=1, cols=2)
        table.style = "Table Grid"
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = "Показатель"
        hdr_cells[1].text = "Значение (мг/л)"

        for name, value in chem_data:
            row_cells = table.add_row().cells
            row_cells[0].text = name
            row_cells[1].text = str(value)

        # --- Заключение (можно добавить логику анализа) ---
        doc.add_paragraph("\nЗаключение:", style='Heading 2')
        doc.add_paragraph("Результаты анализа будут добавлены после обработки данных.")

        # --- Подписи ---
        doc.add_paragraph("\n\nРуководитель: ___________________/____________/")
        doc.add_paragraph("Исполнитель: ___________________/____________/")
        doc.add_paragraph(f"Дата составления: {datetime.now().strftime('%d.%m.%Y')}")
        doc.add_paragraph("М.П.")

        doc.save(filename)
        return filename  # Возвращаем имя сохраненного файла

    def _create_info_card():
        """Создает информационную карточку с описанием требований"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Зачем нужно описание места:",
                            size=18,
                            weight="bold",
                            color=Colors["light_green"]),
                    ft.Markdown(
                        "Детальное описание помогает:\n"
                        "- Точной идентификации точки отбора\n"
                        "- Повторному нахождению места для контрольных замеров\n"
                        "- Анализу влияния окружающей среды на состав воды\n"
                        "- Корректному оформлению протокола по ГОСТ Р 51592-2000",
                    ),
                    ft.Text("Пример хорошего описания:",
                            size=16,
                            weight="bold",
                            color=Colors["light_green"]),
                    _create_example_container()
                ]),
                padding=20
            ),
            color=Colors["dark_green"],
            elevation=3,
            margin=ft.margin.only(bottom=20)
        )

    def _create_example_container():
        """Создает контейнер с примером описания"""
        return ft.Container(
            ft.Text(
                '"Родник в парке Горького, 50 м на север от главного входа. '
                'Каменное оформление, металлическая труба для отвода воды. '
                'Окружающая растительность: дубы, клены. Рядом пешеходная дорожка."',
                color=Colors["white"],
                italic=True
            ),
            padding=10,
            border=ft.border.all(1, Colors["light_green"]),
            bgcolor=ft.Colors.GREY_100
        )

    def _create_input_card():
        """Создает карточку с полями ввода данных"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Характеристики точки отбора:",
                            size=20,
                            weight="bold",
                            color=Colors["dark_green"]),
                    ft.Divider(height=10, color="transparent"),
                    _create_input_fields(),
                    _create_action_buttons()
                ]),
                padding=25
            ),
            elevation=8,
            color=Colors["dark_green"],
            margin=ft.margin.only(bottom=30),
        )

    def _create_input_fields():
        """Создает поля ввода с улучшенным оформлением"""
        return ft.ResponsiveRow(
            [
                ft.Column([
                    ft.Text("Детальное описание места:",
                            color=Colors["white"],
                            weight="bold"),
                    ft.Text("(рельеф, источник, окружение)",
                            color=Colors["white"],
                            size=12),
                    description_input,
                ], col={"sm": 12, "md": 8}, spacing=5),

                ft.Column([
                    ft.Text("Идентификационный номер:",
                            color=Colors["white"],
                            weight="bold"),
                    ft.Text("(уникальный для каждой точки)",
                            color=Colors["white"],
                            size=12),
                    number_of_point_input,
                    _create_auto_number_button()
                ], col={"sm": 12, "md": 4}, spacing=10),
            ],
            spacing=20,
        )

    def _create_auto_number_button():
        """Кнопку для автоматического назначения номера"""
        return ft.ElevatedButton(
            "Автоназначение номера",
            icon=ft.Icons.AUTOFPS_SELECT,
            style=ft.ButtonStyle(
                bgcolor=Colors["medium_green"],
                color=Colors["white"],
                padding=10
            ),
            on_click=lambda _: _generate_point_number()
        )

    def _generate_point_number():
        """Генерирует уникальный номер точки и обновляет поле ввода"""
        number_of_point_input.value = f"PT-{datetime.now().strftime('%Y%m%d-%H%M')}"
        page.update()

    def _create_action_buttons():
        """Создает кнопки действий (сохранить, прикрепить фото)"""
        return ft.Row([
            ft.ElevatedButton(
                "Сохранить описание",
                icon=ft.Icons.SAVE,
                style=ft.ButtonStyle(
                    bgcolor=Colors["medium_green"],
                    color=Colors["white"],
                    padding=20
                )
            ),
            ft.ElevatedButton(
                "Прикрепить фото",
                icon=ft.Icons.CAMERA_ALT,
                style=ft.ButtonStyle(
                    bgcolor=Colors["light_green"],
                    color=Colors["white"],
                    padding=20
                )
            )
        ], spacing=15, alignment=ft.MainAxisAlignment.CENTER)

    def _create_footer_notification():
        """Создает уведомление в нижней части страницы"""
        ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.INFO, color=Colors["light_green"]),
                ft.Text(
                    "Эти данные будут включены в итоговый протокол анализа",
                    color=Colors["white"]
                )
            ]),
            alignment=ft.alignment.center,
            bgcolor= Colors["light_green"]
        )
        page.add(content)

    def water_quality_index(e):
        """Функция построения страницы расчета УКИЗВ"""
        # Очищаем страницу
        page.controls.clear()

        # Настройка AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Расчет УКИЗВ", color=Colors["white"], size=40, italic=True),
            center_title=True,
            bgcolor=Colors["dark_green"],
            toolbar_height=70
        )

        # Инициализация полей ввода
        substance_name_input = create_input_field("Название показателя")
        pdk_input = create_input_field("ПДК (норматив)")
        total_samples_input = create_input_field("Общее количество проб")
        exceed_samples_input = create_input_field("Количество проб с превышением")
        concentrations_container = ft.Column(spacing=10)

        # Создаем карточку с полями ввода
        input_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Параметры воды для анализа",
                            size=16, weight="bold", color=Colors["dark_green"]),
                    ft.Divider(height=1, color=Colors["medium_green"]),
                    ft.Row([
                        substance_name_input,
                        ft.Column([pdk_input, total_samples_input], spacing=10)
                    ], spacing=20),
                    exceed_samples_input,
                    concentrations_container,
                ], spacing=15),
                padding=20,
                width=600
            ),
            elevation=8,
            color=Colors["medium_green"],
            margin=ft.margin.only(bottom=30),
        )

        # Кнопки действий
        buttons_row = ft.Row(
            [
                ft.ElevatedButton(
                    text="Рассчитать УКИЗВ",
                    icon=ft.Icons.CALCULATE,
                    style=btn_style,
                    width=200,
                    on_click=lambda e: calculate_water_quality()
                ),
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(text="Сохранить в TXT", icon=ft.Icons.TEXT_SNIPPET),
                            ft.PopupMenuItem(text="Сохранить в Word", icon=ft.Icons.DESCRIPTION),
                        ],
                        icon=ft.Icons.SAVE,
                        tooltip="Выберите формат сохранения",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=12),
                            side=ft.BorderSide(1, Colors["medium_green"]),
                            bgcolor=ft.Colors.WHITE,
                        )
                    ),
                    padding=10,
                    border_radius=12,
                    border=ft.border.all(1, Colors["medium_green"]),
                    bgcolor=ft.Colors.WHITE,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30
        )

        # Добавляем элементы на страницу
        page.add(
            ft.Column(
                [menubar, input_card, buttons_row, save_message_container, result_container],
                spacing=20,
                expand=True,
            )
        )
        page.update()

    def calculate_water_quality():
        """Основная функция расчета УКИЗВ с табличным выводом"""
        try:
            if not substances_data:
                raise ValueError("Добавьте хотя бы один показатель для расчета")

            # Создаем таблицу для результатов
            data_table = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Показатель", weight="bold")),
                    ft.DataColumn(ft.Text("αi (%)", weight="bold")),
                    ft.DataColumn(ft.Text("Sα", weight="bold")),
                    ft.DataColumn(ft.Text("βi ср.", weight="bold")),
                    ft.DataColumn(ft.Text("Sβ", weight="bold")),
                    ft.DataColumn(ft.Text("Si", weight="bold")),
                    ft.DataColumn(ft.Text("Крит.", weight="bold")),
                ],
                rows=[],
                border=ft.border.all(1, Colors["medium_green"]),
                border_radius=5,
                heading_row_color=Colors["light_green"],
                heading_row_height=40,
            )

            total_Si = 0
            critical_indicators = 0
            results = []

            for sub in substances_data:
                if sub["exceed_samples"] == 0:
                    continue

                # Расчет параметров
                alpha_i = (sub["exceed_samples"] / sub["total_samples"]) * 100
                S_alpha = calculate_S_alpha(alpha_i)
                sum_beta_i = sum([c / sub["pdk"] for c in sub["concentrations"]])
                avg_beta_i = sum_beta_i / sub["exceed_samples"]
                S_beta = calculate_S_beta(avg_beta_i)
                S_i = S_alpha + S_beta

                is_critical = S_i >= 9
                if is_critical:
                    critical_indicators += 1
                total_Si += S_i

                # Добавляем строку в таблицу
                data_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(sub["name"])),
                            ft.DataCell(ft.Text(f"{alpha_i:.1f}")),
                            ft.DataCell(ft.Text(f"{S_alpha:.2f}")),
                            ft.DataCell(ft.Text(f"{avg_beta_i:.2f}")),
                            ft.DataCell(ft.Text(f"{S_beta:.2f}")),
                            ft.DataCell(ft.Text(f"{S_i:.2f}",
                                                color=Colors["red"] if is_critical else None,
                                                weight="bold" if is_critical else None)),
                            ft.DataCell(ft.Text("✓" if is_critical else "✗",
                                                color=Colors["red"] if is_critical else Colors["green"])),
                        ],
                        color=Colors["light_green_50"] if len(data_table.rows) % 2 else None
                    )
                )

                results.append({
                    "name": sub["name"],
                    "alpha_i": alpha_i,
                    "S_alpha": S_alpha,
                    "avg_beta_i": avg_beta_i,
                    "S_beta": S_beta,
                    "S_i": S_i,
                    "is_critical": is_critical
                })

            # Расчет общего УКИЗВ
            n = len(results)
            if n == 0:
                result_text = "Нет превышений ПДК. Вода чистая."
                quality = "Очень чистая (I класс)"
                S_ud = 0
            else:
                F = critical_indicators
                k = 1 - (0.1 * F) if F > 0 else 1.0
                S_ud = (total_Si / n) * k
                quality = calculate_water_quality_class(S_ud)

            # Создаем карточку с результатами
            result_card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Результаты расчёта УКИЗВ",
                                size=18, weight="bold", color=Colors["medium_green"]),
                        ft.Divider(height=1, color=Colors["medium_green"]),

                        # Таблица с показателями
                        ft.Container(
                            content=data_table,
                            padding=10,
                            margin=10,
                            border_radius=5,
                        ),

                        # Итоговые показатели
                        ft.Column([
                            ft.Row([
                                ft.Text("Количество показателей:", width=200),
                                ft.Text(f"{n}", weight="bold")
                            ]),
                            ft.Row([
                                ft.Text("Критических показателей:", width=200),
                                ft.Text(f"{critical_indicators}",
                                        color=Colors["red"] if critical_indicators > 0 else None,
                                        weight="bold")
                            ]),
                            ft.Row([
                                ft.Text("УКИЗВ:", width=200),
                                ft.Text(f"{S_ud:.2f}", weight="bold")
                            ]),
                            ft.Row([
                                ft.Text("Качество воды:", width=200),
                                ft.Text(quality,
                                        color=get_quality_color(quality),
                                        weight="bold")
                            ]),
                        ], spacing=10)
                    ], spacing=15),
                    padding=20,
                    width=800
                ),
                elevation=8,
                color=Colors["medium_green"],
                margin=10
            )

            result_container.controls.clear()
            result_container.controls.append(result_card)
            page.update()

        except Exception as err:
            show_save_message(f"Ошибка расчета: {str(err)}", is_error=True)
            page.update()

    # Вспомогательные функции расчета
    def calculate_S_alpha(alpha_i):
        """Расчет S_alpha по alpha_i"""
        if alpha_i < 1:
            return 0
        elif 1 <= alpha_i < 5:
            return 1.1
        elif 5 <= alpha_i < 10:
            return 1.4
        elif 10 <= alpha_i < 20:
            return 2.15
        elif 20 <= alpha_i < 30:
            return 2.6
        elif 30 <= alpha_i < 40:
            return 3.2
        elif 40 <= alpha_i < 50:
            return 3.85
        elif 50 <= alpha_i < 70:
            return 4.0
        else:
            return 5.0

    def calculate_S_beta(avg_beta_i):
        """Расчет S_beta по среднему beta_i"""
        if avg_beta_i < 1.3:
            return 1.0
        elif 1.3 <= avg_beta_i < 2.0:
            return 1.17
        elif 2.0 <= avg_beta_i < 3.0:
            return 2.01
        elif 3.0 <= avg_beta_i < 5.0:
            return 2.35
        elif 5.0 <= avg_beta_i < 10.0:
            return 3.86
        else:
            return 5.0

    def calculate_water_quality_class(S_ud):
        """Определение класса качества воды по УКИЗВ"""
        if S_ud < 1:
            return "Очень чистая (I класс)"
        elif 1 <= S_ud < 2:
            return "Чистая (II класс)"
        elif 2 <= S_ud < 4:
            return "Умеренно загрязнённая (III класс)"
        elif 4 <= S_ud < 6:
            return "Загрязнённая (IV класс)"
        elif 6 <= S_ud < 10:
            return "Грязная (V класс)"
        else:
            return "Очень грязная (VI класс)"

    def get_quality_color(quality):
        """Возвращает цвет для класса качества воды"""
        if "I класс" in quality:
            return Colors["dark_green"]
        elif "II класс" in quality:
            return Colors["green"]
        elif "III класс" in quality:
            return Colors["yellow"]
        elif "IV класс" in quality:
            return Colors["orange"]
        elif "V класс" in quality:
            return Colors["red"]
        else:
            return Colors["dark_red"]


    def show_result_e(e):
        try:
            # Получаем и проверяем входные данные
            aluminum = float(Aluminum_input.value)
            ammonium = float(ammonium_input.value)
            iron = float(iron_input.value)
            manganese = float(manganese_input.value)
            copper = float(copper_input.value)
            nitrite = float(nitrite_input.value)
            phenols = float(phenols_input.value)
            formaldehyde = float(formaldehyde_input.value)
            phosphates = float(phosphates_input.value)
            fluorides = float(fluorides_input.value)
            chroma = float(chroma_input.value)

            # Форматируем результат
            result_text = f"""
    ╔════════════════════════════════════════════╗
    ║        РЕЗУЛЬТАТЫ АНАЛИЗА ВОДЫ            ║
    ╚════════════════════════════════════════════╝

    ▌ Химические показатели:
    ├────────────────────────────────────────────
    │ ▪ Алюминий (Al+2): {aluminum} мг/л
    │ ▪ Аммоний: {ammonium} мг/л
    │ ▪ Железо общее: {iron} мг/л
    │ ▪ Марганец: {manganese} мг/л
    │ ▪ Медь: {copper} мг/л
    │ ▪ Нитрит: {nitrite} мг/л
    │ ▪ Фенолы: {phenols} мг/л
    │ ▪ Формальдегид: {formaldehyde} мг/л
    │ ▪ Фосфаты: {phosphates} мг/л
    │ ▪ Фториды: {fluorides} мг/л
    │ ▪ Цветность: {chroma}°
    ╰────────────────────────────────────────────
    """

            # Создаем карточку с результатами
            result_card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Анализ качества воды",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=Colors["dark_green"]),
                        ft.Divider(height=10, color="white"),
                        ft.Text(result_text,
                                font_family="Italic",
                                size=14,
                                color=Colors["dark_green"],
                                selectable=True)
                    ], spacing=5),
                    padding=25,
                    width=1050
                ),
                elevation=10,
                color=Colors["light_green"],
                margin=15,
                shadow_color=Colors["dark_green"]
            )

            # Очищаем и обновляем контейнер с результатами
            result_container.controls.clear()
            result_container.controls.append(
                ft.Row([result_card], alignment=ft.MainAxisAlignment.CENTER)
            )
            page.update()

        except ValueError as ve:
            show_save_message(f"Ошибка ввода: {str(ve)}", is_error=True)
            page.update()
        except Exception as ex:
            show_save_message(f"Ошибка анализа: {str(ex)}", is_error=True)
            page.update()


    # Контейнер для сообщений о сохранении
    save_message = ft.Text(color=Colors["medium_green"], size=14)
    save_message_container = ft.Container(
        content=ft.Row(
            [
                save_message,
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    on_click=lambda e: setattr(save_message_container, "visible", False) or page.update(),
                    icon_size=18,
                    tooltip="Закрыть"
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        padding=15,
        border_radius=10,
        bgcolor=Colors["medium_green"],
        visible=False,
        animate_opacity=300,
        width=400,
        margin=ft.margin.only(bottom=20)
    )

    # Выпадающее меню для сохранения с иконками
    save_menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(
                text="Сохранить в TXT",
                icon=ft.Icons.TEXT_SNIPPET,
                on_click=create_water_protocol,
            ),
            ft.PopupMenuItem(
                text="Сохранить в Word",
                icon=ft.Icons.DESCRIPTION,
                on_click=create_water_protocol,
            ),
            ft.PopupMenuItem(
                text="Сохранить в Excel",
                icon=ft.Icons.TABLE_CHART,
                on_click=create_water_protocol,
            ),
        ],
        icon=ft.Icons.SAVE,
        tooltip="Выберите формат сохранения",
        # Стиль для меню

    )

    # Кнопки в строку с выпадающим меню сохранения
    buttons_row = ft.Row(
        [
            ft.ElevatedButton(
                text="Рассчитать",
                icon=ft.Icons.CALCULATE,
                style=btn_style,
                width=200,
                on_click=show_result_e
            ),
            ft.Container(
                content=save_menu,
                padding=10,
                border_radius=12,
                border=ft.border.all(1, Colors["medium_green"]),
                bgcolor=ft.Colors.WHITE,
                on_hover=lambda e: setattr(e.control, "bgcolor", Colors["medium_green"]) or e.control.update()
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30
    )

    # Контейнер для результатов
    result_container = ft.Column([], spacing=10)

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
        color=Colors["medium_green"],
        margin=ft.margin.only(bottom=30),
    )
    # Стиль для кнопок меню (выносим в переменную для повторного использования)
    menu_button_style = lambda color: ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=8),
        bgcolor={
            ft.MaterialState.DEFAULT: "transparent",
            ft.MaterialState.HOVERED: color,
        },
        padding=10,
        overlay_color=ft.Colors.TRANSPARENT,
    )

    def menu_button_style(color):
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            bgcolor={
                "": "transparent",  # Стандартное состояние
                "hovered": color,   # При наведении
            },
            padding=10,
        )

    # Создаем MenuBar с актуальными параметрами
    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=Colors["medium_green"],
        ),
        controls=[
            # Меню "Информация"
            ft.SubmenuButton(
                content=ft.Text("Информация", color=Colors["white"]),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("О нас", color=Colors["dark_green"]),
                        leading=ft.Image(
                            src="C://Users//wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/О нас.png",
                            width=30,
                            height=30,
                        ),
                        style=menu_button_style("#E2D4F0"),
                        on_click=about_page,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Методические указания", color=Colors["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/Инструкция.png",
                            width=30,
                            height=30,
                        ),
                        style=menu_button_style("#E2D4F0"),
                        on_click=methods_page,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Нормативы", color=Colors["dark_green"]),leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/ГОСТ.png",
                            width=30,
                            height=30,
                        ),
                        style=menu_button_style("#E2D4F0"),
                        on_click=normative_page,
                    ),
                ],
            ),

            # Основное меню расчетов
            ft.SubmenuButton(
                content=ft.Text("Расчёты", color=Colors["white"]),
                controls=[
                    # Позиционирование
                    ft.SubmenuButton(
                        content=ft.Text("Позиционирование в пространстве", color=Colors["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/Земля.png",
                            width=30,
                            height=30,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Определение координат", color=Colors["dark_green"]),
                                leading=ft.Image(
                                    src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/координаты.png",
                                    width=25,
                                    height=25,
                                ),
                                style=menu_button_style("#fcef72"),
                                on_click=coordinates_page,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Описание места", color=Colors["dark_green"]),
                                leading=ft.Image(
                                    src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/место.png",
                                    width=25,
                                    height=25,
                                ),
                                style=menu_button_style("#fcef72"),
                                on_click=location_page,
                            ),
                        ],
                    ),

                    # Энергетический расчет
                    ft.SubmenuButton(
                        content=ft.Text("Общая концентрация", color=Colors["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/концентрация.png",
                            width=30,
                            height=30,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("16 Параметров", color=Colors["dark_green"]),
                                leading=ft.Image(
                                    src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/Входные данные.png",
                                    width=30,
                                    height=30,
                                ),
                                style=menu_button_style("#14b88a"),
                                on_click=input_11_parametrs_page,

                            ),
                        ],

                    ),
                    # Энергетический расчет
                    ft.SubmenuButton(
                        content=ft.Text("Качество воды", color=Colors["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/концентрация.png",
                            width=30,
                            height=30,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Расчёт УКИВЗ", color=Colors["dark_green"]),
                                leading=ft.Image(
                                    src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/Входные данные.png",
                                    width=30,
                                    height=30,
                                ),
                                style=menu_button_style("#14b88a"),
                                on_click=water_quality_index,

                            ),
                        ],

                    ),
                    # СППР
                    ft.SubmenuButton(
                        content=ft.Text("Отклонение от ПДК", color=Colors["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/Отклонение от ПДК.png",
                            width=30,
                            height=30,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Сравнение проб", color=Colors["dark_green"]),
                                leading=ft.Image(
                                    src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/химик.png",
                                    width=30,
                                    height=30,
                                ),
                                style=menu_button_style("#16cc99"),
                                on_click=comparison_page,

                            ),
                        ],

                    ),
                ],
            ),

        ]
    )
    # Добавляем в страницу
    content = ft.Column(
        spacing=20,
        scroll="adaptive",
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Добро пожаловать в Aquaminerale!",
                        size=26,
                        weight="bold",
                        color=Colors["white"],
                        text_align="center"
                    ),

                    ft.Text(
                        "Профессиональный инструмент для анализа природных водных источников в полевых условиях",
                        size=20,
                        color=Colors["white"],
                        text_align="center"
                    ),

                    ft.Divider(height=20, color=Colors["light_green"]),

                    ft.Text(
                        "Основные возможности программы:",
                        size=22,
                        weight="bold",
                        color=Colors["light_green"]
                    ),

                    ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=Colors["light_green"]),
                            ft.Text(" Анализ 11 ключевых параметров воды (Al, Fe, Mn, NO₂ и др.)",
                                    color=Colors["white"])
                        ]),
                        ft.Row([
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=Colors["light_green"]),
                            ft.Text(" Автоматический расчет УКИЗВ с классификацией качества воды",
                                    color=Colors["white"])
                        ]),
                        ft.Row([
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=Colors["light_green"]),
                            ft.Text(" Система поддержки решений для прогнозирования параметров",
                                    color=Colors["white"])
                        ]),
                        ft.Row([
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=Colors["light_green"]),
                            ft.Text(" Генерация отчетов в 3 форматах (Word, Excel, TXT) по ГОСТ",
                                    color=Colors["white"])
                        ]),
                        ft.Row([
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=Colors["light_green"]),
                            ft.Text(" Геопривязка проб с координатами и описанием местности",
                                    color=Colors["white"])
                        ]),
                    ], spacing=10),

                    ft.Divider(height=20, color=Colors["light_green"]),

                    ft.Text(
                        "Как начать работу:",
                        size=22,
                        weight="bold",
                        color=Colors["light_green"]
                    ),

                    ft.Column([
                        ft.Text("1. Введите концентрации ионов (мг/л), полученные:",
                                color=Colors["white"]),
                        ft.Text("   - Фотоколориметром Экотест-2020",
                                color=Colors["white"], style="italic"),
                        ft.Text("   - Инструментальными методами анализа",
                                color=Colors["white"], style="italic"),

                        ft.Text("2. Нажмите 'Произвести расчет' для анализа данных",
                                color=Colors["white"]),

                        ft.Text("3. Сохраните отчет в нужном формате:",
                                color=Colors["white"]),
                        ft.Text("   - .docx (полноформатный протокол по ГОСТ)",
                                color=Colors["white"], style="italic"),
                        ft.Text("   - .xlsx (табличные данные для Excel)",
                                color=Colors["white"], style="italic"),
                        ft.Text("   - .txt (простые текстовые данные)",
                                color=Colors["white"], style="italic"),
                    ], spacing=10),

                    ft.Divider(height=20, color=Colors["light_green"]),

                    ft.Text(
                        "ВАЖНО:",
                        size=18,
                        weight="bold",
                        color=Colors["light_green"]
                    ),

                    ft.Text(
                        "• Все отчеты автоматически формируются по требованиям ГОСТ\n"
                        "• Программа поддерживает оффлайн-работу в полевых условиях\n"
                        "• Для точных результатов используйте свежие пробы воды",
                        color=Colors["white"]
                    )
                ],
                    spacing=15),
                padding=25,
                border_radius=15,
                bgcolor=Colors["dark_green"],
                border=ft.border.all(2, Colors["light_green"])
            )
        ]
    )
    auth_button = ft.ElevatedButton(
        "Войти",
        icon=ft.Icons.LOGIN,
        color=COLORS["white"],
        bgcolor=COLORS["light_green"]
    )

    register_button = ft.ElevatedButton(
        "Зарегистрироваться",
        icon=ft.Icons.PERSON_ADD,
        color=COLORS["white"],
        bgcolor=COLORS["light_green"]
    )

    change_theme = ft.IconButton(
        icon=ft.Icons.BRIGHTNESS_4,
        tooltip="Сменить тему",
        icon_color=COLORS["white"]
    )

    scroll_up_button = ft.FloatingActionButton(
        icon=ft.Icons.ARROW_UPWARD,
        bgcolor=COLORS["light_green"],
        mini=True
    )
    # Правильное добавление элементов на страницу
    page.add(
        ft.Column(
            controls=[
                menubar,
                ft.Row(
                    controls=[
                        auth_button,
                        register_button,
                        change_theme,
                        scroll_up_button,
                    ],
                    alignment="end",
                    spacing=15
                ),
                content,
            ],
            spacing=0,
            expand=True
        )
    )

ft.app(target=main)