path = "/home/user/Documents/../Pictures"

#Python program to simplify a path in a Unix-style file system

def simplify_path(path):
    stack = []
    
    for p in path.split("/"):
        if p == " " or p == ".":
            continue
        elif p == "..":
            if stack:
                stack.pop()
                
        else:
            stack.append(p)
    
    return '/'.join(stack)

ans = simplify_path(path)
print(ans)


#Ruby program to simplify a path in a Unix-style file system

def simplify_path(path)
    stack = []

    path.split("/").each do |p|
        if p == "" || p == "."
            next
        elsif p == ".."
            if stack.any?
                stack.pop()
            end
        else
            stack << p
        end
    end
    "/" + stack.join("/")
    
end