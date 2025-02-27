#Task 1
fac = 1
sample_number = int(input("Enter a number: "))
for i in range(2,sample_number+1):
    fac *= i
print("Factorial of", sample_number, "is:",fac)