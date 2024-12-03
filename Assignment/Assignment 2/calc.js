const inputArea = document.getElementById("calc-val");
const calcMax = document.getElementById("calc-max");
const calcMin = document.getElementById("calc-min");
const calcSum = document.getElementById("calc-sum");
const calcAvg = document.getElementById("calc-avg");
const calcRev = document.getElementById("calc-rev");

function calculator() {
    var inputVal = inputArea.value;
    var handle = inputVal.split(",");
    console.log(handle);
  
    sum(handle);
    maxN(handle);
    minN(handle);
    avg(handle);
    var rev = handle.reverse();
    calcRev.textContent = `${rev}`;
    }


function sum(arr){
  var sum = 0;
  for (p=0; p<arr.length; p++){
      n = parseInt(arr[p]);
      console.log(n);
      if (n==arr[p]){
        if (!isNaN(n)){
          sum += n;
          calcSum.textContent = sum;
      } 
    }

  }
  return sum;
}


function maxN(arr){
  var max = Number.NEGATIVE_INFINITY;
  for (p=0; p<arr.length; p++){
    n = parseInt(arr[p]);
    if (max<n) {
      max = n;
      calcMax.textContent = max;
    }
  }
}


function minN(arr){
  var min = Number.POSITIVE_INFINITY;
  for (p=0; p<arr.length; p++){
    n = parseInt(arr[p]);
    if (min>n) {
      min = n;
      calcMin.textContent = min;
    }
  }
}


function avg(arr){
  var sum = 0;
  var len = 0;
  for (p=0; p<arr.length; p++){
    n = parseInt(arr[p]);
    if (!isNaN(n)){
      sum += n;
      len+=1;
      calcAvg.textContent = sum/len;
    } 
  }
}

inputArea.addEventListener("input", calculator);