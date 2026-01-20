import math  

def main():
    A = int(input("Enter A "))
    B = int(input("Enter B "))
    pythag(A,B)


def pythag(A,B):
    C = math.sqrt(A**2 + B**2)
    print(C)

main()