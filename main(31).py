#Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)
