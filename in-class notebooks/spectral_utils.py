import numpy as np
fft = np.fft.fft

def spectral_representation(x0,uhat,xi):
    """
    Returns a truncated Fourier series representation of a function.

    Parameters:
    x0 (float): The left endpoint of the domain of the function.
    uhat (numpy.ndarray): The Fourier coefficients of the function.
    xi (numpy.ndarray): The vector of wavenumbers.

    Returns:
    u_fun: A vectorized function that represents the Fourier series.
    """
    u_fun = lambda y : np.real(np.sum(uhat*np.exp(1j*xi*(y+x0))))/len(uhat)
    u_fun = np.vectorize(u_fun)
    return u_fun

def fine_resolution(f, n, x, xi):
    """
    Interpolates a periodic function `f` onto a finer grid of `n` points using a Fourier series.

    Parameters:
    -----------
    f : function
        The function to be interpolated.
    n : int
        The number of points in the finer grid.
    x : array-like
        The original grid of `f`.
    xi : array-like
        The Fourier modes.

    Returns:
    --------
    x_fine : array-like
        The finer grid of `n` points.
    f_spectral : function
        The Fourier interpolation `f` on the finer grid.
    """
    fhat = fft(f)
    f_spectral = spectral_representation(x[0],fhat,xi)
    x_fine = np.linspace(x[0],x[-1],n)
    return x_fine, f_spectral(x_fine)
