def find_n(x):
    left = 0
    right = 10**10
    while left < right:
        mid = (left + right) // 2
        if (3*mid**2)+(3*mid)+1 < x <= (3*(mid+1)**2)+(3*(mid+1))+1:
            return mid
        elif (3*mid**2)+(3*mid)+1 >= x:
            right = mid
        else:
            left = mid + 1
    return -1


print(find_n(int(input()))+2)
