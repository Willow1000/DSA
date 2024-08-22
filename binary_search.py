def binary_search(list,target):
    first=0
    last=len(list)-1

    while first<=last:
        m=round((first+last)/2)
        if list[m]>target:
            last-=1
        elif list[m]<target:
            first+=1
        else:
            return m
    return None

items=[1,2,3,8,9,int(0)]
ans=binary_search(items,0)

print(ans)


