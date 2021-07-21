// console.log("Hello World!");
// document.write("Hello World!");

/* ARRAYS */

// let cars = ["BMW", "Volvo", "Honda"];
// console.log(cars);

/* iterates through array */
// cars.forEach((item, index, array) => (console.log(item, index)));

/* toString() converts an array into a string */
// console.log(cars.toString())

/* pop() removes the last element in an array */
/* push("new element") adds a new element at the end of an array */
/* shift() removes the first element in an array */
/* unshift("element") adds an element at the beginning of an array */

/* concat() creates a new array by merging existing arrays */
// let bikes = ["haha", "toy", "food"];
// let vech = cars.concat(bikes);
// console.log(vech);

/* sort() sort an array in ascending order */
/* reverse() reverses the elements of an array */


// MAP, REDUCE & FILTER 
/* The map() method creates a new array and performs a function on each array element */
// let num1 = [2, 3, 4];

// function multiply(val){
//     return val * 2;
// }

// let num2 = num1.map(multiply);
// console.log(num2);

/* The filter() method takes each element in an array and it applies a conditional statement against it */
// function even(val){
//     return val % 2 == 0;
// }

// let num2 = num1.filter(even);
// console.log(num2);

/* reduce() method reduces an array of values down to just one value using a function */
// function sum(total, val){
//     return total + val;
// }

// let num2 = num1.reduce(sum);
// console.log(num2);


/* LOOPS */
//For loops
// for(x=0; x<5; x++){
//     console.log(x);
// }

//While loops
// let x = 0;
// while(x<=5){
//     console.log(x);
//     x++;
// }

//Do-while loop
// let x = 5;
// do{
//     console.log(x);
//     x++
// }
// while(x<10)


/* OBJECTS */
// const student = {
//     name: "Chris",
//     age: 21,
//     studies: "Computer Science",
// };

// document.getElementById("demo").innerHTML = `${student.name} is ${student.age}yrs of age and he studies ${student.studies}.`;

// const stu = new Object();
// stu.name = "Chris";
// stu.studies = "Computer Science";
// stu.age = 21;

// document.getElementById("demo").innerHTML = `${stu.name} is ${stu.age}yrs of age and he studies ${stu.studies}.`;

// function student(name, age, study){
//     this.name = name;
//     this.age = age;
//     this.study = study;
// }

// const cate = new student("Chris", 21, "Computer");
// console.log(cate);


// /* getters and setters */
// var car = {
//     name: "BMW",
//     color: "Navy Blue",
//     fuel_type: "Diesel",
//     // set fuel(fuel){
//     //     this.fuel_type = fuel;
//     // }
//     // get fuel(){
//     //     treturn this.fuel_type;
//     // }
// };

// car.fuel_type = "Petrol";
// console.log(car.fuel_type);

/* FUNCTIONS */
// let x = function(val){ return val * val; };
// console.log(x(5));

// //Function constructor
// var myfunction = new Function("a", "b", "return a + b");
// console.log(myfunction(5, 20));

//Self-invoking functions: they are invoked automatically without being called. 
//Syntax:
//  (function() {
//          function_body   //It calls itself
//    })();

// (function() {
//     console.log(5+8);
// })();


//arrow functions
//note: they are not recommended for use as methods and constructors. 
// const myfunc = (a, b, c) => {return a*b*c};
// console.log(myfunc(2,3,4));


/* Predefined functions */
// eval: evaluates a string and returns a value
// parseInt: parses a string arguement and returns an integer of the specified radix or base.
// parseFloat: parses a string arguement and returns a float.
// escape: returns the hexadecimal encoding of an arguement. 
// unescape: Returns the ASCII string for a specified value.

/****************************************/

/* CLOSURES */
// is a feature where an inner function has access to the outer function's variables. 
// A closure has three scope chains. 
// Has access to variables its own scope, outer functions and global variables. 
// A scope chain is a stack consisting of all the references to the variables for the function being executed. 

// let a = 10;
// function first(){
//     let b = 20;
//     function second(){
//         let c = 20 + a + b;
//         return c;
//     }
//     return second()
// }

// let sum = first();
// console.log(`The sum is ${sum}`);


/* PROMISES */
// A promise is an asynchronous action that may complete at some point in the future and produce a value. 
// Promises has 3 states: pending, fulfilled and rejected. 
// General syntax:
// let some_action = new Promise(function(resolve, reject){
//  //perform some work
// })
// let car = new Promise(function(resolve, reject){
//     fuel_fullTank = true;
//     if(fuel_fullTank){
//         resolve();
//     }
//     else{
//         reject();
//     }
// });

// car.then(function(){
//     console.log("The fuel tank is full");
// });

// car.catch(function(){
//     console.log("The fuel tank is empty")
// });


// //nested promises
// let empty_tank = function(){
//     return new Promise(function(resolve, reject){
//         resolve("The car doesn't have enough fuel.");
//     });
// }

// let hot_engine = function(msg){
//     return new Promise(function(resolve, reject){
//         resolve( msg + "The engine is overheating.");
//     });
// }

// let travel = function(msg){
//     return new Promise(function(resolve, reject){
//         resolve(msg + "The car is not safe for travelling.");
//     });
// }


