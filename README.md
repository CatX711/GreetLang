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
greet("Hello, World!");
```

<br />

The output will the string `Hello, World!` printed to the screen.

<br />
<br />

### Semicolons 

Use semicolons (;) to end lines of code.

```js
greet("What's your name?"); <--
```

If you are well aquainted with C, and many other languages, you will know that the semicolon lets the compiler know that the current line has been executed and it should stop running it, and move onto the next line of code. The semicolon is only not needed in very rare occasions, such as `importing` `modules` (explained later on in the docs).

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
    int/integer: An integer.
    float: A floating point number.
    bool/boolean: A boolean value (true or false).
    char/character: A single character.
    str/string: A sequence of characters.
```

<br />

****

## Variables

In GreetLang, variables are declared using the ***let*** keyword:

```js
let x: int = 10;
let name: str = "Alice";
```

<br />

`let x: int = 10; `: In this code, we declare the variable using `let`, and then specify it's type, in this case, and `integer`, and after that we specify it's value. <br />
`let name: str = "Alice"; `: This is the same, however, with a string. This means that we have to specify this using `str` and give the variable a value in `parenthesis` (using `" "`)
****

## Functions

**In GreetLang, functions are declared using the func keyword:**

```c
func add_numbers(num1 input: int, num2: int) rt integer {
    let sum: int = num1 + num2;
    return sum;
}
```

<br />

Then you would call the function by doing this:

```c
add_numbers();
```

<br />
<br />

