import sys

def input_coef(index, text):
    try:
        coef_str = sys.argv[index]
    except:
        print(text)
        coef_str = input()
    coef = float(coef_str)
    return coef


def get_coef():
    coef_a = input_coef(1, "Введите A:")
    coef_b = input_coef(2, "Введите B:")
    coef_c = input_coef(3, "Введите C:")
    return coef_a, coef_b, coef_c


def solution(a, b, c):
    roots = []
    d = b * b - 4 * a * c
    if d < 0.0:
        return 0, roots
    elif d == 0.0:
        t = (-b + (d**0.5)) / (2 * a)
        if t < 0.0:
            return 0, roots
        elif t == 0.0:
            roots.append(t)
            return 1, roots
        else:
            roots.append(t**0.5)
            roots.append(-(t**0.5))
            return 2, roots
    else:
        t1 = (-b + (d**0.5)) / (2 * a)
        t2 = (-b - (d**0.5)) / (2 * a)
        if t1 < 0.0:
            if t2 < 0.0:
                return 0, roots
            elif t2 == 0.0:
                roots.append(0)
                return 1, roots
            else:
                roots.append(t2**0.5)
                roots.append(-(t2**0.5))
                return 2, roots
        elif t1 == 0.0:
            if t2 < 0.0:
                roots.append(0)
                return 1, roots
            elif t2 == 0.0:
                roots.append(0)
                return 1, roots
            else:
                roots.append(0)
                roots.append(t2**0.5)
                roots.append(-(t2**0.5))
                return 3, roots
        else:
            if t2 < 0.0:
                roots.append(t1**0.5)
                roots.append(-(t1**0.5))
                return 2, roots
            elif t2 == 0.0:
                roots.append(t1**0.5)
                roots.append(-(t1**0.5))
                roots.append(0)
                return 3, roots
            else:
                roots.append(t1**0.5)
                roots.append(-(t1**0.5))
                roots.append(t2**0.5)
                roots.append(-(t2**0.5))
                return 4, roots


def print_roots(kol_roots, roots):
    if kol_roots != len(roots):
        print(f'Ошибка. Уравнение содержит {kol_roots} действительных корней, ' +
              f'но было вычислено {len(roots)} корней.')
    else:
        if kol_roots == 0:
            print('Нет корней')
        elif kol_roots == 1:
            print(f'Один корень: {roots[0]}')
        elif kol_roots == 2:
            print(f'Два корня: {roots[0]} и {roots[1]}')
        elif kol_roots == 3:
            print(f'Три корня: {roots[0]}, {roots[1]} и {roots[2]}')
        elif kol_roots == 4:
            print(f'Четыре корня: {roots[0]}, {roots[1]}, {roots[2]} и {roots[3]}')


def main():
    coef_a, coef_b, coef_c = get_coef()
    kol_roots, roots = solution(coef_a, coef_b, coef_c)
    print_roots(kol_roots, roots)


if __name__ == "__main__":
    main()
