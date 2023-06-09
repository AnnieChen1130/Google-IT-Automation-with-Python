# Editing Files using Substrings
### Introduction
In this lab, you'll change the username of your coworker Jane Doe from "jane" to "jdoe" in compliance with company's naming policy. The username change has already been done. However, some files that were named with Jane's previous username "jane" haven't been updated yet. To help with this, you'll write a bash script and a Python script that will take care of the necessary rename operations.

What you'll do

Practice using the cat, grep, and cut commands for file operations
* Use > and >> commands to redirect I/O stream
* Replace a substring using Python
* Run bash commands in Python

### Prerequisites
For this lab, you should have a sound knowledge of these Linux commands:

* cat
* grep
* cut

## cat:

The cat command allows us to create single or multiple files, view the contents of a file, concatenate files, and redirect output in terminal or other files.

**cat [file]**

_Example:_

cat list.txt

![Alt text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/cat.png)

## grep:

The grep command, which stands for "global regular expression print", processes text line-by-line and prints any lines that match a specified pattern.

**grep [pattern] [file-directory]**

Here, [file-directory] is the path to the directory/folder where you want to perform a search operation. The grep command is also used to search text and match a string or pattern within a file.

**grep [pattern] [file-location]**

_Example:_

Let's try out the commands we learned in the previous section to catch all the "jane" lines.

grep 'jane' ../data/list.txt

This returns all the files with the pattern "jane". It also matches the file that has string "janez" within it.

![Alt_text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/catch-all-the-jane-lines.png)

Now, we'll list only the files containing the string "jane" and not include "janez".

grep ' jane ' ../data/list.txt

This now returns only files containing the string "jane".

![Alt-text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/catch-jane-only-exclude-janez.png)

## cut:

The cut command extracts a given number of characters or columns from a file. A delimiter is a character or set of characters that separate text strings.

**cut [options] [file]**

For delimiter separated fields, the - d option is used. The -f option specifies the field, a set of fields, or a range of fields to be extracted.

**cut -d [delimiter] -f [field number]**

_Example:_ 

Next, we'll use the cut command with grep command. For cut command, we'll use the whitespace character (‘ ‘) as a delimiter (denoted by -d) since the text strings are separated by spaces within the list.txt file. We'll also fetch results by specifying the fields using -f option.

Let's fetch the different fields (columns) using -f flag :

grep " jane " ../data/list.txt | cut -d ' ' -f 1

![Alt_text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/cut-grep-f1.png)

grep " jane " ../data/list.txt | cut -d ' ' -f 2

![Alt_text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/cut-grep-f2.png)

grep " jane " ../data/list.txt | cut -d ' ' -f 3

![Alt_text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/cut-grep-f3.png)

You can also return a range of fields together by using:

grep " jane " ../data/list.txt | cut -d ' ' -f 1-3

To return a set of fields together:

grep " jane " ../data/list.txt | cut -d ' ' -f 1,3


## Linux I/O Redirection
Redirection is defined as switching standard streams of data from either a user-specified source or user-specified destination. Here are the following streams used in I/O redirection:

Redirection into a file using **>**

Append using **>>**

Redirection into a file

Each stream uses redirection commands. A single greater than sign (>) or a double greater than sign (>>) can be used to redirect standard output. If the target file doesn't exist, a new file with the same name will be created.

Commands with a single greater than sign (>) overwrite existing file content.

**cat > [file]**

Commands with a double greater than sign (>>) do not overwrite the existing file content, but it will append to it.

**cat >> [file]**

So, rather than creating a file, the >> command is used to append a word or string to the existing file.

## Create a file using a Redirection operator
We'll now use the redirection operator (>) to create an empty file simply by specifying the file name. The syntax for this is:

**> [file-name]**

Let's create a file named test.txt using the redirection operator.

**> test.txt**

![Alt_text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/Create-a-file-using-a-Redirection-operator.png)

To append any string to the test.txt file, you can use another redirection operator (>>).

**echo "I am appending text to this test file" >> test.txt*

You can view the contents of the file at any time by using the cat command.

**cat test.txt**

![Alt_text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/append-any-string-to-the-test-txt-file.png)

## Test command
We'll now use the test command to test for the presence of a file. The command test is a command-line utility on Unix-like operating systems that evaluates conditional expressions.

The syntax for this command is:

**test EXPRESSION**

We'll use this command to check if a particular file is present in the file system. We do this by using the -e flag. This flag takes a filename as a parameter and returns True if the file exists.

We'll check the existence of a file named jane_profile_07272018.doc using the following command:

**if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi**

![Alt_text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/check-the-existence-of-a-file.png)

## Iteration
Another important aspect of a scripting language is iteration. Iteration, in simple terms, is the repetition of a specific set of instructions. It's when a set of instructions is repeated a number of times or until a condition is met. And for this process, bash script allows three different iterative statements:

* For: A for loop repeats the execution of a group of statements over a set of items.
* While: A while loop executes a set of instructions as long as the control condition remains true.
* Until: An until loop executes a set of instructions as long as the control condition remains false.

Let's now iterate over a set of items and print those items.

**for i in 1 2 3; do echo $i; done**

![Alt_text](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course2-Using-Python-to-Interact-with-the-Operating-System/Lab6-Editing-Files-Using-Substrings/images/for-loop-scripting.png)





