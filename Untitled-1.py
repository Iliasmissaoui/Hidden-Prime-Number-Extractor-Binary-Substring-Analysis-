import time  # Import the time module to measure duration

def is_prime(n):
    "Check if a number is prime"
    if n < 2:
        return False
    if n in {2, 3}:  # Check small prime numbers
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6  # Skip unnecessary numbers

    return True

def find_hidden_primes(binary_string, limit):
    "Extract unique prime numbers from a binary string"
    primes_found = set()

    for start in range(len(binary_string)):
        for end in range(start + 1, len(binary_string) + 1):
            decimal_number = int(binary_string[start:end], 2)
            if decimal_number > 1 and decimal_number < limit:  # Ignore 0 and 1
                if is_prime(decimal_number):
                    primes_found.add(decimal_number)

    return primes_found  # Return set of unique primes

# Test cases
test_cases = [
    ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678),
]

# Run the test cases and measure duration
for binary_string, limit in test_cases:
    start_time = time.time()  # Start timing
    found_primes = find_hidden_primes(binary_string, limit)
    end_time = time.time()  # End timing

    duration = end_time - start_time  # Calculate duration
    print(f"Prime numbers found in '{binary_string}' with limit {limit}: {sorted(found_primes)}")
    print(f"Duration: {duration:.4f} seconds")  # Print duration with 4 decimal places