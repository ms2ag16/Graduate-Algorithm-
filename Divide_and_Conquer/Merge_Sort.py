
def MergeSort(data):
    if len(data)>1:
        leftList=MergeSort(data[:len(data)/2])
        rightList=MergeSort(data[len(data)/2:])
        return merge(leftList, rightList)
    else:
        return data

def merge(leftList, rightList):
    result,i,j=[],0,0

    for k in range(len(leftList)+len(rightList)):
          if i <len(leftList) and j <len(rightList):
              if leftList[i]<=rightList[j]:
                  result.append(leftList[i])
                  i+=1
              else:
                  result.append(rightList[j])
                  j+=1
          else:
              result.append(leftList[i] if i <len(leftList) else rightList[j])
              i+=1
              j+=1
    #print result
    return result

if __name__=='__main__':
     result=MergeSort([2,4,7,5,9,8,1,3,6])
     print result
