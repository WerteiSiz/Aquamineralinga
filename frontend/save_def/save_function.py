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

def create_water_protocol_word(
            gradys_d_input, gradys_sh_input, location_input, description_input,
            number_of_point_input, Aluminum_input, ammonium_input, iron_input,
            manganese_input, copper_input, nitrite_input, phenols_input,
            formaldehyde_input, phosphates_input, fluorides_input, chroma_input,
            filename="Анализ_воды.docx"):

        doc = Document()

        # --- Настройка стилей ---
        style = doc.styles["Normal"]
        style.font.name = "Times New Roman"
        style.font.size = Pt(12)
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")

        # --- Текущая дата и время ---
        current_datetime = datetime.now()
        report_date = current_datetime.strftime("%d.%m.%Y")
        sampling_time = current_datetime.strftime("%H:%M")

        # --- Заголовок протокола ---
        title = doc.add_paragraph("Протокол полного химического анализа минеральной воды")
        title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        title.runs[0].bold = True
        title.runs[0].font.size = Pt(14)

        # --- Основная информация ---
        info = [
            f"№ ______ от «{report_date}» г.",
            f"Наименование и адрес лаборатории: {description_input}",
            f"Местоположение источника: {location_input}",
            f"Номер точки отбора: {number_of_point_input}",
            f"Дата и время отбора: {report_date} {sampling_time}"
        ]

        for item in info:
            doc.add_paragraph(item)

        # --- Органолептические показатели ---
        doc.add_paragraph("\nОрганолептические показатели:")
        ol_text = (
            f"Прозрачность: прозрачная, "
            f"Цвет: бесцветная, "
            f"Осадок: отсутствует, "
            f"Вкус и запах: нейтральный"
        )
        doc.add_paragraph(ol_text)

        # --- Таблица химических показателей ---
        doc.add_paragraph("\nХимические показатели:")
        table = doc.add_table(rows=1, cols=4)
        table.style = "Table Grid"

        # Заголовки
        hdr = table.rows[0].cells
        hdr[0].text = "Показатель"
        hdr[1].text = "Значение"
        hdr[2].text = "ПДК"
        hdr[3].text = "Нормативный документ"

        # Данные (примерные ПДК, можно заменить на актуальные)
        indicators = [
            ("Алюминий (Al)", Aluminum_input, "0.5 мг/л", "СанПиН 1.2.3685-21"),
            ("Аммоний (NH₄⁺)", ammonium_input, "2.0 мг/л", "ГОСТ 4192-82"),
            ("Железо (Fe)", iron_input, "0.3 мг/л", "ГОСТ 4011-72"),
            ("Марганец (Mn)", manganese_input, "0.1 мг/л", "ГОСТ 4974-72"),
            ("Медь (Cu)", copper_input, "1.0 мг/л", "ГОСТ 4388-72"),
            ("Нитриты (NO₂⁻)", nitrite_input, "3.0 мг/л", "ГОСТ 4192-82"),
            ("Фенолы", phenols_input, "0.001 мг/л", "СанПиН 1.2.3685-21"),
            ("Формальдегид", formaldehyde_input, "0.05 мг/л", "СанПиН 1.2.3685-21"),
            ("Фосфаты (PO₄³⁻)", phosphates_input, "3.5 мг/л", "ГОСТ 18963-73"),
            ("Фториды (F⁻)", fluorides_input, "1.5 мг/л", "ГОСТ 4386-89"),
            ("Хром (Cr)", chroma_input, "0.05 мг/л", "ГОСТ 4974-72")
        ]

        for name, value, pdk, normative in indicators:
            row = table.add_row().cells
            row[0].text = name
            row[1].text = str(value)
            row[2].text = pdk
            row[3].text = normative

        # --- Физические показатели ---
        doc.add_paragraph("\nФизические показатели:")
        doc.add_paragraph(f"Градусы D: {gradys_d_input}")
        doc.add_paragraph(f"Градусы SH: {gradys_sh_input}")

        # --- Подписи ---
        doc.add_paragraph("\n\nРуководитель: ___________________/____________/")
        doc.add_paragraph("Исполнитель: ___________________/____________/")
        doc.add_paragraph("М.П.")

        doc.save(filename)

def create_water_protocol_txt(e):
            try:
                # Получаем данные из полей ввода
                gradys_d = gradys_d_input.value
                gradys_sh = gradys_sh_input.value
                location = location_input.value
                description = description_input.value
                point_number = number_of_point_input.value

                # Химические показатели
                aluminum = Aluminum_input.value
                ammonium = ammonium_input.value
                iron = iron_input.value
                manganese = manganese_input.value
                copper = copper_input.value
                nitrite = nitrite_input.value
                phenols = phenols_input.value
                formaldehyde = formaldehyde_input.value
                phosphates = phosphates_input.value
                fluorides = fluorides_input.value
                chroma = chroma_input.value

                # Формируем текст отчета
                result_text = f"""
        ╔════════════════════════════════════════════╗
        ║          ПРОТОКОЛ АНАЛИЗА ВОДЫ            ║
        ╠════════════════════════════════════════════╣
        ║  ОСНОВНАЯ ИНФОРМАЦИЯ                       ║
        ║  • Номер точки: {point_number:>20}       ║
        ║  • Дата: {datetime.now().strftime('%d.%m.%Y'):>26}       ║
        ║  • Координаты: {gradys_sh}° с.ш., {gradys_d}° в.д. ║
        ║  • Местоположение: {location:>15}       ║
        ║  • Описание: {description:>22}       ║
        ╠════════════════════════════════════════════╣
        ║  ХИМИЧЕСКИЕ ПОКАЗАТЕЛИ (мг/л)              ║
        ║  • Алюминий (Al+2): {aluminum:>18}       ║
        ║  • Аммоний: {ammonium:>25}       ║
        ║  • Железо общее: {iron:>21}       ║
        ║  • Марганец: {manganese:>23}       ║
        ║  • Медь: {copper:>27}       ║
        ║  • Нитрит: {nitrite:>25}       ║
        ║  • Фенолы: {phenols:>25}       ║
        ║  • Формальдегид: {formaldehyde:>19}       ║
        ║  • Фосфаты: {phosphates:>23}       ║
        ║  • Фториды: {fluorides:>24}       ║
        ║  • Цветность: {chroma:>22}°       ║
        ╠════════════════════════════════════════════╣
        ║  ЗАКЛЮЧЕНИЕ                                ║
        ║  • Результаты сохранены {datetime.now().strftime('%d.%m.%Y %H:%M')} ║
        ╚════════════════════════════════════════════╝
        """

                # Формируем имя файла с датой и номером точки
                filename = f"Анализ_воды_точка_{point_number}_{datetime.now().strftime('%Y%m%d')}.txt"

                # Сохраняем файл
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(result_text)

                show_save_message(f"Данные сохранены в {filename}")

            except Exception as ex:
                show_save_message(f"Ошибка при сохранении: {str(ex)}", is_error=True)


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
