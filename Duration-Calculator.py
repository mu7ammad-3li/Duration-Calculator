

#TODO: Define isLeepYear(Year)
def isLeapYear(Year):
    if ((Year%4==0 and not (Year %100==0)) or Year %400==0 ):
        #print (f"Year {Year} is Leep Year")
        return True 
    else:
        return False 

#TODO: Define daysInMonth(Year,Month)
def daysInMonth(Year,Month):
    match Month:
        case 1:
            return 31
        case 2 :
            if(isLeapYear(Year)):
                return 29
            else: 
                return 28
        case 3 :
            return 31
        case 4 :
            return 30
        case 5 :
            return 31
        case 6 :
            return 30
        case 7 :
            return 31
        case 8 :
            return 31
        case 9 :
            return 30
        case 10 :
            return 31
        case 11 :
            return 30
        case 12 :
            return 31
        
#TODO: Define nextDay()
def nextDay(year,month,day):

    Days = daysInMonth(year,month)
    #TODO:logical Error When Days Of Feb Is more Than 28
    if (day<Days):
        return year,month,day+1
    else:
        if (month<12):
            return year,month+1,1
        else:
            return year+1,1,1

#TODO: Define isBeforeDate1()
def isBeforeDate1(Y1,M1,D1,Y2,M2,D2):
    if(Y2>Y1):
        return True
    elif(Y2==Y1):
        if(M2>M1):
            return True
        elif(M2==M1):
            if(D2>D1):
                return True
            else:
                return False
    else:
        return False

#TODO: Define durationCaluclator()
def durationCaluclator(Y1,M1,D1,Y2,M2,D2):


    assert not isBeforeDate1(Y2,M2,D2,Y1,M1,D1)
    daysInBetween= 0
    while(isBeforeDate1(Y1,M1,D1,Y2,M2,D2)):
        result =nextDay(Y1,M1,D1)
        daysInBetween +=1
        Y1 = int(result[0])
        M1 = int(result[1])
        D1 = int(result[2])
    return daysInBetween

def test (): 
    print("Case 1 : 2015, 1, 1, 2016, 1, 1")
    print("Case 1 : 2015, 1, 1, 2015, 1, 1")
    print("Case 1 : 2000, 1, 1, 2001, 1, 1")
    print("===============================")
    assert durationCaluclator(2015, 1, 1, 2016, 1, 1) ==365
    print("Test Case 1 => PASSED")
    assert durationCaluclator(2015, 1, 1, 2015, 1, 1) ==0
    print("Test Case 1 => PASSED")
    assert durationCaluclator(2000, 1, 1, 2001, 1, 1) ==366
    print("Test Case 1 => PASSED")
    print ("All Test Cases PASSED")




if __name__ == "__main__":
    test ()

