----------------------------------------------------------
## Exercise 1:
----------------------------------------------------------
** Read this whole exercise before executing any steps **

  1. Open the help menu for the w command,
     by typing :help w

  2. Close it by typing :q

  3. Open the help menu for the :e command,
     by typing :help :e

  4. Use the :e command to open part6.md,
     by typing :e part6.md.

  5. Come back to this file by typing :e part7.md

  Answer: Opened help with `:help w` and `:help :e`, switched files with `:e part6.md` and back with `:e part7.md`.


----------------------------------------------------------
## Exercise 2:
----------------------------------------------------------
  1. Make sure Vim is not in compatible mode:  :set nocp

  2. Look what files exist in the directory:  :!ls   or  :!dir

  3. Type the start of a command:  :e

  4. Press  CTRL-D  and Vim will show a list of commands that start with "e".

  5. Type  d<TAB>  and Vim will complete the command name to ":edit".

  6. Now add a space and the start of an existing file name:  :edit FIL

  7. Press <TAB>.  Vim will complete the name (if it is unique).

  Answer: Practiced completion with `CTRL-D` and `<TAB>` from `:e`/`:edit`.

