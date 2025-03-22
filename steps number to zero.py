def numberOfSteps(count:int, num: int):
        if num == 0:
            return count
        
        if(num % 2 == 0):
            count += 1
            return numberOfSteps(count,num//2)

        else:
            count +=1
            return numberOfSteps(count,num - 1)
        return count


count = 0
print(numberOfSteps(count,14))
print(numberOfSteps(count,3))
print(numberOfSteps(count,20))
print(numberOfSteps(count,50))
print(numberOfSteps(count,123))
print(numberOfSteps(count,1023))
