def print_sum(nums):
    num_int = [int(num) for num in nums]
    print(sum(num_int))

numbers = input().split(" ")
print_sum(numbers)