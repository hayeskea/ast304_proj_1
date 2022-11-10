########################################################################
# Team Gorilla Flip-Flops: Keara Hayes, Atticus Chong, Evelyn Fuhrman, Zachary Malzahn
# AST304, Fall 2020
# Michigan State University
########################################################################

"""
<Description of this module goes here: what it does, how it's used.>
"""

import astro_const as ac
import numpy as np

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
    
    # replace following lines with body of routine
    p = (1/5) * ((3/(2*ac.fourpi))**(2/3)) * ((ac.h**2)/ac.m_e) * ((rho/(mue * ac.m_u))**(5/3)) # electron degeneracy pressure in Pa

    return p

# def density(p, mue):
#     """
#     Arguments
#         p
#             electron degeneracy pressure (Pascal)
#         mue
#             baryon/electron ratio
        
#     Returns
#         mass density (kg/m**3)
#     """
    
#     # replace following lines with body of routine
#     m_u = 1.661e-27 # atomic mass unit in kg
#     h = 6.62607015e-34 # Planck's constant -- m^2 * kg/s
#     m_e = 9.1093837015e-31 # mass of an electron in kg
#     rho = (((5*p*m_e)/(h**2))**(3/5)) * (((8*np.pi)/3)**(2/5)) # mass density in kg/m^3
#     return rho

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
    
    # replace following lines with body of routine
<<<<<<< HEAD
    rho = (p*(1/5 * (3/(2*ac.fourpi))**(2/3) * ac.h**2/ac.m_e)**-1)**(3/5) * mue * ac.m_u
    return rho
=======
    rho = ((p*((1/5)*((3/8*pi)**2/3)*(h**2/(2*me)))**-1)**(3/5))*mu*mue
    return rho
>>>>>>> 3225f70276d0d0b9f051fdea6eac8ca8800654e4
