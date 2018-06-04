from numpy import multiply, add, array, sqrt, dot, linalg
from random import randint

from rosenbrock.gramm_schmidt import gs


class Rosenbrock():
    def __init__(self, x0, f):
        self.alpha = 3
        self.beta = - 0.5
        self.x0 = array(x0)
        self.matrix_s = [array([1, 0]), array([0, 1])]
        self.e_step = array([1, 1])
        self.f = f

        self.gramm_schmidt_counter = 0
        self.steps_counter = 0
        self.success_counter = [0, 0]
        self.failure_counter = [0, 0]
        self.progress_d = [1, 1]
        self.prev_progress = self.x0

    def gram_schmitt_orto(self):
        d = self.progress_d
        S = self.matrix_s
        # cast_vectors = list()

        self.gramm_schmidt_counter += 1

        q1 = add(multiply(d[0], S[0]), multiply(d[1], S[1]))
        q2 = multiply(d[1], S[1])

        v1 = q1
        S1 = v1 / linalg.norm(v1)

        v2 = q2 - dot(dot(q2, v1) / dot(v1, v1), S1)
        S2 = v2 / linalg.norm(v2)

        print(v1, v2, S1, S2)

        self.matrix_s = [array(S1), array(S2)]

        # for i in range(min(len(d), len(S) + 1)):
        #     print()
        #     qn = array([0, 0])
        #     for j in range(i, len(S) + 1, 1):
        #         qn += (d[j]+S[j])
        #
        #     cast_vectors.append(qn)
        #
        # new_base = list()
        # new_base.append(cast_vectors[0])
        #
        # for i in range(1, len(cast_vectors)):
        #     vn = cast_vectors[i] - S[i]*((cast_vectors[i]*S[i].T)/sqrt(dot(S[i], S[i].T)))
        #     new_base.append(vn/sqrt(dot(vn, vn.T)))
        #
        # self.matrix_s = new_base

        print(self.matrix_s)

    def calculate_new_coords(self, index):
        return add(self.x0, multiply(self.e_step[index], self.matrix_s[index]))

    def change_start_point(self):
        self.steps_counter = 0

        value = randint(-2, 2)
        diff = (value * 0.5) + 0.1

        if value % 2 is 0:
            self.x0 = array([self.x0[0] + value / diff, self.x0[1]])
        else:
            self.x0 = array([self.x0[0], self.x0[1] + value / diff])

    def step_forward(self, j):
        index = j - 1
        new_x0 = self.calculate_new_coords(index)

        if self.f(new_x0) < self.f(self.x0):
            self.x0 = new_x0
            self.e_step[index] = self.alpha * self.e_step[index]
            self.success_counter[index] = 1
        else:
            self.e_step[index] = self.beta * self.e_step[index]
            self.failure_counter[index] = 1

    def both_failure(self):
        is_failed = sum(self.failure_counter) == 2
        return is_failed

    def execute(self):
        while True:
            directions = range(1, len(self.matrix_s) + 1)
            for j in directions:
                self.step_forward(j)

            if self.both_failure():
                self.failure_counter = [0, 0]
                self.success_counter = [0, 0]

                self.progress_d = self.x0 - self.prev_progress
                self.prev_progress = self.x0

                if self.steps_counter == 0:
                    print('Zmiana poczatkowego punktu', self.x0)
                    self.change_start_point()
                    continue

                if self.gramm_schmidt_counter is not 5:
                    print('Obrot wspolrzednych')
                    self.gram_schmitt_orto()
                    continue
                else:
                    print('Sukces w punkcie: ', self.x0)
                    break

            if self.gramm_schmidt_counter is not 0:
                print('Punkt startowy zostal zmieniony. Brak minimum')
                break

            self.steps_counter += 1


def f(args):
    [x, y] = array(args)

    return (1-x)**2 + 100*((y-x**2)**2)


def main():
    Rosenbrock([7, 9], f).execute()


if __name__ == '__main__':
    main()
