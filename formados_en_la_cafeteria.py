import io, os

if __name__ == '__main__':
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    num_actions = int(input().decode())
    student_queue = []
    worker_queue = []
    for i in range(num_actions):
        action = input().decode()
        if 'LLEGA' in action:
            name = action.split()[2]
            if 'ALUMNO' in action:
                student_queue.append(name)
            else:
                worker_queue.append(name)
        else:
            if worker_queue:
                print(worker_queue[0])
                worker_queue.pop(0)
            else:
                print(student_queue[0])
                student_queue.pop(0)
