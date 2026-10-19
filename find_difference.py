s = "abcd"
t = "abcdp"

#Python program to find the difference between two strings using XOR operation
def find_diff(s,t):
    result = 0
    for char in (s+t):
        result = result ^ ord(char)

    return chr(result)

ans = find_diff(s, t)
print(ans)

#Ruby program to find the difference between two strings using XOR operation
def find_diff(s, t)
    result = 0
    (s+t).each_char do|char|
        result = result ^ char.ord
    end
    return result.chr
end

puts find_diff(s, t)