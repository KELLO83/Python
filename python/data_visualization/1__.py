from cProfile import label
import imp
from turtle import right
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt #차트 색깔바꾸기
import numpy as np



# plt.plot([1,2,3,4]) # X의 값은 [0,1,2,3] 으로 자동초기화


# plt.plot([1,2,3,4],[5,10,20,30]) #x값도 지정 y의값도 지정해준다


# plt.plot([1,2,3,4],[10,11,15,17],'r') # r=red 실선 ,ro=red 색깔로 실선이 아닌 점으로 표시해준다
# plt.axis([0,6,0,20]) #그래프가 보여주는 x최소부터 최대 y최소부터 y최대범위를 지정해준다
# #[xmin, xmax, ymin, ymax]를 지정했습니다.


t=np.arange(0,5,0.2) #np.arrage 배열 나타내기  (0,5] 간격을 0.2초간격으로 list형태로 반환한다
"""
[0.  0.2 0.4 0.6 0.8 1.  1.2 1.4 1.6 1.8 2.  2.2 2.4 2.6 2.8 3.  3.2 3.4
3.6 3.8 4.  4.2 4.4 4.6 4.8]
"""

# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^') # -- 는 실선 bs 는 blue에 네모 g^  green에 세모


# plt.plot([2,3,5,10]) #꺽은선 그래프 (0.2),(1,3),(2,5),(3,10) 그래프

# data_dict={'data_x':[0,2,4,6,8],'data_y':[10,17,11,15,20]}

# plt.plot('data_x','data_y',data=data_dict) #딕셔너리를 활욜한 그래프 그리기 

def f(number):
    
    k1=np.exp(-number)*np.cos(2*np.pi*number) #y=밑이 e이고 지수가-t 곱하기 cos(2*파이*t)
    #np.exp 밑이 e에 지수가 -number 
    plt.plot(k1) 
    plt.show()

    
def f_1(number):
    return np.exp(-number)*np.cos(2*np.pi*number)
    


t1=np.arange(0,10,0.5) #(0,10] 까지 0.5초간격을 list반환


# plt.plot(t1,f_1(t1)) #첫번쨰 인수로 리스트를 줄경우 그 리스트의 열린구간부터 닫힌구간까지의 범위만
# #그래프로 그린다 

def Histogram():
    np.random.seed(20180107) # seed값 20180107
    mu,sigma=100,15
    x=mu+sigma*np.random.randn(10000)
    """
    np.random,randint 균일분포의 정수 난수 1개 생성
    np.random.rand 0부터 1사이의 균일 분포에서 난수 matrix array 생성
    np.random.randn 가우시안 표준 정규 분포에서 난수 matrix array생성
    """
    
    plt.hist(x,100,facecolor='g',alpha=0.3)  #2번쨰인수 히스토그램 세분화 
    #alpha 투명도 
    
    plt.xlabel('X_Axis',labelpad=5,loc='right') #x축 이름 loc 라벨위치 정하기 right center left
    plt.ylabel('Y_Axis',labelpad=5,loc='center') #y축 이름 labelpad 여백 공간 5pt
    plt.title('test') #그래프 title 
    plt.text(70,270,r'$\alpha=100,\Delta=20$') # x=70 y=270 에 text입력
    plt.grid(True) #그래프에서그리드 간격을 보여주는설정을 on
    plt.show()
    

def legend():
    plt.plot([1,2,3,4],[2,3,5,10],label='X-1') #범례표시
    plt.plot([10,20,30,40],label='X-2')
    plt.legend(loc='upper left',ncol=2,fontsize=10) #loc=() 범례위치 정하기 ncol 열의 갯수 지정하기 지정안할시 기본 열1 fontsize 폰트사이즈 정하기
    plt.legend(frameon=True,shadow=True) #frameon 범례상자의 테두리를 표시할지 여부를 선택 shadow 텍스트상자에 그림자 표시여부
    plt.show()



def object_create():
    fig,ax=plt.subplots() #튜블형태로 반환한다
    
    plt.show()
    print("{},{}".format(type(fig),type(ax)))
    
if __name__=="__main__":
    legend()


    
