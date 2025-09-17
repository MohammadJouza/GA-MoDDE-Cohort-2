console.log("25-09-17");

/* C R U D */

//                   1 2 3 / variables
// element.onclick = func()

// [] () {}
//                   parameters <=> variables

const num3 = 3;
// variable   objName.property
// func()     objName.methodName()
// console.log("line 20:", num3);

// sum(3, 4);
// sum(5, 2);

// inside the func - sum
//  executed
// console.log(1);
// console.log(2);
// console.log(3);

// console.log("X:", x);
// console.log("Y:", y);

// ===================

const sum = function (x, y) {
  console.log("THE FUNC SUM GOT CALLED / EXECUTED");
  // console.log("X:", x, "Y:", y);
};

// I need to select the 'btn' using 'id' via CSS selector 'btn-1'

// check that we selected correct
// console.log("BTN", myButton);
// console.dir('BTN',myButton)

// add event type 'click' to my 'btn' and attached the func 'sum'
// node.method(eventName, func = callbackFunc)
// myButton.addEventListener("click", sum);

console.clear();

// Global Scope
const myButton = document.querySelector("#btn-1");
console.log("BTN", myButton);
//
const input1 = document.querySelector("#input-text");
const ul1 = document.querySelector("#comments-section ul");
//                                   anonyms function
myButton.addEventListener("click", function () {
  console.log(1);
  console.log(2);

  const newListItem = document.createElement("li");

  newListItem.textContent = input1.value;

  ul1.appendChild(newListItem);

  // var = newValue
  // obj.prop = newValue
  input1.value = "";
});
/*
myButton.addEventListener("click", function () {
  console.log(1);
  console.log(2);

  // STEP 1 : add the comments - 2 (get the text inside the input)
  // 1.1 Select input
  //             document.getElementById("input-text");
  // const input1 = document.querySelector("#input-text");
  // 1.2 check
  // console.log(input1);
  // 1.3 get the text inside the input
  //// DONE T= 'bla bla bla'
  // console.log("VALUE:", input1.value);
  // concept => objName.propertyName
  // answer =>         input1.value

// STEP 2: create an 'li' element inside 'ul'
// 2.1 create li
const newListItem = document.createElement("li");
// console.log("75:", newListItem);
// <li></li>

// 2.2 li - text (the comment - 2 = > T)
// obj.textContent    property method()
newListItem.textContent = "yup yup";
// <li> yup yup </li>

// 2.3 insert 'li' inside the ul
//// select li
// select 'ul'
// const ul1 = document.querySelector("#comments-section ul");
// console.log(ul1)

// not defined
// console.log(first());
// console.log(sec);

// 30 JD  => withdraw 50 JD

// insert 'li' inside the ul
// parentNode.appendChild( chidNode )
ul1.appendChild( newListItem )

});
*/

// Yanal => Hamza => Salsabel = > Qusi

//
/* 
Order to 

1. Read Event Obj
target
add 2 buttons <=> function
different target

2. read a little a bit about 'THIS'

3. Try - Removing Event Listeners

4. Part 2: Tasks  S1+2+3
4+5+6

5. Lab - Advanced => one button with each Todo item - so you can delete
 
6. Further Study - Event Bubbling + Event Delegation

 */
