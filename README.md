# folder_organizer

version: 0.1 

Description:
------------- 
Got a cluttered folder that needs organizing? Folder organizer can look at the extensions of all files in a folder that you provide as input and it helps segregate them based on their extensions.

This approach/python program does not help you completely in organizing your folder , it helps you place same file extensions within a single folder which then later helps you clear them(move/delete etc..) easily , looking at a smaller subset of files than looking at an entire huge set of files helps in organization, thats the whole idea behind folder organizer.

Specifications:
----------------
Extensions that the folder organizer can currently handle.
    "pdf" <br />
    "exe" <br />
    "msi" <br />
    "txt" <br />
    "zip" <br />
    "log" <br />
Sample output after running the script.<br />
    input  => C:\Users\<user>\Downloads <br />
    output => below directories will be created within the above folder and places the files inside them based on their extenions. <br />
    "pdf_files" <br />
     - contains all pdf files <br />
    "exe_files" <br />
     - contains all *.exe files. <br />
    .....

Coming up soon in next version (0.2):
------------------------------------
 - allow to add more extensions via a json file. <br />
 - add logging to understand better the file categorization steps. <br />
