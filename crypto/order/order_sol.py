# Solution outline: 
# First of all, note that if we know t then we can find the flag from inv W * a mod M. 
# Let the order of sus mod M be ord. Since sus ^ (t+1) == 1 mod M, t+1 is a multiple of ord
# The problem has then been reduced to finding the order. 
# There are many ways to find the order. I will present one that requires less math. 
# First note that M can be factored as p^e * q for some primes p and q 
# Since sus == 1 mod p and 1 mod q, we know that sus ^ (p^(e-1) * q) == 1 mod p^e * q == 1 mod M 
# Then the order is a divisor of this exponent. We can just test each possibility until we find the true order
# Finally, we can keep testing multiples of the order until we find the correct value of t

M = 48743250780330593211374612602058842282787459461925115700941964201240170956193881047849685630951233309564529903
a = 19733537947376700017757804691557528800304268370434291400619888989843205833854285488738413657523737062550107458
sus = 11424424906182351530856980674107667758506424583604060548655709094382747184198

p = 3853
e = 29 
q = 500891

exp = p ** (e-1) * q

assert pow(sus, exp, M) == 1

divisors = [p ** i for i in range(e)]
divisors += [q * x for x in divisors]

potentials = []
for d in divisors: 
    if pow(sus, d, M) == 1:
        potentials.append(d)
        
order = min(potentials)

mult = 1

while True: 

    t = order * mult - 1
    W = (pow(t, -1, M) * a) % M
    W = hex(W)[2:] 
    
    try:
        flag = bytes.fromhex(W).decode('utf-8')
        
        if "flag" in flag: 
            print(flag)
            break
            
    except ValueError: 
        pass
        
    mult+= 1