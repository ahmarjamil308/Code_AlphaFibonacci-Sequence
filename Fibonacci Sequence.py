def fibonacci_iterative(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence
n_terms = int(input("Enter the length of Fibonacci sequence: "))
print(fibonacci_iterative(n_terms))
