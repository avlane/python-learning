"""Sieve of Eratosthenes and a trial division check."""

def primes_up_to(limit):
    """Sieve of Eratosthenes: all primes <= limit."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for n in range(2, int(limit ** 0.5) + 1):
        if sieve[n]:
            for multiple in range(n * n, limit + 1, n):
                sieve[multiple] = False
    return [n for n, is_prime in enumerate(sieve) if is_prime]


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, int(n ** 0.5) + 1, 2):
        if n % d == 0:
            return False
    return True


def main():
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print(" ".join(str(p) for p in primes_up_to(limit)))


if __name__ == "__main__":
    main()
