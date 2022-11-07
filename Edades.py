

if __name__ == '__main__':
    n = int(input())
    ages = sorted([int(i) for i in input().split()])
    i = 0
    while i < len(ages):
        current_age = ages[i]
        count = 1
        i += 1
        while i < len(ages) and current_age == ages[i]:
            count += 1
            i += 1
        print(str(current_age) + ' ' + str(count))
