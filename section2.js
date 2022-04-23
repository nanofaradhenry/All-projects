// variables and operators for javascript

alert("Welcome to section2");
// test and introductory code
console.log("Welcome to the program");
console.log("calculating", 23 + 4);

//test and introductory code 



let continent = (true);
console.log(typeof (continent))
/// type of allows you to find what type of element a certain script is
let man = ('person');
console.log(typeof (man));
console.log(man);
// you can also add a , in order to display multiple values
const yourage = 2057 - 1999;
const theirage = 2057 - 2002;
console.log(yourage, theirage);
// const variables are never changed
// let variables can be changed
console.log(yourage + 2, theirage / 3, yourage ** 2);
// ** allows you to represent an exponent
// example yourage ** 2 is yourage to the power of 2


//to create a space between strings
const banker = ('mr.curtis');
const officer = ('mr.brown');
console.log(banker + ' ' + officer);

// simplifying operators
let x = (10 + 5); // will give 15
x += (5); // will give 20 without having to do x= x+5
// will now print welcome to program
x = ('welcome to program')
console.log(x)

const fireman = ('Sr.Benjamin');
const pilot = ('Mr.Robinson')
console.log('Officials' + ' ' + fireman + ' ' + 'and' + '  ' + pilot);


/// assignment operators

let b = 25;// b is 25
console.log(b)
b += 10; // b is 35
console.log(b)
b *= 4;// b is 35 *4 ( 140)
console.log(b)
b--; // -- will subtract 1 from b ; now 139 
console.log(b)
b--; // -- will subtract 1 from b; now 138
console.log(b)

//comparison operators ( true or false )
//boolean values can either be true or false
// examples < , > , >= , <=  
let agehenry = (5);
let agetobias = (10);

console.log(agehenry > agetobias); // will print false
console.log(agetobias <= 4); // will print false 
console.log(agetobias >= 4); // will print true

//operator precedence


const currentyear = (2022);

const joesbday = (1995);
const mariesbday = (2002);
// the function that will precede will be either addition or subtraction whichever is first, left to right
console.log(currentyear - joesbday > currentyear - mariesbday);//should print true


// defining two variables

let zee, quu = (99); // will show 99 for both 
console.log(zee, quu);

//
x = y = 25 - 10 - 5;
console.log(x, y) //console will show 10 10 ; because x and y both equal 10


// average age

const theyear = (2022);
const MikesAge = (theyear - 1997);
const NigelsAge= (theyear - 2002);
const average=((MikesAge + NigelsAge) /2);// parenthesis inside ensure both variables run before division occurs

console.log(MikesAge , NigelsAge , average); // should print two ages and an average