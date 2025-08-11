nums=[3,34,4,12,5,2]
target=16
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("true")
            break
    else:
        continue
    break
else:
    print("false")
                 

        
            


            
