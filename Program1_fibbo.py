
# Fibonacci using Recursive Method

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter number of terms: "))
print("Fibonacci using Recursive Method:")

for i in range(n):
    print(fibonacci(i), end=" ")

print()


# Fibonacci using Non-Recursive Method

nterms = int(input("Enter number of terms: "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence:", n1)
else:
    print("Fibonacci using Non-Recursive Method:")

    while count < nterms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
