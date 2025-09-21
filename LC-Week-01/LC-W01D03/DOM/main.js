// print
// method - .fun()
// string - txt
console.log("25-09-16 Tue");

// function - fun()
// sum(1,2)

// error
// letEatSomeFood('Rice')
// console.log(letEatSomeFood("Rice"));

// JS - camelCase
// this is the node = h1
const titleElement = document.getElementById("title");
// titleElement = "asdsad" =>  error
let sum1 = 1 + 2;
console.log("sum1");
console.log("1:", sum1);

// call teh name = new value
sum1 = 4;
console.log("2:", sum1);

console.log(titleElement);
// Function <=> method: name()
// varible <=> property: name

// need to see in the console wht the text inside h1
console.log(titleElement.textContent);

// change var you cant change var inside cons

titleElement.textContent = "Omar";

// getleme by id
//           document.getElementById("title");
const par1 = document.querySelector("#main-section p");
// HW: what  happened if CSS selector got two elements
console.log("par text:", par1.textContent);
console.log("par1:", par1);

// Happy
// property = newValue
// variables
par1.style.color = "blue";

// HW: Attributes VS property
// Tips: you need to excuse the right method
// Accessing/Modifying the Attributes of an Element
// https://git.generalassemb.ly/Jordan-Modee/js-dom-intro-lesson?tab=readme-ov-file#accessingmodifying-the-attributes-of-an-element
