# Introduction to Git
### Introduction
In this scenario, you are a project lead in an IT company. You and your team are working on a huge project, which consists of multiple functionalities and modules. This project is evolving over time and so your team is expecting a lot of code revisions. In this lab, you'll learn how to use a distributed version control system called Git. You'll also discover how to connect to a VM instance, install Git, and configure your Git user information. Next, you'll create a local Git repository, add a file to the repository, and do some basic operations like adding a file, editing files, and making commits.

What you'll do
* Create a git repository.
* Add files to this repository
* Edit the files
* Commit the changes to the repository.

## Install Git
Before you install Git on your Linux VM, you need to first make sure that you have a fresh index of the packages available to you. To do that, run:

sudo apt update

Now, you can install Git on your Linux host using apt by running the following command:

sudo apt install git

For any prompts, continue by clicking Y.

Note: Installing Git may take a couple of minutes.

Check the installed version of git by using the command below:

git --version

## Initialize a new repository
Create a directory to store your project in. To do this, use the following command:

mkdir my-git-repo

Now navigate to the directory you created.

cd my-git-repo

Next, initialize a new repository by using the following command:

git init

The git init command creates a new Git repository. In our case, it transformed the current directory into a Git repository. It can also be used to convert an existing, unversioned project to a Git repository or to initialize a new, empty repository.

Executing git init creates a .git subdirectory in the current working directory, which contains all of the necessary Git metadata for the new repository. This metadata includes subdirectories for objects, refs, and template files. A HEAD file is also created which points to the currently checked out commit.

If you've already run git init on a project directory containing a .git subdirectory, you can safely run git init again on the same project directory. The operation is what we call idempotent; running it again doesn't override an existing .git configuration.

## Configure Git
Git uses a username to associate commits with an identity. It does this by using the git config command. To set Git username use the following command:

git config --global user.name "Name"

Replace Name with your name. Any future commits you push to GitHub from the command line will now be represented by this name. You can use git config to even change the name associated with your Git commits. This will only affect future commits and won't change the name used for past commits.

Let's set your email address to associate it with your Git commits.

git config --global user.email "user@example.com"

Replace user@example.com with your email-id. Any future commits you now push to GitHub will be associated with this email address. You can even use git config to change the user email associated with your Git commits.

## Git Operations
Let's now create a text file named README. We will be using the nano editor for this.

nano README

Type any text within the file, or you can use the following text:

This is my first repository.

Save the file by pressing Ctrl-o, Enter key, and Ctrl-x.

Git is now aware of the files in the project. We can check the status using the following command:

git status

This command displays the status of the working tree. It also shows changes that have been staged, changes that haven't been staged, and files that aren't tracked by Git.


