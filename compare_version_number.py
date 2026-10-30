version1 = "1.2"
version2 = "1.10"

#Python function to compare version numbers

def comapare_version(version1,version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    
    n = max(len(v1),len(v2))

    for i in range(n):
        num1 = int(v1[i]) if i < len(v1) else 0
        num2 = int(v2[i]) if i < len(v2) else 0

        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
    return 0

ans = comapare_version(version1,version2)
print(ans)


#Ruby function to compare version numbers

def compare_version(version1, version2)
    v1 = version1.split('.')
    v2 = version2.split('.')
    n = [v1.length, v2.length].max
    
    (0...n).each do |i|
        num1 = i <v1.length.to_i ? v1[i] : 0
        num2 = i <v2.length.to_i ? v2[i] : 0
    
        if num1 > num2
            return 1
        elsif num1 < num2
            return -1
        end
    end
    return 0
end


note -> to convert string to integer in ruby we can use .to_i method