def fizzbuzz(num):
    if num%3==0 and num%5==0:
        return "fizzbuzz"
    if num == 0:
       return "fizzbuzz"
    if num%3==0:
        return "fizz"
    if num%5==0:
        return "buzz"
    return num


print(fizzbuzz(3))
print(fizzbuzz(18))
print(fizzbuzz(20))
print(fizzbuzz(7))
print(fizzbuzz(0))
print(fizzbuzz(-9))
print(fizzbuzz(15))