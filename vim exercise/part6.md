----------------------------------------------------------
## Exercise 1:
----------------------------------------------------------
  1. Move the cursor to the first line below marked --->.

  2. Type the lowercase letter  o  to open up a line BELOW the cursor and place
     you in Insert mode.

  3. Now type some text and press <ESC> to exit Insert mode.

---> After typing  o  the cursor is placed on the open line in Insert mode.
     I added a line below using o.

  4. To open up a line ABOVE the cursor, simply type a capital	O , rather
     than a lowercase  o.  Try this on the line below.

     I added a line above using O.
---> Open up a line above this by typing O while the cursor is on this line.


----------------------------------------------------------
## Exercise 2:
----------------------------------------------------------
  1. Move the cursor to the start of the first line below marked --->.

  2. Press  e  until the cursor is on the end of  li .

  3. Type an  a  (lowercase) to append text AFTER the cursor.

  4. Complete the word like the line below it.  Press <ESC> to exit Insert
     mode.

  5. Use  e  to move to the next incomplete word and repeat steps 3 and 4.

---> This line will allow you to practice appending text to a line.
---> This line will allow you to practice appending text to a line.

NOTE:  a, i and A all go to the same Insert mode, the only difference is where
       the characters are inserted.


----------------------------------------------------------
## Exercise 3:
----------------------------------------------------------
  1. Move the cursor to the first line below marked --->.  Move the cursor to
     the beginning of the first  xxx .

  2. Now press  R  and type the number below it in the second line, so that it
     replaces the xxx .

  3. Press <ESC> to leave Replace mode.  Notice that the rest of the line
     remains unmodified.

  4. Repeat the steps to replace the remaining xxx.

---> Adding 123 to 456 gives you 579.
---> Adding 123 to 456 gives you 579.


----------------------------------------------------------
## Exercise 4:
----------------------------------------------------------
  1. Move to the line below marked ---> and place the cursor after "a)".

  2. Start Visual mode with  v  and move the cursor to just before "first".

  3. Type  y  to yank (copy) the highlighted text.

  4. Move the cursor to the end of the next line:  j$

  5. Type  p  to put (paste) the text.  Then type:  a second <ESC> .

  6. Use Visual mode to select " item.", yank it with  y , move to the end of
     the next line with  j$  and put the text there with  p .

--->  a) this is the first item.
      b) this is the second item.


----------------------------------------------------------
## Exercise 5:
----------------------------------------------------------
  1. Search for 'ignore' by entering:  /ignore <ENTER>
     Repeat several times by pressing  n .

  2. Set the 'ic' (Ignore case) option by entering:   :set ic

  3. Now search for 'ignore' again by pressing  n
     Notice that Ignore and IGNORE are now also found.

  4. Set the 'hlsearch' and 'incsearch' options:  :set hls is

  5. Now type the search command again and see what happens:  /ignore <ENTER>

  6. To disable ignoring case enter:  :set noic

  Answer: Practiced /ignore with n, then :set ic and :set hls is, then :set noic.


