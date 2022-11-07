

if __name__ == '__main__':
    input()
    nums_a, nums_b = input().split(), input().split()
    ans = 1
    for a, b in zip(nums_a, nums_b):
        if not a > b:
            ans = 0
            break
    print(ans)

