import random as r


def findbest(arr):
    """
    Uses the 37% algorithm to statistically find the best option between
    a series of numbers
    """

    if arr: #If the array is not empty

        #Look phase
        lookel = (len(arr)*37) // 100
        exp = arr[0]
        for n in arr[:lookel-1]:
            if n > exp:
                exp = n

        #Leap phase
        for n in arr[lookel-1:]:
            if n == arr[-1]:
                sel = n
            if n >= exp:
                sel = n
                break

        #Check phase
        c = 1
        for n in set(arr):
            if n > sel:
                c += 1
        print(f"the selected number is the {c} best option")
        return sel


    else:
        print("\nthe array is empty")


numlist = []
for n in range(1000):
    numlist.append(r.randint(1,1000))

sel = findbest(numlist)
print(numlist)
print(sel)
