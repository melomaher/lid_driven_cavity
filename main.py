# this is a script to solve a laminar flow inside a cavity
# the flow is 2D, incompressible, steady, and Newtonian
# the flow is examined for case of Re=100 and Re=1000
# x=1 m, y=1 m, U=1 m/s
# **********************
# the script discretize the vorticity and stream-function equations
# it will use structured fixed size meshes and clustered meshes
# ***********************
# the solver will use explicit and implicit methods
# ***********************
# finally, it will produce velocity profiles, streamlines, and vorticity contours.
# and validate against published data
import numpy as np


def main():
    # the geometry
    L = 1
    M = 100  # number of nodes in x
    N = 100  # number of nodes in y
    dx = L/M
    dy = L/N
    # flow properties
    U = 1
    Re = float(input('Enter Reynolds Number: '))
    nu = U * L / Re
    # might choose certain Re to ease the process of validating the results

    # define outcomes
    Psi = np.zeros([100, 100])
    Omega = np.zeros([100, 100])

    # define BCs
    # for Psi, it is equal to zero at all boundaries.
    # for Omega, its value must be calculated through the Poisson's equation.
    # left and right walls
    for j in range(1, N-1):
        Omega[0][j] = (-2/dx**2) * (Psi[1][j] - Psi[0][j])
        Omega[M-1][j] = (-2 / dx ** 2) * (Psi[M-2][j] - Psi[M-1][j])
    # bottom and top walls
    for i in range(1, M-1):
        Omega[i][0] = (-2 / dy ** 2) * (Psi[i][1] - Psi[i][0])
        Omega[i][N-1] = (-2 / dy ** 2) * (Psi[i][N-2] - Psi[i][N-1] + dy * U)

    # solve
    # first, explicit Gauss Seidel method



if __name__ == '__main__':
    main()
