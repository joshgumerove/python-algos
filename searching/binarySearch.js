function binarySearch(arr, val) {
  let start = 0;
  let end = arr.length - 1;
  middle = Math.floor((start + end) / 2);

  while (arr[middle] !== val && start <= middle) {
    if (val < arr[middle]) {
      end = middle - 1;
    } else {
      start = middle + 1;
    }
    middle = Math.floor((start + end) / 2);
  }

  if (arr[middle] === val) {
    return middle;
  }

  return -1;
}

let sortedArr = [2, 3, 19, 23, 25, 27];
console.log(binarySearch(sortedArr, 19));
console.log(binarySearch(sortedArr, 25));
console.log(binarySearch(sortedArr, 50));
