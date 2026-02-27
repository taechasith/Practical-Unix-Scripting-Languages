----------------------------------------------------------
## Exercise 1:
----------------------------------------------------------
  1. Go to the beginning of the first line marked with --->

  2. Type   f=   to go to the next equal sign.

  3. Go to the right by one by pressing   l   .

  4. Change the function call to f with the number 1.
     Do this using the   ct;   command (change till ;)
     It should now match the second line


---> let x = 1;
---> let x = 1;


----------------------------------------------------------
## Exercise 2:
----------------------------------------------------------
  1. Go down to the line marked with --->

  2. Replace "hello world" with "goodbye".
     Do this using the   ci"   command (change inside quotes)

  3. Now remove everything besides print.
     Do this using the   da)   command (delete arround parenthesis)

---> print


----------------------------------------------------------
## Exercise 3:
----------------------------------------------------------
  1. The code below is not indented correctly.
     Indent the 3 lines inside the if statement,
     use the   >2j   command for this.

  2. Now indent the code inside the if statement using >>.

```js
let x = 0;
for (let i=0; i<10; i++) {
  if (f(i)) {
    x += 1;
  }
}
```

```js
let x = 0;
for (let i=0; i<10; i++) {
  if (f(i)) {
    x += 1;
  }
}
```


----------------------------------------------------------
## Exercise 4:
----------------------------------------------------------
  1. Rename the function below from "function_name" to
     "other_function" using the   cw   command (change word).

  2. Rename the other function by repeating the last command
     by pressing   .   (period). Make sure you are at the start
     of the line again.

  3. There are too many arguments in the function! Remove the
     first 3 using a single action.
  
  4. Repeat it for the other function calls by pressing period.

```py
other_function(4, 5)
other_function(4, 23)
other_function(9, 23)
other_function(9, 23)
other_function(23, 9)
```


