/* Setting variables can be done in two ways*/
// var (For global variables)
// let (with let, you can re-assign values)
// const (You cannot re-assign values)

// let age = 25;
// console.log(age);

// Primitive Data types: Strings, Numbers, Boolean, null, undefined, Symbol

// const iden = "John";
// const years = 30;
// const isCool = true;
// const rating = 2.5;
// const x = null;
// const y = undefined;
// let z; The same as const z = undefined

// console.log(typeof years);  see the datatype


// // Concatenation
// const iden = "John";
// const years = 30;
// console.log("My name is " + iden + " and I am " + years + " years of age.");
// //Template literials
// console.log(`My name is ${iden} and I am ${years} years`);

// String properties
// const x = "Hello World";
// const y = "technology, computers, it, code"
// console.log(x.length);
// console.log(x.toUpperCase());
// console.log(x.substring(0, 5));
// console.log(y.split(','));


// // Arrays
// const num = new Array(1, 2, 3, 4, 5);
// console.log(num);
// const fruits = ["apples", "oranges", "pears"];

// // Adding values by assigning
// fruits[3] = "grapes";
// // Adding values to the end of the array
// fruits.push("mangoes");
// // Adding values to the beginning of the array
// fruits.unshift("Lemon");
// // Remove the last item of an array
// fruits.pop();
// To check if an array
// 


// Object literials - is more like key value pairs more like a python dictionary
// const person = {
//     firstName: "John",
//     lastName: "Doe",
//     age: 30,
//     hobbies: ["music", "movies", "sleeping"],
//     address: {
//         street: "50 main st",
//         city: "Boston",
//         state: "MA"
//     }
// };

// console.log(person);
// // Keys can be accessed using dot(.) syntax
// console.log(person.firstName, person.lastName);
// console.log(person.hobbies[1]);

// You can do destructuring and pull out keys from object literials into actual vaiables.
// const { lastName, firstName, address: {city} } = person;
// console.log(lastName, firstName, city);

// Properties can be added later
// person.email = "johndoe@gamil.com";
// console.log(person);



// // JSON - Javascript Object Notation
// const todos = [
//     {
//         id: 1,
//         text: "Take out trash",
//         isCompleted: true
//     },
//     {
//         id: 2,
//         text: "Meeting with boss",
//         isCompleted: true
//     },
//     {
//         id: 3,
//         text: "Dentist Appointment",
//         isCompleted: false
//     },
// ];

// console.log(todos);
// console.log(todos[1].text)

// // Converting to JSON
// const todosJSON = JSON.stringify(todos);
// console.log(todosJSON);


// // Loops
// For loop
// for(let i = 0; i <= 10; i++){
//     console.log(`For loop number: ${i}`);
// }

// // While loop
// let i = 0;
// while(i < 10){
//     console.log(`While loop number: ${i}`);
//     i++;
// }

// // // Loop through arrays
// // of
// for(let todo of todos){
//     console.log(todo.text);
// }

//forEach: loops through them

/*
SYNTAX:
 array_name.forEach(function(variable){
    //statements
    e.g. console.log(variable)
 });
*/

// todos.forEach(function(todo) {
//     console.log(todo.text);
// });

// map: allows to create a new array from an array
// const todoText = todos.map(function(todo) {
//     return todo.text;
// });
// console.log(todoText);

// filter: allows to create a new array based on a condition
// const todoCompleted = todos.filter(function(todo) {
//     return todo.isCompleted === true;
// });


// const todoCompletedText = todos.filter(function(todo) {
//     return todo.isCompleted === true;
// }).map(function(todo){
//     return todo.text;
// });

// console.log(todoCompleted);


// // // Conditionals
// const x = 10;
// const y = 5;
// // == matches the value not the data type
//  if(x == 10){
//      console.log("x is 10");
//  }
//  else {
//      console.log("x is not 10");
//  }

// // === matches both the value and the data type
//  if(x === 10){
//     console.log("x is 10");
// }

