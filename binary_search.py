


#Function takes in array, length, position
def binary_sort(sortedlist,n,x):
 #loop initiated to 0
 start = 0
 #loop is equal to n length 
 end = n 

 while(start <= end):
  mid = (start + end)/2 #creating mid-point of list
  if (x == sortedlist[mid]): #if x is equal to middle number in list, return it
   return mid
  elif(x < sortedlist[mid]): #subtract binary -1 from middle point in list
   end = mid - 1 #now end becomes middle number - 1, fulfilling its destiny of a binary search
  else:
   start = mid + 1 #add binary +1 to mid number, next iteration loop is halved and starts from binary mid position
 
   return -1 #returns an error message if number is not found

n = input("Enter the size of the list: ") #determine length of list

sortedlist = [] #before appending to array, we initialize it

for i in range(n):
 sortedlist.append(input("Enter %dth element: "%i)) #Each interated number is appended into sortedlist array

x = input("Enter the number to search: ") #x is momentarily stored in memory 
position = binary_sort(sortedlist, n, x)#faster way of comparing function, assigning it to position

if(position != -1): #if number is present
 print("Entered number %d is present at position: %d"%(x,position))#index is found
else:
 print("Entered number %d is not present in the list"%x)
 

 
