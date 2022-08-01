def linearSearch(list , n ,ele):
       for i in range(0 , n):
           if list[i] == ele:
               return i
   
       return -1
   list = [1, 2 , 5 , 10 , 22]
   ele = int(input())
   n = len(list)
  res = linearSearch(list , n , ele)
  if (res == -1):
      print("Element not found")
  else:
      print("Element found at ", res) 
