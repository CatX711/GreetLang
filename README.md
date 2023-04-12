# GreetLang
A fictional programming language by me. GreetLang does not exist, it is a concept. <br />
GreetLang will be regularly expanded upon by me. Feel free to point out inconsistency issues, general problems, <br />
and ideas. <br />
Thank you, and please enjoy reading the full documentation.
<br />
<br />


<img width="350" alt="image" src="https://user-images.githubusercontent.com/104099162/231164817-f48e1412-f9b4-4d03-aa34-0eb9b822f60d.png">



<br />
<br />
<br />
<br />
<br />


# GreetLang Programming Language Documentation

<br />
<br />

## Introduction

GreetLang is a high-level programming language designed for ease of use and readability. It combines the simplicity of Python, the speed of C, the flexibility of JavaScript, and the safety of Rust.
GreetLang is a statically typed language, which means that variable types are determined at compile time rather than at runtime. This allows for faster execution of programs and helps to catch errors early on in the development process.

<br />

## Basic Syntax

<br />
<br />

### Greetings!

In GreetLang, to print something to the screen, you use the `greet()` function. <br />

```shell
greet("Hello, World!")
```

<br />

The output will the string `Hello, World!` printed to the screen.

<br />
<br />

### Comments

GreetLang supports both single-line and multi-line comments:

```c
// This is a single-line comment.

/*
    This is a multi-line comment.
*/
```

<br />
<br />

****

### Data Types

**GreetLang supports the following data types:**

```
    int: A 32-bit integer.
    float: A 64-bit floating point number.
    bool: A boolean value (true or false).
    char: A single character.
    string: A sequence of characters.
```

<br />

****

## Variables

In GreetLang, variables are declared using the ***let*** keyword:

```js
let x: int = 10;
let name: string = "Alice";
```
****

## Functions

**In GreetLang, functions are declared using the func keyword:**

```c
func add_numbers(num1 input: int, num2: int) rt integer {
    return num1 + num2;
}
```

<br />

Then you would call the function by doing this:

```c
add_numbers()
```

<br />
<br />

