from numpy import multiply, add, array

x0 = array([0, 0])
a = 1.2
b = 0.7
S = [None, array([0, 1]), array([1, 0])]
e = array([1, 4])

start_points = [x0]
function_values = []
steps_counter = 0

step_success_counter = [
    None, [1], [2]
]


def f(args):
    [x, y] = array(args)
    return 2 * x * x + 5 * y * y


def calculate_new_coords(j):
    coords = add(start_points[j - 1], multiply(e, S[j]))
    return coords


def step_forward(j):
    global e

    new_coords = calculate_new_coords(j)

    result = f(new_coords)
    function_values.append(result)

    if j is not 0:
        if function_values[-1] < function_values[-2]:
            print('Krok pomyslny. Zwiekszanie wartosci kroku')
            step_success_counter[j].append(True)
            start_points.append(new_coords)
            e = multiply(e, a)
            # step_forward(j)
        else:
            print('Krok niepomyslny. Zmniejszanie wartosci kroku')
            step_success_counter[j].append(False)
            start_points.append(start_points[-1])
            e = multiply(e, b)


def main():
    global steps_counter
    function_values.append(f(x0))
    print(step_success_counter[1][-1:] != step_success_counter[2][-1])
    while True:
        if steps_counter == 5:
            break

        for j in range(1, len(S)):
            print('------- ITERACJA {} -------'.format(j))
            print("Start Points:", start_points)
            print("Step Value:", e)
            print("Function Values:", function_values, '\n')
            step_forward(j)
        if step_success_counter[1][-1] is False and step_success_counter[2][-1] is [False]:
            break
        steps_counter += 1


if __name__ == '__main__':
    main()
