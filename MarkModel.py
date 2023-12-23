import numpy as np
import pandas as pd


# Все квартиры находятся в Южнопортовом районе Москвы
states = ['Однокомнатная квартира', 'Двухкомнатная квартира', 'Трехкомнатная квартира']

actions = ['Покупка', 'Инвестирование в улучшения', 'Удержание недвижимости']

# Матрица переходных вероятностей
P = np.array([
    [0.1, 0.8, 0.1],  # Вероятности перехода для действия X1
    [0.3, 0.5, 0.1],  # Вероятности перехода для действия X2
    [0.2, 0.3, 0.5]   # Вероятности перехода для действия X3
])

# Матрица вознаграждений
R = np.array([
    [30, 155, 10],  # Вознаграждения за действие X1
    [25, 15, 15],  # Вознаграждения за действие X2
    [10, 50, 35]   # Вознаграждения за действие X3
])

def markov_decision_process_fixed(states, actions, P, R):
    num_states = len(states)
    num_actions = len(actions)

    V = np.zeros(num_states)
    gamma = 0.9  # Коэффициент дисконтирования
    threshold = 0.0001

    # Первый этап - Оценивание параметров
    while True:
        V_prev = np.copy(V)
        for s in range(num_states):
            V[s] = max([sum([P[a, s_next] * (R[s, a] + gamma * V_prev[s_next]) for s_next in range(num_states)]) for a in range(num_actions)])

        # Проверка на сходимость
        if np.max(np.abs(V - V_prev)) < threshold:
            break

    # Второй этап - Извлечение оптимальной политики (улучшение стратегии)
    policy = np.zeros(num_states)
    for s in range(num_states):
        policy[s] = np.argmax([sum([P[a, s_next] * (R[s, a] + gamma * V[s_next]) for s_next in range(num_states)]) for a in range(num_actions)])

    return V, policy

# Вычисление оптимальной стратегии
V_optimal, policy_optimal = markov_decision_process_fixed(states, actions, P, R)
optimal_strategy = [actions[int(a)] for a in policy_optimal]

print("Рассмотрены квартиры в Южнопортовом районе: однокомнтная, двухкомнатная и трехкомнатная")
print("Оптимальные значения функции стоимости (V):", V_optimal)
print("Оптимальная стратегия для каждого состояния:", optimal_strategy)