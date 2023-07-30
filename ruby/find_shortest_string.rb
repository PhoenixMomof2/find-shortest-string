def find_shortest_string(arr)
  idx = 0
  min_length = arr[0].length

  arr.each_with_index do |str, i|
    if str.length < min_length
      min_length = str.length
      idx = i
    end
  end

  arr[idx]
end

# Test the function
input_array = ["apple", "banana", "kiwi", "orange"]
shortest_string = find_shortest_string(input_array)
puts shortest_string # Output: "kiwi"


if __FILE__ == $PROGRAM_NAME
  puts "Expecting: 'a'"
  puts "=>", find_shortest_string(['aaa', 'a', 'bb', 'ccc'])

  puts

  puts "Expecting: 'hi'"
  puts "=>", find_shortest_string(['cat', 'hi', 'dog', 'an'])

  puts

  puts "Expecting: 'lily'"
  puts "=>", find_shortest_string(['flower', 'juniper', 'lily', 'dadelion'])

  # Don't forget to add your own!

  # BENCHMARK HERE
end

# Please add your pseudocode to this file
# And a written explanation of your solution
