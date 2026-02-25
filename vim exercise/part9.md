----------------------------------------------------------
## Exercise 1:
----------------------------------------------------------
  1. The functions are in the wrong order. Put your cursor
     on the line with "def f3():".

  2. Go into visual line mode by pressing shift-V.

  3. Go down to the end of the function by pressing   3j   .
  
  4. Delete it by pressing   d   .

  5. Go down to the end of the last function.

  6. Paste it at the end by pressing   p   .

  7. Repeat step 1-6 but with function f2 instead of f3.

```py
def f2():
  ...
  ...
  ...

def f3():
  ...
  ...
  ...

def f1():
  ...
  ...
  ...
```


----------------------------------------------------------
## Exercise 4:
----------------------------------------------------------
  1. Select all the function names by going into visual block
     mode (pressing ctrl-v)

  2. Change "function_name" to "other_function" by using the
        c   command. (change)

  3. There are too many arguments in the function! Select the
     first argument including the comma by going into
     visual block mode.
  
  4. Delete it by pressing   d   .

```py
function_name(1, 2, 3, 4, 5)
function_name(2, 2, 3, 4, 23)
function_name(2, 2, 43, 9, 23)
function_name(2, 83, 7, 9, 23)
function_name(2, 83, 7, 23, 9)
```


