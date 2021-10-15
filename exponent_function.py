#basic exponent code
print(2**3)

#Exponent using functions

def raise_to_power(base_num, power):
    result = 1
    for index in range(power):
        result = result * base_num
    return result

print(raise_to_power(3, 4))
