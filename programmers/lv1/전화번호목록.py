def solution(phone_book):
    cnt = len(phone_book)
    while cnt > 0:
        n = phone_book.pop(0)
        for i in phone_book:
            if n == i[:len(n)]:
                return False
        phone_book.append(n)
        cnt -= 1
    return True