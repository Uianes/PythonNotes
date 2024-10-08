def simple_search(list, item):
    for index in range(len(list)):
        if list[index] == item:
            return index 
    return None 

if __name__ == "__main__":
    list = [1, 3, 5, 7, 9]
    print(simple_search(list, 3))
