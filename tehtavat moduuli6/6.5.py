def remove_odds(nums: list[int]) -> list[int]:
    return [n for n in nums if n % 2 == 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = remove_odds(lst)
print(lst)
print(filtered)