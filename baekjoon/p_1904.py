n = int(input())
byte_value = bin(n)
answer = 0
for i in byte_value:
    if i == '1':
        answer += 1
print(answer)