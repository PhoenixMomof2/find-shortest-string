function findShortestString(arr) {
  // map through the array and note the length of each string at each index
    let idx = 0
    let min_length = arr[0].length
  
  for (i = 0; i < arr.length; i++) {
    if (arr[i].length < min_length) {
      min_length = arr[i]
      idx = i
    }
  }
  return arr[idx]
}

if (require.main === module) {
  // add your own tests in here
  console.log("Expecting: 'a'");
  console.log("=>", findShortestString(['aaa', 'a', 'bb', 'ccc']));

  console.log("");

  console.log("Expecting: 'hi'");
  console.log("=>", findShortestString(['cat', 'hi', 'dog', 'an']));

  console.log("");

  console.log("Expecting: 'lily'");
  console.log("=>", findShortestString(['flower', 'juniper', 'lily', 'dadelion']));

  // BENCHMARK HERE
}

module.exports = findShortestString;

// Please add your pseudocode to this file
// And a written explanation of your solution
