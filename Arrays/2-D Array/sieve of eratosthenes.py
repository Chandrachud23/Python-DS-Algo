def make_sieve(MAX):
    MAX += 1
    least_prime = [0] * MAX
    for i in range(2, MAX): 
        if least_prime[i] == 0:
            least_prime[i] = 0
            for j in range(i * i, MAX, i) : 
                if (least_prime[j] == 0) : 
                    least_prime[j] = 1
    for i in range(2, MAX):
        if least_prime[i]==0:
            print(i)

result = make_sieve(50)
