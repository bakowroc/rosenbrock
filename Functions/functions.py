
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy

def rosenbrock_function(x, y):
    return (1-x)**2 + 100*((y-x**2)**2)


def parabolid(a,b, x, y):
    return (x**2)/(a**2) +(y**2)/(b**2)


def return_linspace(x_start, x_stop, y_start, y_stop, step):
    x = numpy.linspace(x_start, x_stop, num=step)
    y = numpy.linspace(y_start, y_stop, num=step)

    return x ,y


def meshup_coordinates(x, y):
    X,Y = numpy.meshgrid(x, y, indexing="xy")
    X = X.reshape((numpy.prod(X.shape),))
    Y = Y.reshape((numpy.prod(Y.shape),))

    return X, Y

if __name__ == "__main__":

    x, y = return_linspace(-5.0, 5.0, -5.0, 5.0, 3)

    X, Y = meshup_coordinates(x, y)
    print(x)
    print(y)
    print(X)
    print(Y)
    #for i in range(x):
     #   for j in range(y):
      #      print(i, j)

    #Z = parabolid(1,1, X, Y)
    z = numpy.array([parabolid(1,1,x,y) for x, y in zip(numpy.ravel(X), numpy.ravel(Y))])
    Z = z.reshape(X.shape)
    print(Z)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')