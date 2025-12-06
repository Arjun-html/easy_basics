# Online Python - IDE, Editor, Compiler, Interpreter

def interest_on_oil(rev_pm, int_rate, years):
    
    months = years*12
    total_interest = 0
    for i in range(months):
        interest = rev_pm*(int_rate/100)*((months - 1 - i)/ months)
        total_interest += interest
    return total_interest
    
    
    
    
ans = interest_on_oil(500, 8, 1)
print(f"total interest on oil is ${ans}")