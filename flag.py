import random
import binascii

t = [7352, 2356, 7579, 19235, 1944, 14029, 1084]
s = [184, 332, 713, 1255, 2688, 5243, 10448]
n = 20910
c = [8436, 22465, 30044, 22465, 51635, 10380, 11879, 50551, 35250, 51223, 14931, 25048, 7352, 50551, 37606, 39550]
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def gcd(a, b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
def check(m):
    for i in range(7):
        if (s[i]*m - t[i])% n != 0:
            return 0;
    return 1;
m = 1
while gcd(m,n) != 1 or check(m) == 0:
    m = random.randint(100, n)
k = modinv(m,n)
for i in c:
    x = i*k % n
    print(x)
    print(' ')
