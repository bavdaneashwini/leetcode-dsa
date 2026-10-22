
s = "ab#c"
t = "ad#c"
#Python function to compare strings after applying backspaces

def backspace_compare(s, t):
    def compare(word):
        stack = []
        for char in word:
            if char== "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
    return compare(s) == compare(t)

ans = backspace_compare(s, t)
print(ans)


#Ruby function to compare strings after applying backspaces

def backspace_compare(s, t)
    def compare(word)
        stack = []
        word.each_char do |char|
        if char == "#"
            if stack.any?
                stack.pop
            end
        else
            stack << char
        end
        stack.join
    end
    
    compare(s) == compare(t)
end