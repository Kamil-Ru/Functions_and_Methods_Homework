# Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as
# 4/3 * π * 𝑟^3

def vol(rad):
    import math
    return 4/3 * math.pi * rad**3

# Check
print(vol(2))