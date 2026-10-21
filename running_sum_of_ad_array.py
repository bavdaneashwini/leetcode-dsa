nums = [1,2,6,5]

#Python function to find running sum of an array

def running_sum(nums):
        prefix_arr = [0] * len(nums)
        prefix_arr[0]=nums[0]
        for i in range(1,len(nums)):
            prefix_arr[i] = prefix_arr[i-1]+nums[i]
        return prefix_arr

ans = running_sum(nums)
print(ans)

def sum_num(nums):
    total = 0
    result = []
    for num in nums:
        total+=num
        result.append(total)
    return result

    
#Ruby function to find running sum of an array

def running_sum(nums)
  prefix_arr = Array.new(nums.length, 0)
  prefix_arr[0] = nums[0]

  (1...nums.length).each do |i|
    prefix_arr[i] = prefix_arr[i - 1] + nums[i]
  end

  prefix_arr
end

ans = running_sum(nums)
puts ans.inspect