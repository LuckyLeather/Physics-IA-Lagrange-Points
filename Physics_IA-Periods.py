import math

"""
    Calculates the period of Lagrange Points (L4 and L5) of Earth-Moon system if the mass of Earth were to increase.
    The distance from Earth to the L points (r), is assumed constant. In reality, the resulting period(s) would
    be lower than the values found here; the r value would decrease due to an increasing gravitational pull, caused 
    by an increasing primary body mass.
    Based on t = 2*π*sqrt(r^3/GM) formula.
"""

EarthMass = 5.972 * 10 ** 24
Gravitational_Constant = 6.67408 * 10 ** -11
r = 384402000
i = 1
while i <= 5:
    print((2 * math.pi * math.sqrt(r ** 3 / (Gravitational_Constant * EarthMass * i))))
    i += 0.5
