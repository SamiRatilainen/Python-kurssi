def sum_list(nums: list[int]) -> int:
    s = 0
    for n in nums:
        s += n
    return s

lst = [3, 7, -2, 10, 5]
print(sum_list(lst))