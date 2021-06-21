class Time:
    def __init__(self,hours=0,mins='00'):
        self.__hours = str(hours)
        if mins==0:
            mins="00"
        self.__mins = str(mins)
    
    def __str__(self):
        return self.__hours+":"+self.__mins


class Date:
    def __init__(self,day,month):
        self._day=str(day)
        self._month=str(month)
    def __str__(self):
        return self._day+'.'+self._month


class TimeFinder:
    SEPARATOR_COLON= ':'
    SEPARATOR_DOT='.'
    PARTS_OF_DAY={"утра":0,"ночи":0,"дня":12,"вечера":12}
    SEASONS={"января":1,"февраля":2,"марта":3,"апреля":4,
             "мая":5,"июня":6,"июля":7,"августа":8,
             "сентября":9,"октября":10,"ноября":11,"декабря":12}
    def __init__(self,string):
        _words=string.split()
        for ind in range(len(_words)):
            if '0' <= _words[ind][0] and _words[ind][0] <= '9': # Main case
                if self.SEPARATOR_COLON in _words[ind]: # If time
                    _nums=list(map(int, _words[ind].split(self.SEPARATOR_COLON)))
                    if _nums[0]<=24 and _nums[1]<=60:
                        print(Time(_nums[0], _nums[1]))
                    else:
                        print("-")
                elif self.SEPARATOR_DOT in _words[ind]: # If date
                    _nums=list(map(int,_words[ind].split(self.SEPARATOR_DOT)))
                    if _nums[0]<32 and _nums[1]<13:
                        print(Date(_nums[0],_nums[1]))
                else:
                    if ind+1<len(_words):
                        if _words[ind+1] in self.PARTS_OF_DAY.keys():
                            _hours=int(_words[ind])+self.PARTS_OF_DAY[_words[ind+1]]
                            if _hours>24:
                                print("-")
                            else:
                                print(Time(_hours))
                        elif _words[ind+1] in self.SEASONS.keys():
                            print(Date(_words[ind],self.SEASONS[_words[ind+1]]))
                        else:
                            print("-")

    
TimeFinder(input())
# Проверка коммитов
