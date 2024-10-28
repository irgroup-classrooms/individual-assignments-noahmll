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
    
