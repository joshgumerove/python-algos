function bubbleSort(customList) {
  for (let i = 0; i < customList.length - 1; i++) {
    for (let j = 0; j < customList.length - i - 1; j++) {
      if (customList[j] > customList[j + 1]) {
        let temp = customList[j];
        customList[j] = customList[j + 1];
        customList[j + 1] = temp;
      }
    }
  }
  console.log(customList);
}

let list1 = [2, 1, 7, 6, 5, 3, 4, 8];
let list2 = [2, 1, 8];

bubbleSort(list1);
bubbleSort(list2);
