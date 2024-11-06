integer = input("Enter numbers (comma-separated): ")
intras = integer.split(",")
numbers = []

# Strip whitespace and convert to integers
for intra in intras:
    numbers.append(int(intra.strip()))

def sumEven(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return f"(The sum of even numbers is {even_sum} and the sum of odd numbers is {odd_sum})"

print(sumEven(numbers))