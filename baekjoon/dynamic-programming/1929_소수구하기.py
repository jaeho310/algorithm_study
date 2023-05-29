def get_prime_list():
    for i in range(2, n + 1):
        if prime_list[i]:
            for j in range(i*2, n+1, i):
                prime_list[j] = False

if __name__ == '__main__':
    m, n = map(int, input().split())
    prime_list = [True for _ in range(n+1)]
    prime_list[1] = False
    get_prime_list()
    for i in range(m, n+1):
        if prime_list[i]:
            print(i)