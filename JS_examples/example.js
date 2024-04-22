// var msg = 'Hello World';
// console.log(msg);

// if (msg.startsWith('Hello')) {
//     console.log('The message starts with Hello');
// }

// let user = new Object();
// user.name = 'John';
// user.age = 25;
// user.isAdmin = true;

// alert(user.name + ' is ' + user.age + ' years old');
// delete user.age;
// console.log(user);


// let fruit = prompt('Which fruit to buy?', 'apple');
// let bag = {
//     [fruit]: 5,
// };
// console.log(bag);


// let user = {
//     name: "John",
//     age: 30,
//     isAdmin: true
//   };
  
//   for (key in user) {
//     // keys
//     alert( key );  // name, age, isAdmin
//     // values for the keys
//     alert( user[key] ); // John, 30, true
//   }

let user = {name: 'John', age: 30};
let admin = user;

admin.name = 'Pete';
alert(user.name); // Pete