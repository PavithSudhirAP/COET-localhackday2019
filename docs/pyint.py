def printint(x):
  if x==1:
    print("1")
  else:
    print(x)
    printint(x-1)
    
printint(10)
