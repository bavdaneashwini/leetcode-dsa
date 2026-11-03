s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# Python function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA string

def find_repeated_dna_sequences(s):
    seen = set()

    repeat_word = set()

    for i in range(len(s)-9):
        sub = s[i:i+10]
        
        if sub in seen:
            repeat_word.add(sub)
        else:
            seen.add(sub)

    return list(repeat_word )

ans = find_repeated_dna_sequences(s)
print(ans)


#Ruby function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA string


def find_repeated_dna_sequences(s)
    seen = Set.new

    repeat_word = Set.new

    (0..s.length - 10).each do |i|
        sub = s[i,10]
        if sub in seen:
        repeat_word.add(sub)
        else
            seen.add(sub)
        end
    end
    return repeat_word
end