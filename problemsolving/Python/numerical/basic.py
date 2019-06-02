
# Recursive Function for a power n

def powerN(a, n):
    if n == 0:
        return 1
    return a * powerN(a, n-1)

def divisibilityTest(n):
    if n % 9 == 0 and n % 11 == 0 and n % 10 != 0:
        return True
    else:
        return False