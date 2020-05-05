# module 35
# hiding secret keys.

# we will learn how we can save seccret keys in environment variable and use that in our python module.

# if people working with databases and accessing api, then they need a secret key or password.
# they directly use their secret key in the python script,
# the problem is that if we are working with a team, or pushing our code to a repository,
# then anyone who see that code with access to our secret information.

# if we save the secret key in the environment variable,
# then we can still share our code to others but our secret information will save to the local machine.

# here we have some fake information.
import os

db_user="user123"
db_password="pass_user123"

print(db_user)
print(db_password)

# so lets move this to environment variables.
# setting environment variable in windows and linux machine is different.
# we will set it to our windows machine here.

# FOLLOW THIS STEPS:
# open the control panel.
# system and security.
# advanced system settings.
# environment variables.

# now within here we can add new user variables or new system variables.
# for our purposes use variables are going to be fine. so we can add to those.

# click new
# enter variable name and value(set variable for username)
# again click new
# set  variable for password
# click ok
# we might need to restart our IDE or editor to make those changes take effect.

# now we can access this.
# to access this we need to import the os module.
# we can access this variables with os.environ dictionary
# we can access the keys of the dictionary just by the get method.
# then we can pass in the keys which are the variables name that we setted earliar.
import os

db_user=os.environ.get("DB_USER")
db_password=os.environ.get("DB_PASS")

# now without actually writting the secret keys in our script we can access those keys.
print(db_user)
print(db_password)
# thats going to be a lot more easier for us,
# since we dont need to be worried about our secret being exposed to the source code.


# there is another method of hiding secret information.

# inputting secret information
# we should keep sensative information in environment variables.
# what if we need to type in a password for our script?
# in order to do this python have a built_in function that will help us out.
# and that function called getpass from getpass module.
# but first look at the wrong way to do this?
username=input("Username: ")
password=input("Password: ")
print("logging you in ...........")
# when we run this code, we could see when we input our password that typed down in our screen which we definately dont want.
# if we are using our program in front of others, we simply dont want that to display that in the screen for everyone to see.
# python has a built_in module called getpass for this type of secret operation.
from getpass import getpass
# and now instead of using input in our password line here, we need to use getpass.
username=input("Username: ")
password=getpass("Password: ")
print("logging you in ...........")
# now we can see that there is a lock sign when we are typing our passwod.
# and when we are done we cant find any passworb in the terminal.
# thats a lot more secure if we want to accept password form a user.