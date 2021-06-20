class Time:
    def __init__(self,hours=0,mins='00'):
        self.__hours = str(hours)
        self.__mins = str(mins)
    
    def __str__(self):
        return self.__hours+":"+self.__mins


class TimeFinder:
    SEPARATOR=':'
    PARTS_OF_DAY={"утра":0,"ночи":0,"дня":12,"вечера":12}
    
    def __init__(self,string):
        words=string.split()
        for ind in range(len(words)):
            if '0' <= words[ind][0] and words[ind][0] <= '9':
                if self.SEPARATOR in words[ind]:
                    nums=list(map(int,words[ind].split(self.SEPARATOR)))
                    if nums[0]<=24 and nums[1]<=60:
                        print(Time(nums[0], nums[1]))
                    else:
                        print("-")
                else:
                    _hours=int(words[ind])+self.PARTS_OF_DAY[words[ind+1]]
                    if _hours>24:
                        print("-")
                    else:
                        print(Time(_hours))

    
TimeFinder(input())
# Проверка коммитов