words = ["Hello","Alaska","Dad","Peace"]

#Python program to find words that can be typed using letters of alphabet on only one row's of American keyboard

def same_line_words(words):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    
    ans = []
    for word in words:
        lower_case_word = word.lower()
        
        valid = True
        for ch in lower_case_word:
            if ch not in row1:
                valid = False
                break
        if valid:
            ans.append(word)
            continue

        valid = True
        for ch in lower_case_word:
            if ch not in row2:
                valid = False
                break
        if valid:
            ans.append(word)
            continue

        valid = True
        for ch in lower_case_word:
            if ch  not in row3:
                valid = False
                break
        if valid:
            ans.append(word)
            continue
            
    return ans

ans = same_line_words(words)
print(ans)


    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []
        
        def check(word,row):
            for ch in word.lower():
                if ch not in row:
                    return False
            return True
        
        for word in words:
            if check(word,row1):
                ans.append(word)
            elif check(word,row2):
                ans.append(word)
            elif check(word,row3):
                ans.append(word)
        return ans

#Ruby program to find words that can be typed using letters of alphabet on only one row's of American keyboard


def same_line_word(words)

    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"

    ans = []

    words.each do |word|
        new_word = word.downcase

        valid = true
        new_word.each_char do|ch|
            if !row1.include?(ch)
                valid = false
                break
            end
        end
        if valid
            ans << word
            next
        end

        valid = true
        new_word.each_char do|ch|
            if !row2.include?(ch)
                valid = false
                break
            end
        end
        if valid
            ans << word
            next
        end

        valid = true
        new_word.each_char do|ch|
            if !row3.include?(ch)
                valid = false
                break
            end
        end
        if valid
            ans << word
            next
        end
    end
    ans
end

words = ["Hello","Alaska","Dad","Peace"]



ans = same_line_word(words)
puts ans.inspect


def check(word, row)
  word.downcase.each_char do |ch|
    if !row.include?(ch)
      return false
    end
  end

  return true
end

def find_words(words)
  row1 = "qwertyuiop"
  row2 = "asdfghjkl"
  row3 = "zxcvbnm"

  ans = []

  words.each do |word|
    if check(word, row1)
      ans << word
    elsif check(word, row2)
      ans << word
    elsif check(word, row3)
      ans << word
    end
  end

  return ans
end

words = ["Hello", "Alaska", "Dad", "Peace"]

ans = find_words(words)
puts ans.inspect