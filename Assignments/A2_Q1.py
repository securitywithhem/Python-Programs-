#QA

def evaluate_expression(expression):
    # Remove the '=' at the end of the expression
    expression = expression.replace("=", "")
    
    # Evaluate the expression using the eval function
    result = eval(expression)
    
    # Return the result as an integer (truncate decimal part)
    return int(result)

# Test the function
expression = "1 + 10 * 9 ="
print(evaluate_expression(expression))  # Output: 91


#QB


square_dict = {i: i ** 2 for i in range(1, 16)}
print(square_dict)