from numpy import multiply, add, array
from random import randint


## e nie moze byc wektorem, ponieważ będzie nim również d
## a to by oznaczało że w kroku obliczania grama-schmitta
## w kroku 1) wychodził by nam wektor q[1x1] dla R2
## a musi być standardowo [1x2]
start_point_x = array([0, 0])
a = 3
b = -0.5
S = [None, array([0, 1]), array([1, 0])]
e = array([1, 4])

gramm_schmidt_counter = 0
steps_counter = 0
step_success_counter = [[None], [None], [None]]


def f(args):
    [x, y] = array(args)
    x = float(x)
    y = float(y)
    print(x,y)
    return x**5 + y*x**2


def calculate_new_coords(j):
    global start_point_x, e, S

    coords = add(start_point_x, multiply(e, S[j]))
    return coords


def change_start_point():
    global start_point_x, steps_counter
    steps_counter = 0
    value = randint(0, 256)
    diff = (value * 0.5) + 0.1
    print(diff)
    if value % 2 is 0:
        start_point_x = array([start_point_x[0] + value / diff, start_point_x[1]])
    else:
        start_point_x = array([start_point_x[0], start_point_x[1] + value / diff])


def step_forward(j):
    global e, start_point_x, steps_counter

    new_coords = calculate_new_coords(j)
    is_success = f(new_coords) < f(start_point_x)

    if is_success:
        start_point_x = new_coords
        e = multiply(e, a)
    else:
        e = multiply(e, b)

    step_success_counter[j] = is_success


def both_failure():
    global step_success_counter, steps_counter

    is_failed = step_success_counter[1] == False and step_success_counter[2] == False
    return is_failed


def gramm_schmidt():
    global gramm_schmidt_counter, S, steps_counter

    steps_counter = 0
    gramm_schmidt_counter += 1
    S = [None, [1, 0], [0, 1]]


def main():
    global steps_counter, start_point_x, gramm_schmidt_counter

    while True:
        for j in range(1, len(S)):
            step_forward(j)

        if both_failure():
            if steps_counter is 0:
                print('Zmiana poczatkowego punktu')
                change_start_point()
                continue

            if gramm_schmidt_counter is 5:
                print('Sukces w punkcie: ', start_point_x)
                break
            else:
                print('Obrot wspolrzednych')
                gramm_schmidt()
                continue

        if gramm_schmidt_counter is not 0:
            print('Punkt startowy zostal zmieniony. Brak minimum')
            break

        steps_counter += 1


if __name__ == '__main__':
    main()
