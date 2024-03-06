var prompt = require("prompt-sync")();

let n1 = parseInt(prompt("Please enter your first number: "));
let n2 = parseInt(prompt("Please enter your second number: "));
let operator = prompt("Please enter your operator (+, -, *, /): ");

if (operator === "+") {
  console.log(`The answer of ${n1} ${operator} ${n2} = ${n1 + n2}`);
} else if (operator === "-") {
  console.log(`The answer of ${n1} ${operator} ${n2} = ${n1 - n2}`);
} else if (operator === "*") {
  console.log(`The answer of ${n1} ${operator} ${n2} = ${n1 * n2}`);
} else if (operator === "/") {
  console.log(`The answer of ${n1} ${operator} ${n2} = ${n1 / n2}`);
} else {
  console.log("Please select the correct operator");
}

export {}