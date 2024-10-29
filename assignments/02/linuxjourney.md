## Assignment 23.10.2024
See: https://linuxjourney.com/lesson/the-shell  
1. #### The Shell
   What should be outputted to the display when you type echo Hello World?  
   `Hello World`  
   Exercise:
   ```sh
   $ date
   Mon Oct 28 16:18:11     2024
   $ whoami
   muell
   ```
2. #### pwd (Print Working Directory)
   How do I find what directory you are currently in?  
   `pwd`
3. #### cd (Change Directory)
   If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use?  
   `cd ..`  
   Exercise:
   ```sh
   cd
   MINGW64 ~
   ```
4. #### ls (List Directories)
   What command would you use to see hidden files?  
   `ls -a`  
   Exercise:
   ```
   ls -R: recursively list directory contents
   ls -r: reverse order while sorting
   ls -t: sort by modification time, newest first
   ```
5. #### touch
   How do you create a file called myfile?  
   `touch myfile`  
   Exercise:
   ```sh
   muell@DESKTOP-87H28LA MINGW64 ~/Desktop/TH-Köln/3_Semester/DIS08
   $ touch myfile
   
   muell@DESKTOP-87H28LA MINGW64 ~/Desktop/TH-Köln/3_Semester/DIS08
   $ ls -l
   total 4
   -rw-r--r-- 1 muell 197611    0 Oct 28 16:46 myfile
   
   muell@DESKTOP-87H28LA MINGW64 ~/Desktop/TH-Köln/3_Semester/DIS08
   $ touch myfile
   
   muell@DESKTOP-87H28LA MINGW64 ~/Desktop/TH-Köln/3_Semester/DIS08
   $ ls -l
   total 4
   -rw-r--r-- 1 muell 197611    0 Oct 28 16:46 myfile
   ```
6. #### file
   What command can you use to find the file type of a file?  
   `file`  
   Exercise:  
   ```sh
   $ file myfile
   myfile: empty
   ```
7. #### cat
   What's a good way to see the contents of a file?  
   `cat`  
   Exercise:  
   ```sh
   $ cat hallo.txt test.txt
   ```
8. #### less
   How do you quit out of a less command?  
   `q`  
9. #### history
   What is the command to clear the terminal?  
   `clear`  
10. #### cp (Copy)
    What flag do you need to specify to copy over a directory?  
    `-r`
11. #### mv (Move)
    How do you rename a file called cat to dog?  
    `mv cat dog`
12. #### mkdir (Make Directory)
    What command is use to make a directory?  
    `mkdir`
13. #### rm (Remove)
    How do you remove a file called myfile?  
    `rm myfile`  
    Exercise:
    ```sh
    $ touch -- -file
    $ rm -file
    ```
14. #### find
    What option should I specify for find if I want to search by name?  
    `-name`  
    Exercise:  
    ```sh
    $ cd
    $ find . -name net
    ```
15. #### help
    How do you get quick command line help for built-in bash commands?  
    `help`  
    Exercise:  
    ```sh
    $ help echo
    echo: echo [-neE] [arg ...]
    Write arguments to the standard output.

    Display the ARGs, separated by a single space character and followed by a
    newline, on the standard output.

    Options:
      -n        do not append a newline
      -e        enable interpretation of the following backslash escapes
      -E        explicitly suppress interpretation of backslash escapes

    `echo' interprets the following backslash-escaped characters:
      \a        alert (bell)
      \b        backspace
      \c        suppress further output
      \e        escape character
      \E        escape character
      \f        form feed
      \n        new line
      \r        carriage return
      \t        horizontal tab
      \v        vertical tab
      \\        backslash
      \0nnn     the character whose ASCII code is NNN (octal).  NNN can be
                0 to 3 octal digits
      \xHH      the eight-bit character whose value is HH (hexadecimal).  HH
                can be one or two hex digits
      \uHHHH    the Unicode character whose value is the hexadecimal value HHHH.
                HHHH can be one to four hex digits.
      \UHHHHHHHH the Unicode character whose value is the hexadecimal value
                HHHHHHHH. HHHHHHHH can be one to eight hex digits.

    Exit Status:
    Returns success unless a write error occurs.

    muell@DESKTOP-87H28LA MINGW64 ~/Desktop/TH-Köln/3_Semester/DIS08
    $ help logout
    logout: logout [n]
    Exit a login shell.

    Exits a login shell with exit status N.  Returns an error if not executed
    in a login shell.

    muell@DESKTOP-87H28LA MINGW64 ~/Desktop/TH-Köln/3_Semester/DIS08
    $ help pwd
    pwd: pwd [-LPW]
    Print the name of the current working directory.

    Options:
      -L        print the value of $PWD if it names the current working
                directory
      -P        print the physical directory, without any symbolic links
      -W        print the Win32 value of the physical directory

    By default, `pwd' behaves as if `-L' were specified.

    Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read.

    ```
16. #### man
    How do you see the manuals for a command?  
    `man`  
17. #### whatis
    What command can you use to see a small description of a command?  
    `whatis`
18. #### alias
    What command is used to make an alias?  
    `alias`  
    Exercise:  
    ```sh
    $ alias foo='ls -la'
    $ foo
    % unalias foo
    ```
19. #### exit
    How can you exit from the shell?  
    `exit`
