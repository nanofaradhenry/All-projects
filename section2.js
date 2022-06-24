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

// multiplication practice
let ab=(5);
let bc=(3);
let abc=(ab*bc)// multiplies ab and bc
console.log(abc);

// division practice 
let at=(28);
let tb=(7);
let atb=(at/tb);
console.log(atb);
// exponent practice
//let ** represent exponent symbol
let trx=(9);
let formula=(trx**2);
console.log(formula);
// more exponent practice
let wrv=(3);
let formula3=(wrv**3);//represents wrv to the exponent of 3
console.log(formula3);// would log 27



// bmi calculator 
//task : store mark and johns mass and height in variables
//calculate BMI USING formula : mass/ (height*height)
//create a Boolean variable 'markhigherbmi'containing information about whether Mark has 
//a higher BMI than John
//TEST DATA 1
//mark weight : 78kg 
//mark height: 1.69m
//john weight : 92kg
//john height: 1.95m
//TEST DATA 2
//mark weight : 95kg
//mark height:1.88m
//john weight :85kg
//john height : 1.76m

//test 1
let mrkwght= (78)
let mrkhght= (1.69)
let jhnwght= (92)
let jhnhght= (1.95)

let mrkbmi = (mrkwght/(mrkhght*mrkhght));
let jhnbmi = (jhnwght/(jhnhght*jhnhght));

markhigherbmi =(mrkbmi > jhnbmi);
console.log(markhigherbmi);// should print true 

//test 2
let mrkwght2= (95)
let mrkhght2 = (1.88)
let jhnwght2 =(85)
let jhnhght2= (1.76)

let mrk2bmi= (mrkwght2 / (mrkhght2 * mrkhght2));
let jhn2bmi= (jhnwght2 / (jhnhght2 * jhnhght2));

markhigherbmi2=(mrk2bmi > jhn2bmi);
console.log(markhigherbmi2)// should print false

//boolean test
let forty5=(45)
let forty4=(44)
whichgreater=(forty4 > forty5);
console.log(whichgreater)//should print false


//strings and template literals
//sample code:
const firsname='jonas';
const job='teacher';
const birthyear= 1991;
const theyearnow= 2022;

const joniss = "I'm"+' '+ firsname +',a' + '  '+ (theyearnow -birthyear ) + ' '+" year old "+' '+ job 
console.log(joniss)

//string template 
// using `` and ${ } allows you to create a much simpler string
// it also allows you to create a string without the need for spaces

const newjonas = `I'm ${firsname} a ${theyearnow - birthyear} year old ${job}`
console.log(newjonas)

//multiline string with template 
// with `` you can simplify code and right cleaner and quicker
console.log(`hello
my
name is
Henry Adams`)

//Taking decisions if/else statements
const age=16;
 // if 18 or older true , if younger false
if(age>=18){
console.log("Can start driving with a Valid license")
} else{
    const yearsleft = 18-age
    console.log(`You have to wait ${yearsleft} more years `)
}

//if  & else controlled structure
//   if(){

//  }else{

//    }

// you must have an else block in order for the script to run




// coding challenge #2
// using the bmi information from previous lesson, I will incorporate 
// if and else statements to determine the higher BMI
//final statement  template Marks bmi (### ) is higher than John's ! 
// output to console


// bmi calculator template
//task : store mark and johns mass and height in variables
//calculate BMI USING formula : mass/ (height*height)
//create a Boolean variable 'markhigherbmi'containing information about whether Mark has 
//a higher BMI than John
//TEST DATA 1
//mark weight : 78kg 
//mark height: 1.69m
//john weight : 92kg
//john height: 1.95m
//TEST DATA 2
//mark weight : 95kg
//mark height:1.88m
//john weight :85kg
//john height : 1.76m


//test data 1 coding challenge #2

let markswght = (78)
let markshght = (1.69)
let johnwght = (92)
let johnhght = (1.95)

let mrksbmi = (78/(1.69*1.69));
let jhnsbmi = (92/(1.95*1.95));

console.log(mrksbmi)
console.log(jhnsbmi)

if(mrksbmi>jhnsbmi){
    console.log( `Marks  BMI  ${mrksbmi} is higher  than Johns ${jhnsbmi} !`)

}else{

    console.log( `Johns BMI ${jhnsbmi}  is higher than Marks ${mrksbmi}  !`)

}

// type conversion 
// you can convert a string into a number within a string

//let inputyear=1991
//console.log(inputyear + 18) // will print 199118 which is what we DONT want
// therefore convert to number
let inputyear=1991
console.log(Number(inputyear) + Number(18))// this will give us 2009

console.log(Number('Jonas'))// will print NaN stating not a number

//strings are white and numbers are purple

console.log(String(23) , 45)// should print 23 as a white value or black and 45 purple 

//type coercion
console.log('I am'+ 23 +'years old')//operation between strings will cause numbers to be converted since plus signs are inserted

console.log(23 *2)

// the singular plus sign combines two values together


