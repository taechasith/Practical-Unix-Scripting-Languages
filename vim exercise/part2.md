----------------------------------------------------------
## Exercise 1:
----------------------------------------------------------
  1. Press  <ESC>  to make sure you are in Normal mode.

  2. Move the cursor to the line below marked --->.

  3. Move the cursor to the beginning of a word that needs to be deleted.

  4. Type   dw	 to make the word disappear.

  5. Repeat steps 3 and 4 until the sentence is correct.

---> There are a some words fun that don't belong paper in this sentence.

  NOTE: The letter  d  will appear on the last line of the screen as you type
	it.  Vim is waiting for you to type  w .  If you see another character
	than  d  you typed something wrong; press  <ESC>  and start over.


----------------------------------------------------------
## Exercise 2:
----------------------------------------------------------
  1. Press  <ESC>  to make sure you are in Normal mode.

  2. Move the cursor to the first line below marked --->.

  3. Press $ to go to the end of this line.

  3. Move the cursor to the end of the correct line (AFTER the first . )
     by pressing h multiple times.

  4. Type    d$    to delete to the end of the line.

  5. Repeat exercises 1-3 on the second line below marked --->

  6. Press capital D to delete to the end of the line

---> Somebody typed the end of this line twice. end of this line twice.

---> Somebody typed the end of this line twice. end of this line twice.


----------------------------------------------------------
## Exercise 3:
----------------------------------------------------------
  1. Move the cursor to the start of the line below marked --->.

  2. Type  2w  to move the cursor two words forward.

  3. Type  3e  to move the cursor to the end of the third word forward.

  4. Type  0  (zero) to move to the start of the line.

  5. Repeat steps 2 and 3 with different numbers.

---> This is just a line with words you can move around in.


----------------------------------------------------------
## Exercise 4:
----------------------------------------------------------
  1. Move the cursor to the first UPPER CASE word in the line marked --->.

  2. Type  d2w  to delete the two UPPER CASE words.

  3. Repeat steps 1 and 2 with a different count to delete the consecutive
     UPPER CASE words with one command.

--->  this ABC DE line FGHI JK LMN OP of words is Q RS TUV cleaned up.


----------------------------------------------------------
## Exercise 5:
----------------------------------------------------------
  1. Move the cursor to the second line in the phrase below.
  2. Type  dd  to delete the line.
  3. Now move to the fourth line.
  4. Type   2dd   to delete two lines.

--->  1)  Roses are red,
--->  2)  Mud is fun,
--->  3)  Violets are blue,
--->  4)  I have a car,
--->  5)  Clocks tell time,
--->  6)  Sugar is sweet
--->  7)  And so are you.


----------------------------------------------------------
## Exercise 6:
----------------------------------------------------------
   ** Press  u	to undo the last commands,   U  to fix a whole line. **

  1. Move the cursor to the line below marked ---> and place it on the
     first error.
  2. Type  x  to delete the first unwanted character.
  3. Now type  u  to undo the last command executed.
  4. This time fix all the errors on the line using the  x  command.
  5. Now type a capital  U  to return the line to its original state.
  6. Now type  u  a few times to undo the  U  and preceding commands.
  7. Now type CTRL-R (keeping CTRL key pressed while hitting R) a few times
     to redo the commands (undo the undo's).

---> Fiix the errors oon thhis line and reeplace them witth undo.

