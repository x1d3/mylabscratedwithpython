# Постоянная Больцмана
k_boltzmann = 1.38e-23  # Дж/К

# Моль водорода
n_moles = 1.0

# Список температур от 10°C до 20°C
temperatures_celsius = range(10, 21)

# Функция для перевода температуры из Цельсия в Кельвины
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Рассчитываем и выводим среднюю кинетическую энергию для каждой температуры
for temp_celsius in temperatures_celsius:
    temp_kelvin = celsius_to_kelvin(temp_celsius)
    rotational_energy = (3/2) * k_boltzmann * temp_kelvin * n_moles
    print(f"При {temp_celsius}°C средняя кинетическая энергия вращения: {rotational_energy:.2e} Дж")