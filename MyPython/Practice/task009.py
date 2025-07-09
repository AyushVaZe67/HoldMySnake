def fibonacci(num):
    result = []
    if num <= 0:
        return result
    elif num == 1:
        result.append(0)
    else:
        result = [0,1]
        for i in range(2,num):
            next_term = result[-1] + result[-2]
            result.append(next_term)
        return result


num = int(input('Enter a number of terms: '))
print(f"Fibonacci sequence up to {num} terms: {fibonacci(num)}")
