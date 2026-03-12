def greet(name):
    """
    A simple greeting function.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to sum
        
    Returns:
        int or float: The sum of the numbers
    """
    return sum(numbers)


if __name__ == "__main__":
    print(greet("World"))
    print(f"Sum: {calculate_sum([1, 2, 3, 4, 5])}")
    print('Welcome to DevAsc')