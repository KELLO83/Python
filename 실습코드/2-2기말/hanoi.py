def move(n,start,end):
    print("{}원반을 {} 에서 {}".format(n,start,end))
    
def hanoi(N,start,end,sub):
    if N==1:
        move(1,start,end)
        return # 
    else:
        hanoi(N-1,start,sub,end)
        move(N,start,end)
        hanoi(N-1,sub,end,start)


if __name__ == "__main__":

    hanoi(4,"A","B","C")

