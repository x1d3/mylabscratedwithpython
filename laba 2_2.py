def check_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def calculate_lead_pipe_mass(length_m, wall_thickness_mm, inner_diameter_mm):
    density_lead_g_cm3 = 11.4  # Плотность свинца в г/см^3
    length_cm = length_m * 100  # Переводим длину из метров в сантиметры
    wall_thickness_cm = wall_thickness_mm / 10  # Переводим толщину стенок из миллиметров в сантиметры
    inner_radius_cm = inner_diameter_mm / 2 / 10  # Переводим внутренний диаметр из миллиметров в сантиметры

    # Вычисляем внешний радиус трубы в сантиметрах
    outer_radius_cm = inner_radius_cm + wall_thickness_cm

    # Вычисляем объем трубы в кубических сантиметрах
    volume_cm3 = 3.14159265 * (outer_radius_cm**2 - inner_radius_cm**2) * length_cm

    # Вычисляем массу трубы в граммах
    mass_g = volume_cm3 * density_lead_g_cm3

    # Переводим массу из граммов в килограммы
    mass_kg = mass_g / 1000

    return mass_kg

# Запрашиваем у пользователя данные
length_m = check_positive_float("Введите длину трубы в метрах: ")
wall_thickness_mm = check_positive_float("Введите толщину стенок трубы в миллиметрах: ")
inner_diameter_mm = check_positive_float("Введите внутренний диаметр трубы в миллиметрах: ")

# Вычисляем массу трубы и выводим результат в килограммах
mass_kg = calculate_lead_pipe_mass(length_m, wall_thickness_mm, inner_diameter_mm)
print(f"Масса свинцовой трубы составляет {mass_kg:.2f} килограмм.")
"""
15.	Вычислить массу свинцовой трубы, длина которой равна b м (плотность свинца равна 11,4 г/см3)
, толщина стенок а мм, а внутренний диаметр тру-бы равен d мм.
"""