input = "ABB"


# Python function to convert excel sheet column number to title

def excel_sheet_colun_number(input):
    result = 0

    for char in input:
        result = result * 26 + (ord(char) - ord('A') +1)
    return result

ans = excel_sheet_colun_number(input)
print(ans)


# Ruby function to convert excel sheet column number to title

def excel_sheet_colun_number(input)
    result = 0 
    input.each_char do |char|
        result = result * 26 + (char.ord - 'A'.ord + 1)
    end

end