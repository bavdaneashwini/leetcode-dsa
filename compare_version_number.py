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

#python two pointers approach to compare version numbers

def compare_version_two_pointers(version1,version2):
    i = 0
    j = 0
    n = len(version1)
    m = len(version2)
    

    while i <n or j < m:
        num1 = 0
        num2 = 0
        while i < n and version1[i] != '.':
            num1 = num1 * 10 + int(version1[i])
            i+=1
            
        while j < m and version2[j] != '.':
            num2 = num2 * 10 + int(version2[j])
            j+=1
            
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        i+=1
        j+=1
    return 0

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