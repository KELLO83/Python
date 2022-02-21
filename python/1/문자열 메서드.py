
str="kello"
number=10

teo="{number}:{str}".format(**locals()) #number와 str를 딕셔너리 형태로 반환한다 .format(**locals())사용을 하여서



te=" ".join(str)#" "공백을 기준으로 str의 문자 하나넣고 공배넣고 문자하나넣고 공백넣고를 반복한다 공백은 다른문자나 숫자로 대체가능

str.ljust(50,"-") #kello--------------------------------------------- 왼쪽에다먼저 문자를 삽이하고 50칸을 -으로 문자를 대체한다
str.rjust(50,"-") #왼쪽에 문자를 넣고 앞쪽을 -50개를 넣는다

slayers="abc\ndef"

slayers.splitlines() #['abc', 'def'] \n을기준으로 쪼갠다 이후 리스트 형태로 반환한다

slayers.split('d',2)
















