from sys import exit


def _exit():
    print("Thank you for using our application.")
    exit()


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
