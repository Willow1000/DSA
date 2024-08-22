def merge_sort(list):
    if len(list)<=1:
        return list
    leftSide,rightSide=split(list)    
    left=merge_sort(leftSide)
    right=merge_sort(rightSide)

    return merge(left,right)
def split(list):
    m=len(list)//2
    return list[:m],list[m:]

def merge(left,right):
    i=0
    j=0
    l=[]

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])    
            j+=1

    while i<len(left)        :
        l.append(left[i])
        i+=1
    while j<len(right)    :
        l.append(right[j])
        j+=1
    return l    
