import random
def user_pow(user:int,exp:int):
    if exp<=1:
        return user
    else:
        return user_pow(user,exp-1)*user

def user_sum(arr):
    if len(arr)<=1:
        return arr
    else:
        pass
        
if __name__=="__main__":
    print(user_pow(2,10))
    arr=[random.randint() for i in range(10)]
    print(arr)
    print(user_sum(arr))
    