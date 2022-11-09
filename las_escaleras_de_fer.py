
if __name__ == '__main__':
    n = int(int(input()) / 10)
    count = 0
    for i in range(1, n + 1):
        count += i
        print(count, end=' ')
