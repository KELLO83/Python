from operator import *
def makeIndex(arr,pos):
    beforeAry = []
    index = 0
    for data in arr:
        beforeAry.append((data[pos],index))
        index +=1
    sortedAry=sorted(beforeAry,key=itemgetter(pos))
    return sortedAry


def seqSearch(arr,key):
    start = 0
    end = len(arr)-1
    
    while start<=end:
        middle = (start+end)//2
        if key== arr[middle][0]:
            return arr[middle][1]
        
        elif key > arr[middle][0]:
            start = middle+1
        else:
            end = middle-1
            
    return -1 # 실패




book = [["데미안","헤르만헤세"],['어린왕자','생뗵쥐베리'],['대지','펄벅'],['신곡','단테']]
print("정렬전",book)
book_sorted_by_author = makeIndex(book,0)
book_sorted_by_book_name = makeIndex(book,1)

print("책의 저자 이름순으로 정렬=>",book_sorted_by_author)
print()
print("책의 이름순으로 정렬",book_sorted_by_book_name)

print("책의 저자이름순으로 찾기를 시도합니다")
r1=seqSearch(book_sorted_by_author,"데미안")
if r1 !=-1:
    print(f"데미안은 {r1} 번째 index에 위치합니다")
else:
    print("검색실패")
    
    
print("책의 이름순으로 찾기를 시도합니다")
r2=seqSearch(book_sorted_by_book_name,"펄벅")
if r2 !=-1:
    print(f"펄벅은 {r2} 번째 index에 위치합니다")
else:
    print("검색실패")
    
    