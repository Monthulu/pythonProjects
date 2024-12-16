# Planetary Weights scale
# Lamont Redd
# This program will give the users weight on planets in our solar system.
# and Pluto's

# Constants:

MERCURY_FACTOR = 0.38
VENUS_FACTOR = 0.91
MOON_FACTOR = 0.165
MARS_FACTOR = 0.38
JUPITER_FACTOR = 2.34
SATURN_FACTOR = 0.93
URANUS_FACTOR = 0.92
NEPTUNE_FACTOR = 1.12
PLUTO_FACTOR = 0.066

# Ask for Input and Convert:

sName = input("Hello, what's your name: ")
nWeight = float(input("What is your weight in pounds: "))

# Compute:

nUserWeightMercury = nWeight * MERCURY_FACTOR
nUserWeightVenus = nWeight * VENUS_FACTOR
nUserWeightMoon = nWeight * MOON_FACTOR
nUserWeightMars = nWeight * MARS_FACTOR
nUserWeightJupiter = nWeight * JUPITER_FACTOR
nUserWeightSaturn = nWeight * SATURN_FACTOR
nUserWeightUranus = nWeight * URANUS_FACTOR
nUserWeightNeptune = nWeight * NEPTUNE_FACTOR
nUserWeightPluto = nWeight * PLUTO_FACTOR

# Output:

print(f"{sName} here are your weights on our Solar System's planets, and Pluto's:")
print(f"{'Weight on Mercury: ':<20}{nUserWeightMercury:10.2f}")
print(f"{'Weight on Venus: ':<20}{nUserWeightVenus:10.2f}")
print(f"{'Weight on our Moon: ':<20}{nUserWeightMoon:10.2f}")
print(f"{'Weight on Mars: ':<20}{nUserWeightMars:10.2f}")
print(f"{'Weight on Jupiter: ':<20}{nUserWeightJupiter:10.2f}")
print(f"{'Weight on Saturn: ':<20}{nUserWeightSaturn:10.2f}")
print(f"{'Weight on Uranus: ':<20}{nUserWeightUranus:10.2f}")
print(f"{'Weight on Neptune: ':<20}{nUserWeightNeptune:10.2f}")
print(f"{'Weight on Pluto: ':<20}{nUserWeightPluto:10.2f}")



