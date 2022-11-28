lst = input("Enter a list: ")
ele = input("Enter the element: ")
lst = [n for n in lst.split(",")]

if ele in lst:
    print(f"{ele} is in the list at the index of {lst.index(ele)}")
else:
    print(f"{ele} is not in the list")