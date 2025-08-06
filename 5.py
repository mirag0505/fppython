from pymonad.maybe import Just, Nothing

def to_left(num):
    def _step(pole):
        l, r = pole
        new = (l + num, r)
        return Nothing if abs(new[0] - new[1]) > 4 else Just(new)
    return _step

def to_right(num):
    def _step(pole):
        l, r = pole
        new = (l, r + num)
        return Nothing if abs(new[0] - new[1]) > 4 else Just(new)
    return _step

def banana(pole):
    return Nothing

def begin():
    return Just((0, 0))

def show(m: Just or Nothing):
    if m == Nothing:
        print("Канатоходец упал!")
    else:
        l, r = m.value
        print(f"Успешно: птиц слева={l}, справа={r}")


# 1) слишком много птиц слева на последнем шаге → падает
show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-2))
)

# 2) баланс не нарушается — проходит успешно
show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-1))
)

# 3) банановая кожура → падает сразу
show(
    begin()
    .bind(to_left(2))
    .bind(banana)
    .bind(to_right(5))
    .bind(to_left(-1))
)
