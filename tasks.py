TASKS = [
    {
        "id": 1,
        "prompt": "Write a Python function called `add(a, b)` that returns the sum of two numbers.",
        "test": "assert add(1, 2) == 3\nassert add(-1, 1) == 0\nassert add(0, 0) == 0"
    },
    {
        "id": 2,
        "prompt": "Write a Python function called `reverse_string(s)` that returns the reversed string.",
        "test": "assert reverse_string('hello') == 'olleh'\nassert reverse_string('') == ''"
    },
    {
        "id": 3,
        "prompt": "Write a Python function called `is_palindrome(s)` that returns True if s is a palindrome.",
        "test": "assert is_palindrome('racecar') == True\nassert is_palindrome('hello') == False"
    },
    {
        "id": 4,
        "prompt": "Write a Python function called `factorial(n)` that returns n factorial. Assume n >= 0.",
        "test": "assert factorial(0) == 1\nassert factorial(5) == 120"
    },
    {
        "id": 5,
        "prompt": "Write a Python function called `fizzbuzz(n)` that returns 'Fizz' if n divisible by 3, 'Buzz' if by 5, 'FizzBuzz' if both, else the number as string.",
        "test": "assert fizzbuzz(3) == 'Fizz'\nassert fizzbuzz(5) == 'Buzz'\nassert fizzbuzz(15) == 'FizzBuzz'\nassert fizzbuzz(7) == '7'"
    },
]