// if (x > 5 || y === 10){
//     console.log("True condition");
// }


// /// Ternary operator: is a single line if statement. Used to set a variable based on a condition.

// const x  = 20;

// const color = x > 10 ? 'Red' : "Blue";

// console.log(color);


// Switches: Used to evaluate a condition
// switch(color) {
//     case 'Red':
//         console.log("Color is Red");
//         break;
//     case "Blue":
//         console.log("Color is Blue");
//         break;
//     default:
//         console.log("Color is not Red or Blue");
//         break;
// }


// // Functions
// function addNums(a = 1, b = 1) {
//     return a + b;
// }

// console.log(addNums(5, 5));

// /* Arrow function */
// const addNums = (a = 1, b = 1) => a + b;

// // const addNums = num1 => num1 + 5;

// console.log(addNums(5, 5));


/* OOP */
// Contructor Function
// function Person(firstName, lastName, dob) {
//     this.firstName = firstName;
//     this.lastName = lastName;
//     this.dob = new Date(dob);
// }
// // Prototyping is used to set constructors => recommended practice
// Person.prototype.getFullName = function(){
//     return `${this.firstName} ${this.lastName}`;
// }

// // Instantiate object
// const person1 = new Person('John', 'Doe', '4-3-1980');
// const person2 = new Person('Mary', 'Smith', '4-3-1890');

// console.log(person1.getFullName());
// console.log(person1);


/* Syntantic sugar OOP */
// // Class
// class Person {
//     constructor(firstName, lastName, dob) {
//     this.firstName = firstName;
//     this.lastName = lastName;
//     this.dob = new Date(dob);
//     }

//     getFullName(){
//         return `${this.firstName} ${this.lastName}`;
//     }
// }

// // Instantiate object
// const person1 = new Person('John', 'Doe', '4-3-1980');
// const person2 = new Person('Mary', 'Smith', '4-3-1890');

// console.log(person1.getFullName());
// console.log(person1);


/* DOM => Document Object Module */
// console.log(window);  //To see all objects in the window

// // Single element
// console.log(document.getElementById("my-form"));
// console.log(document.querySelector("h1"));

// // Multiple element
// console.log(document.querySelectorAll(".item"));
// console.log(document.getElementsByClassName("form-floating"));
// console.log(document.getElementsByTagName("label"));

// const ul = document.querySelector(".items");

// ul.remove();
// ul.lastElementChild.remove();
// ul.firstElementChild.textContent = "Hello";
// ul.children[1].innerText = "Brad";
// ul.lastElementChild.innerHTML = "<h4>Hello</h4>";

// const btn = document.querySelector(".btn");
// btn.style.background = 'red';

// /* events */
// const btn = document.querySelector(".btn");

// btn.addEventListener('mouseout', (e) => {
//     e.preventDefault();
//     document.querySelector("#my-form").style.background = '#ccc';
//     document.querySelector("body").style.background = "#000";
//     document.querySelector("body").style.color = "#fff";
//     ul.lastElementChild.innerHTML = "<h1>Hello</h1>"
// });

// ------------------------------------------------------------------------


// Form handling test
// const myForm = document.querySelector("#my-form");
// const nameInput = document.querySelector("#name");
// const emailInput = document.querySelector("#email");
// const msg = document.querySelector(".msg");
// const userList = document.querySelector("#users");


// myForm.addEventListener("submit", onsubmit);

// function onsubmit(e) {
//     e.preventDefault();
//     if(nameInput.value === "" || emailInput.value === ""){
//         msg.innerHTML = "Please enter all fields!";
//         setTimeout(() => msg.remove(), 3000);
//     }
//     else {
//         const li = document.createElement("li");
//         li.appendChild(document.createTextNode(`${nameInput.value}: ${emailInput.value}`));

//         userList.appendChild(li);

//         //Clear fields
//         nameInput.value = "";
//         emailInput.value = "";
//     }
// }



/* Lookup MDN documentation */





