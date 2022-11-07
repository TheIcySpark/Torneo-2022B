

if __name__ == '__main__':
    input()
    nums = [int(i) for i in input().split()]
    p = int(input())
    ans = list(filter(lambda x: (x % 2 == p), nums))
    print(' '.join(str(i) for i in ans))

