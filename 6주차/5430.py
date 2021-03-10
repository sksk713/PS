from collections import deque
T = int(input())

for _ in range(T):
    func = input()
    arr_num = int(input())
    arr = input()[1:-1]
    if len(arr) == 0:
        print("error")
        continue

    arr_list = deque(map(int, arr.split(",")))

    flag = False

    for i in func:
        if i == 'R':
            arr_list.reverse()
        else:
            if len(arr_list) == 0:
                flag = True
                break
            else:
                arr_list.popleft()
    
    if flag:
        print("error")
    else:
        print(list(arr_list))

