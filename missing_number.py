def find_missing(List1, List2):
   extraList = []
   lesserList = []
   if len(List1) > len(List2): #compares the two lenghts for thr lists
       extraList = List1
       lesserList = List2
   else:
       extraList = List2
       lesserList = List1
   extraNumber = [x for x in extraList if x not in lesserList]
   if len(extraNumber) == 0:
       return 0
   return extraNumber.pop()