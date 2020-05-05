# module 30
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
# somepeople say that, the 20th principle is for giving importance of our own opinion.
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