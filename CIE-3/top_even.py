# Write a function to return top 3 even numbers from a list
def top_three_even_numbers(numbers):
    """
    Returns the top 3 even numbers from the given list in descending order.
    If there are fewer than 3 even numbers, return all of them sorted.
    """
    # Filter even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    # Sort in descending order
    even_numbers.sort(reverse=True)
    # Return the top 3
    return even_numbers[:3]

# Example usage
if __name__ == "__main__":
    sample_list = [26, 52, 42, 8, 3, 7, 14]
    print(top_three_even_numbers(sample_list))  # Output: [22, 14, 10]