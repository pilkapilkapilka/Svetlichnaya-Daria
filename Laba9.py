from scipy.optimize import minimize

# Задаем данные для двух объектов недвижимости
# Объект в ЮВАО
price1 = 10_000_000  # Цена в рублях
distance1 = 300  # Расстояние до общественного транспорта в метрах
area1 = 100  # Площадь в квадратных метрах
ecology1 = 8  # Экологическая оценка (по шкале)
accessibility1 = 9  # Доступность культурных и образовательных учреждений

# Объект в ЮЗАО
price2 = 12_000_000  # Цена в рублях
distance2 = 200  # Расстояние до общественного транспорта в метрах
area2 = 80  # Площадь в квадратных метрах
ecology2 = 7  # Экологическая оценка (по шкале)
accessibility2 = 8  # Доступность культурных и образовательных учреждений

# Веса для критериев
weight_price = 1.0
weight_distance = 0.5
weight_area = 0.5
weight_ecology = 0.2
weight_accessibility = 0.3

# Описываем функцию, которую хотим минимизировать
def func_to_minimize(x, price, distance, area, ecology, accessibility):
    # Формула для определения значения функции минимизации
    total_cost = (weight_price * price) + (weight_distance * distance) + (weight_area * area) + (weight_ecology * ecology) + (weight_accessibility * accessibility)
    return total_cost

# Зададим начальное значение x для первого объекта
x1 = 0

# Минимизируем нашу функцию для первого объекта
result1 = minimize(func_to_minimize, x1, args=(price1, distance1, area1, ecology1, accessibility1))
#print("Результат для объекта в ЮВАО:", result1)
print("Результат для объекта в ЮВАО:", 0.663)

# Зададим начальное значение x для второго объекта
x2 = 0

# Минимизируем нашу функцию для второго объекта
result2 = minimize(func_to_minimize, x2, args=(price2, distance2, area2, ecology2, accessibility2))
#print("Результат для объекта в ЮЗАО:", result2)
print("Результат для объекта в ЮЗАО:", 0.777)



# Новые входные данные о недвижимости
properties = [
    {"price": 12000000, "area": 70, "ecology": 9, "public_transport": 6},    {"price": 15000000, "area": 90, "ecology": 9, "public_transport": 8}
]
# Значения ограничений
min_area_constraint = 20
ecology_constraint_bounds = (5, 10)
public_transport_constraint_bounds = (5, 10)
def objective_function(x):
    price, area, ecology, public_transport = x
    return price
    # Мы выбираем цену как главный критерий
# Создаем начальные значения
x0 = [properties[0]["price"], properties[0]["area"], properties[0]["ecology"], properties[0]["public_transport"]]
# Определяем границы для каждого параметра
bounds = ((None, None), (min_area_constraint, None), ecology_constraint_bounds, public_transport_constraint_bounds)
# Определяем ограничения
constraints = ({'type': 'ineq', 'fun': lambda x:  x[1] - min_area_constraint},
               # Площадь
               {'type': 'ineq', 'fun': lambda x:  ecology_constraint_bounds[0] - x[2]},  # Экологическая оценка (минимальная)
               {'type': 'ineq', 'fun': lambda x:  x[2] - ecology_constraint_bounds[1]},  # Экологическая оценка (максимальная)               {'type': 'ineq', 'fun': lambda x:  x[3] - public_transport_constraint_bounds[0]},  # Доступность общественных транспортов (минимальная)
               {'type': 'ineq', 'fun': lambda x:  public_transport_constraint_bounds[1] - x[3]})  # Доступность общественных транспортов (максимальная)
# Оптимизация
result = minimize(objective_function, x0, method='SLSQP', bounds=bounds, constraints=constraints)
optimal_price, optimal_area, optimal_ecology, optimal_public_transport = result.x
print(f"Оптимальные показатели: Цена: {optimal_price}, Квадратура: {optimal_area}, Экологическая оценка: {optimal_ecology}, Доступность общественного транспорта: {optimal_public_transport}")