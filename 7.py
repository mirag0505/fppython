from pymonad.state import State
from pymonad.tools import curry
from functools import reduce

# Каррированная функция для проверки координат
@curry(3)
def is_valid(N, M, point):
    x, y = point
    return 1 <= x <= N and 1 <= y <= M

# Генерация соседних точек для одной точки
@curry(2)
def generate_neighbors(directions, point):
    return [(point[0] + dx, point[1] + dy) for dx, dy in directions]

# Фильтрация и объединение новых точек
@curry(3)
def process_neighbors(N, M, directions, captured):
    # Генерируем всех возможных соседей
    neighbors_list = map(generate_neighbors(directions), captured)
    
    # Объединяем все списки в один набор
    all_neighbors = reduce(lambda acc, lst: acc | set(lst), neighbors_list, set())
    
    # Фильтруем только валидные точки
    valid_neighbors = filter(is_valid(N, M), all_neighbors)
    return set(valid_neighbors)

# Основной шаг симуляции
@curry(3)
def simulation_step(N, M, state):
    captured, day = state
    total_areas = N * M
    
    # Проверка завершения
    if len(captured) == total_areas:
        return (day, (captured, day))
    
    # Направления для генерации соседей
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # Получаем новых соседей
    new_neighbors = process_neighbors(N, M, directions, list(captured))
    
    # Объединяем с текущими точками
    new_captured = captured | new_neighbors
    
    # Проверка на отсутствие прогресса
    if new_captured == captured:
        return (day, (captured, day))
    
    # Проверка полного захвата
    if len(new_captured) == total_areas:
        return (day + 1, (new_captured, day + 1))
    
    # Продолжаем процесс
    return (None, (new_captured, day + 1))

# Рекурсивная функция для выполнения шагов
def run_simulation(state, N, M):
    s = State(simulation_step(N, M))
    result, new_state = s.run(state)
    return result if result is not None else run_simulation(new_state, N, M)

# Основная функция
def ConquestCampaign(N, M, L, battalion):
    # Создаем начальное множество точек
    points = zip(battalion[::2], battalion[1::2])
    initial_captured = set(points)
    
    # Проверка полного захвата в первый день
    if len(initial_captured) == N * M:
        return 1
    
    # Начальное состояние
    initial_state = (initial_captured, 1)
    
    # Запуск симуляции
    return run_simulation(initial_state, N, M)

print(ConquestCampaign(3, 4, 2, [2, 2, 3, 4]))