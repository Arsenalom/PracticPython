def statistics(*nums):
    if not nums: return
    print(f"Сумма: {sum(nums)}, Среднее: {sum(nums)/len(nums)}, "
          f"Max: {max(nums)}, Min: {min(nums)}, Кол-во: {len(nums)}")

statistics(5,8,3,9)
statistics(6,45,3,4,45,78)
statistics(3,2)