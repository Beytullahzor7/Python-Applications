filter(lambda x : x % 2 == 0,[1,2,3,4,5])

list(filter(lambda x : x % 2 == 0,[1,2,3,4,5]))

print(list(filter(lambda x : x % 2 == 0,[1,2,3,4,5])))

#######################################################

def asal_mi(x):

    i=2

    if (x == 1):
        return False
    elif (x == 2):
        return True
    else:

        while (i<x):

            if(x%i==0):
                return False

            i+=1

        return True

list(filter(asal_mi,range(1,100)))
print(list(filter(asal_mi,range(1,100))))

