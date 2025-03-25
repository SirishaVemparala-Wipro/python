def sum_and_product(a, b):
    
    sum_result = a + b
    
    product_result = a * b
    
    return sum_result, product_result  # Returns both values as a tuple

num1, num2 = 4, 5

result_sum, result_product = sum_and_product(num1, num2)

print(f"Sum of {num1} and {num2} is: {result_sum}")

print(f"Product of {num1} and {num2} is: {result_product}")
