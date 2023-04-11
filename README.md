# GreetLang
A fictional programming language by me. GreetLang does not exist, it is a concept. <br />
Please enjoy reading the full documentation.

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

<br />

## Basic Syntax

<br />
<br />

In GreetLang, to print something to the screen, you use the `greet()` function. <br />

```shell
greet("Hello, World!")
```

<br />

The output will be a string printed to the screen.

<br />
<br />

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
func add_numbers(a input: int, b: int) rt integer {
    return a + b;
}
```

In this code, a function called `add_number` is declared. In the () the paramaters are defined. The paramaters show that `a` and `b` are both integers. `a input` makes the program ask for a user input (if you do not want user input just don't include `input`). After the paramaters is `rt integer`, which is where we tell the language what return type we want. In this case, we want an integer returned, so we do `rt integer`. This program uses user input to add two numbers. <br />
If you wanted to return a string, you could define it inside the function. <br />
<br />

*Example:*

```c
func hello(a: str) rt string {
    a = "Hello World!"
    return a;
}
```
>Notice that there is nothing asking for input in the parameters area. This can be changed.

<br />

And if you wanted to use the function in a greet:

```c
func hello(a: str) rt string {
    a = "Hello World!"
}

greet(hello, " It's a beautiful day today!")

// Variation 2:

/*
greet(hello + " It's a beautiful day today!")
*/
```

<br />

**Or**

Going back to the add_numbers function, if we made it so the function does not take in an input (by removing the `input` in `a input: int`,
we could use it in a greet while manually giving it our own values instead of giving it user input.

```
greet("The sum of 2 and 3 is " + add_numbers(2, 3))
```

<br />

****

### Conditional Statements

**GreetLang supports if statements for conditional execution of code:**

```python
if x > 0 {
    // Do something if x is greater than 0.
} else {
    // Do something else if x is less than or equal to 0.
}
```
****

### Loops

GreetLang supports for and while loops:

```py
for i in 0..10 {
    // Do something for each value of i from 0 to 9.
}

while x > 0 {
    // Do something while x is greater than 0.
}
```

****

### Comments

GreetLang supports both single-line and multi-line comments:

```c
// This is a single-line comment.

/*
    This is a multi-line comment.
*/
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

>Extra info for those who are confused:
>In this code, r is a parameter of the constructor (init method) of the Circle class. The constructor is called when a new instance of the >Circle class is created. It takes a single argument r, which is a float representing the radius of the circle. <br />
>
>The line radius = r; sets the value of the radius attribute of the Circle instance to the value of the r parameter. This means that when >you create a new Circle instance and pass in a value for r, that value will be used to initialize the radius attribute of the instance.


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



Modules
