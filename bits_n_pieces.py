""" These are all the things that appear in Project 2, but which are not  altered 
in Project 3. They are imported in Project 3 through this script rather than
appearing there directly for the sake of brevity."""

import numpy as np
import pandas as pd
from numpy.linalg import norm
import math
import matplotlib.pyplot as plt
import astropy.constants as _ac
import astropy.units as _au
from numpy import pi
from scipy import optimize

###importing constants

# solar mass, radius, luminosity
Msun = _ac.M_sun.value
Rsun = _ac.R_sun.value
Lsun = _ac.L_sun.value

# physical constants from astropy, all in MKS units
G = _ac.G.value
h = _ac.h.value
hbar = _ac.hbar.value
m_e = _ac.m_e.value
m_p = _ac.m_p.value
m_n = _ac.m_n.value
m_u = _ac.u.value
c = _ac.c.value
kB = _ac.k_B.value
pc = _ac.pc.value
au = _ac.au.value
year = _au.year.to(_au.second)
sigmaSB = _ac.sigma_sb.value

# other constants
mue = 2
K_e = ((1/5)*((3/(8*pi))**(2/3))*(h**2/(m_e*(mue*m_u)**(5/3))))

### rk4 routine from Project 1
def rk4(f,t,z,h,args=()):
    """    
    Arguments
        f(t,z,...)
            function that contains the RHS of the equation dz/dt = f(t,z,...)
    
        t (scalar)
            current time
            
        z (array-like)
            function value
            
        h (scalar)
            step size
    
        args (tuple, optional)
            additional arguments to pass to f
    
    Returns
        znew = z(t+h)
    """
   
    if not isinstance(args,tuple):
        args = (args,)

    k1 = f(t, z, *args)

    k2 = f(t + h/2, z + (h/2)*k1, *args)

    k3 = f(t + h/2, z + (h/2)*k2, *args)

    k4 = f(t + h, z + h*k3, *args)
    
    return z + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

def pressure(rho, mue):
    """
    Arguments
        rho
            mass density (kg/m**3)
        mue
            baryon/electron ratio
    
    Returns
        electron degeneracy pressure (Pascal)
    """

    p = (1/5)*(3/(8*np.pi))**(2/3)*(h**2/m_e)*(rho/(mue*m_u))**(5/3)
    return p

def density(p, mue):
    """
    Arguments
        p
            electron degeneracy pressure (Pascal)
        mue
            baryon/electron ratio  
        mu
            amu
        h
            Planck's constant
        me
            electron mass
        
    Returns
        mass density (kg/m**3)
    """
    
    
    rho = mue*m_u*(5*p*(m_e/h**2)*(3/(8*np.pi))**(-2/3))**(3/5)
    return rho