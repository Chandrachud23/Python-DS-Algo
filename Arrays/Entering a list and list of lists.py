#Code for entering list

# For list of integers 
lst1 = []   
  
# For list of strings/chars 
lst2 = []   
  
lst1 = [int(item) for item in input("Enter the list items for num : ").split()] 
  
lst2 = [item for item in input("Enter the list items as words : ").split()] 
  
print(lst1) 
print(lst2)



# Entering a list of lists code

grid_len = int(input("Enter Grid Length: "))
lst = [[input("Enter number: ") for i in range(grid_len)] for j in range(grid_len)]
print(lst)
