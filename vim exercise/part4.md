----------------------------------------------------------
## Exercise 1:
----------------------------------------------------------
  1. Press  G  to move you to the bottom of the file.
     Type  gg  to move you to the start of the file.

  2. Go to line 10 by typing   10G   .

  3. Go back in your location history by pressing ctrl+o.

  4. Go forward in your location history by pressing ctrl+i


----------------------------------------------------------
## Exercise 2:
----------------------------------------------------------
  1. In Normal mode type the  /  character.  Notice that it and the cursor
     appear at the bottom of the screen as with the  :	command.

  2. Now type 'errroor' <ENTER>.  This is the word you want to search for.

  3. To search for the same phrase again, simply type  n .
     To search for the same phrase in the opposite direction, type  N .

  4. To search for a phrase in the backward direction, use  ?  instead of  / .

--->  "errroor" is not the way to spell error;  errroor is an error.
NOTE: When the search reaches the end of the file it will continue at the
      start, unless the 'wrapscan' option has been reset.


----------------------------------------------------------
## Exercise 3:
----------------------------------------------------------
  1. Place the cursor on any (, [, or { in the line below marked --->.

  2. Now type the  %  character.

  3. The cursor will move to the matching parenthesis or bracket.

  4. Type  %  to move the cursor to the other matching bracket.

  5. Move the cursor to another (,),[,],{ or } and see what  %  does.

---> This ( is a test line with ('s, ['s ] and {'s } in it. ))


NOTE: This is very useful in debugging a program with unmatched parentheses!


----------------------------------------------------------
## Exercise 4:
----------------------------------------------------------
  1. Move the cursor to the line below marked --->.

  2. Type  :s/thee/the <ENTER>  .  Note that this command only changes the
     first occurrence of "thee" in the line.

  3. Now type  :s/thee/the/g .  Adding the  g  flag means to substitute
     globally in the line, change all occurrences of "thee" in the line.

---> thee best time to see thee flowers is in thee spring.


