
if __name__ == '__main__':
    stack = []
    n = int(input())
    for i in range(n):
        operation = input()
        if 'AGREGA' in operation:
            stack.append(int(operation.split()[1]))
        elif 'CONSUME' in operation:
            a = stack[-1]
            stack.pop()
            stack[-1] = stack[-1] + a
        else:
            print(stack[-1])