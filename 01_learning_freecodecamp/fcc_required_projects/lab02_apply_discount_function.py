# -------------------------------------------------------------
# EVALUATION: Lab 02 - Build an Apply Discount Function
# NOTES: Independent lab creating a robust calculation function with strict parameter type checking and edge-case value validation.
# -------------------------------------------------------------

# USER STORIES TO FULFILL:
# 1. Define a function named apply_discount.
# 2. Function must accept exactly two parameters: price and discount.
# 3. If price is not an int or float -> return "The price should be a number"
# 4. If discount is not an int or float -> return "The discount should be a number"
# 5. If price <= 0 -> return "The price should be greater than 0"
# 6. If discount < 0 or > 100 -> return "The discount should be between 0 and 100"
# 7. If valid, calculate the discount amount as a percentage of the price.
# 8. Return the final calculated price after subtracting the discount.

# -------------------------------------------------------------

def apply_discount(price, discount):
    if isinstance(price,int) or isinstance(price,float):
        if price <=0:
            return "The price should be greater than 0"
    else:
        return "The price should be a number"
    
    if isinstance(discount,int) or isinstance(discount,float):
        if discount <0 or discount >100:
            return "The discount should be between 0 and 100" 
        else:
            discount=discount/100
            price=price-(price*discount)        
    else:
        return "The discount should be a number"
    return price

print(apply_discount(100,20))