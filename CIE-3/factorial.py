# Recursive function to calculate factorial
def factorial(n):
    """
    Recursive function to calculate the factorial of a number.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
if __name__ == "__main__":
    number = 6
    print(f"The factorial of {number} is {factorial(number)}")  
