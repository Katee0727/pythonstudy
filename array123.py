def array123(nums):
    first = nums.index(1)
    if first >= 0:
        if nums.index(2) == first+1:
            if nums.index(3) == first+2:
                return True
        else:
            first = nums.index(1,first+1)
    return False


print array123([1,1,2,3,1])

