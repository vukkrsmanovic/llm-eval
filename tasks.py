TASKS = [
    # ── Strings ──────────────────────────────────────────
    {
        "id": 1, "category": "strings",
        "prompt": "Write a Python function called `reverse_string(s)` that returns the reversed string.",
        "test": "assert reverse_string('hello') == 'olleh'\nassert reverse_string('') == ''"
    },
    {
        "id": 2, "category": "strings",
        "prompt": "Write a Python function called `is_palindrome(s)` that returns True if s is a palindrome, False otherwise.",
        "test": "assert is_palindrome('racecar') == True\nassert is_palindrome('hello') == False\nassert is_palindrome('') == True"
    },
    {
        "id": 3, "category": "strings",
        "prompt": "Write a Python function called `count_vowels(s)` that returns the number of vowels in s (a, e, i, o, u, case-insensitive).",
        "test": "assert count_vowels('hello') == 2\nassert count_vowels('AEIOU') == 5\nassert count_vowels('xyz') == 0"
    },
    {
        "id": 4, "category": "strings",
        "prompt": "Write a Python function called `title_case(s)` that returns s with the first letter of each word capitalized.",
        "test": "assert title_case('hello world') == 'Hello World'\nassert title_case('python is great') == 'Python Is Great'"
    },
    {
        "id": 5, "category": "strings",
        "prompt": "Write a Python function called `compress_string(s)` that compresses consecutive duplicate characters, e.g. 'aaabbc' -> 'a3b2c1'.",
        "test": "assert compress_string('aaabbc') == 'a3b2c1'\nassert compress_string('abc') == 'a1b1c1'"
    },
    # ── Math ─────────────────────────────────────────────
    {
        "id": 6, "category": "math",
        "prompt": "Write a Python function called `add(a, b)` that returns the sum of two numbers.",
        "test": "assert add(1, 2) == 3\nassert add(-1, 1) == 0\nassert add(0, 0) == 0"
    },
    {
        "id": 7, "category": "math",
        "prompt": "Write a Python function called `factorial(n)` that returns n factorial. Assume n >= 0.",
        "test": "assert factorial(0) == 1\nassert factorial(5) == 120\nassert factorial(1) == 1"
    },
    {
        "id": 8, "category": "math",
        "prompt": "Write a Python function called `is_prime(n)` that returns True if n is prime, False otherwise. Assume n >= 0.",
        "test": "assert is_prime(2) == True\nassert is_prime(7) == True\nassert is_prime(1) == False\nassert is_prime(9) == False"
    },
    {
        "id": 9, "category": "math",
        "prompt": "Write a Python function called `fizzbuzz(n)` that returns 'Fizz' if n is divisible by 3, 'Buzz' if by 5, 'FizzBuzz' if both, else the number as a string.",
        "test": "assert fizzbuzz(3) == 'Fizz'\nassert fizzbuzz(5) == 'Buzz'\nassert fizzbuzz(15) == 'FizzBuzz'\nassert fizzbuzz(7) == '7'"
    },
    {
        "id": 10, "category": "math",
        "prompt": "Write a Python function called `fibonacci(n)` that returns the nth Fibonacci number (0-indexed, so fibonacci(0)==0, fibonacci(1)==1).",
        "test": "assert fibonacci(0) == 0\nassert fibonacci(1) == 1\nassert fibonacci(6) == 8"
    },
    # ── Lists ─────────────────────────────────────────────
    {
        "id": 11, "category": "lists",
        "prompt": "Write a Python function called `flatten(lst)` that flattens a list of lists into a single list.",
        "test": "assert flatten([[1,2],[3,4]]) == [1,2,3,4]\nassert flatten([[1],[2],[3]]) == [1,2,3]\nassert flatten([]) == []"
    },
    {
        "id": 12, "category": "lists",
        "prompt": "Write a Python function called `remove_duplicates(lst)` that returns a list with duplicates removed, preserving order.",
        "test": "assert remove_duplicates([1,2,2,3,3,3]) == [1,2,3]\nassert remove_duplicates([]) == []\nassert remove_duplicates([1]) == [1]"
    },
    {
        "id": 13, "category": "lists",
        "prompt": "Write a Python function called `chunk(lst, n)` that splits lst into chunks of size n.",
        "test": "assert chunk([1,2,3,4,5], 2) == [[1,2],[3,4],[5]]\nassert chunk([1,2,3], 3) == [[1,2,3]]"
    },
    {
        "id": 14, "category": "lists",
        "prompt": "Write a Python function called `rotate(lst, k)` that rotates lst to the right by k positions.",
        "test": "assert rotate([1,2,3,4,5], 2) == [4,5,1,2,3]\nassert rotate([1,2,3], 0) == [1,2,3]"
    },
    {
        "id": 15, "category": "lists",
        "prompt": "Write a Python function called `two_sum(nums, target)` that returns the indices of two numbers that add up to target.",
        "test": "assert two_sum([2,7,11,15], 9) == [0,1]\nassert two_sum([3,2,4], 6) == [1,2]"
    },
    # ── Algorithms ───────────────────────────────────────
    {
        "id": 16, "category": "algorithms",
        "prompt": "Write a Python function called `binary_search(lst, target)` that returns the index of target in sorted lst, or -1 if not found.",
        "test": "assert binary_search([1,3,5,7,9], 5) == 2\nassert binary_search([1,3,5,7,9], 4) == -1"
    },
    {
        "id": 17, "category": "algorithms",
        "prompt": "Write a Python function called `bubble_sort(lst)` that returns lst sorted in ascending order using bubble sort.",
        "test": "assert bubble_sort([3,1,2]) == [1,2,3]\nassert bubble_sort([]) == []\nassert bubble_sort([1]) == [1]"
    },
    {
        "id": 18, "category": "algorithms",
        "prompt": "Write a Python function called `max_subarray(nums)` that returns the maximum sum of a contiguous subarray (Kadane's algorithm).",
        "test": "assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6\nassert max_subarray([1]) == 1"
    },
    # ── Dicts ─────────────────────────────────────────────
    {
        "id": 19, "category": "dicts",
        "prompt": "Write a Python function called `word_count(s)` that returns a dictionary with the count of each word in s.",
        "test": "assert word_count('hello world hello') == {'hello': 2, 'world': 1}\nassert word_count('') == {}"
    },
    {
        "id": 20, "category": "dicts",
        "prompt": "Write a Python function called `group_by_length(words)` that groups words by their length into a dictionary.",
        "test": "assert group_by_length(['hi', 'hey', 'bye', 'yo']) == {2: ['hi', 'yo'], 3: ['hey', 'bye']}"
    },
]