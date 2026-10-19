# -------------------------------------------------------------
# EVALUATION: Lab 04 - Build a Number Pattern Generator
# NOTES: Independent lab focusing on type enforcement, integer bounds checking, and loop-driven string construction.
# -------------------------------------------------------------

# USER STORIES TO FULFILL:
# 1. Define a function named number_pattern(n) that takes a single positive integer.
# 2. Inside the function, you must use a for loop.
# 3. Return a space-separated string containing all integers from 1 through n inclusive (e.g., "1 2 3 4").
# 4. If n is not an integer type -> return "Argument must be an integer value."
# 5. If n is less than 1 -> return "Argument must be an integer greater than 0."

# -------------------------------------------------------------

def number_pattern(n):
    if isinstance(n,int)!=True:
        return "Argument must be an integer value."
    if n<=0:
        return "Argument must be an integer greater than 0."
    
    str_num = [str(num) for num in range(1, n+1)]
        
    return " ".join(str_num)
print(number_pattern(4))