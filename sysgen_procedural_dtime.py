import numpy as np
import numpy.random as npr
import numpy.linalg as la

# Generate systems procedurally i.e. according to parameters and/or randomness

def rand_system(n=2, m=2, p=2, spectral_radius=0.9, noise_scale=1, noise_shape='eye', seed=1):
    """
    Generate a system whose matrices have Gaussian random entries
    :param n: Number of states, integer
    :param m: Number of inputs, integer
    :param p: Number of outputs, integer
    :param spectral_radius: Open-loop spectral radius of A, float
    :param noise_scale: Scaling of noise covariance, float
    :param noise_shape: Shape of noise covariance, string, valid options are 'full', 'diag', 'eye'
    :param seed: Seed for random number generator, positive integer
    :returns: Number of states, number of inputs, state matrix, input matrix, state cost matrix, input cost matrix,
              additive noise covariance matrix
    """

    npr.seed(seed)
    A = npr.randn(n, n)
    A *= spectral_radius/np.max(np.abs(la.eig(A)[0]))
    B = npr.randn(n, m)
    C = npr.randn(p, n)
    D = npr.randn(p, m)
    U = npr.randn(n, n)
    V = npr.randn(m, m)
    Y = npr.randn(n, n)
    Q = np.dot(U, U.T)
    R = np.dot(V, V.T)
    if noise_shape == 'full':
        W = noise_scale*np.dot(Y, Y.T)
    elif noise_shape == 'diag':
        W = noise_scale*np.diag(np.diag(np.dot(Y, Y.T)))
    elif noise_shape == 'eye':
        W = noise_scale*np.eye(n)


    keys = ['A', 'B', 'C', 'D', 'Q', 'R', 'W']
    values = [A, B, C, D, Q, R, W]
    return dict(zip(keys, values))


def pendulum_system(inverted, mass=10, damp=2, dt=0.1):
    """
    Generate a system representing a pendulum with a torque actuator and dynamics linearized about a vertical position
    with forward Euler discretization.
    :param inverted: Specification of whether to linearize dynamics about the inverted or hanging position, boolean
    :param mass: Generalized mass constant, float
    :param damp: Generalized damping constant, float
    :param dt: Discretization time interval, float
    """

    if inverted:
        sign = 1
    else:
        sign = -1
    A = np.array([[1, dt], [sign*mass*dt, 1-damp*dt]])
    B = np.array([[0], [dt]])
    C = None
    D = None

    keys = ['A', 'B', 'C', 'D']
    values = [A, B, C, D]

    return dict(zip(keys, values))