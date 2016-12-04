def find_missing(List1, List2):
  List1 = set(List1) #Convert list to set
  List2 = set(List2)  #Convert list to set
  if List1 != List2:  #compare the 2 sets
    finallist = list(List2 - List1)
    for i in finallist:
      return i
  else:
    return 0
