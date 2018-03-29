if __name__ == '__main__':
    N = int(input())
    list_n= []
    for i in range(N):
        input_command= input()
        
        if input_command[0:6]== "insert":
             list_n.insert(int(input_command[7]),int(input_command[9:]))
        
        elif input_command[0:6]== "remove":
            list_n.remove(int(input_command[7]))
       
        elif input_command[0:6]== "append":
            list_n.append(int(input_command[7:]))
        
        elif input_command=="sort":
            list_n.sort()
        elif input_command=="pop":
            list_n.pop(len(list_n)-1)
        elif input_command=="reverse":
            list_n=list_n[::-1]
        elif input_command=="print":
            print(list_n)
