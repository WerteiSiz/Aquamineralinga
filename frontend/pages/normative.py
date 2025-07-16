def normative_page(e):
        page.controls.clear()
        # Настройка AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Нормативы",
                          color=Colors["white"], size=44, italic=True),
            center_title=True,
            bgcolor=Colors["dark_green"],
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
                DataColumn(Text("Анализируемый компонент (в воде)", weight="bold", color=ft.Colors.WHITE)),
                DataColumn(Text("Диапазон измерений, мг/л", weight="bold", color=ft.Colors.WHITE)),
                DataColumn(Text("Объем пробы, мл", weight="bold", color=ft.Colors.WHITE)),
                DataColumn(Text("Длина волны, нм", weight="bold", color=ft.Colors.WHITE)),
                DataColumn(Text("ПДК, мг/л", weight="bold", color=ft.Colors.WHITE)),
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
                color=ft.Colors.BLACK12,
                offset=Offset(0, 3),
            )
        )

