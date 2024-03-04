import collections
import sys

line =int(input())
data=collections.deque()

for i in range(line):
        user=sys.stdin.readline().split()
        
        command = user[0]
        
        if command=='push_front':
            data.appendleft(int(user[1]))
            
        elif command=='push_back':
            data.append(int(user[1]))
            
        elif command=='pop_back':
            try:
                print(data.pop())
            except:
                print("-1")
                
        elif command=="pop_front":
            try:
              print(data.popleft())
            except:
                print("-1")
            
        elif command=="size":
            print(len(data))
            
        elif command=='empty':
            if len(data)==0:
                print("1")
            else:
                print("0")
                
        elif command == 'front':
            try:
                print(data[0])
            except:
                print('-1')
                
        elif command == 'back':
            try:
                print(data[len(data)-1])
            except:
                print('-1')
                        

                