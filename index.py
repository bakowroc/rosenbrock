from RosenbrockAlgorithm import RosenbrockAlgorithm

start_point = [4, 6]
base_vector_matrix = [[1, 0], [0, 1]]
start_step = [1, 4]
step_inc_corr = 3
step_dec_corr = 0.5


def function_logic(x):
    return 5*x*x - 6*x + 2


method = RosenbrockAlgorithm(start_point, base_vector_matrix, start_step, step_inc_corr, step_dec_corr)
method.set_testing_function(function_logic)

method.iterate(5)

