const inputArea = document.getElementById("calc-val");
const calcMax = document.getElementById("calc-max");
const calcMin = document.getElementById("calc-min");
const calcSum = document.getElementById("calc-sum");
const calcAvg = document.getElementById("calc-avg");
const calcRev = document.getElementById("calc-rev");

function calculator() {
    var inputVal = inputArea.value;
    var handle = inputVal.split(",");
    // console.log(handle);
    calcMax.textContent = `${Math.max(...handle)}`;
    calcMin.textContent = `${Math.min(...handle)}`;
    var sum = 0;
    var i = 0;
    handle.forEach( num => {
        sum += parseInt(num);
        i += 1;
      })
    calcSum.textContent = `${sum}`;
    calcAvg.textContent = `${sum/i}`
    var rev = handle.reverse();
    calcRev.textContent = `${rev}`;
}

inputArea.addEventListener("input", calculator);