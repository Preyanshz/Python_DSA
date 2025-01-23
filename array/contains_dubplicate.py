def hasDuplicate(nums):
    count_dict = set()
    for i in nums:
        if i in count_dict:
            return True
        count_dict.add(i)
    return False

nums = map(int, input().split())
print(hasDuplicate(nums))