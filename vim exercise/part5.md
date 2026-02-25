----------------------------------------------------------
## Exercise 1:
----------------------------------------------------------
  1. Type the familiar command	:  to set the cursor at the bottom of the
     screen.  This allows you to enter a command-line command.

  2. Now type the  !  (exclamation point) character.  This allows you to
     execute any external shell command.

  3. As an example type   ls   following the ! and then hit <ENTER>.  This
     will show you a listing of your directory, just as if you were at the
     shell prompt.  Or use  :!dir  if ls doesn't work.


----------------------------------------------------------
## Exercise 2:
----------------------------------------------------------
  1. Type  :!dir  or  :!ls  to get a listing of your directory.
     You already know you must hit <ENTER> after this.

  2. Choose a filename that does not exist yet, such as TEST.

  3. Now type:	 :w TEST   (where TEST is the filename you chose.)

  4. This saves the whole file (these exercises) under the name TEST.
     To verify this, type    :!dir  or  :!ls   again to see your directory.

NOTE: If you were to exit Vim and start it again with  vim TEST , the file
      would be an exact copy of these exercises when you saved it.

  5. Now remove the file by typing (Unix):	 :!rm TEST

----------------------------------------------------------
## Exercise 3:
----------------------------------------------------------
  1. Move the cursor to this line.

  2. Press  v  and move the cursor to the fifth item below.  Notice that the
     text is highlighted.

  3. Press the  :  character.  At the bottom of the screen  :'<,'> will appear.

  4. Type  w TEST  , where TEST is a filename that does not exist yet.  Verify
     that you see  :'<,'>w TEST  before you press <ENTER>.

  5. Vim will write the selected lines to the file TEST.  Use  :!dir  or  :!ls
     to see it.  Do not remove it yet!  We will use it in the next lesson.

----------------------------------------------------------
## Exercise 4:
----------------------------------------------------------
  1. Place the cursor just above this line.

  2. Now retrieve your TEST file using the command   :r TEST   where TEST is
     the name of the file you used.
     The file you retrieve is placed below the cursor line.

  3. To verify that a file was retrieved, cursor back and notice that there
     are now two copies of exercise 3, the original and the file version.

