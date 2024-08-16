// let codes = {
//     "+49": "Germany",
//     "+41": "Switzerland",
//     "+44": "Great Britain",
//     // ..,
//     "+1": "USA",
//     Micheal: "Smith",
//     John: "Joe",
// };

// function isEmpty(obj) {
//     if (Object.keys(obj).length == 0) {
//         return true;
//     }
//     return false;
// }

// for (let code in codes) {
//     console.log(code); // 1, 41, 44, 49
// }

// class User {
//     constructor(name) {
//         this.name = name;
//     }
//     sayHi() {
//         console.log(this.name);
//     }
// }

// function User(name) {
//     this.name = name;
//     this.sayHi = function() {
//         console.log(this.name);
//     }
// }

let user = {name: "John"};

let permission1 = {canView: true};
let permission2 = {canEdit: true};

Object.assign(user, permission1, permission2);

let clone = structuredClone(user);

console.log(user);

function accessAllowed(user) {
    return user.age > 18;
}
