if __name__ == '__main__':
    out_list=[]
    
    for _ in range(int(input())):
        in_list=[]
        name = input()
        score = float(input())
        in_list.append(name)
        in_list.append(score)
        out_list.append(in_list)
    #print(out_list)
    score=[] 
    for i in out_list:
        score.append(i[1])
    #print(score)
    minimum=min(score)
    #print(minimum)
    
    score=[x for x in score if x!=minimum]
    #print(score)
    second_min=min(score)
    names=[]
    for i in out_list:
        if i[1]==second_min:
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)
