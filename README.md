# Pseudo-Random Sequence Generators (PRSG)
A pack of PRSG, contains: Lineral Congruent, Blum-Blum-Shub (BBS), 

# Files

* `lineral.py` - Lineral Congruent PRSG (Zuev version)
* `lcg.py` - Lineral Congruent PRSG
* `bbs.py` - Blum-Blum-Shub PRSG
* `period.py` - To find period in result (for some generators it realized inside code)
* `xorshift.py` - Xorshift PRSG

# Lineral Congruent

Works by simple math formula `Xn+1=(a * Xn + c) mod m`
Primitive `for` cycle:
```
x = seed
for n in range(m):
    x = (a * x + c) % m
```
Needs 4 coefficents: `a, seed, c, m` they are inputable
Also for finding period correctly need to up range to 
```
n = 1000000
for n in range(m):
...
```