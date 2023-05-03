# Greetlang+

<p align="center"><img width="649" alt="Greetlang+" src="https://user-images.githubusercontent.com/104099162/233203284-dc165de9-bd13-48b2-a663-fac39b626ebe.png"> </p>

<br />
<br />
<br />
<br />
<br />
<br />


====================================================================================================

## Table of Contents:

<!-- TOC -->
- **1.   [Basic Info](#info)**
- **2.   [Gl+ Documentation Beginning](#beginning)**
- **3.   [Data Types](#data-types)**
- **4.   [Basics](#basics)**  
    -- **4.1 [Your First Program](#first_program)** <br />
    -- **4.2 [Running Our Program](#runprogram)** 

<!-- /TOC -->
    

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />


====================================================================================================

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<p align="center">
    Hey! Scroll past me to see the documentation!
</p>    
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

****

## Basic Information <a name="info"></a>

This is a revamped version of the concept `Greetlang` programming language created by, me, of course. I have been very happy with my documentation over the language and all of my own "original" ideas. However, the key word is, `original`. I realised that, very far into production of the language, most of my ideas had already been done by other people. This occured to me while trying out Rust, where I saw that you could specify the type of a variable if needed. I saw my code and thought, <br />

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

greet(x * 7);
```

If you can't see my point, look at the Rust code. When simplified it means `let x: int = 4`.

<br />
<br />

When I investigated more and more into GL and it's features, I kept on finding unoriginal ideas. So GreetLang `Plus`, is here to change that. Me personally, having spent so much work on that language, would like to pay it some justice after all my effort into essentially a harder version of Rust, C, and Python mixed together to vomit out some unoriginal ideas marketed as my own. I may be being a bit harsh on GreetLang, but I would like my language to be as original as possible (with some tried and tested elements from other languages, of course). GreetLang+ also aims to add a better syntax, new features, and a lot more. When I created GreetLang, I did not really have a good grasp on programming as a whole, let alone designing the languages you use to write code. So now that I've learned more about that, I think I'm ready to try again. Enjoy!

<br />
<br />

*- Daniel C.*

<br />
<br />
<br />
<br />
<br />
<br />

====================================================================================================

# Greetlang+ Documentation <a name="beginning"></a>

<br />
<br />
<br />

Greetlang+ is a simple programming language that is designed to be easy to learn and use. It is a revamp of Greetlang, which adds several new features, as well as reworking the syntax to make it more easy to read and intuitive. <br />
GL+ strives to be a syntactically sound language (which will probably never happen) that is fast, clean, easy to read and fast and easy to learn.



<br />
<br />
<br />

## Data Types <a name="data-types"></a>

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

## Comments

GreetLang+ supports `single line` and `multi-line` comments.

<br />

**Single line:**

```
// Hey! This is a gl+ single line comment
```

<br />

**Multi line:**
```
/* I am a multi-line comment.
You can write across multiple lines,
and then end the comment like this -> */
```

<br />
<br />

****

## The Holy Semicolon 

<br />

`;` <-- This character, is responsible for the ***entire*** program not just bursting into flames. The semicolon is used for telling the compiler to stop executing the current line of code, and move on to the next one. You *must* end your lines of code with the semicolon `(as a reminder, this is the semicolon: ;)` otherwise the program will not run.

<br />
<br />

Alright, now that you know the simple stuff, let's go into more detail in the `Basics` of GreetLang+

<br />
<br />

****

# Basics <a name="basics"></a>


<br />
<br />

In many languages, including GreetLang+ and it's predecessor `GreetLang`, you can of course write code straight away. For example, in C, you can just slap in an `int main()` and get writing! However, the truth is, you actually can't. Why is this? And why am I going back on something that I just stated? Well, you can do this, but it's not advised, and it'll make your code just not run. <br />
Let me explain. 

<br />
<br />

Look at this C code: <br /> <br />

```c


int main(){
    printf("Hello, world!\n");
    
    return 0;
}
```

<br />

Ah yes, sweet, sweet familiarity. This is part of the most famous program ever, the `C Hello World` program, created by `Brian Kernigham`, for the `C Programming Language` book in 1973. But wait, something is missing, what could it be? <br />
Well, at the top of the program, we're missing the essential line of code that imports the standard library the language uses, containing all of the `printf functions, variable and function defining methods, return types, etcetera.` <br /> <br />
```c
#include <stdio.h>

int main(){
    printf("Hello, world!\n");
    
    return 0;
}
```

<br />

There, thats better! <br />
In conclusion, you can write code, but without including the standard libraries for the code to function, the compiler has no idea what the heck you're talking about! <br />
Now, how does all this tie back to GL Plus? Well, in GreetLang+, you would not need to include/import any libraries for the language to gain basic functionality. However, when working with arithmetics and mathematics and booleans, it just wont function without importing the libraries that contain the info for the compiler to understand that code. <br /> <br /> <br />

Before we begin, <br />
Here is a list of what GreetLang+ comes pre-packaged with:
```
op() <-- OutPut is essentially the "print" function.
func st() <-- "Function Start()" is essentially "int main()". mostly all of the code goes inside of it
while <-- While loops
for <-- For loops
if <-- If statement
elif <-- Else If statement
else <-- Esle statement
import <-- essentially "#include". used for importing libraries into the code


It knows how to create a variable:

def var [varname] -> [type] = [value]


And how to create functions:

func [funcname (first letter must be capitalised) ](parameters [if none leave blank]) rt [return type]{
    [code]
}

Preprocessing (must go directly below any library imports, also no semicolons needed):

!PPR{
    #mac [macro name] = [type]
}

(or like this):

!PPR{
    #mac [macro name](parameters) \
        [code] \
        [when going over multiple lines use backslash -> \] 
}
```
Keep in mind that these will be explained later on.

<br />
<br />
<br />
<br />

### Your First program <a name="first_program"></a>

<br />
<br />

Begin your first GL+ program by creating a `.gpp` file. This should create a new GreetLang+ file and allow for it to be edited. <br />
You can use whatever editor you like, to be honest, it doesn't really matter!

<br />
<br />

Alright, lets start. <br />
Begin by calling the `main` function. You do this by typing `func main`, followed by it's return type (int), and two curly brackets `{}`

```js
func st() rt:int{
    // your code goes inside here
}
```

<br />

Alright, let's break this down. `func st()` is how we start the program, mostly all of our code will go inside of `st()`, as it is a renamed version of the tried and true `main()`. There's a blank space in the brackets, because all functions `can` (not `must`) take parameters, however, we won't get into that now. Okay, so, you might be wondering what in the world `rt:int[0]` means. Well, it's a way of telling the GreetLang+ compiler that we want our function to return an integer, `(either 0 or 1)`, 0 being a `code` that tells us that our program has `run succesfully`, and 1, obviously `doing the opposite`. <br /> <br /> Let's move on to the next part now. <br />

```js
func st() rt:int[0]{
    op("Hello, world!"); // remember to end your line of code with a semicolon!!!
}
```

<br />

Using the `op()` (output) function, we can output some text to the screen. In this case, we're displaying `"Hello, world!"` for everyone to see. If you're an experienced C developer, you may be wondering why we don't include an `return 0;` in our code. This is because we already specify the return type in the first line of code! To remind you, here is what I'm talking about: `func st() rt:int[0]` 

<br />
<br />

## Running our program <a name="runprogram"></a>

<br />
<br />

Now that we've created our program, we need to compile and run it. Here's how we do that. <br />
Open up your terminal, and enter in the text, `gpc [filename.gp]` <br />
This is telling the `GreetLang+ Compiler` `(gpc)`, to compile our code. We dont need to name the binary file that is produced, as we would in C, it just auto names it to your file name. <br /> <br />

After compiling, if we write `./[filename]`, we can run our code. <br />
The output should be this:

<br />

```
Hello, world!
```

<br />
<br />

Great job! You've just written your first GreetLang+ code! You're now ready to become a professional GL+ developer! :D

<br />

****















