# more tips

# tip1
# zen of python
# we should always make our code clean and readable.
# it is helpful because if anybody read our code, or sometime in future we may need to read our code,
# then it will be lot more easier to understand what we did there in our code.
# whether we are so busy or not, we should always follow some steps to make our code an ideal one.
# it is a good habit that will help us to be a good programmar in future.

# the steps we need to follow  to code a ideal programm is called "zen of python"
# we can find zen of python by importing this module.
import this

# a interesting thing about zen of python is that-
# there are 20 principles in zen of python, but python only show 19 of them.
# some people say that, the 20th principle is for giving importance of our own opinion.
# other say that, the 20th line is a example of giving white spaces in our code.


# tip2
# PEP
# pep means python enhancements proposal.
# it means some advise from experienced python dvelopers to make python code featureful, efficient, strong and clean.
# we can find all the PEPs in this link
"""https://www.python.org/dev/peps/"""


# tip3
# -*- coding: utf-8 -*-
# what does this comment line mean?
# we can find this comment line in the beginning of many scripts.
# here one encoing is defined.
# but why this encoding? and what is for?
# we all know computer worked with binarys 0 and 1
# encoding means a maping table where it is defined that A=00100001(this is ASCII endoing table) or something like that
# but in this table there is not sufficient code of all computer programming languages for all languages of the world.
# on the other hand, we might need those characters in our code which isn't have that encoding table.
# there is another long encoding table called utf-8 encoding table.
# so if our code has a character form outside of ASCII table, we need to use this commment to tell python that,
# "bro, you need to pass this source code according to utf-8 encoding file 
# unless you wont be able to know what i am saying"
name="শাওকি"
print(name)

# by the way, it is not obious to write down # -*- coding: utf-8 -*-
# if we write # please encoding: utf-8 python will still know what we intend to do.


# tip4
#! /usr/bin/env python

# we can see this line before many scripts.
# actually this line set what will be the default intrapretar of this script.
# it means after we enter the command "chmod+x file.py" for making file.py an executable
# and then if we want to execute that file with ./file.py command, system will choose an intrepreter to execute the command.
# we will indicate the intrepreteur by this line "!/usr/bin/env python"

# here we are setting the default python script of unix system as intrepreteur.
# env is the binary which situated in unix system.
# it can automatically find all the environment variable situated in unix system.
# so we are telling python to use this system via this line.

# we can also use the path for python intrepreteur.
# different system has different path for python interpreteur.
# but if we use the above line then it will work for every interpreteur as it is an absolute path.


# tip 5
# interactive shell

# when we run a python script in the shell we generally use this command.
"python script_name.py"
# we can use the interective shell by using a -i tag in this command.
"python -i script_name.py"

# lets say we have a python script helpers where we have a function named function13.
# if we open the script using interective mode,
"python -i helpers.py"

# now we can work with this function of the helpers module within the shell.
"function13(20)"

# this could be really useful for developing and testing things like bots.
# so it will load our function script and instead of closing the script after running the code, 
# it will give us access to all the functions and variables in that script.


# tip 6
# pdb (python debugger)

# pdb can stop our script before it is executing so that we can debug.

# for example, lets say we have a simple add() function here.
def add(a,b):
    return a+b

# if we run this function with differnt data types, we will get an error in the shell.
#print(add("d",9))

# and that case we can import pdb
import pdb
# and we can call the set_trace() method to pause the execution
pdb.set_trace()
print(add("d",9))

# now we have opened the pdb. we can see the prefix name before that.
# we can now print values and if we do any mistakes we can see the error and it wont stop our code.

# we can print value by p command.
#p add(1,2)

# we can also use pdb for complex multiple level function calls.
# the great thing about pdb is that we can import it between the codes instead of importing it in the top.
# it gives us the ability to remove the importation after our work has done.