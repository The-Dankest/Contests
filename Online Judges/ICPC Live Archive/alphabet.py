def lis(arr): 
    n = len(arr) 
    lis = [1]*n 
    for i in range (1, n): 
        for j in range(0, i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1 
    return max(lis) 

while True:
    try:
        s = input().strip()
        print((26 - lis(list(s))))
    except EOFError:
        break