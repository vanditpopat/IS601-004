# a = [3,6,7,10,9,13,12,15,23]
# total = 0
# for i in a:
#      total+=float(i)

# # total = round(total,2)
# print("Total/Sum = " "% .2f" % total)
# # print(f"Sum/Total = {total}")
a1 = [10.001, 11.591, 0.011, 5.991, 16.121, 0.131, 100.981, 1.001]
a2 = [1.99, 1.99, 0.99, 1.99, 0.99, 1.99, 0.99, 0.99]
a3 = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
a4 = [10.01, -12.22, 0.23, 19.20, -5.13, 3.12]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    total = 0.00
    #UCID - vp645 Date 02/06/2022 - Total
    for i in arr:
        total +=i
    total = "%0.2f" % total
    print("\nThe total is {}:\n".format(total))


print("Problem 2")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)