In this code, a function called `add_number` is declared. In the () the paramaters are defined. The paramaters show that `num1` and `num2` are both integers. `num1 input` makes the program ask for a user input (if you do not want user input just don't include `input`). In GreetLang you only use one `input` in the parameters section. You do not need to use `input` after both of your paramaters. After the paramaters is `rt integer`, which is where we tell the language what return type we want. In this case, we want an integer returned, so we do `rt integer`. This program uses user input to add two numbers. <br />
If you wanted to return a string, you could define it inside the function. <br />
<br />

*Example:*

```c
func hello(txt: str) rt string {
    txt = "Hello World!"
    return txt;
}
```
>Notice that there is nothing asking for input in the parameters area. This can be changed.

<br />

And if you wanted to use the function in a greet:

```c
func hello(a: str) rt string {
    a = "Hello World!"
}

greet(hello(), " It's a beautiful day today!")

// Variation 2:

/*
greet(hello() + " It's a beautiful day today!")
*/
```

**Or**

Going back to the add_numbers function, if we made it so the function does not take in an input (by removing the `input` in `a input: int`,
we could use it in a greet while manually giving it our own values instead of giving it user input.

```
greet("The sum of 2 and 3 is " + add_numbers(2, 3))
```

<br />

***REMEMBER:***

What you call the paramaters for functions does not matter. For instance, `num1` and `num2` could be `a` and `b`, it would not affect the code whatsoever.

<br />
<br />


Click on `More Examples` for some extra info about functions in GreetLang.

<details>
<summary>More Examples</summary> 

```c
func addnums(num1: int, num2: int) rt integer {   // Use "rt" to specify the return type
    let sum = num1 + num2   // Declare a variable "sum" to store the sum of the two numbers
    return sum   // Return the sum as an integer
}


// Call the function and pass two numbers as arguments
greet(addnums(5, 3))   // Output: 8
```

The first line declares a function called addnums that takes two parameters num1 and num2, both of which are of type int (short for integer). The rt symbol specifies the return type of the function, which in this case is an integer.

Inside the function, a variable called sum is declared and assigned the value of num1 plus num2, which is the sum of the two input numbers.
Finally, the sum variable is returned by the function using the return keyword.

The last line of code calls the addnums function with the arguments 5 and 3, and the result (which is the sum of 5 and 3) is passed to the greet function, which displays the output "8".

In summary, this code defines a function that adds two numbers together and returns the sum, and then calls that function with the values 5 and 3, displaying the result "8".
</details>

<br />

****

### Conditional Statements

**GreetLang supports if statements for conditional execution of code:**

```c
if x > 0 {
    // Do something if x is greater than 0.
} else {
    // Do something else if x is less than or equal to 0.
}
```
****

### Loops

GreetLang supports for and while loops:

```c
for i in 0..10 {
    // Do something for each value of i from 0 to 9.
}

while x > 0 {
    // Do something while x is greater than 0.
}
```

****

## Advanced Syntax:

<br />

### Arrays

GreetLang supports arrays of any data type:

```js
let numbers: [int] = [1, 2, 3, 4, 5];
```

**Arrays can be accessed using the index operator ([]):**

```js
let first_number: int = numbers[0];
```

****

### Structures

**GreetLang supports structures, which are custom data types that can contain multiple fields:**

```c
struct Point {
    x: float,
    y: float,
}

let p: Point = Point { x: 0.0, y: 0.0 };
```

****

### Classes

GreetLang supports classes, which are similar to structures but can also contain methods:

<br />

```c
class Circle {
    let PI: float = 3.14;

    radius: float;

    func __init__(r: float) {
        radius = r;
    }

    func area() rt float {
        return PI * radius * radius;
    }
}

let c: Circle = Circle(2.0);
let area: float = c.area();
```
The above code is a definition of a class called Circle in. This class has three attributes - PI, radius, and two methods - __init__ and area.

The __init__ method is the constructor of the class, which is called when an instance of the class is created. It takes a single parameter r of type float and initializes the radius attribute with the given value.
<br />
The area method calculates and returns the area of the circle using the formula PI * radius * radius. It returns the area as a float value.

Overall, this code defines a blueprint for creating circle objects, which can be instantiated and manipulated.

>Extra info for those who are confused: <br />
>In this code, r is a parameter of the constructor (init method) of the Circle class. The constructor is called when a new instance of the Circle class is created. It takes a single argument r, which is a float representing the radius of the circle. <br />
>
>The line `radius = r;` sets the value of the radius attribute of the Circle instance to the value of the r parameter. This means that when you create a new Circle instance and pass in a value for r, that value will be used to initialize the radius attribute of the instance.


****

### Inheritance

GreetLang supports inheritance between classes:

```c
class Shape {
    func area() rt float {
        // The area of a generic shape is undefined.
        return 0.0;
    }
}

class Rectangle : Shape {
    width: float;
    height: float;

    func __init__(w: float, h: float) {
        width = w;
        height = h;
    }

    override func area() rt float {
        return width * height;
    }
}

let r: Rectangle = Rectangle(2.0, 3.0);
let area: float = r.area();
```

<br />

This greetlang code defines two classes, Shape and Rectangle, and uses them to calculate the area of a rectangle.

The Shape class has a single method, area(), which returns a float representing the area of the shape. This method is currently set to return 0.0 as the area of a generic shape is undefined.

The Rectangle class extends the Shape class, and defines two attributes, width and height, which are used to calculate the area of the rectangle. The __init__() method is used to initialize these attributes with the values of the arguments w and h respectively.

The override keyword is used to override the area() method in the Shape class. In this case, the area() method in the Rectangle class calculates the area of the rectangle using the formula width * height.

The last two lines of the code create a new instance of Rectangle called r with width 2.0 and height 3.0. The area of the rectangle is then calculated using the area() method of the Rectangle class and stored in the variable area.

****

<br />

Modules:

<br />

WIP
