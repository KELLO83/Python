#하노이탑 구현

def move(disk,x,y):
    if disk>1:
        move(disk-1,x,6-x-y)
        
    print(f"원반{disk}를 {x}에서{y}로 이동합니다")
    
    if disk>1:
        move(disk-1,6-x-y,y)


if __name__=="__main__":
    move(3,1,3)
    
    
