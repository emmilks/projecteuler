with open('euler13.txt', 'r') as f:
    nums = [int(line) for line in f]

sum_nums = str(sum(nums))
print(sum_nums[0:10])