In this code, a function called `add_number` is declared. In the () the paramaters are defined. The paramaters show that `num1` and `num2` are both integers. `num1 input` makes the program ask for a user input (if you do not want user input just don't include `input`). In GreetLang you only use one `input` in the parameters section. You do not need to use `input` after both of your paramaters. After the paramaters is `rt integer`, which is where we tell the language what return type we want. In this case, we want an integer returned, so we do `rt integer`. This program uses user input to add two numbers. <br />
If you wanted to return a string, you could define it inside the function. <br />
<br />

*Example:*

```c
func hello() rt string {
    let text: str = "Hello World!";
    return text;
}
```
>Notice that there is nothing asking for input in the parameters area. This can be changed.

<br />

And if you wanted to use the function in a greet:

```c
func hello() rt string {
    let hello: str = "Hello World!";
    return hello;
}

greet(hello(), " It's a beautiful day today!");

// Variation 2:

/*
greet(hello() + " It's a beautiful day today!");
*/
```

**Or**

Going back to the add_numbers function, if we made it so the function does not take in an input (by removing the `input` in `num1 input: int`, we could use it in a greet while manually giving it our own values instead of giving it user input.

```
greet("The sum of 2 and 3 is " + times(2, 3));
```

<br />

***REMEMBER:***

What you call the paramaters for functions does not matter. For instance, `num1` and `num2` could be `a` and `b`, it would not affect the code whatsoever.

<br />
<br />


Click on `More Examples` for some extra info about functions in GreetLang.

<details>
<summary>More Examples</summary> 

Times (num1 * num2):

```c
func times(num1: int, num2: int) rt integer {   // Use "rt" to specify the return type
    let prod: int = num1 * num2;   // Declare a variable "prod" to store the product of the two numbers
    return prod;   // Return the product as an integer
}


// Call the function and pass two numbers as arguments
greet(addnums(5, 3));   // Output: 8
```

The first line declares a function called `times` that takes two parameters num1 and num2, both of which are of type int (short for integer). The `rt symbol` specifies the `return type` of the function, which in this case is an `integer`.

Inside the function, a variable called `prod` is declared and assigned the value of `num1` times  `num2`, which is the product of the two input numbers.
Finally, the `prod` variable is returned by the function using the `return keyword`.

The last line of code calls the `times` function with the arguments `5` and `3`, and the result (which is `5` times `3`) is passed to the `greet function`, which displays the output "15".
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
let numbers: int = [1, 2, 3, 4, 5]; // index values: 0, 1, 2, 3, 4
                                    // actual value  1, 2, 3, 4, 5  
```

**Arrays can be accessed using the index operator ([]):**

```js
let first_number(lt(numbers)): int = numbers[0];
```

<br />

In the code above we create a variable named `first_number`, link it to the `number` array using `lt` (link-to) and set the value of it to the index of 0 on the `number` array which is in this case, the integer `1`. <br />
Do not worry about overflows, as the compiler automatically allocates memory for the array.

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

## Warning! 

**This section is outdated and has been replaced by `modules support` which is in the section after this one. Thank you.**

<br />
<br />

### MFFS (Multi-File Function Sharing):

<br />

GreetLang has a useful feature which allows you to import your own functions from other files in the folder location. <br />
You can create a function in a separate GreetLang file, then import that function into another GreetLang file using the include statement.
For example, let's say you have a file called `math.gl` that contains a function called `addnums` which adds two numbers and returns the result:

<br />

```csharp
func addnums(num1: int, num2: int) rt integer {
    let sum: int = num1 + num2;
    return sum;
}
```

To use this function in another GreetLang file, you would use the include statement to import the `addnums function` from the `math.gl` file:

```csharp
from [math.gl] include "addnums"

greet(addnums(5, 3));  // Output: 8
```

This will make the `addnums function` available in the current file, allowing you to call it with the `addnums` function name followed by the arguments in `parentheses`.

****

<br />

### Modules

<br />

Define a module using the module keyword followed by the module name and the module body enclosed in curly braces:

```ruby
universal module mymodule {
    // module body goes here
}
```

Use `universal` identifier to let the module be used in all of the .gl files on your computer.
Define functions, variables, and other constructs inside the module:


```csharp
universal module mymodule {
    func myfunc() {
        // function body goes here
    }
    
    let myvar: int = 42;
    
    // more constructs go here
}
```

The `export keyword` is used to specify which constructs (functions, variables, etc.) can be accessed from outside the module. 


```js
universal module mymodule {
    export func myfunc() {
        // function body goes here
    }
    
    export let myvar: int = 42;
    
    // more constructs go here
}
```

Import a module using the import keyword followed by the module name:

```arduino
import mymodule
```
Use the exported constructs from the imported module:

```c
greet(mymodule.myfunc());   // call a function from the module
greet(mymodule.myvar);   // access a variable from the module
```

Here's an example that shows how to define and import a module in GreetLang:

```js
// In a different file:

// define a module called "mymodule"
universal module Mymodule {
    export func sayhello() {
        return "Hello, world!";
    }
    
    export let pi: float = 3.14159;
}

// In the file we want to import the module into:

// import the "mymodule" module
import mymodule

// use the exported functions and variables from the module
greet(mymodule.sayhello());
greet("The value of pi is " + str(mymodule.pi));
```

This example defines a module called `"mymodule"` that exports a function called `"sayhello"` and a variable called `"pi"`. The module is then imported and the exported constructs are used in the program. The output of the program would be:

```txt
Hello, world!
The value of pi is 3.14159
```


<br />
<br />

**Errors:**

<br />

When you have 2 or more modules with the same name, the GreetLang compiler will spew out an error message notifying you of the problem and showing you the files where the module is created. <br /> 
*For example:*

```js
Warning! Error in module names: Two itterations of the same module have been found.

MathModule.gl

================================================================

universal module Math {
    export func times(num1, num2) {
        let prod: int = num1 * num2;
        return prod;
    }
    export func add(num1, num2) {
        let sum: int = num1 + num2;
        return sum;
    }
    export func divide(num1, num2) {
        let divide: int = num1 / num2;
        return divide;
        if num1 or num2 == 0:
            greet_error("You cannot divide a number by zero!");
    }
}

================================================================

MyFirstModule.gl

================================================================

universal module Math {
    export func times(num1, num2) rt integer{
        let prod: int = num1 * num2;
        return prod;
    }
    export func add(num1, num2) rt integer{
        let sum: int = num1 + num2;
        return sum;
    }
    export func divide(num1, num2) rt integer{
        let divide: int = num1 / num2;
        return divide;
        if num1 or num2 == 0:
            greet_error("You cannot divide a number by zero!");
    }
}

================================================================

Module declared in MathModule.gl ("Math" module) has the same name as the module declared in MyFirstModule.gl ("Math" module).
Fix this to continue the program.

```


<br />

<br />
<br />
<br />

Benifits of using `Modules` instead of `MFFS`:

- Can add extra things, not just functions.
- Makes module universal for all future or past .gl files in the computer.
- Less bugs.
- More efficient.

<br />

****

<br />


### Gui Libary Support


```js
import gui

// Define a function to handle button clicks
func button_click(gui) {
    gui.message_box("Button clicked!");
}

// Create a new window with a button
let window = gui.window("My Window");
let button = gui.button("Click me", on_click=button_click);
window.add(button);

// Show the window
window.show();
```
>Note:
>When creating the `button_click` function we do not need to specify the `return type` as that is already contained in the gui library (which the GreetLang compiler gets told when we put the library name in the parameters. (EXTRA NOTE: even if you have the library name in the function parameters, you can still give it other parameters too)). When defining the `window` and `button` variables, because we give it a value of something "gui.", we do not need to specify it's `type` as it is considered a variable related to the library and the GreetLang compiler knows that it's type is related to whatever the code the library has that specifies that when a variable is related to the library, it's type is auto defined. 

<details>
<summary>Click for an in depth explination of the code that auto defines this.</summary>
<br />

In the official GreetLang GUI library, this code (written in Zardakvos (another fictional language)) allows the GreetLang compiler to know the auto defined value of a when a variable it's connected to the library.

```fortran
// rest of library code is not in this

CONNECT TO glcompiler.c
FROM winx12_calpice RETRIEVE data.xtl
USE 0x00212a0d TO ACCESS 0x00262ab40
USING bytes:32 TAKE 4:= 87 AND PRIORATISE 0x00262ab40
PERFORM definetype.gl
ACCESS defineype.gl AND CONNECT TO glcompiler.c 
TRANSFER [bitdata] AND USE xenoflux.htlpx TO HYPERCONFLUGTUATE vartype.und // .undefined file
HYPERAXSENSUATE bl.s  // save state file
WITH bl.s USING DATA FROM vartype.und CREATE [types.cc] // .compiler connect file

ENTER CC EDITOR--CNFRM // confirm entering the compiler connect file editor

types.cc:
---------------------------------------
;instantiate Types === var_types(array)

;vartypes[

?if code="let [varname] = gui.{stringvalue}"
    vartype in vartypes === stringflux

?elseif code="let [varname] = gui.{integervalue}"
    vartype in vartypes === numflux 
    
?elseif code="let [varname] = gui.{othervalue}"
    vartype in vartypes === gui:component
    
]

connect types.cc to [gl] compiler
---------------------------------------

EXIT types.cc

USE "vartypes" IN types.cc TO DETERMINE variabletypes
FIN bl.s // finish bl.s using data sources
USING data.xtl, vartype.und, calpise.lib, variabletypes ULTIMISE definetype.gl

FINALLY{[CONNECT definetypes.gl TO glcompiler.c]}

END
```
</details>

<br />
<br />

In this example, we import the gui module, which provides functions and classes for creating and manipulating graphical elements. We define a function button_click to handle button clicks, which simply displays a message box with a message.

We then create a new window and a button, and set the button's on_click property to the button_click function. We add the button to the window, and then show the window.

Of course, this is just a simple example, and there are many more complex graphical elements and features that could be added to GreetLang's GUI library, such as menus, dialogs, text formatting, and image manipulation. However, the basic principles would be the same: define constructs for graphical elements, provide functions for manipulating them, and create bindings to a GUI toolkit or library.

****

### Playing Audio

<br />

In Greetlang, to play audio, you will have to make sure your audio file is in the same folder as you GreetLang file. You will then create a variable, and assign it a type of `audio`.

**Example**

```c

import "drums.mp3" type="audio";

// use "play()" function

play(drums.mp3);
```
