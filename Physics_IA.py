import math

"""
    Calculates change in velocity of Lagrange Points L4 and L5 of Earth-Moon system if mass of Earth were to increase.
    Based on v = sqrt(GM/r) formula.
"""

EarthMass = 5.972 * 10 ** 24
Gravitational_Constant = 6.67408 * 10 ** -11
r = 384402000
i = 1
while i <= 5:
    print(math.sqrt(i * EarthMass * Gravitational_Constant / r) / 1000, 'km/s')
    i += 0.5
