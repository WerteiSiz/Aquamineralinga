import COLORS
import import_module
class ThemeManager:
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_theme = "light"
        self.apply_theme()

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme()
        self.page.update()

    def apply_theme(self):
        colors = COLORS[self.current_theme]
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=colors["primary"],
                on_primary=colors["on_primary"],
                secondary=colors["secondary"],
                surface=colors["surface"],
                on_surface=colors["on_surface"],
                background=colors["background"],
            ),
        )
        self.page.bgcolor = colors["background"]


def main(page: ft.Page):
    theme_manager = ThemeManager(page)
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
        side=ft.BorderSide(1, COLORS["medium_green"]),
        bgcolor=ft.Colors.WHITE,
        overlay_color=ft.Colors.TRANSPARENT
    )
    page.title = "Aquaminerale"
    page.bgcolor = COLORS["Fon"]
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO  # Включение автоматической прокрутки
    page.auto_scroll = True  # Автоматическая прокрутка при добавлении новых элементов

    page.appbar = ft.AppBar(
        title=ft.Text("Aquaminerale", color=COLORS["white"],size=48,italic=True),
        bgcolor=COLORS["dark_green"],
        center_title=True,
        toolbar_height=70
    )
    def create_input_field(label):
        return ft.TextField(
            label=label,
            border_color=COLORS["medium_green"],
            border_radius=10,
            border_width=1.5,
            bgcolor=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=COLORS["dark_green"]),
            color=COLORS["dark_green"],  # Цвет вводимого текста
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

    #перевод на СНО и Волонтёрский центр
    def open_url(e):
        url = "https://vcrtumirea.ru"  # вц
        webbrowser.open(url)
    def open_url1(e):
        url = "https://vk.com/mirea_sno?ysclid=m9r49jnbat498182103"  # сно
        webbrowser.open(url)

    def show_save_message(message, is_error=False):
        """Показывает красивое сообщение о сохранении"""
        save_message.value = message
        save_message.color = ft.Colors.PINK_400 if is_error else COLORS["light_green"]
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
    from docx import Document
    from docx.shared import Pt
    from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
    from datetime import datetime


    def load_data_from_excel(file_path):
        """Загружает и валидирует данные из Excel-файла"""
        try:
            # Проверка существования файла
            if not Path(file_path).exists():
                raise FileNotFoundError(f"Файл {file_path} не найден")

            df = pd.read_excel(file_path, engine='openpyxl')

            # Проверка обязательных колонок
            required_columns = ['Вещество', 'ПДК', 'n_i', "n_i'", 'Концентрации']
            if not all(col in df.columns for col in required_columns):
                missing = set(required_columns) - set(df.columns)
                raise ValueError(f"Отсутствуют обязательные колонки: {missing}")

            data = []
            for _, row in df.iterrows():
                try:
                    concentrations = []
                    if pd.notna(row['Концентрации']):
                        concentrations = [float(x.strip()) for x in str(row['Концентрации']).split(',') if x.strip()]

                    data.append({
                        'name': row['Вещество'],
                        'pdk': float(row['ПДК']),
                        'total_samples': int(row['n_i']),
                        'exceed_samples': int(row["n_i'"]),
                        'concentrations': concentrations
                    })
                except Exception as e:
                    print(f"Ошибка обработки строки {row['Вещество']}: {e}")
                    continue

            return data
        except Exception as e:
            print(f"Критическая ошибка загрузки данных: {e}")
            return None

    def create_water_protocol_excel(file_path):
            """Расчёт УКИЗВ с улучшенной обработкой ошибок"""
            substances = load_data_from_excel(file_path)
            if not substances:
                print("Невозможно продолжить расчёт из-за ошибок в данных")
                return

            results = []
            total_Si = 0
            critical_indicators = 0

            print("\n=== Начало расчёта УКИЗВ ===")

            for sub in substances:
                try:
                    name = sub["name"]
                    pdk = sub["pdk"]
                    total_samples = sub["total_samples"]
                    exceed_samples = sub["exceed_samples"]
                    concentrations = sub["concentrations"]

                    # Валидация данных
                    if total_samples <= 0:
                        print(f"\n{name}: некорректное количество проб ({total_samples})")
                        continue

                    if exceed_samples < 0:
                        print(f"\n{name}: отрицательное количество превышений ({exceed_samples})")
                        continue

                    # Пропуск показателей без превышений
                    if exceed_samples == 0 or not concentrations:
                        print(f"\n{name}: нет превышений ПДК")
                        continue

                    # 1. Расчёт α_i
                    alpha_i = (exceed_samples / total_samples) * 100

                    # 2. Определение S_α
                    if alpha_i < 1:
                        S_alpha = 0
                    elif alpha_i < 5:
                        S_alpha = 1.1
                    elif alpha_i < 10:
                        S_alpha = 1.4
                    elif alpha_i < 20:
                        S_alpha = 2.15
                    elif alpha_i < 30:
                        S_alpha = 2.6
                    elif alpha_i < 40:
                        S_alpha = 3.2
                    elif alpha_i < 50:
                        S_alpha = 3.85
                    elif alpha_i < 70:
                        S_alpha = 4.0
                    else:
                        S_alpha = 5.0

                    # 3. Расчёт β_i
                    sum_beta_i = sum(c / pdk for c in concentrations)
                    avg_beta_i = sum_beta_i / exceed_samples

                    # 4. Определение S_β
                    if avg_beta_i < 1.3:
                        S_beta = 1.0
                    elif avg_beta_i < 2.0:
                        S_beta = 1.17
                    elif avg_beta_i < 3.0:
                        S_beta = 2.01
                    elif avg_beta_i < 5.0:
                        S_beta = 2.35
                    elif avg_beta_i < 10.0:
                        S_beta = 3.86
                    else:
                        S_beta = 5.0

                    # 5. Общий балл S_i
                    S_i = S_alpha + S_beta

                    # Проверка на критический показатель
                    if S_i >= 9:
                        critical_indicators += 1

                    total_Si += S_i

                    results.append({
                        'name': name,
                        'alpha_i': alpha_i,
                        'S_alpha': S_alpha,
                        'sum_beta_i': sum_beta_i,
                        'avg_beta_i': avg_beta_i,
                        'S_beta': S_beta,
                        'S_i': S_i,
                        'is_critical': S_i >= 9
                    })

                except Exception as e:
                    print(f"\nОшибка при расчёте показателя {name}: {e}")
                    continue

            # Расчёт УКИЗВ
            if not results:
                print("\nНет показателей с превышением ПДК. Вода соответствует нормативам.")
                return

            n = len(results)
            F = critical_indicators
            k = 1 - 0.1 * F if F > 0 else 1.0
            S_ud = (total_Si / n) * k

            # Форматированный вывод
            print("\n=== Детальные результаты ===")
            df_results = pd.DataFrame(results)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', 1000)
            print(df_results[['name', 'alpha_i', 'S_alpha', 'avg_beta_i', 'S_beta', 'S_i', 'is_critical']])

            print("\n=== ИТОГИ ===")
            print(f"Количество показателей: {n}")
            print(f"Критических показателей (S_i ≥ 9): {critical_indicators}")
            print(f"УКИЗВ (S_уд) = {S_ud:.2f}")

            quality = (
                "Чистая (S_уд < 2)" if S_ud < 2 else
                "Слабо загрязнённая (2 ≤ S_уд < 4)" if S_ud < 4 else
                "Загрязнённая (4 ≤ S_уд < 6)" if S_ud < 6 else
                "Сильно загрязнённая (6 ≤ S_уд < 8)" if S_ud < 8 else
                "Чрезвычайно загрязнённая (S_уд ≥ 8)"
            )

            print(f"\nКачество воды: {quality}")


    #Странички
    def input_11_parametrs_page(e):
        """страница с анализом проб"""
        page.controls.clear()
        # Настройка AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Входные параметры",
                          color=COLORS["white"],size=44, italic=True),
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
    def coordinates_page(e):
        """Страница ввода географических координат и описания места отбора проб"""
        page.controls.clear()

        # Настройка AppBar с иконкой
        page.appbar = ft.AppBar(
            title=ft.Row([
                ft.Icon(ft.icons.LOCATION_ON, size=36),
                ft.Text(" Географическая локация", size=36, italic=True)
            ]),
            center_title=True,
            bgcolor=COLORS["dark_green"],
            toolbar_height=80,
            color=COLORS["white"]
        )

        # Информационная карточка
        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Инструкция по заполнению:",
                            size=18,
                            weight="bold",
                            color=COLORS["dark_green"]),
                    ft.Text(
                        "1. Укажите точные координаты места отбора пробы\n"
                        "2. Добавьте описание местности и источника\n"
                        "3. Пронумеруйте точку отбора для идентификации\n"
                        "4. Данные сохранятся автоматически при вводе",
                        color=COLORS["dark_green"]
                    )
                ]),
                padding=20
            ),
            color=COLORS["light_green"],
            elevation=3,
            margin=ft.margin.only(bottom=20)
        )

        # Поля ввода с пояснениями
        coord_inputs = ft.ResponsiveRow(
            [
                ft.Column([
                    ft.Text("Широта (градусы):", color=COLORS["white"]),
                    gradys_sh_input
                ], col={"sm": 12, "md": 3}, spacing=5),

                ft.Column([
                    ft.Text("Долгота (градусы):", color=COLORS["white"]),
                    gradys_d_input
                ], col={"sm": 12, "md": 3}, spacing=5),

                ft.Column([
                    ft.Text("Описание места:", color=COLORS["white"]),
                    description_input
                ], col={"sm": 12, "md": 3}, spacing=5),

                ft.Column([
                    ft.Text("Номер точки:", color=COLORS["white"]),
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
                            color=COLORS["dark_green"]),
                    ft.Divider(height=10, color="transparent"),
                    coord_inputs,
                    ft.ElevatedButton(
                        "Показать на карте",
                        icon=ft.icons.MAP,
                        style=ft.ButtonStyle(
                            bgcolor=COLORS["medium_green"],
                            color=COLORS["white"],
                            padding=20
                        ),
                        on_click=lambda _: webbrowser.open(
                            f"https://www.google.com/maps?q={gradys_sh_input.value},{gradys_d_input.value}")
                    )
                ]),
                padding=25
            ),
            elevation=8,
            color=COLORS["white"],
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
                            color=COLORS["white"],
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
    def location_page(e):
        """
        Страница описания места отбора проб воды
        """
        # Очищаем страницу перед построением
        page.controls.clear()

        # Создаем AppBar с иконкой
        app_bar = ft.AppBar(
            title=ft.Row([
                ft.Icon(ft.icons.PIN_DROP, size=36),
                ft.Text(" Описание места отбора проб", size=36, italic=True)
            ]),
            center_title=True,
            bgcolor=COLORS["dark_green"],
            toolbar_height=80,
            color=COLORS["white"]
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
    def _create_info_card():
        """Создает информационную карточку с описанием требований"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Зачем нужно описание места:",
                            size=18,
                            weight="bold",
                            color=COLORS["light_green"]),
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
                            color=COLORS["light_green"]),
                    _create_example_container()
                ]),
                padding=20
            ),
            color=COLORS["dark_green"],
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
                color=COLORS["white"],
                bgcolor=COLORS["light_green"],
                italic=True
            ),
            padding=10,
            border=ft.border.all(1, COLORS["light_green"]),
            bgcolor=ft.colors.GREY_100
        )
    def _create_input_card():
        """Создает карточку с полями ввода данных"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Характеристики точки отбора:",
                            size=20,
                            weight="bold",
                            color=COLORS["white"]),
                    ft.Divider(height=10, color="transparent"),
                    _create_input_fields(),
                    _create_action_buttons()
                ]),
                padding=25
            ),
            elevation=8,
            color=COLORS["dark_green"],
            margin=ft.margin.only(bottom=30),
        )
    def _create_input_fields():
        """Создает поля ввода с улучшенным оформлением"""
        return ft.ResponsiveRow(
            [
                ft.Column([
                    ft.Text("Детальное описание места:",
                            color=COLORS["white"],
                            weight="bold"),
                    ft.Text("(рельеф, источник, окружение)",
                            color=COLORS["white"],
                            size=12),
                    description_input,
                ], col={"sm": 12, "md": 8}, spacing=5),

                ft.Column([
                    ft.Text("Идентификационный номер:",
                            color=COLORS["white"],
                            weight="bold"),
                    ft.Text("(уникальный для каждой точки)",
                            color=COLORS["white"],
                            size=12),
                    number_of_point_input,
                    _create_auto_number_button()
                ], col={"sm": 12, "md": 4}, spacing=10),
            ],
            spacing=20,
        )
    def _create_auto_number_button():
        """Создает кнопку для автоматического назначения номера"""
        return ft.ElevatedButton(
            "Автоназначение номера",
            icon=ft.icons.AUTOFPS_SELECT,
            style=ft.ButtonStyle(
                bgcolor=COLORS["medium_green"],
                color=COLORS["white"],
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
                icon=ft.icons.SAVE,
                style=ft.ButtonStyle(
                    bgcolor=COLORS["light_green"],
                    color=COLORS["white"],
                    padding=20
                )
            ),
            ft.ElevatedButton(
                "Прикрепить фото",
                icon=ft.icons.CAMERA_ALT,
                style=ft.ButtonStyle(
                    bgcolor=COLORS["light_green"],
                    color=COLORS["white"],
                    padding=20
                )
            )
        ], spacing=15, alignment=ft.MainAxisAlignment.CENTER)
    def _create_footer_notification():
        """Создает уведомление в нижней части страницы"""
        return ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.INFO, color=COLORS["light_green"]),
                ft.Text(
                    "Эти данные будут включены в итоговый протокол анализа",
                    color=COLORS["white"],
                    bgcolor=COLORS["light_green"],
                )
            ]),
            alignment=ft.alignment.center
        )
    def water_quality_index(e):
        """Функция построения страницы расчета УКИЗВ"""
        # Очищаем страницу
        page.controls.clear()

        # Настройка AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Расчет УКИЗВ",
                          color=COLORS["white"],
                          size=40,
                          italic=True),
            center_title=True,
            bgcolor=COLORS["dark_green"],
            toolbar_height=70
        )


        # Инициализация полей ввода
        substance_name_input = create_input_field("Название показателя" )
        pdk_input = create_input_field("ПДК (норматив)")
        total_samples_input = create_input_field("Общее количество проб",)
        exceed_samples_input = create_input_field("Количество проб с превышением")
        concentrations_container = ft.Column(spacing=10)

        # Создаем карточку с полями ввода
        input_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Параметры воды для анализа",
                            size=16,
                            weight="bold",
                            color=COLORS["dark_green"]),
                    ft.Divider(height=1, color=COLORS["medium_green"]),

                    ft.Row([
                        substance_name_input,
                        ft.Column([
                            pdk_input,
                            total_samples_input
                        ], spacing=10)
                    ], spacing=20),

                    exceed_samples_input,
                    concentrations_container,

                ], spacing=15),
                padding=20,
                width=600
            ),
            elevation=8,
            color=COLORS["medium_green"],
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
                            ft.PopupMenuItem(
                                text="Сохранить в TXT",
                                icon=ft.Icons.TEXT_SNIPPET,
                                #on_click=save_result_txt,
                            ),
                            ft.PopupMenuItem(
                                text="Сохранить в Word",
                                icon=ft.Icons.DESCRIPTION,
                                #on_click=save_result_to_word,
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
    def sample_compaires(e):
            page.scroll = "adaptive",
            page.controls.clear()
            page.appbar = ft.AppBar(
                title=ft.Text("Информация о нас", color=COLORS["white"], italic=True, size=40),
                center_title=True,
                bgcolor=COLORS["dark_green"],
            )
            page.add(ft.Row([menubar])),
            page.add(
                ft.Container(
                    ft.Text(
                        value="Вводное слово",
                        text_align="center",
                        size=24,
                        color=COLORS["dark_green"],
                        italic=True,
                    ),
                ),
                ft.Container(
                    ft.Text(
                        value="Современный рынок разработки программного обеспечения обязывает разработчиков программного обеспечения не только быть специалистами своей области, но и ориентироваться в большинстве смежных технологических областей и даже получать знания в фундаментальных областях науки для решения масштабных задач. Данная работа посвящена разработке программного обеспечения для помощи учёным химикам, гидрологам и микробиологам для проведения анализа, помощи в сборе и структуризации данных пробоотборов в полевых условиях. Такая деятельность, помимо формирования практического опыта, позволяет сформировать новое видение классических задач по разработке программных комплексов и программного обеспечения, а также открывает ряд новых возможностей для взаимодействия людей разных специальностей для достижения одной большой цели.",
                        size=18,
                    ),
                ),
                ft.Container(
                    ft.Text(
                        value="Преимущества",
                        text_align="center",
                        size=24,
                        color=COLORS["dark_green"],
                        italic=True,
                    ),
                ),
                ft.Container(
                    ft.Text(
                        value="С помощью наших расчетов вы сможете учитывать все важные факторы, влияющие на эффективность работы антенны, такие как частота, угол наклона и размеры. Мы стремимся сделать процесс проектирования антенн более эффективным и доступным, предлагая надежные решения под любые задачи.",
                        text_align="justify",
                        size=18,
                    ),
                ),

                ft.Container(
                    ft.ElevatedButton(
                        text="Узнать больше о Волонтерском центре",
                        color=COLORS["white"],
                        on_click=open_url,
                        bgcolor=COLORS["medium_green"],

                    )
                ),
                ft.Container(
                    ft.ElevatedButton(
                        text="Узнать больше о СНО РТУ МИРЭА",
                        color=COLORS["white"],
                        on_click=open_url1,
                        bgcolor=COLORS["medium_blue"],
                    )
                )

            )
    def methods_page(e):
        page.scroll = "adaptive",
        page.controls.clear()
        page.appbar = ft.AppBar(
                title=ft.Text("Информация о нас", color=COLORS["white"], italic=True, size=40),
                center_title=True,
                bgcolor=COLORS["dark_green"],
        )
        content = ft.Container(
                ft.Text("Помогите мне пж, я хз как я сюда попала...",
                                size=26,
                                color=COLORS["dark_green"],
                                weight="w600",
                                text_align="center")

                )
        page.padding = 20
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
    def normative_page(e):
        page.controls.clear()
        # Настройка AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Нормативы",
                          color=COLORS["white"], size=44, italic=True),
            center_title=True,
            bgcolor=COLORS["dark_green"],
            toolbar_height=70
        )

        page.padding = 20
        page.add(
            ft.Column(
                controls=[
                    menubar,
                    ft.Container(
                        content=create_analysis_table(),
                        padding=20
                    )
                ],
                spacing=0,
                expand=True
            )
        )
   
        page.scroll = "adaptive"
        page.controls.clear()

        # Загрузка кастомной иконки волонтерского центра
        volunteer_icon = ft.Image(
            src=r"C:/Users/wertei siz/Dropbox/ПК/Downloads/вц.png",
            width=65,
            height=65,
            fit=ft.ImageFit.CONTAIN,
        )

        # Стилизованный AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Информация о нас",
                          color=ft.colors.WHITE,
                          size=32,
                          weight="w600",
                          font_family="RobotoSlab"),
            center_title=True,
            bgcolor=COLORS["dark_green"],
            toolbar_height=80,
        )

        # Основное содержимое
        content = ft.Column(
            spacing=20,
            scroll="adaptive",
            controls=[
                # Заголовок и основной текст
                ft.Container(
                 content=ft.Column([
                        ft.Text("Вводное слово",
                                size=26,
                                color=COLORS["dark_green"],
                                weight="w600",
                                text_align="center"),

                        ft.Text(
                            "Современный рынок разработки программного обеспечения обязывает разработчиков "
                            "не только быть специалистами своей области, но и ориентироваться в смежных "
                            "технологиях и фундаментальных науках для решения масштабных задач.\n\n"
                            "Наша работа посвящена созданию ПО для учёных-химиков, гидрологов и микробиологов "
                            "для анализа, сбора и структуризации данных пробоотборов в полевых условиях.",
                            size=18,
                            text_align="justify",
                            color=ft.colors.BLACK87,
                        ),
                    ],
                        spacing=15),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.colors.GREY_100,
                ),

                # Блок преимуществ
                ft.Container(
                    content=ft.Column([
                        ft.Text("Преимущества",
                                size=26,
                                color=COLORS["dark_green"],
                                weight="w600",
                                text_align="center"),

                        ft.Text(
                            "С помощью нашего ПО вы сможете:\n"
                            "• Учитывать все важные факторы анализа\n"
                            "• Автоматизировать сбор и обработку данных\n"
                            "• Получать точные и структурированные результаты\n"
                            "• Работать в полевых условиях без интернета\n\n"
                            "Мы стремимся сделать научные исследования более эффективными и доступными.",
                            size=18,
                            text_align="justify",
                        ),
                    ],
                        spacing=15),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.colors.GREY_100,
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
                            color=COLORS["dark_green"],
                            bgcolor=COLORS["white"],
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
                                ft.Icon(ft.icons.SCHOOL, size=20),
                                ft.Text(" СНО РТУ МИРЭА", size=16,color=ft.colors.WHITE),
                            ],
                                alignment="center",
                                spacing=10),
                            color=ft.colors.WHITE,
                            bgcolor=COLORS["medium_blue"],
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
    def show_result_11_parametrs(e):
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
                                color=COLORS["accent"]),
                        ft.Divider(height=10, color="transparent"),
                        ft.Text(result_text,
                                font_family="Courier New",
                                size=14,
                                color=COLORS["dark_purple"],
                                selectable=True)
                    ], spacing=5),
                    padding=25,
                    width=450
                ),
                elevation=10,
                color=COLORS["ACCENT"],
                margin=15,
                shadow_color=COLORS["dark_green"]
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
    def create_analysis_table():
        # Цвета
        ACCENT_GREEN = "#34C92A"
        HEADER_BG = "#2A8C22"
        BORDER_COLOR = "#5CD954"
        HOVER_COLOR = "#E8F7E7"
        BG_COLOR = "#F5FDF5"

        # Данные для таблицы
        components = [
            "Алюминий", "Аммоний", "Железо общее", "Марганец", "Медь",
            "Нитрит", "Фенолы", "Формальдегид", "Фосфаты", "Фториды", "Цветность"
        ]

        measurements = [
            "0,15-1,0", "0,2-4,0", "0,05-2,0", "0,8-1,0", "0,1-4,0",
            "0,04-2,0", "0,002-0,05", "0,03-0,4", "0,1-3,5", "0,04-3,0", "20-200 град."
        ]

        sample_volumes = ["10", "5", "10", "10", "10", "5", "250", "10", "10", "5", "5"]
        wavelengths = ["525", "430", "502", "470", "470", "525", "470", "525", "660", "620", "400"]
        pdk_values = ["0,5", "2,6", "0,3", "0,1", "1,0", "3,3", "0,1", "0,05", "3,5", "0,7-1,5", "35"]

        # Создаем таблицу
        table = DataTable(
            columns=[
                DataColumn(Text("Анализируемый компонент (в воде)", weight="bold", color=colors.WHITE)),
                DataColumn(Text("Диапазон измерений, мг/л", weight="bold", color=colors.WHITE)),
                DataColumn(Text("Объем пробы, мл", weight="bold", color=colors.WHITE)),
                DataColumn(Text("Длина волны, нм", weight="bold", color=colors.WHITE)),
                DataColumn(Text("ПДК, мг/л", weight="bold", color=colors.WHITE)),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text(components[i])),
                        DataCell(Text(measurements[i])),
                        DataCell(Text(sample_volumes[i])),
                        DataCell(Text(wavelengths[i])),
                        DataCell(Text(pdk_values[i]))
                    ]
                ) for i in range(len(components))
            ],
            border=border.all(1, BORDER_COLOR),
            border_radius=10,
            heading_row_color=HEADER_BG,
            heading_row_height=40,
            data_row_color={"hovered": HOVER_COLOR},
            divider_thickness=1,
            show_checkbox_column=False,
        )

        return Container(
            content=Column([
                Text("Параметры химического анализа воды",
                     size=18, weight="bold", color=HEADER_BG),
                table
            ], spacing=10),
            padding=20,
            border_radius=15,
            bgcolor=BG_COLOR,
            margin=10,
            border=border.all(1, BORDER_COLOR),
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=colors.BLACK12,
                offset=Offset(0, 3),
            )
        )

    # Функции расчета
    # Разнообразные вычисления
    def calculate_water_quality():
        """Основная функция расчета УКИЗВ"""
        try:
            if not substances_data:
                raise ValueError("Добавьте хотя бы один показатель для расчета")

            results = []
            total_Si = 0
            critical_indicators = 0

            for sub in substances_data:
                if sub["exceed_samples"] == 0:
                    continue

                alpha_i = (sub["exceed_samples"] / sub["total_samples"]) * 100

                if alpha_i < 1:
                    S_alpha = 0
                elif 1 <= alpha_i < 5:
                    S_alpha = 1.1
                elif 5 <= alpha_i < 10:
                    S_alpha = 1.4
                elif 10 <= alpha_i < 20:
                    S_alpha = 2.15
                elif 20 <= alpha_i < 30:
                    S_alpha = 2.6
                elif 30 <= alpha_i < 40:
                    S_alpha = 3.2
                elif 40 <= alpha_i < 50:
                    S_alpha = 3.85
                elif 50 <= alpha_i < 70:
                    S_alpha = 4.0
                else:
                    S_alpha = 5.0

                sum_beta_i = sum([c / sub["pdk"] for c in sub["concentrations"]])
                avg_beta_i = sum_beta_i / sub["exceed_samples"]

                if avg_beta_i < 1.3:
                    S_beta = 1.0
                elif 1.3 <= avg_beta_i < 2.0:
                    S_beta = 1.17
                elif 2.0 <= avg_beta_i < 3.0:
                    S_beta = 2.01
                elif 3.0 <= avg_beta_i < 5.0:
                    S_beta = 2.35
                elif 5.0 <= avg_beta_i < 10.0:
                    S_beta = 3.86
                else:
                    S_beta = 5.0

                S_i = S_alpha + S_beta
                if S_i >= 9:
                    critical_indicators += 1
                total_Si += S_i

                results.append({
                    "name": sub["name"],
                    "alpha_i": alpha_i,
                    "S_alpha": S_alpha,
                    "avg_beta_i": avg_beta_i,
                    "S_beta": S_beta,
                    "S_i": S_i,
                })

            n = len(results)
            if n == 0:
                result_text = "Нет превышений ПДК. Вода чистая."
            else:
                F = critical_indicators
                k = 1 - (0.1 * F) if F > 0 else 1.0
                S_ud = (total_Si / n) * k

                if S_ud < 1:
                    quality = "Очень чистая (I класс)"
                elif 1 <= S_ud < 2:
                    quality = "Чистая (II класс)"
                elif 2 <= S_ud < 4:
                    quality = "Умеренно загрязнённая (III класс)"
                elif 4 <= S_ud < 6:
                    quality = "Загрязнённая (IV класс)"
                elif 6 <= S_ud < 10:
                    quality = "Грязная (V класс)"
                else:
                    quality = "Очень грязная (VI класс)"

                substances_text = "\n".join([
                    f"║  • {res['name']:15} S_i={res['S_i']:.2f} (α={res['alpha_i']:.1f}%, β={res['avg_beta_i']:.1f}) ║"
                    for res in results
                ])

                result_text = f"""
    ╔══════════════════════════════════════════╗
    ║          РЕЗУЛЬТАТЫ АНАЛИЗА ВОДЫ          ║
    ╠══════════════════════════════════════════╣
    ║  Количество показателей: {n:15}       ║
    ║  Критических показателей: {F:14}       ║
    ╠══════════════════════════════════════════╣
    {substances_text}
    ╠══════════════════════════════════════════╣
    ║  УКИЗВ: {S_ud:34.2f}       ║
    ║  Качество воды: {quality:25} ║
    ╚══════════════════════════════════════════╝
    """

            result_card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Результаты расчёта УКИЗВ",
                                size=18,
                                weight="bold",
                                color=COLORS["medium_green"]),
                        ft.Divider(height=1, color=COLORS["medium_green"]),
                        ft.Text(result_text,
                                font_family="Consolas",
                                size=14,
                                color=COLORS["dark_green"])
                    ], spacing=10),
                    padding=20,
                    width=600
                ),
                elevation=8,
                color=COLORS["medium_green"],
                margin=10
            )

            result_container.controls.clear()
            result_container.controls.append(result_card)
            page.update()

        except Exception as err:
            show_save_message(f"Ошибка расчета: {str(err)}", is_error=True)
            page.update()
    def add_substance(name_input, pdk_input, total_input, exceed_input, conc_container):
        """Добавление нового показателя"""
        try:
            if not name_input.value:
                raise ValueError("Введите название показателя")
            if not pdk_input.value or float(pdk_input.value) <= 0:
                raise ValueError("ПДК должно быть положительным числом")
            if not total_input.value or int(total_input.value) <= 0:
                raise ValueError("Количество проб должно быть положительным числом")
            if not exceed_input.value or int(exceed_input.value) < 0:
                raise ValueError("Количество превышений не может быть отрицательным")

            concentrations = []
            for control in conc_container.controls:
                if isinstance(control, ft.TextField) and control.value:
                    concentrations.append(float(control.value))

            substances_data.append({
                "name": name_input.value,
                "pdk": float(pdk_input.value),
                "total_samples": int(total_input.value),
                "exceed_samples": int(exceed_input.value),
                "concentrations": concentrations
            })

            name_input.value = ""
            pdk_input.value = ""
            total_input.value = ""
            exceed_input.value = ""
            conc_container.controls.clear()

            show_save_message(f"Добавлен показатель: {substances_data[-1]['name']}", is_error=False)
            page.update()

        except ValueError as err:
            show_save_message(f"Ошибка: {str(err)}", is_error=True)
            page.update()
    def show_water_quality_result(e):
        try:
            # Получаем данные из полей ввода
            substances_data = []
            for substance in substances_inputs:
                name = substance['name'].value
                pdk = float(substance['pdk'].value)
                total_samples = int(substance['total_samples'].value)
                exceed_samples = int(substance['exceed_samples'].value)

                concentrations = []
                if exceed_samples > 0:
                    for conc in substance['concentrations']:
                        concentrations.append(float(conc.value))

                substances_data.append({
                    "name": name,
                    "pdk": pdk,
                    "total_samples": total_samples,
                    "exceed_samples": exceed_samples,
                    "concentrations": concentrations,
                })

            # Выполняем расчеты
            results = []
            total_Si = 0
            critical_indicators = 0

            for sub in substances_data:
                if sub["exceed_samples"] == 0:
                    continue

                # Расчет параметров
                alpha_i = (sub["exceed_samples"] / sub["total_samples"]) * 100

                # Определение S_alpha
                if alpha_i < 1:
                    S_alpha = 0
                elif 1 <= alpha_i < 5:
                    S_alpha = 1.1
                elif 5 <= alpha_i < 10:
                    S_alpha = 1.4
                elif 10 <= alpha_i < 20:
                    S_alpha = 2.15
                elif 20 <= alpha_i < 30:
                    S_alpha = 2.6
                elif 30 <= alpha_i < 40:
                    S_alpha = 3.2
                elif 40 <= alpha_i < 50:
                    S_alpha = 3.85
                elif 50 <= alpha_i < 70:
                    S_alpha = 4.0
                else:
                    S_alpha = 5.0

                # Расчет beta_i
                sum_beta_i = sum([c / sub["pdk"] for c in sub["concentrations"]])
                avg_beta_i = sum_beta_i / sub["exceed_samples"]

                # Определение S_beta
                if avg_beta_i < 1.3:
                    S_beta = 1.0
                elif 1.3 <= avg_beta_i < 2.0:
                    S_beta = 1.17
                elif 2.0 <= avg_beta_i < 3.0:
                    S_beta = 2.01
                elif 3.0 <= avg_beta_i < 5.0:
                    S_beta = 2.35
                elif 5.0 <= avg_beta_i < 10.0:
                    S_beta = 3.86
                else:
                    S_beta = 5.0

                S_i = S_alpha + S_beta
                if S_i >= 9:
                    critical_indicators += 1
                total_Si += S_i

                results.append({
                    "name": sub["name"],
                    "alpha_i": alpha_i,
                    "S_alpha": S_alpha,
                    "avg_beta_i": avg_beta_i,
                    "S_beta": S_beta,
                    "S_i": S_i,
                })

            # Расчет УКИЗВ
            n = len(results)
            if n == 0:
                result_text = """
    ╔══════════════════════════════╗
    ║     РЕЗУЛЬТАТЫ АНАЛИЗА ВОДЫ     ║
    ╠══════════════════════════════╣
    ║  Превышений ПДК не обнаружено  ║
    ║  Вода соответствует нормативам ║
    ╚══════════════════════════════╝
    """
            else:
                F = critical_indicators
                k = 1 - (0.1 * F) if F > 0 else 1.0
                S_ud = (total_Si / n) * k

                # Определение класса воды
                if S_ud < 1:
                    quality = "Очень чистая (I класс)"
                elif 1 <= S_ud < 2:
                    quality = "Чистая (II класс)"
                elif 2 <= S_ud < 4:
                    quality = "Умеренно загрязнённая (III класс)"
                elif 4 <= S_ud < 6:
                    quality = "Загрязнённая (IV класс)"
                elif 6 <= S_ud < 10:
                    quality = "Грязная (V класс)"
                else:
                    quality = "Очень грязная (VI класс)"

                # Формируем текст результатов
                substances_text = "\n".join([
                    f"║  • {res['name']:15} S_i={res['S_i']:.2f} (α={res['alpha_i']:.1f}%, β={res['avg_beta_i']:.1f}) ║"
                    for res in results
                ])

                result_text = f"""
    ╔══════════════════════════════════════════╗
    ║          РЕЗУЛЬТАТЫ АНАЛИЗА ВОДЫ          ║
    ╠══════════════════════════════════════════╣
    ║  Количество показателей: {n:15}       ║
    ║  Критических показателей: {F:14}       ║
    ╠══════════════════════════════════════════╣
    {substances_text}
    ╠══════════════════════════════════════════╣
    ║  УКИЗВ: {S_ud:34.2f}       ║
    ║  Качество воды: {quality:25} ║
    ╚══════════════════════════════════════════╝
    """

            # Создаем карточку с результатами
            result_card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Результаты расчёта УКИЗВ",
                                size=18,
                                weight="bold",
                                color=COLORS["medium_green"]),
                        ft.Divider(height=1, color=COLORS["medium_green"]),
                        ft.Text(result_text,
                                font_family="Consolas",
                                size=14,
                                color=COLORS["dark_green"])
                    ], spacing=10),
                    padding=20,
                    width=600
                ),
                elevation=8,
                color=COLORS["medium_green"],
                margin=10
            )

            # Очищаем контейнер и добавляем новую карточку
            result_container.controls.clear()
            result_container.controls.append(
                ft.Row([result_card], alignment=ft.MainAxisAlignment.CENTER)
            )
            page.update()

        except ValueError as err:
            show_save_message(f"Ошибка: {str(err)}", is_error=True)
            page.update()
    def create_substance_input(index):
        """Создает элементы ввода для одного показателя"""
        name = ft.TextField(
            label=f"Показатель {index + 1}",
            border_color=COLORS["medium_green"],
            width=200
        )

        pdk = ft.TextField(
            label="ПДК",
            border_color=COLORS["medium_green"],
            width=100
        )

        total_samples = ft.TextField(
            label="Всего проб",
            border_color=COLORS["medium_green"],
            width=100
        )

        exceed_samples = ft.TextField(
            label="Превышений",
            border_color=COLORS["medium_green"],
            width=100,
            on_change=lambda e: update_concentration_inputs(e, index)
        )

        return {
            "name": name,
            "pdk": pdk,
            "total_samples": total_samples,
            "exceed_samples": exceed_samples,
            "concentrations": []
        }
    def update_concentration_inputs(e, index):
        """Обновляет поля ввода концентраций при изменении количества превышений"""
        try:
            exceed = int(e.control.value)
            if exceed < 0:
                return

            # Удаляем старые поля
            for conc in substances_inputs[index]['concentrations']:
                if conc in input_container.controls:
                    input_container.controls.remove(conc)

            # Создаем новые поля
            substances_inputs[index]['concentrations'] = []
            for i in range(exceed):
                conc = ft.TextField(
                    label=f"Конц. пробы {i + 1}",
                    border_color=COLORS["light_green"],
                    width=120
                )
                substances_inputs[index]['concentrations'].append(conc)

            # Перестраиваем интерфейс
            build_input_interface()
            page.update()
        except ValueError:
            pass
    def build_input_interface():
        """Строит интерфейс ввода данных"""
        input_container.controls.clear()

        # Добавляем заголовок
        input_container.controls.append(
            ft.Text("Введите данные по показателям загрязнения:",
                    size=16,
                    color=COLORS["dark_green"])
        )

        # Добавляем поля для каждого показателя
        for i, substance in enumerate(substances_inputs):
            row = ft.Row([
                substance['name'],
                substance['pdk'],
                substance['total_samples'],
                substance['exceed_samples'],
            ], spacing=10)

            input_container.controls.append(row)

            # Добавляем поля концентраций при необходимости
            if substance['concentrations']:
                conc_row = ft.Row(
                    substance['concentrations'],
                    wrap=True,
                    spacing=10
                )
                input_container.controls.append(conc_row)

        # Добавляем кнопки управления
        input_container.controls.append(
            ft.Row([
                ft.ElevatedButton(
                    "Добавить показатель",
                    icon=ft.icons.ADD,
                    on_click=add_substance
                ),
                ft.ElevatedButton(
                    "Рассчитать УКИЗВ",
                    icon=ft.icons.CALCULATE,
                    on_click=show_water_quality_result
                )
            ], spacing=20)
        )
    def add_substance(self, name_input, min_input, max_input, unit_input, container):
        """Добавляет новый показатель для ввода"""
        substances_inputs.append(create_substance_input(len(substances_inputs)))
        build_input_interface()
        page.update()
   #УКИЗВ СТРАНИЦА
    def water_quality_page():
        """Страница расчета УКИЗВ"""
        page.controls.clear()

        # Настройка AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Расчет УКИЗВ",
                          color=COLORS["white"],
                          size=40),
            center_title=True,
            bgcolor=COLORS["dark_green"],
            toolbar_height=70
        )

        # Инициализация данных
        global substances_inputs, input_container, result_container
        substances_inputs = [create_substance_input(0)]
        input_container = ft.Column(spacing=15)
        result_container = ft.Column()

        # Строим интерфейс
        build_input_interface()

        # Добавляем элементы на страницу
        page.add(
            ft.Column(
                [
                    input_container,
                    result_container
                ],
                scroll=True,
                expand=True
            )
        )
        page.update()


    # Контейнер для сообщений о сохранении
    save_message = ft.Text(color=COLORS["medium_green"], size=14)
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
        bgcolor=COLORS["medium_green"],
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
                on_click=create_water_protocol_txt,
            ),
            ft.PopupMenuItem(
                text="Сохранить в Word",
                icon=ft.Icons.DESCRIPTION,
                on_click=create_water_protocol_word,
            ),
            ft.PopupMenuItem(
                text="Сохранить в Excel",
                icon=ft.Icons.TABLE_CHART,
                on_click=create_water_protocol_excel,
            ),
        ],
        icon=ft.Icons.SAVE,
        tooltip="Выберите формат сохранения",
        # Стиль для меню
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            side=ft.BorderSide(1, COLORS["medium_green"]),
            bgcolor=ft.Colors.WHITE,
        )
    )

    # Кнопки в строку с выпадающим меню сохранения
    buttons_row = ft.Row(
        [
            ft.ElevatedButton(
                text="Рассчитать",
                icon=ft.Icons.CALCULATE,
                style=btn_style,
                width=200,
                on_click=show_result_11_parametrs
            ),
            ft.Container(
                content=save_menu,
                padding=10,
                border_radius=12,
                border=ft.border.all(1, COLORS["medium_green"]),
                bgcolor=ft.Colors.WHITE,
                on_hover=lambda e: setattr(e.control, "bgcolor", COLORS["medium_green"]) or e.control.update()
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
        color=COLORS["medium_green"],
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
        overlay_color=ft.colors.TRANSPARENT,
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
            bgcolor=COLORS["medium_green"],
        ),
        controls=[
            # Меню "Информация"
            ft.SubmenuButton(
                content=ft.Text("Информация", color=COLORS["white"]),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("О нас", color=COLORS["dark_green"]),
                        leading=ft.Image(
                            src="C://Users//wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/О нас.png",
                            width=30,
                            height=30,
                        ),
                        style=menu_button_style("#E2D4F0"),
                        on_click=about_page,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Методические указания", color=COLORS["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/DesktopПО/Иконки флет/Инструкция.png",
                            width=30,
                            height=30,
                        ),
                        style=menu_button_style("#E2D4F0"),
                        on_click=methods_page,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Нормативы", color=COLORS["dark_green"]),leading=ft.Image(
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
                content=ft.Text("Расчёты", color=COLORS["white"]),
                controls=[
                    # Позиционирование
                    ft.SubmenuButton(
                        content=ft.Text("Позиционирование в пространстве", color=COLORS["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/Земля.png",
                            width=30,
                            height=30,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Определение координат", color=COLORS["dark_green"]),
                                leading=ft.Image(
                                    src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/координаты.png",
                                    width=25,
                                    height=25,
                                ),
                                style=menu_button_style("#fcef72"),
                                on_click=coordinates_page,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Описание места", color=COLORS["dark_green"]),
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
                        content=ft.Text("Общая концентрация", color=COLORS["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/концентрация.png",
                            width=30,
                            height=30,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("11 Параметров", color=COLORS["dark_green"]),
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
                        content=ft.Text("Качество воды", color=COLORS["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/концентрация.png",
                            width=30,
                            height=30,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Расчёт УКИВЗ", color=COLORS["dark_green"]),
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
                        content=ft.Text("Отклонение от ПДК", color=COLORS["dark_green"]),
                        leading=ft.Image(
                            src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/Отклонение от ПДК.png",
                            width=30,
                            height=30,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Сравнение проб", color=COLORS["dark_green"]),
                                leading=ft.Image(
                                    src="C:/Users/wertei siz/Dropbox/ПК/Desktop/ПО/Иконки флет/химик.png",
                                    width=30,
                                    height=30,
                                ),
                                style=menu_button_style("#16cc99"),
                                on_click=sample_compaires,

                            ),
                        ],

                    ),
                ],
            ),

        ]
    ),

    # Основной контент
    content = ft.Column(
            spacing=20,
            scroll="adaptive",
            controls=[
                ft.Container(
                    content=ft.Column([
                        # Заголовок и описание
                        ft.Text(
                            "Добро пожаловать в Aquaminerale!",
                            size=26,
                            weight="bold",
                            color= COLORS["white"],
                            text_align="center"
                        ),
                        ft.Text(
                            "Профессиональный инструмент для анализа природных водных источников в полевых условиях",
                            size=20,
                            color=COLORS["white"],
                            text_align="center"
                        ),

                        ft.Divider(height=20, color=COLORS["light_green"]),

                        # Блок возможностей
                        ft.Text(
                            "Основные возможности программы:",
                            size=22,
                            weight="bold",
                            color=COLORS["light_green"]
                        ),
                        ft.Column([
                            ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE, color=COLORS["light_green"]),
                                    ft.Text(" Анализ 11 ключевых параметров воды (Al, Fe, Mn, NO₂ и др.)",
                                            color=COLORS["white"])]),
                            ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE, color=COLORS["light_green"]),
                                    ft.Text(" Автоматический расчет УКИЗВ с классификацией качества воды",
                                            color=COLORS["white"])]),
                            ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE, color=COLORS["light_green"]),
                                    ft.Text(" Система поддержки решений для прогнозирования параметров",
                                            color=COLORS["white"])]),
                            ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE, color=COLORS["light_green"]),
                                    ft.Text(" Генерация отчетов в 3 форматах (Word, Excel, TXT) по ГОСТ",
                                            color=COLORS["white"])]),
                            ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE, color=COLORS["light_green"]),
                                    ft.Text(" Геопривязка проб с координатами и описанием местности",
                                            color=COLORS["white"])]),
                        ], spacing=10),

                        ft.Divider(height=20, color=COLORS["light_green"]),

                        # Инструкция
                        ft.Text("Как начать работу:", size=22, weight="bold", color=COLORS["light_green"]),
                        ft.Column([
                            ft.Text("1. Введите концентрации ионов (мг/л), полученные:", color=COLORS["white"]),
                            ft.Text("   - Фотоколориметром Экотест-2020", color=COLORS["white"], style="italic"),
                            ft.Text("   - Инструментальными методами анализа", color=COLORS["white"], style="italic"),
                            ft.Text("2. Нажмите 'Произвести расчет' для анализа данных", color=COLORS["white"]),
                            ft.Text("3. Сохраните отчет в нужном формате:", color=COLORS["white"]),
                            ft.Text("   - .docx (полноформатный протокол по ГОСТ)", color=COLORS["white"], style="italic"),
                            ft.Text("   - .xlsx (табличные данные для Excel)", color=COLORS["white"], style="italic"),
                            ft.Text("   - .txt (простые текстовые данные)", color=COLORS["white"], style="italic"),
                        ], spacing=10),

                        ft.Divider(height=20, color=COLORS["light_green"]),

                        # Важная информация
                        ft.Text("ВАЖНО:", size=18, weight="bold", color=COLORS["light_green"]),
                        ft.Text(
                            "• Все отчеты автоматически формируются по требованиям ГОСТ\n"
                            "• Программа поддерживает оффлайн-работу в полевых условиях\n"
                            "• Для точных результатов используйте свежие пробы воды",
                            color=COLORS["white"]
                        )
                    ],
                        spacing=15
                    ),
                    padding=25,
                    border_radius=15,
                    bgcolor=COLORS["dark_green"],
                    border=ft.border.all(2, COLORS["light_green"]))
            ]
    )
    auth_button = ft.ElevatedButton(
        "Войти",
        icon=ft.icons.LOGIN,
        color=COLORS["white"],
        bgcolor=COLORS["light_green"]
    )

    register_button = ft.ElevatedButton(
        "Зарегистрироваться",
        icon=ft.icons.PERSON_ADD,
        color=COLORS["white"],
        bgcolor=COLORS["light_green"]
    )

    change_theme = ft.IconButton(
        icon=ft.icons.BRIGHTNESS_4,
        tooltip="Сменить тему",
        icon_color=COLORS["white"]
    )

    scroll_up_button = ft.FloatingActionButton(
        icon=ft.icons.ARROW_UPWARD,
        bgcolor=COLORS["light_green"],
        mini=True
    )
    page.add(
        ft.Column(
            controls=[
                menubar,
                ft.Row(
                    controls=[
                        auth_button,
                        register_button,
                        change_theme,
                        scroll_up_button
                    ],
                    alignment="end",
                    spacing=15
                ),
                # Основной контент
                ft.Container(content=content, padding=20)
            ],
            spacing=0,
            expand=True
        )
    )


ft.app(target=main)