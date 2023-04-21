# Greetlang+

<p align="center"><img width="649" alt="Greetlang+" src="https://user-images.githubusercontent.com/104099162/233203284-dc165de9-bd13-48b2-a663-fac39b626ebe.png"> </p>

<br />
<br />

This is a revamped version of the concept `Greetlang` programming language created by, me, of course. I have been very happy with my documentation over the language and all of my own "original" ideas. However, the key word is, `original`. I soon realised, that, very far into production of the language, most of my ideas had already been done by other people, `and I hadn't even realised`. This occured to me while learning Rust, where I saw that you could specify the type of a variable if needed. I saw my code and thought, <br />

<br />

*Hey, that looks a lot like GreetLang!*


<br />

I looked back at my code. <br />

```rs
fn main() {
    let mut x: i32 = 4; <-- Look here.
    println!("x is: {}", x); 
}
```

<br />
<br />

And back and my GreetLang. <br />

```c
let x: int = 6; <-- Look here,
let y: int = 7; <-- and here.

greet(x * 7)
```

If you can't see my point, look at the Rust code. When simplified it means `let x: int = 4`.

<br />
<br />

When I investigated more and more into GL and it's features, I kept on finding unoriginal ideas. So Greetlang `Plus`, is here to change that. Me personally, having spent so much work on that language, would like to pay it some justice after all my effort into essentially a harder version of Rust, C, and Python mixed together to vomit out some unoriginal ideas marketed as my own. I may be being a bit harsh on GreetLang, but I would like my language to be as original as possible (with some tried and tested elements from other languages, of course). If that means recreating the whole thing from the ground up, <br />
`I will do it.`

<br />
<br />

Get ready for a flurry of original ideas, and a mix of useful and effective syntax, because GreetLang+ is now here.



<br />
<br />
<br />
<br />
<br />
<br />

====================================================================================================

# Greetlang+ Documentation

<br />
<br />
<br />

Greetlang+ is a simple programming language that is designed to be easy to learn and use. It is an extension of Greetlang, which adds several new features such as support for functions with parameters, basic mathematical operations, as well as reworking the syntax to make it more easy to read and intuitive.


<br />
<br />
<br />

## Data Types

<br />
<br />

Greetlang+ supports the following data types:

    string: A sequence of characters enclosed in quotes, e.g. "Hello, World!".
    number: A numeric value, e.g. 42.
    boolean: A value that is either true or false.
    undefined: A value that is used to represent an uninitialized variable or an absent value.

<br />
<br />

****

## The Holy Semicolon 

`;` <-- This character, is responsible for the ***entire*** program not just bursting into flames. The semicolon is used for telling the compiler to stop executing the current line of code, and move on to the next one. You *must* end your lines of code with the semicolon `(as a reminder, this is the semicolon: ;)` otherwise the program will not run.

<br />
<br />

****

## Output

To output text to the console in Greetlang+, you can use the greet function. For example:

```js
greet("Hello, World!");
```

<br />

You can also use the greetmany function to output multiple strings on separate lines:

<br />

```js
greetmany("Hello", "World", "!");
```

<br />

****

## Variables

Variables in Greetlang+ are declared using the var keyword. The value of a variable can be assigned using the = operator. For example:

```csharp
var message = "Hello, World!";
```

Variables can be reassigned by simply using the = operator again:

```c
message = "Goodbye, World!";
```

<br />
<br />

****

<br />

## Functions

Functions in Greetlang+ are declared using the function keyword, followed by the name of the function and its parameters in parentheses. The body of the function is enclosed in curly braces {}.

For example, here's a function that takes two numbers as parameters and returns their sum:

```js
function add(num1, num2) {
  return num1 + num2;
}
```

<br />

Functions can be called by using their name and passing arguments in parentheses. For example:

<br />

```csharp
var result = add(2, 3); // result is now 5
```

****

<br />

## Basic Mathematical Operations

Greetlang+ supports the following basic mathematical operations:

    Addition: +
    Subtraction: -
    Multiplication: *
    Division: /

<br />

For example:

<br />

```csharp
var sum = 10 + 5; // sum is now 15
var difference = 10 - 5; // difference is now 5
var product = 10 * 5; // product is now 50
var quotient = 10 / 5; // quotient is now 2
```

<br />
<br />

****

<br />

## Control Flow Statements

Greetlang+ supports control flow statements that allow for conditional and iterative execution of code.

<br />

### If Statement

<br />

The if statement is used for conditional execution of code. If the condition inside the parentheses is true, the code inside the curly braces will be executed.

For example:

```js
if (true) {
greet("This code will be executed.");
}
```

If the condition is false, the code will be skipped.

<br />

### If-Else Statement

The if-else statement is used for conditional execution of code where if the condition inside the parentheses is true, the code inside the first curly braces will be executed. If the condition is false, the code inside the second curly braces will be executed.

For example:

<br />

```
if (false) {
greet("This code will not be executed.");
} else {
greet("This code will be executed.");
}
```

### While Loop

The while loop is used for iterative execution of code. As long as the condition inside the parentheses is true, the code inside the curly braces will be executed repeatedly.

For example:

<br />

```c
var count = 0;
while (count < 5) {
greet("Count is " + count);
count++;
}
```

<br />

****

<br />


### For Loop

The for loop is used for iterative execution of code, with more control over the number of iterations. The loop has three parts separated by semicolons:

    Initialization: executed before the loop starts.
    Condition: checked before each iteration. If it is false, the loop ends.
    Increment: executed after each iteration.

For example:

```js
for (var i = 0; i < 5; i++) {
greet("i is " + i);
}
```

This loop will execute 5 times, with i starting at 0 and incrementing by 1 each time until i reaches 4.















