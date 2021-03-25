arr = [1,2,3,4,5,1,2,3,2,2,2,4,3, 7, 1, 2]
firstarr = []
secarr = []
temp = 0
i = 0
while i < len(arr):

    temp += arr[i]

    if temp < 7:
        firstarr.append(str(arr[i]))
        i += 1           
                                                                                                                            
    else:
        if arr[i] >= 7:
            i += 1
        else:
            secarr.append([firstarr])
            firstarr = []
            temp=0
    

secarr.append([firstarr])
print(arr)
print(secarr)






    