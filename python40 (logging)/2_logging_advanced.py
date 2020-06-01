# advanced logging
# in this module, we will learn about loggers, different handlers and some other things.

# here we have two files calc.py and employee.py. there we have some code.
# actually, throughout this module we will code there and comment here.
# so we have to follow both at a time.

""" go to calc.py """
""" go to employee.py """


# first lets go to calc.py and run that file.
# we can see that it creates a Calc_Log.log file and we can see our formatting there.

# now lets go to employee.py file and run that.
# we can see it creates a Employee_Log.log file with our format.

# we haven't deiscusseed what this root message mean yet.
# this message specifies that we are working with the root logger.
# this isnt a bad thing when we are working with smaller applications and specific files.
# but it is best to build the habit of logging with specific loggers that can all be configured separately.

# but working with this root logger isn't the best idea. why?
# let us first delete this Calc_Log.log and  Employee_Log.log files.

# now if we are working with 2 modules then we can import one to another.
# lets just import employee module in the calc module. 

# when we import a module it runs all the code from that module when it was imported.
# so if we run this calc.py module it will log our all employees

# we can see that we have Employee_Log.log file here.
# but our Calc_Log.log file that we specify in this module isn't created.

# so what happened here?
# the reason it do something like that it is because when we set up this logger here whitin this employee class,
# it configures the root logger there with that Employee_Log.log file name, log level and format.
# and that happen first because we have imported calc.py file.
# and this module is sharing that logger.
# so by the time we get to configuring within this module, the logger already figured with those other values.
# so this doesn't actually do anything, it doesn't overwrite the previous initial configuration.
# the reason is that our log statements are logging down at the bottom is that the root logger is set to the info level in calc.py module.
# so the debug doesn't hit that level.

# if we change the debug to info and rerun this.
# we can see in Employee_Log.log file it did log the information from this module.
# but this is still kind of mess as we are sharing this root logger.
# we are not getting the file or the format or the level that we want.

# so lets get a logger for each of our modules so that we can configure them separately.
# in the employee.py module,
        # lets comment out the previous code and follow steps below:
        # 1. we will create a variable loggers = logging.getLogger()
            # now we need to specify any naming in the getLogger() function.
            # but the convention is __name__ variable.
            # so if we run this file derectly, this __name__ will be equal to "__main__"
            # if we import that in another module then it will be its own module name.
            # now we are getting a new logger here if it doesn't exits it will be created.
        # 2. now we should use the logger variable to run the log method.
            # NOTE: when we are writing logging.info, instead of that we will write logger.info
            # one nice thing about this loggers, is that they are within the hierarchy.
            # it means if this employee logger doesn't have something set, then it will fall back to the root logger.
            # for example, this logging.basicConfig() we still configuring the root logger.
            # if we run this module, we can see that it doesn't print anything in the console, it print the message in the Employee_Log.log file.
            # here we can see the logger is now set to __main__
        # 3. now lets configure the logging with the our logger, not the root logger.
        # 4. first to specify the employee.log file that we want to log to we have to add a file handler.
            # so we will create a new variable file_handler = logging.FileHandler("Employee_Log.log") # we need to pass the name of our log file here.
        # 5. now we have this file_handler but it need to be added to our logger.
            # to do that we can say, logger.addHandler(file_handler)
        # 6. now we need the formatting to be same that we specify in our basicConfig()
            # NOTE: we need to add this formatting to the file_handler not to the logger.
        # 7. first lets create a formatter variable, formatter=logging.Formatter("%(levelname)s:%(name)s:%(message)s")
            # now we need to add this to our file handler.
            # we can do this by, file_handler.setFormatter(formatter)
        # 8. and lastly lets set the log_level in this employee logger.
            # to do this we can say, logger.setLevel(logging.INFO)
        # 9. now lets delete our basicConfig() and Employee_Log.log file.
        
        # now rerun out loggingA.helpers module.
        # now we can see that it logs all the messages with correct format.
        # now lets back to our current script.

# before that it was giving us problem because we are sharing the root logger.
# but we rerun this now, we can see this time it created a new Calc_Log.log file with our specific format.
# in this case it stills the root logger.
# in employee.log file, we can see this prints the message correctly and it gave the name calc.py to the logger this time because we imported it.

# now quickly set up a logger for our this calc.py module.
# first lets comment out the previous code and write them again in below.

# now if we rerun this calc.py module and see to our log files.
# we can see that everything is working as we thought.
# now, lets delete this log files once again.

# one good thing for logging like this is that now we got a lot more flexibility, its nice how this hierarchy works.
# for example, we wanted our logger level debug but we only wanted our errors or worst to get logged to Calc_Log.log file.
# to do this, we can set level to the file_handler as well.

# so if we want to keep our logger level to debug but only capture the errors or above, in this specific file handler
# then we can, file_handler.setLevel(logging.ERROR)

# now if we run this we can see it created our log file.
# but there is nothing in our Calc_Log.log
# it didnt log those debug statements because the logging statements doesn't match.
# lets put some error in our code of calc.py file.

# now if we run that and go to Calc_Log.log file we can see it logged our error.
# NOTE: anytime we will logging an error, we should include traceback so that we can get multiple information about what exactly happened.
# and the logging module allows us to do this very easily.
# we can do this by changing the logging.error() to logging.exception().

# now if we run this calc.py file again, we can see that we get the traceback in our log file.

# another good thing is that it is easy to add multiple handlers to loggers.
# for example, lets say we want to see this debug statements that we are executing in the bottom.
# but we only want to display those to the console.
# what we can do here is that we can create another handler but instead of a fileHandler(), we will create a StreamHandler().

# now if we run the calc.py module, we can see it log our debug and error in the console, 
# and the error is only printed to the log file.
# one thing to notice here is that, the formatting to the console insn't same that we have here in the log file.
# but we can set the formatter for stream_handler like the file_handler.

# now we can run that and see that the format is changed.
# we can also create a new formatter and change the format as well.



# every projects need logging to their production point.
# good logs can save us from headache of lots of debug problems.
# we can do lot more advanced and complex thing in logging.
# we can learn them in python documentation and we can look at other handlers that python have.
# there are some handlers that send us email when some error occurs or something like that.
# they also have rotating logs so that one log file doesn't build up too much.