// // The message in the resolve can be retrieved from the result param
// empty_tank().then(res => {
//     return hot_engine(res)
// }).then( res => {
//     return travel(res)
// }).then(res => {
//     return console.log(res)
// })



// // .then(function(result){
// //     return travel(result);
// // }).then(function(result){
// //     console.log("Done!" + result);
// // })


// let floor_state = function(num){
//     switch(num){
//         case 1:
//             return "Form 2";
//             break;
//         case 2:
//             return "Form 1";
//             break;
//         case "ground":
//             return "Form 3";
//             break;
//         default:
//             return "false";
//     }
// }


// let house_color = function(color){
//     switch(color){
//         case "red":
//             return "House 1";
//             break;
//         case "blue":
//             return "House 2";
//             break;
//         case "yellow":
//             return "House 3";
//             break;
//         case "green":
//             return "House 4";
//             break;
//         default:
//             return "false";
//     }
// }


// let state = function(floor, color){
//     if(floor_state(floor) == "false" || house_color(color) == "false" ){
//         console.log("House color or floor does not exist")
//     } else{
//         var result = `${floor_state(floor)}, ${house_color(color)}`;
//     console.log(result);
//     }
// }

// state("ground", "red");


/* ASync & Await */
// // They are built on top of promises. 
// Genereal Syntax:
// async function func_name(){
//     await some_promsise();
// }

// let result = function (score) {
//     return new Promise(function (resolve, reject) {
//         console.log("Calculating results...")
//         if (score > 50) {
//             resolve("congratulations! You passed")
//         } else if(typeof score != "number"){
//             reject("Please enter a valid score")
//         }
//         else {
//             reject("You have failed")
//         }
//     })
// }

// let grade = function (response) {
//     return new Promise(function (resolve, reject) {
//         console.log("Calculating your grade...")
//         resolve("Your grade is A, " + response)
//     })
// }

// result(80).then(response => {
//     console.log("Results received")
//     return grade(response)
// }).then(final_grade => {
//     console.log(final_grade)
// }).catch(err => {
//     console.log(err)
// })


// //async declarations cannot be initialsed as an arrow function
// async function Calc() {
//     try{
//         const response = await result(80)
//         console.log("Results received")
//         const final_grade = await grade(response)
//         console.log(final_grade)
//     } catch(err){
//         console.log(err)
//     }
// }

// Calc()


/* THIS Keyword */
// 'this' keyword refers to an object which is executing the current piece of code. It references the object that is executing the current function. 
// // if the function being referenced is a regular function, 'this' references the global object.  
// var value = 100

// let func = () => {
//     let value = 50
//     console.log(`Function's value: ${value}`)
//     console.log((`Global value: ${this.value}`))
// }

// func()

// // If the function that is being referenced is a method in an object, 'this' references the object itself.
// const random = {
//     name: "John",
//     info(){
//         console.log(`My name is ${this.name}`)
//     }
// }

// random.info()



// const rand = {
//     name: "Tutorial",
//     video: ["JavaScript", "Python", "CSS"],
//     info(){
//         this.video.forEach(tag =>{
//             console.log(tag, this.name)
//         })
//     }
// }


// const rand = {
//     name: "Tutorial",
//     video: ["JavaScript", "Python", "CSS"],
//     info(){
//         this.video.forEach(function (tag){
//             console.log(tag, this.name)
//         }, this)
//     }
// }

// rand.info()


/** FORM VALIDATION */
// let validate = () => {
//     if(document.myform.Email.value == ""){
//         alert("Please provide your Email ID")
//         document.myform.Email.focus()
//         return false
//     } else if(document.myform.Password.value == ""){
//         alert("Please provide your Password")
//         document.myform.Password.focus()
//         return false
//     } else {
//         return true
//     }
// }


/* REGEX */
// A regular expression is a sequence of characters that forms a search pattern

// FLAGS specify the behavior of regular expressions 
// Some example:
// g - global - finds all matches instead of stopping at the first.
// i - ignore case - /[a-z]i is equivalent to /[a-zA-Z]/
// m - multiline - ^ and $ match the beginning and the end of each line respectively
// u - unicode 
// y - finds all consecutive adjacent matches

// PATTERNS are brackets used to find the range of characters. 
// [a-z] - Finds all characters from a to z (lowercase)
// [0-9] - Finds any digit berween 0 and 9
// [a-z|0-9] - Finds any character of digits separated by '|'

// QUANTIFIERS define the number of occurences in a string
// + - indicates one or more occurence of a character
// * - indicates zero or more occurences of a character
// ? - indicates zero or one occurence of a character 

// /^\(?(\d{3})\)/g


// const num = "(555)-555-1254"
// const regex = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/g
// const found = regex.test(num)

// if(!found){
//     console.log("Not valid!")
// } else{
//     console.log("Valid")
// }

/* EMAIL VALIDATION */
// const email = "dasorange@gmail.com"
// const regex = /^([a-zA-Z0-9\._]+)@([a-zA-Z0-9\._])+[com]$/g
// const found = regex.test(email)

// if(!found){
//     console.log("Not valid!")
// } else{
//     console.log("Valid")
// }


// ------------------------------------------------------------------------

