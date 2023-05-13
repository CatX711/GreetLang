# Greetlang+

<p align="center"><img width="649" alt="Greetlang+" src="https://user-images.githubusercontent.com/104099162/233203284-dc165de9-bd13-48b2-a663-fac39b626ebe.png"> </p>

<br />
<br />

>Computers are good at following instructions, but not at reading your mind.
>
>*- Donald Knuth*

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
<br />
<br />
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
- **5.   [Variables](#vars)**     
    -- **5.1 [Variable Names](#varnames)** <br />
    -- **5.2 [Adding Integer Variables Together](#adding_int_vars)**     
    -- **5.3 [Merging String Variables](#)** <!-- not completed yet --> 
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

<br />

# Basic Information <a name="info"></a>

This is a revamped version of the concept generic use programming language, `Greetlang` (otherwise known as `Greet`), created by, me, of course. I have been very happy with my documentation over the language and all of my own "original" ideas. However, the key word is, `original`. Very far into production of the language, I realised that most of my ideas had already been done by other people, and what especially surprised me, was the *OFFICIAL* `Carbon-Language` actually had nearly the exact same ideas as GreetLang! The first instance of me discovering the similarities of GreetLang with other languages occured to me while trying out Rust, where I saw that you could specify the type of a variable if needed. I saw my code and thought, <br />

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

>Any fool can write code that a computer can understand. Good programmers write code that humans can understand.
>
>*- Martin Fowler*

<br />
<br />
<br />


Greetlang+ is a simple programming language that is designed to be easy to learn and use. It is a revamp of Greetlang, which adds several new features, as well as reworking the syntax to make it more intuitive and easy to read. <br />
GL+ strives to be a syntactically sound language (which will probably never happen) that is fast, clean, easy to read and learn.



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

>The computer programmer is a creator of universes for which he alone is responsible. Universes of virtually unlimited complexity can be created in the form of computer programs.
>
>*- Joseph Weizenbaum*

<br />
<br />
<br />

In many languages, including GreetLang+ and it's predecessor `GreetLang`, you can of course write code straight away. For example, in C, you can just slap in an `int main()` and get writing! However, the truth is, you actually can't. Why is this? And why am I going back on something that I just stated? Well, you can do this, but it's not advised, and it'll make your program cease to run. <br />
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
Begin by calling the `main` function. You do this by typing `func st`, followed by it's return type `(int)`, and two curly brackets `{}`

```js
func st() rt:int[0]{
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

Oh, and one more thing, normally an op() function automatically creates a newline when moving on to the next line of code, like in `Python`, so it's more of an ease of life feature. However, this can be turned off by adding this to the beginning of your `start function`:
<br />
<br />

```js
func st() rt:int[0]{
    &newline::op = '1'; // sets to false
        
    op("Oh, automatic newlines are disabled now...");
    op("I sure hope this doesn't do anything bad!");
}
```

<br />

With this at the top of the `st`, the following code would go from outputting, <br />

```
Oh, automatic newlines are disabled now...
I sure hope this doesn't do anything bad!
```

<br />

To 

<br />

```
Oh, automatic newlines are disabled now...I sure hope this doesn't do anything bad!
```

<br />

Remember, you can manually insert a newline using `"\n"` at the end of your op(), like this: <br /> <br />

```js
op("Hey, newlines are back!\n"); 
```



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

<br />
<br />

## Variables <a name="vars"></a>

<br />

>Talk is cheap. Show me the code.
>
>*- Linus Torvalds*

<br />
<br />
<br />

Ah yes, `variables`, the go-too way of storing data in a sort of container. <br />
Think of a variable as a box, which you can name and can put things inside. The items you would `put inside` the box are the values you `assign` to the variable. For example in C, if you wanted to give a variable a value of an `integer`, you would do something like this:

<br />

```c
int num1 = 87;
```

<br />
<br />

That is an example of `putting a value in our box`. In this case, the value is the `integer` 87, and now that the variable has been created and assigned a value, we can use it later in our code. <br /> <br />

GreetLang+ is a bit different. You start by using the `def` keyword. This stops any confusion you would have in C like `int` and `char` and `char varname[100]` (<-- Character array, I'll go in to how that's different in GreetLang+ soon), so it's just `define`. Nothing confusing.
Following that is `var`, which tells the GL+ compiler that we're defining a `VARIABLE`, not something else. Next up is the variable name, and it's value. Make sure to end the line of code with a semicolon!

<br />
<br />

```js
// Code for the stuff shown above

func st() rt:int[0]{
    def var hello = "Hello!";
}
```

<br />

I said I was going to go into how character arrays are different in GL+, so I'll quickly skim over that and move on. <br />
In C and many other older languages, they didn't necessarily have `string types`, so their alternative was to create an `array of characters` and use that instead. Obviously this is just a more complicated way of writing `strings`, as they are obviously character arrays if you think about it. <br /> <br />

An array is a spreadsheet of information, <br />
a character is a single letter, <br /> 
and a character array is a collection of characters that can form a sentence or a name or whatever you want. <br /> <br />

Starting to see my point here?

<br />
<br />

Now let's move on to how you would actually use one in your code. <br />
Below is the code to include a variable with an `integer` value in an output `(op)`: 
<br />
<br />

```js
func st() rt:int[0]{
    def var friends = 122;
    
    op("Hey, I have {!friends} on FaceBook!");
}
```

<br />

Surrounding a variable name in curly brackets and an exclamation mark tells the GL+ compiler that we want to put a variable in that position. When doing this, you won't have to worry about converting the number to a string, or any nonsense like that, the lovely GL+ compiler automatically does it for you. Thanks GL+ compiler!

<br />
<br />  	

Click on `More Examples` for some extra examples about variables in GreetLang+

<details>
<summary>More Examples</summary> 

<br />	
	
```js
func st() rt:int[0]{
	
  def var hello = "Hey there!";	
  op("{!hello}"); // outputs "Hey there!" to the terminal	
}
```

<br />
	
**Hello!** 

<br />
<br />
	
```js
func st() rt:int[0]{
  
  def var middle_name = "Jackson"		
  def var surname = "Kerg";
	
  op("Hello, my name is Samuel {!middle_name} {!surname}. What's yours?");		
}
```
	
<br />
	
**Hello, my name is Samuel Jackson Kerg. What's yours?**	

	
</details>



<br />
<br />

## Variable Names <a name="varnames"></a>

<br />
Before we go into any more detail about variables in GreetLang+, let's go over some basic variable naming rules.
<br />
<br />


You can use any characters in the range 0-9, A-Z, a-z, and underscore for variable names, with the following rules: <br />
• You can’t start a variable with a digit 0-9. <br />
• You can’t start a variable name with two underscores. 

<br /> 
<br />

Now that we have that cleared up, let's continue!

## Adding Integer Variables Together <a name="adding_int_vars"></a>

<br />

You can add integer variables quite easily, by containing the equation you would like to calculate in a single `{!}`. This is a feature in GL+ that reduces the complication of, for example, in C, where you would have to do a complicated mess of remembering the calling characters for specific variable types.

<br />
<br />

```c
int main() {

  int num1 = 22;
  int num2 = 23;
  
  printf("%d", num1 + num2);
}
```

<br />

The C code can be shortened very much in GL+, as you can see in this code below that shows how to add integer variables in it.

<br />

```js
func st() rt:int[0]{

  def var num1 = 22;
  def var num2 = 23;
  
  op("{!num1 + num2}");
}
```

<br />

The GreetLang+ compiler, as stated before, automatically checks what type a variable is, so you wont have to worry about <br /> 
`"%d" or "%f" or "%lf"`

<br />
<br />

One neat feature most programming languages, including GL+ have is giving variables the value of the answer to an equation. Yeah, that probably sounds vague as hell, so let me quickly explain it.

<br />

```js
func st() rt:int[0]{
  def var RandomNumberWithAnExtremelyLongVariableName = 2 * 2;
  
  op("{!RandomNumberWithAnExtremelyLongVariableName}");
}
```

<br />

This code is actually a perfect example for GreetLang-Plus's `Short-hand Variable Names`, but thats for later. In the code above, we make `RandomNumberWithAnExtremelyLongVariableName` equivalent to `2 times 2` (which as we all know is 4), this is just a neat little thing we can do. There is also something else you can do, using mathematical operators. This is the first time we'll have to import a library into GreetLang+<br />
We can do this via the `import` keyword. This is just what we use in Python to import libraries. It's the exact same as `#include` in C. <br />
Note that you do not need to end `imports` with a semicolon.

<br />
<br />

```js
import math.gph // greetlang plus header file

func st() rt:int[0]{
  def var number1 = sqr("22"); // squares the number
  
  op("{!number1}"); // outputs "484"
}
```



****

<!-- for functions section eventually do a comparison between these two: 

GreetLang Original:

func add_nums(num1: int, num2: int) rt integer {
    let sum: int = num1 + num2;
    return sum;
}

GreetLang+ 

func add_nums(num1, num2) rt:userdef[]{ <-- user defined return type (in this case, sum) 
	def var sum = num1 + num2;
	return sum;
} 

-->






<!-- GL+ feature: nicknames (think of better name lol)

you can assign a variable a nickname to shorten down it's name if it is long

def var OneThousandTimesTwo:<OneKx2> = 1000 * 2; // sets value to 2k

normally this would be used in code similar to this:


func st() rt:int[0]{
  def var OneThousandTimesTwo = 1000 * 2;

  op("One thousand times two is {!OneThousandTimesTwo}");
}



but with nicknames, it would be this

func st() rt:int[0]{
  def var OneThousandTimesTwo:<OneKx2> = 1000 * 2;

  op("One thousand times two is {!OneKx2}");
}



idea for new name:

short-hand variable names

-->

<!--

more ideas:

you can import individual glp libraries, however, `import gpultim.gph` will import
EVERY gp library, but it will take up more memory.
stick to individual imports when working on small projects
shoot for `gp-ultimate` when working on bigger projects

-->



