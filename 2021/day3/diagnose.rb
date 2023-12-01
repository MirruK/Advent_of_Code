# Array to keep count of number of ones in each column
counts = Array.new(12) { |_| 0 }

num_lines = 0

# Read lines from standard input until EOF (Ctrl+D on Linux)
while line = gets
  line.chomp.chars().each_with_index { |value, index| counts[index] += value.to_i()}
  num_lines += 1
end

bin_array = counts.map { |val| (val.to_f()/num_lines >= 0.5) && 1 || 0 }
bin_value = (bin_array.reverse().each_with_index.map {|value, index| (2**index)*value}).sum()
puts bin_value * (bin_value ^ 0b111111111111)

