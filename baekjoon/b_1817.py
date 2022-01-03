import sys


def solution(books_weight, m):
    box_cnt = 1
    current_weight = 0
    while books_weight:
        book_weight = books_weight.pop()
        current_weight += book_weight
        if current_weight > m:
            books_weight.append(book_weight)
            box_cnt += 1
            current_weight = 0
    return box_cnt

if __name__ == '__main__':
    n, m = map(int, input().split())
    if n == 0:
        print(0)
        sys.exit()
    books = list(map(int, input().split()))
    print(solution(books, m))