function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let minIndex = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[minIndex] > arr[j]) {
        let temp = arr[minIndex];
        arr[minIndex] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr;
}

const customList = [2, 1, 7, 6, 5, 3, 4, 9, 8];

console.log(selectionSort(customList));
console.log(customList);
