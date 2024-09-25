---

# Pseudo-Random Sequence Generators (PRSG)

A collection of PRSGs, including: Linear Congruential Generator, Blum-Blum-Shub (BBS).

## Files

* `lineral.py` - Linear Congruential PRSG (Zuev version)
* `lcg.py` - Linear Congruential PRSG
* `bbs.py` - Blum-Blum-Shub PRSG
* `period.py` - To find the period of the results (for some generators, this is handled within the code)
* `xorshift.py` - Xorshift PRSG

## Linear Congruential Generator

Works using the simple mathematical formula: `Xn+1 = (a * Xn + c) mod m`.

Primitive `for` loop:
```python
x = seed
for n in range(m):
    x = (a * x + c) % m
```
Requires 4 coefficients: `a, seed, c, m`, which are inputtable. Additionally, to find the period correctly, the range should be increased to:
```python
n = 1000000
for n in range(m):
...
```

## Blum-Blum-Shub

The algorithm works using the formula: `Xn+1 = (Xn)^2 mod M`, where `M = p * q`.
The primes `p` and `q` must satisfy `p % 4 = 3` and `p != q`.

Correctness checks:
```python
# Check that p and q are prime numbers
if not (sympy.isprime(p) and sympy.isprime(q)):
    raise ValueError("Both numbers must be prime")

# Check that p and q are not equal
if p == q:
    raise ValueError("Numbers p and q must not be equal")

# Check that p and q satisfy the condition p % 4 == 3 and q % 4 == 3
if p % 4 != 3 or q % 4 != 3:
    raise ValueError("Numbers p and q must be of the form 3 (mod 4)")
```

After checking, the seed must be coprime with `n`:
```python
if gcd(seed, self.n) != 1:
    raise ValueError("Seed must be coprime with n")

# Function to compute the GCD (necessary for seed check)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

Then we perform the formula operations:
```python
def DegreeM(a, k, n):
    b = 1
    while k != 0:
        if k % 2 == 1:
            b = (b * a) % n
        k = k // 2
        a = (a * a) % n
    return b

def next_number(self):
    # Generate the next state
    self.state = (self.state**2) % self.n
    return self.state
```

## Xorshift

The Xorshift algorithm operates using XOR logic operations and shifting bits left or right several times. Its implementation is straightforward:
```python
def next(self) -> int:
    x = self.state
    a = self.a
    b = self.b
    c = self.c
    x ^= (x << a) & 0xFFFFFFFFFFFFFFFF
    x ^= (x >> b) & 0xFFFFFFFFFFFFFFFF
    x ^= (x << c) & 0xFFFFFFFFFFFFFFFF
    self.state = x
    return x
```
Additionally, we run the x64 version of the algorithm, which requires the use of the mask `0xFFFFFFFFFFFFFFFF`.

---