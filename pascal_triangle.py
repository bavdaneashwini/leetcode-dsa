numRows = 5
Output= [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


#python function to generate pascal triangle

def generate_triangle(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

ans = generate_triangle(numRows)
print(ans)


#ruby function to generate pascal triangle
def generate_triangle(numRows)
  triangle = []
  (0...numRows).each do |i|
    row = Array.new(i + 1, 1)
    (1...i).each do |j|
      row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    end
    triangle << row
  end
  triangle
end
