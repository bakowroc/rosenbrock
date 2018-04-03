from MFunction import MFunction
import numpy


class RosenbrockAlgorithm:
    def __init__(self, start_point, base_vector_matrix, start_step, step_inc_corr, step_dec_corr):
        self.start_points = [numpy.array(start_point)]
        self.base_vector_matrix = numpy.array(base_vector_matrix)
        self.step_value = numpy.array(start_step, dtype=numpy.float64)
        self.step_inc_corr = step_inc_corr
        self.step_dec_corr = step_dec_corr
        self.testing_function = None
        self.start_point_values = []

    def set_testing_function(self, logic):
        self.testing_function = MFunction(logic)

    def execute_step(self, param):
        try:
            return self.testing_function.execute(param)
        except ValueError:
            print("No function specified")
            return False

    def get_value_in_start_point(self):
        x = self.start_points[-1][1]
        self.start_point_values.append(self.execute_step(x))

    def get_value_for_matrix(self, matrix_vector):
        self.start_points.append(self.step_value * matrix_vector)

    def is_step_successful(self):
        return self.start_point_values[-2] > self.start_point_values[-1]

    def run(self):
        self.get_value_in_start_point()
        for matrix_vector in self.base_vector_matrix:
            self.get_value_for_matrix(matrix_vector)
            self.get_value_in_start_point()
            is_success = self.is_step_successful()

            if is_success:
                self.step_value *= self.step_inc_corr
            else:
                self.step_value *= - self.step_dec_corr

    def iterate(self, count):
        for i in range(count):
            print("Executing algorithm. Take number {}".format(i+1))
            self.run()

        print('Points:' + str(self.start_points))
        print('Values:' + str(self.start_point_values))
