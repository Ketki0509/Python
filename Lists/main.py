# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    l = ["Ketki",26.3,True,None,'c',10]
    '''print(len(l))
    print(l[0])
    print(l[-1])
    #print(l[7])
    print(l[1:3])

    print(l[0:60:2])

    l1 = [10,20]
    print(l1+l)
    print(l * 3)

    l.append(10)
    print(l)
    l.insert(2,20)
    print(l)

# difference in append and extennd is append add list [1,1] as one item to list and extend add 2,2 as 2 items to list
    l.append([1,1])
    print(l)
    l.extend([2,2])
    print(l)

    l.remove(True)
    #l.remove("a") it gives an error as a not present in list
    print(l)
    l.remove(10)  #it only removes first occurence of 10
    print(l)

    l.pop() # it removes last item from list i.e -1
    print(l)
    l.pop(2) # it removes that index item i.e 20
    print(l)'''
    l1 = [6,3,-1,3,0]
    l.reverse()
    print(l)
    l1.sort()
    print(l1)
    l1.sort(reverse=True)
    print(l1)

    c = l1.count(6)
    print(c)

    l=[10,-2,1,3,9]
    l.sort()
    print(l)

    print(False in l)
    print(min(l))
    print(max(l))
    print(sum(l))

    l1 = [1,2,3,8,[1,6,2],[2,4],[2,0,9,1,[0,1]]]
    print(l1[6][4][0])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
