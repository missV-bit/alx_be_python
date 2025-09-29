#!/usr/bin/env python3

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation.

    Parameters:
        num1 (float): first number
        num2 (float): second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float | str: numeric result, or an error message string if division by zero
                     or invalid operation.
    """
    op = operation.strip().lower()
    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation"
