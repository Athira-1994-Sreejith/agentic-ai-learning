point = (10,20)
print(len(point))
print(point[0])
print(point)



def min_max(num):
    return (min(num), max(num))

low,high = min_max([5, 10,15,20])
print(low,high)

tup_eg = ("Athira",31,"Bangalore")
print(tup_eg[0])  # Output: Athira