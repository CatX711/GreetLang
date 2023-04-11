# GreetLang
A fictional programming language by me. GreetLang does not exist, it is a concept. <br />
Please enjoy reading the full documentation.

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

# GreetLang Programming Language Documentation
## Introduction

GreetLang is a high-level programming language designed for ease of use and readability. It combines the simplicity of Python, the speed of C, the flexibility of JavaScript, and the safety of Rust.

<br />

## Basic Syntax

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
func add_numbers(a: int, b: int) rt integer {
    return a + b;
}
```

In this code, a function called `add_number` is declared. In the () the paramaters are defined. The paramaters show that `a` and `b` are both integers. After the paramaters is `rt integer`, which is where we tell the language what return type we want. In this case, we want an integer returned, so we do `rt integer`.

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

### Comments

GreetLang supports both single-line and multi-line comments:

```c
// This is a single-line comment.

/*
    This is a multi-line comment.
*/
```

## Advanced Syntax:

<br />

### Arrays

GreetLang supports arrays of any data type:

greetlang

let numbers: [int] = [1, 2, 3, 4, 5];

Arrays can be accessed using the index operator ([]):

greetlang

let first_number: int = numbers[0];

Structures

GreetLang supports structures, which are custom data types that can contain multiple fields:


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
