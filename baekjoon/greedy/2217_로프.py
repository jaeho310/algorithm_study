if __name__ == '__main__':
    n = int(input())
    rope_list = []
    for _ in range(n):
        new_rope = int(input())
        rope_list.append(new_rope)
    rope_list.sort(reverse=True)
    ans = 0
    for index, item in enumerate(rope_list):
        ans = max(ans, (index+1) * item)
    print(ans)

