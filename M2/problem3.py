a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    x =[]
    #UCID - vp645 Date 02/06/2022 - Positive change value
    for i in arr:
        if type(i) == str:
            i = abs(int(i))
            x.append(str(i))
        else:
            x.append(abs(i))
    [print(f"{i} {type(i)}") for i in x]



print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
