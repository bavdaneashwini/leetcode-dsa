s = "asjdjbhbdhdsdjjdfcbfbj"


#Python approach not brute force 
def long_palin_substr(s):
    res = ""
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1] and len(sub)>len(res):
                res = sub
        
    return res

ans = long_palin_substr(s)
print(ans)

#Python approach brute force

#Ruby approach not brute force
def long_palin_substr(s)
  res = ""

  (0...s.length).each do |i|
    (i...s.length).each do |j|
      sub = s[i..j]

      if sub == sub.reverse && sub.length > res.length
        res = sub
      end
    end
  end

  res
end

s = "ashwinibavdane"
ans = long_palin_substr(s)
puts ans