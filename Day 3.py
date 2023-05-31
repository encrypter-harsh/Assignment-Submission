Write a Python to count number of odd and even number from the series of the list:

a=[ 2,3,4,55,56,78,75,69,66,101,100 ]
def c_odd(list1):
  count=0
  for i in list1:
    if i % 2!=0:
      count+=1
  return count
def c_event(list1):
  count=0
  for i in list1:
    if i % 2==0:
      count+=1
  return count
odd=c_odd(a)
even=c_even(a)
print("The odd and even numbers in the list are",odd,"and",even) 
