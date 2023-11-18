
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=MY+LABS+CREATED+WITH+PYTHON)](https://git.io/typing-svg)
 ```diff
- красный текст означает что лаба на данный момент не сдана и возможно есть ошибки
+ зеленый, что полностью верно решена, прошла все проверки и сдана
! оранжевый, что решена и проверена мной на работоспособность, но не сдана
@@ в самих кодах программ внизу есть многострочные комментарии с условием задачи(если в условии задачи уравнение, то оно отсуствует)@@
```
Here is my repository with my python labs created for university lab work
# LABA 2
```diff
+  DESCRIPTION LAB 1
```
Данный код выполняет следующие действия:

1. Импортирует функцию `sqrt` (квадратный корень) из модуля `math`.

2. Запрашивает у пользователя ввод значения переменной `b` в виде вещественного числа.

3. Вычисляет два выражения:

   - `z1 = (sqrt(2*b + 2*sqrt(b**2 - 4))/(sqrt(b**2 - 4))+ b + 2)`
   
     Это выражение включает в себя квадратный корень, деление, сложение и вычитание.

   - `z2 = 1/sqrt(b+2)`
   
     Это выражение также содержит деление и квадратный корень.

4. Выводит результаты вычислений на экран с использованием функции `print`.

   - `print("z1 = ", z1)` выводит значение `z1`.
   - `print("z2 = ", z2)` выводит значение `z2`.

Таким образом, код выполняет математические вычисления, основанные на введенном пользователем значении `b` и выводит результаты вычислений `z1` и `z2` на экран.
```diff
+  DESCRIPTION LAB 2
```
Этот код выполняет следующие действия:

1. Определяет функцию `check_positive_float(prompt)`, которая запрашивает у пользователя ввод числа типа float и проверяет, что введенное значение неотрицательное. Если ввод не соответствует требованиям, программа выводит сообщение об ошибке и запрашивает ввод снова.

2. Определяет функцию `calculate_lead_pipe_mass(length_m, wall_thickness_mm, inner_diameter_mm)`, которая принимает три параметра: длину трубы в метрах, толщину стенок трубы в миллиметрах и внутренний диаметр трубы в миллиметрах. Функция вычисляет массу свинцовой трубы, исходя из заданных параметров.

3. Запрашивает у пользователя ввод данных: длину трубы, толщину стенок и внутренний диаметр трубы, используя функцию `check_positive_float` для обеспечения корректного ввода.

4. Вычисляет массу свинцовой трубы, используя функцию `calculate_lead_pipe_mass` с введенными данными.

5. Выводит результат на экран, указывая массу свинцовой трубы в килограммах с точностью до двух десятичных знаков.
```diff
+  DESCRIPTION LAB 3
```
Этот код выполняет следующие действия:

1. Задаёт константы: универсальную газовую постоянную `R`, давление `P_Pa` в Паскалях и температуру `T_Celsius` в градусах Цельсия.

2. Пересчитывает температуру в Кельвины, добавляя 273.15 к значению в градусах Цельсия.

3. Пересчитывает давление из Ньютона на квадратный метр (Н/м²) в Паскали, хотя это действие в коде излишне, так как значение переменной `P_Pa` не изменяется.

4. Вычисляет количество вещества (`n`), используя уравнение состояния газа (PV = nRT), где `P` - давление, `V` - объем, `n` - количество вещества, `R` - универсальная газовая постоянная, и `T` - температура в Кельвинах.

5. Задаёт молярную массу воздуха `molar_mass_air` в г/моль.

6. Вычисляет плотность воздуха `rho_air_g_per_l` в г/л, умножая количество вещества на молярную массу и деленную на объем (плотность = масса / объем).

7. Выводит результат на экран, указывая плотность воздуха при заданной температуре и давлении с точностью до двух десятичных знаков.
# LABA 3
```diff
+  DESCRIPTION LAB 1
```
Этот код выполняет следующие действия:

1. Определяет две функции:
   - `input_positive_float(prompt)`, которая запрашивает у пользователя ввод числа типа float, проверяя, что введенное значение положительное. Если ввод не соответствует требованиям, программа выводит сообщение об ошибке и продолжает запрашивать ввод.
   - `input_coordinate(prompt)`, которая запрашивает у пользователя ввод координаты в виде числа и проверяет, что введенное значение является числом. Если ввод не соответствует требованиям, программа выводит сообщение об ошибке и продолжает запрашивать ввод.

2. Запрашивает у пользователя ввод координат `a1` и `a2` с использованием функции `input_coordinate`.

3. Запрашивает у пользователя ввод радиуса окружности с использованием функции `input_positive_float`.

4. Вычисляет расстояние от точки `(a1, a2)` до начала координат по формуле Евклидова расстояния: `distance = sqrt(a1**2 + a2**2)`.

5. Проверяет, попадает ли точка внутрь окружности с заданным радиусом. Если расстояние меньше или равно радиусу, выводит сообщение о том, что точка находится внутри окружности, иначе сообщение о том, что точка не попадает в окружность.
```diff
+  DESCRIPTION LAB 2
```
Этот код выполняет следующие действия:

1. Определяет функцию `number_to_words(c)`, которая принимает число `c` в диапазоне от 0 до 7 и возвращает его словесное представление с использованием словаря `words`.

2. Вводит число с клавиатуры в цикле `while True`, обеспечивая, что введенное значение является целым числом.

3. Проверяет, что введенное число находится в допустимом диапазоне от 0 до 7.

4. Если ввод корректен, вызывает функцию `number_to_words(c)` для преобразования числа в словесную форму и выводит результат на экран.

5. Если ввод не соответствует требованиям (например, не является целым числом или выходит за пределы диапазона), выводит соответствующее сообщение об ошибке и продолжает запрашивать ввод.
```diff
+  DESCRIPTION LAB 3
```
Этот код определяет функцию `main()`, которая включает в себя бесконечный цикл (`while True`), предназначенный для ввода значения `x` с клавиатуры и вычисления соответствующего значения `y` на основе заданных условий.

Вот краткое описание логики кода:

1. В цикле `while True` программа запрашивает у пользователя ввод значения `x` с использованием функции `float(input(...))`.

2. Используя условные операторы `if-elif-else`, программа проверяет, в каком интервале находится введенное значение `x` и вычисляет соответствующее значение `y` в каждом случае.

3. Если введенное значение `x` находится вне допустимого диапазона, программа выводит сообщение об ошибке.

4. Если введенное значение `x` не является числом (возникает исключение `ValueError`), программа выводит сообщение об ошибке и продолжает цикл для ввода нового значения.

5. Если все условия выполнились успешно, программа выводит значение `y` с точностью до трех знаков после запятой.

6. Если пользователь введет некорректное значение `x`, программа сообщит об ошибке и продолжит цикл для нового ввода.

Кроме того, код включает проверку `if __name__ == "__main__":`, что позволяет использовать этот код как модуль или самостоятельную программу. Если скрипт запускается напрямую (а не импортируется как модуль), вызывается функция `main()`.
# LABA 4
```diff
!  DESCRIPTION LAB 1
```
Этот код выполняет следующие действия:

1. Определяет функцию `distance(x1, y1, x2, y2)`, которая вычисляет расстояние между двумя точками в двумерном пространстве, используя формулу расстояния между двумя точками на плоскости.

2. Вводит радиус окружности с использованием цикла `while True` и обработки исключения `ValueError` для проверки корректности ввода.

3. Вводит количество точек `n` с использованием цикла `while True` и обработки исключения `ValueError` для проверки корректности ввода.

4. Инициализирует счетчик `count` для отслеживания количества пересекающихся окружностей.

5. Запускает цикл `for` для ввода координат точек и проверки, пересекаются ли они с данной окружностью.

   - В цикле запрашиваются числовые значения координат точек (`x` и `y`) с использованием обработки исключения для проверки корректности ввода.

   - Для каждой точки вычисляется расстояние от центра окружности до этой точки с использованием функции `distance`.

   - Если расстояние меньше, чем `2 * r` (диаметр окружности), то окружности пересекаются, и счетчик увеличивается.

6. Выводит результат, указывая количество окружностей, которые пересекают данную окружность.
```diff
!  DESCRIPTION LAB 2
```
Этот код выполняет следующие действия:

1. Определяет функцию `control_function(x)`, которая возвращает значение функции `-log(2 * sin(x / 2))`.

2. Определяет функцию `calculate_series(x, eps)`, которая вычисляет сумму ряда, используя заданный параметр точности `eps`. Ряд представлен выражением `cos(nx)/n`, где `n` - номер члена ряда.

3. Инициализирует переменные `x` (значение аргумента функций), `eps` (точность вычислений), и вызывает функции `control_function` и `calculate_series` для заданных значений `x` и `eps`.

4. Выводит на экран значения контрольной функции `y` и суммы ряда `S` с указанием точности.

Примечание:
- Важно отметить, что в цикле вычисления суммы ряда переменная `term` инициализируется значением `math.cos(x)`, но внутри цикла обновляется новым значением `math.cos(n * x) / n`. Это позволяет последовательно добавлять члены ряда к сумме до тех пор, пока значение очередного члена не станет меньше заданной точности `eps`.
```diff
!  DESCRIPTION LAB 3
```
Этот код выполняет следующие действия:

1. Задает значение постоянной Больцмана `k_boltzmann` (1.38e-23 Дж/К).

2. Задает количество молекул водорода `n_moles` (1.0 моль).

3. Задает список температур в градусах Цельсия от 10 до 20 включительно.

4. Определяет функцию `celsius_to_kelvin(celsius)`, которая принимает температуру в градусах Цельсия и возвращает температуру в Кельвинах.

5. В цикле для каждой температуры в градусах Цельсия рассчитывает температуру в Кельвинах с использованием функции `celsius_to_kelvin`.

6. Рассчитывает среднюю кинетическую энергию вращения молекулы водорода по формуле `(3/2) * k * T * n`, где `k` - постоянная Больцмана, `T` - температура в Кельвинах, `n` - количество молекул.

7. Выводит результаты расчетов на экран, указывая температуру в градусах Цельсия и соответствующую среднюю кинетическую энергию вращения молекулы водорода в Джоулях с использованием форматирования строк.

Таким образом, код демонстрирует, как рассчитать среднюю кинетическую энергию вращения молекулы водорода при различных температурах.
# LABA 5
```diff
!  DESCRIPTION LAB 1
```
Этот код определяет процедуру `print_age`, которая принимает два аргумента (`name` и `years`) и выводит сообщение о возрасте на основе этих данных. Затем эта процедура вызывается три раза, каждый раз с новыми входными данными.

Вот пошаговое описание кода:

1. Определяется процедура `print_age` с двумя параметрами (`name` и `years`).

2. В теле процедуры используется функция `print` для вывода сообщения о возрасте с использованием переданных параметров.

3. Затем три раза запрашиваются данные с клавиатуры (имя и возраст), и вызывается процедура `print_age` с введенными значениями.

Пример работы кода:

```python
Name: Alice
 age: 25
Alice is 25 years old.
Name: Bob
 age: 30
Bob is 30 years old.
Name: Carol
 age: 22
Carol is 22 years old.
```

Каждый раз, когда процедура `print_age` вызывается, она использует введенные данные для вывода сообщения о возрасте.
```diff
!  DESCRIPTION LAB 2
```
Этот код выполняет следующие действия:

1. Определяет функцию `find_arithmetic_progression_elements(a1, d, n)`, которая вычисляет элементы арифметической прогрессии с заданным первым элементом `a1`, разностью `d` и количеством элементов `n`.

2. Вводит с клавиатуры значения `a1` и `d` с использованием циклов `while True` и обработки исключений `ValueError` для проверки корректности ввода.

3. Устанавливает значение `n` в 7, так как в коде ищутся второй, третий, четвертый и седьмой элементы арифметической прогрессии.

4. Вызывает функцию `find_arithmetic_progression_elements` с введенными значениями `a1`, `d` и `n` и сохраняет результат в переменной `elements`.

5. Выводит на экран найденные элементы арифметической прогрессии: второй, третий, четвертый и седьмой.

6. Рассчитывает сумму найденных элементов и выводит ее на экран.

Таким образом, код ищет и выводит несколько элементов арифметической прогрессии, а также их сумму.
```diff
-  DESCRIPTION LAB 3
```
Этот код использует библиотеку `sympy` для символьного интегрирования и вычисления значения определенного интеграла.

Вот краткое описание кода:

1. Определяет функцию `integral_recursive(x, n, a, b)`, которая рекурсивно вычисляет значение интеграла. В базовых случаях (когда n = 0 и n = 1), функция возвращает элементарные функции. В общем случае, она использует рекуррентную формулу для интегрирования.

2. Вводит от пользователя целое число `n` (степень в интеграле), проверяя корректность ввода.

3. Задает границы интегрирования `a` и `b`.

4. Использует библиотеку `sympy` для символьного вычисления интеграла с помощью функции `integrate`.

5. Выводит результат вычисления значения интеграла с использованием `evalf()` для получения числового значения.

Код, таким образом, позволяет пользователю ввести значение степени `n` и вычислить значение интеграла в символьной и числовой формах.
# LABA 6
```diff
!  DESCRIPTION LAB 1
```
Этот код создает массив случайных целых чисел и затем вычисляет сумму элементов массива, которые делятся на 3 без остатка.

Вот шаги, которые выполняет код:

1. Запрашивает пользователя ввести количество элементов массива `n`.

2. Создает массив `L` длиной `n` и заполняет его случайными целыми числами в диапазоне от -10 до 10 (включительно).

3. Выводит массив `L`.

4. Инициализирует переменную `S` для хранения суммы.

5. Использует цикл `for` для просмотра каждого элемента массива `L`.

6. Если элемент делится на 3 без остатка (`L[i] % 3 == 0`), то его значение прибавляется к переменной `S`.

7. Выводит на экран сумму `S`.

Пример работы кода:

```
Введите количество элементов массива: 10
[4, -6, 0, 2, -7, 7, -4, 10, -5, -5]
S =  -12
```

В этом примере создается массив из 10 случайных чисел, затем выводится сам массив, и наконец, выводится сумма элементов, которые делятся на 3.
```diff
!  DESCRIPTION LAB 2
```
Этот код выполняет следующие действия:

1. Вводит размер массива `n` с использованием цикла `while True` и обработки исключения `ValueError` для проверки корректности ввода.

2. Вводит элементы массива с использованием вложенного цикла `for` и `while True` для обработки исключения `ValueError` при вводе каждого элемента.

3. Вычисляет среднее арифметическое значение элементов массива.

4. Преобразовывает исходный массив, вычитая из каждого элемента среднее арифметическое.

5. Выводит на экран среднее значение и преобразованный массив.

Пример работы кода:

```
Введите размер массива: 5
Введите элемент 1: 2
Введите элемент 2: 4
Введите элемент 3: 6
Введите элемент 4: 8
Введите элемент 5: 10
Среднее значение: 6.0
Преобразованный массив: [-4.0, -2.0, 0.0, 2.0, 4.0]
```

В этом примере пользователь вводит массив размера 5, а затем вводит элементы. Программа вычисляет среднее значение (в данном случае, 6.0) и преобразует исходный массив, вычитая из каждого элемента это среднее значение.
```diff
!  DESCRIPTION LAB 3
```
Этот код решает задачу о расстановке символов '#' и '.' в матрице. Программа рекурсивно перебирает различные варианты расстановки и подсчитывает количество возможных матриц, удовлетворяющих определенным правилам.

Вот пошаговое описание кода:

1. Определяется функция `is_valid_matrix(matrix)`, которая проверяет, что матрица состоит только из символов '#' и '.'.

2. Определяется функция `count_matrices(matrix)`, которая рекурсивно подсчитывает количество возможных матриц. Для каждой пустой ячейки '.' программа пытается установить '#' и вызывает себя для новой матрицы, проверяя ее валидность.

3. В основной функции `main()` запрашивается у пользователя количество строк `m` и столбцов `n`. Затем программа запрашивает ввод каждой строки матрицы, проверяя ее валидность.

4. Вызывается функция `count_matrices(matrix)` для подсчета количества возможных матриц.

5. Выводится результат.

Пример работы кода:

```
Введите количество строк (m): 3
Введите количество столбцов (n): 3
Введите строку 1 (длиной 3 символов, используйте '#' и '.'): .#.
Введите строку 2 (длиной 3 символов, используйте '#' и '.'): ...
Введите строку 3 (длиной 3 символов, используйте '#' и '.'): ..#
Количество возможных матриц: 6
```

В этом примере программа создает матрицу 3x3 и подсчитывает количество возможных матриц, удовлетворяющих условиям задачи.
# LABA 7
```diff
!  DESCRIPTION LAB 1
```
Этот код решает задачу о поиске кратчайшего пути во взвешенном графе с использованием алгоритма Дейкстры. Давайте разберем, как это работает:

1. `graph`: Это словарь, представляющий граф. Ключи - узлы графа, а значения - словари, где ключи - соседние узлы, а значения - веса ребер.

2. `path_len`: Это словарь, в котором ключи - узлы, а значения - длины кратчайших путей от начального узла до данного узла. Изначально все значения установлены на бесконечность (`inf`), кроме начального узла, у которого длина пути равна 0.

3. `visited`: Это множество, в котором хранятся узлы, которые уже были посещены.

4. `node` и `value`: Это переменные, которые отслеживают текущий узел и длину текущего пути.

5. `final_node`: Это целевой узел, до которого нужно найти кратчайший путь.

6. Внутренний цикл `while`: Продолжает выполняться, пока текущий узел не равен целевому узлу и пока не все узлы посещены. Внутри цикла:

   - Проходится по всем соседям текущего узла, которые еще не были посещены.
   - Обновляет длины кратчайших путей до соседей, если новая длина меньше текущей.
   - Добавляет текущий узел в множество посещенных.
   - Обновляет `path_len` для текущего узла на бесконечность, так как он уже посещен.

7. После завершения цикла выводит длину кратчайшего пути до целевого узла.

Этот код использует жадный алгоритм, каждый раз выбирая узел с наименьшей длиной пути. В результате выполнения кода, длина кратчайшего пути от узла 1 до узла 7 будет выведена на экран.
```diff
!  DESCRIPTION LAB 2
```
Этот код выполняет следующие действия:

1. Создает три множества: `set1`, `set2`, и `set3`.

2. Пользовательский ввод строк для каждого из множества с использованием `input`.

3. Выводит на экран введенные множества.

4. Находит множество строк, которые состоят не только из строчных английских букв, заканчиваются на "xyz" и имеют длину 4. Результат сохраняется в `result_b` и выводится на экран.

5. Находит самую короткую строку, состоящую только из строчных английских букв, не заканчивающуюся на "xyz" и не имеющую длины 4. Результат сохраняется в `result_c` и выводится на экран.

Пример работы кода:

```
Введите строку для первого множества: abcd
Введите строку для второго множества: xyzw
Введите строку для третьего множества: abcdefgh

Множество 1: {'abcd'}
Множество 2: {'xyzw'}
Множество 3: {'abcdefgh'}

Множество строк, соответствующих условиям б): {'abcd'}
Самая короткая строка, соответствующая условиям в): 'xyzw'
```

В этом примере пользователь ввел строки для каждого множества, и программа вывела результаты в соответствии с условиями задачи.
```diff
!  DESCRIPTION LAB 3
```
Этот код представляет собой простую программу управления данными о товарах в магазинах. Программа предоставляет следующие функции:

1. `add_data(price)`: добавляет новые данные о товаре в словарь `price`.

2. `view_all_data(price)`: выводит все данные из словаря `price`.

3. `view_data_by_key(price, search_key)`: выводит данные по заданному ключу (наименование магазина, наименование товара).

4. `delete_data_by_key(price, search_key)`: удаляет данные по заданному ключу из словаря.

5. `search_data_by_name_and_cost(price)`: осуществляет поиск информации о магазинах и товарах по заданным критериям (название товара и максимальная стоимость).

6. `main()`: основная функция, предоставляющая пользователю меню с возможностью выбора различных действий.

Программа выполняется в бесконечном цикле, пока пользователь не выберет опцию выхода (6). Ввод данных защищен от ошибок, таких как ввод текста вместо чисел, и обеспечивает корректное выполнение основных операций.

Пример использования:
```
МЕНЮ:
1. Ввод данных
2. Просмотр всех данных
3. Вывод данных по ключу
4. Удаление данных по ключу
5. Поиск 1
6. Выход
Выберите действие (введите номер): 1
Введите наименование магазина: Store1
Введите наименование товара: Product1
Введите количество товара на складе: 10
Введите стоимость товара: 50
Данные успешно добавлены!

МЕНЮ:
1. Ввод данных
2. Просмотр всех данных
3. Вывод данных по ключу
4. Удаление данных по ключу
5. Поиск 1
6. Выход
Выберите действие (введите номер): 2
Ключ: ('Store1', 'Product1'), Значение: {'store_name': 'Store1', 'product_name': 'Product1', 'quantity': 10, 'cost': 50.0}

МЕНЮ:
1. Ввод данных
2. Просмотр всех данных
3. Вывод данных по ключу
4. Удаление данных по ключу
5. Поиск 1
6. Выход
Выберите действие (введите номер): 6
Выход из программы.
```
# LABA 8
```diff
!  DESCRIPTION LAB 1
```
Этот код выполняет следующие действия:

1. Считывает строки из файла `input.txt`.
2. Ищет арифметические выражения в каждой строке.
3. Если арифметическое выражение найдено, вычисляет результат и выводит его на экран.
4. Записывает арифметическое выражение и его результат в файл `output8_1.txt`.

Пример содержимого файла `input.txt`:
```
Выражение 1: 5 + 3
Текст без выражения
Еще одно выражение: 10 / 2
```

Пример вывода на экран:
```
5 + 3 = 8
10 / 2 = 5.0
```

Пример содержимого файла `output8_1.txt`:
```
5 + 3 = 8
10 / 2 = 5.0
```

Обратите внимание, что использование `eval()` для вычисления математических выражений может быть опасным, особенно если входные данные не являются надежными. В данном случае, программа выполняет выражения, найденные в файле, что может привести к выполнению произвольного кода, если файл создается или модифицируется злоумышленником. Будьте осторожны при обработке пользовательских данных.
```diff
!  DESCRIPTION LAB 2
```
Этот код выполняет следующие действия:

1. Считывает строки из двух файлов: `input0.txt` и `input1.txt`.
2. Преобразует строки в списки чисел.
3. Вычисляет наибольший общий делитель (НОД) для каждой пары чисел из обоих файлов.
4. Записывает результаты вычислений в файл `output8_2.txt`.

Пример содержимого файла `input0.txt`:
```
12 24 36
8 16 24
```

Пример содержимого файла `input1.txt`:
```
18 30 45
4 8 12
```

Пример содержимого файла `output8_2.txt` (результаты вычислений НОД для соответствующих пар чисел):
```
6 2 9
4 8 12
```

В данном случае, результаты вычислений НОД записываются в файл `output8_2.txt` в формате строк, каждая из которых содержит результаты для соответствующей пары чисел из двух входных файлов.
```diff
!  DESCRIPTION LAB 3
```
обновленный код включает функции для сохранения данных в файл и загрузки данных из файла, используя модуль `json`. Это позволяет сохранять состояние данных между запусками программы.

Основные изменения:

1. **Функция `save_to_file`:** Эта функция преобразует ключи в строки (используя `_` в качестве разделителя) и сохраняет данные в файл в формате JSON. Функция также выводит сообщение об успешном сохранении данных.

2. **Функция `load_from_file`:** Эта функция загружает данные из файла, декодирует их из формата JSON и восстанавливает исходные ключи (разделяя строки по `_`). Она также выводит сообщение об успешной загрузке данных.

3. **Добавлено сохранение при выходе:** При выборе пункта "Выход" (пункт 8), программа автоматически сохраняет данные в файл перед завершением.

4. **Добавлена проверка на наличие файла при загрузке:** Если файл не найден, программа выведет сообщение об этом. Также добавлена обработка ошибок `json.JSONDecodeError`, которая сообщит о проблемах с декодированием JSON в файле.

Теперь программа может сохранять и загружать данные, что делает ее более удобной и гибкой для использования.
# LABA 9
```diff
!  DESCRIPTION LAB 1
```
код включает функции для получения целочисленного ввода, поиска индексов элемента в списке и матрице, а также генерации случайной матрицы. Использование функций делает код более читаемым и модульным.

# Небольшие замечания:

1. **Функция `find_indices_in_list`:** Вы можете использовать функцию `enumerate` для более компактного кода:

    ```python
    def find_indices_in_list(element, input_list):
        return [i for i, el in enumerate(input_list) if el == element]
    ```

2. **Функция `find_indices_in_matrix`:** Аналогично, можно улучшить функцию с использованием вложенного генератора списков:

    ```python
    def find_indices_in_matrix(element, matrix):
        return [(i, j) for i, row in enumerate(matrix) for j, el in enumerate(row) if el == element]
    ```

3. **Оптимизация проверки наличия элементов:** После выполнения `flattened_matrix`, вы можете проверить, есть ли элемент в списке, просто используя `if element_to_find in flattened_matrix`. Таким образом, вам не нужно вызывать отдельную функцию `find_indices_in_list`.

4. **Оптимизация вывода результатов:** Вместо использования двух отдельных условий для вывода результатов, вы можете объединить их в одно, используя тернарный оператор:

    ```python
    print(f"Индексы элемента {element_to_find} в списке: {indices_in_list}" if indices_in_list else f"Элемент {element_to_find} не найден в списке.")
    ```

    И аналогично для матрицы.

Это всего лишь некоторые предложения для улучшения, и код уже вполне функционален.
# ЧТО ДЕЛАЕТ КОД 9 1

1. **Функция `get_integer_input(prompt):`**
   - Запрашивает пользователя ввод целого числа с сообщением `prompt`.
   - Использует цикл `while True`, чтобы продолжать запрос, пока не будет введено корректное целое число.
   - В случае возникновения `ValueError` при попытке преобразования введенного значения в целое число, выводит сообщение об ошибке и продолжает запрос.

2. **Функция `find_indices_in_list(element, input_list):`**
   - Ищет все индексы элемента в одномерном списке `input_list`.
   - Использует цикл `for` и функцию `enumerate` для перебора элементов вместе с их индексами.
   - Если текущий элемент равен искомому элементу, добавляет индекс в список `indices`.
   - Возвращает список найденных индексов.

3. **Функция `find_indices_in_matrix(element, matrix):`**
   - Ищет все индексы элемента в матрице `matrix`.
   - Использует вложенные циклы `for` и функцию `enumerate` для перебора строк и элементов в строках.
   - Если текущий элемент равен искомому элементу, добавляет кортеж индексов `(i, j)` в список `indices`, где `i` - индекс строки, `j` - индекс столбца.
   - Возвращает список найденных индексов.

4. **Функция `generate_random_matrix(rows, cols):`**
   - Генерирует случайную матрицу заданных размеров (`rows` строк и `cols` столбцов).
   - Использует вложенный генератор списка для создания матрицы, заполняя ее случайными целыми числами от 1 до 10.
   - Возвращает сгенерированную матрицу.

5. **Основная часть программы в блоке `if __name__ == "__main__":`**
   - Запрашивает у пользователя количество строк и столбцов для матрицы.
   - Генерирует случайную матрицу с использованием функции `generate_random_matrix` и выводит ее на экран.
   - Запрашивает у пользователя элемент для поиска.
   - Использует функции `find_indices_in_list` и `find_indices_in_matrix` для поиска индексов элемента в списке и матрице соответственно.
   - Выводит результаты поиска на экран. Если элемент найден, выводит индексы, иначе сообщает, что элемент не найден.

Пример взаимодействия с программой:
```
Введите количество строк в матрице: 3
Введите количество столбцов в матрице: 4
Сгенерированная матрица:
[2, 10, 6, 9]
[1, 7, 1, 3]
[2, 3, 10, 5]
Введите элемент для поиска: 1
Индексы элемента 1 в списке: [4]
Индексы элемента 1 в матрице: [(1, 0), (2, 2)]
```

В этом примере пользователь вводит размеры матрицы (3 строки, 4 столбца), программа генерирует случайную матрицу и предлагает пользователю ввести элемент для поиска (в данном случае, число 1). Программа затем выводит матрицу и индексы найденного элемента как в одномерном списке, так и в матрице.
```diff
!  DESCRIPTION LAB 2
```
Давайте разберем данный код более подробно:

1. **Функция `generate_random_matrix(rows, cols):`**
   - Генерирует случайную матрицу заданных размеров (`rows` строк и `cols` столбцов).
   - Использует вложенный генератор списка для создания матрицы, заполняя ее случайными целыми числами от 1 до 100.
   - Возвращает сгенерированную матрицу.

2. **Функция `flatten_matrix(matrix):`**
   - "Выпрямляет" матрицу, преобразуя ее в одномерный список.
   - Использует генератор списка для объединения элементов матрицы в один список.
   - Возвращает одномерный список.

3. **Функция `sort_matrix_with_functions(matrix):`**
   - Сортирует матрицу с использованием встроенной функции `sorted`.
   - Выпрямляет матрицу с помощью функции `flatten_matrix`.
   - Сортирует выпрямленный список.
   - Разбивает отсортированный список обратно на строки матрицы.
   - Возвращает отсортированную матрицу.

4. **Функция `sort_matrix_without_functions(matrix):`**
   - Сортирует матрицу без использования встроенных функций.
   - Выпрямляет матрицу с помощью функции `flatten_matrix`.
   - Использует алгоритм пузырьковой сортировки для сортировки выпрямленного списка.
   - Разбивает отсортированный список обратно на строки матрицы.
   - Возвращает отсортированную матрицу.

5. **Функция `print_matrix(matrix):`**
   - Выводит матрицу на экран, построчно.
   - Использует цикл `for` для итерации по строкам матрицы и вложенный цикл `for` для вывода элементов в каждой строке.

6. **Основная часть программы в блоке `if __name__ == "__main__":`**
   - Запрашивает у пользователя количество строк и столбцов для матрицы.
   - Генерирует случайную матрицу с использованием функции `generate_random_matrix` и выводит ее на экран.
   - Сортирует матрицу с использованием функций `sort_matrix_with_functions` и `sort_matrix_without_functions`, выводит отсортированные матрицы на экран.

Пример взаимодействия с программой:
```
Введите количество строк в матрице: 3
Введите количество столбцов в матрице: 4
Исходная матрица:
[94, 66, 39, 21]
[88, 31, 63, 77]
[97, 95, 99, 17]

Сортировка с использованием функций:
[17, 21, 31, 39]
[63, 66, 77, 88]
[94, 95, 97, 99]

Сортировка без использования функций:
[17, 21, 31, 39]
[63, 66, 77, 88]
[94, 95, 97, 99]
```
```diff
!  DESCRIPTION LAB 3
```

Данный код представляет собой реализацию игры "Угадай число" компьютером.

1. **Инициализация переменных:**
   - `low_limit`: Нижний предел диапазона чисел, которые можно загадать (включительно).
   - `high_limit`: Верхний предел диапазона чисел, которые можно загадать (включительно).
   - `attempts`: Количество попыток компьютера угадать число.

2. **Печать инструкций:**
   - Выводит инструкции пользователю, чтобы загадать число от `low_limit` до `high_limit`.

3. **Основной игровой цикл:**
   - Входит в цикл, который продолжается, пока число не будет угадано.
   - Компьютер предполагает число, выбирая середину текущего диапазона (`(low_limit + high_limit) // 2`).
   - Выводит предполагаемое число.
   - Пользователь вводит ответ: '+++' (если число угадано), '-' (если число меньше), или '+' (если число больше).
   - Увеличивает количество попыток.
   - В зависимости от ответа пользователя обновляет границы диапазона для следующей попытки:
     - Если ответ '+++', выводит сообщение о победе и завершает игру.
     - Если ответ '-', уменьшает `high_limit` до значения на 1 меньше предполагаемого числа.
     - Если ответ '+', увеличивает `low_limit` до значения на 1 больше предполагаемого числа.
     - Если введенный ответ не соответствует ожидаемым, выводит сообщение об ошибке.

4. **Основная часть программы:**
   - Запускает игру, вызывая функцию `guess_number()`.

**Пример взаимодействия:**
```
Загадайте число от -1024 до 1024.
Компьютер предполагает: 0
Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: -
Компьютер предполагает: -512
Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: +
Компьютер предполагает: -256
Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: +
Компьютер предполагает: -128
Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: +
Компьютер предполагает: -64
Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: -
Компьютер предполагает: -96
Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: +
Компьютер предполагает: -80
Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: +
Компьютер предполагает: -72
Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: +++
Компьютер угадал число -72 за 8 попыток.
```
