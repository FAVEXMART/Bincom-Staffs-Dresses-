
// 1 //
// The mean color doesn't make sense in this context, as colors are categorical variables and can't be averaged. We can calculate the mode (most frequent color) or median (middle value when sorted) instead. //


// 2 //
colors = [
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE",
    "BLUE", "BLUE", "GREEN",
    "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE",
    "BLUE", "BLUE", "BLUE",
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE",
    "WHITE", "WHITE",
    "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE",
    "BLUE", "BLUE", "GREEN",
    "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE",
    "BLUE", "WHITE"
]


// 3 //
color_counts = {}
for color in colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1

print("Most frequent color:", max(color_counts, key=color_counts.get)) 


// 4 //
sorted_colors = sorted(color_counts.items(), key=lambda x: x[1])
median_index = len(sorted_colors) // 2
print("Median color:", sorted_colors[median_index][0])


// 5 //
frequencies = list(color_counts.values())
mean_frequency = sum(frequencies) / len(frequencies)
variance = sum((x - mean_frequency) ** 2 for x in frequencies) / len(frequencies)
print("Variance of frequencies:", variance)


// 6 //
print("Probability of red:", 3 / 35)


// 7 //
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS colors (color TEXT, frequency INTEGER)")

for color, frequency in color_counts.items():
    cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))

conn.commit()
cur.close()
conn.close()


// 8 //
def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return recursive_binary_search(arr, target, low, mid - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter a number: "))
result =


// 9 //
import random

def generate_random_binary_number(digits):
    binary_number = ''.join(str(random.randint(0, 1)) for _ in range(digits))
    decimal_number = int(binary_number, 2)
    return binary_number, decimal_number

binary_number, decimal_number = generate_random_binary_number(4)
print(f"Binary Number: {binary_number}, Decimal Number: {decimal_number}")



def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

fib_sequence = fibonacci_sequence(50)
print(f"Fibonacci Sequence: {fib_sequence}")
print(f"Sum of Fibonacci Sequence: {sum(fib_sequence)}")
