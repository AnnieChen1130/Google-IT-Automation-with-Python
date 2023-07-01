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

## grep:

The grep command, which stands for "global regular expression print", processes text line-by-line and prints any lines that match a specified pattern.

**grep [pattern] [file-directory]**

Here, [file-directory] is the path to the directory/folder where you want to perform a search operation. The grep command is also used to search text and match a string or pattern within a file.

**grep [pattern] [file-location]**

## cut:

The cut command extracts a given number of characters or columns from a file. A delimiter is a character or set of characters that separate text strings.

**cut [options] [file]**

For delimiter separated fields, the - d option is used. The -f option specifies the field, a set of fields, or a range of fields to be extracted.

**cut -d [delimiter] -f [field number]**

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
