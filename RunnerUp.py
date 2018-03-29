if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner=max(arr)
    second=[]
    for i in arr:
        if i<winner:
            second.append(i)
            
    print(max(second))
