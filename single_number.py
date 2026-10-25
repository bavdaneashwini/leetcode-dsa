nums = [3,4,7,3,4]

#Python function to find the single number in an array

def single_number(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num in count:
        if count[num] == 1:
            return num

ans = single_number(nums)   
print(ans)

def single_number_xor(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

ans = single_number_xor(nums)
print(ans)

#Ruby function to find the single number in an array

def single_number(nums)
    count = Hash.new(0)
    
    nums.each do |num|
        if !count[num]
            count[num] = 0
        end
        count[num] += 1
    end

    count.each do |key,val|
        if val == 1
            return key
        end
    end
end

nums = [3,4,5,5,4]
ans = single_number(nums)
puts ans