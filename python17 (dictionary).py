# using dictionary in python

# how to open a dictionary.
# first method-
d={}
#second method-
h=dict()
# this are the example of an empty dictionary.

# how to open a dictionary with key-value pairs?
student={"name":"Shawki", "age":"14", "courses":["math","comsci"]} 
print(student)
# colon is used to separate keys and values.
# comma is used to separate different key-value pairs. 

# dictionaries inputs are sometime called "key-value-pairs".
# how to add a key value pair in the dictionary?
d={}
d["Shawki"]=14
d["Sowad"]=15
# we can add many pair in the dictionary as we want.

# printing key's value
print(d["Shawki"])
print(d["Sowad"])

#how to change the value of a key
#this is called updating a value in the dictionary.
d["CR7"]=33
print(d["CR7"])
d["CR7"]=20
print(d["CR7"])

# We can also update values using the update method.
# this is a useful method if we want to update multiple values at a time.
student.update({"name":"as8", "age":"15", "phone":"444-4444"})
print(student)
# if we update a value which is not exits in the dictionary, it will automatically added into the dictionary.

# merging two dictionaries.
dic1={"a":1,"b":2}
dic2={"c":3,"d":4}
merge_dic={**dic1,**dic2}
print(merge_dic)

# the values can be any time.
# but the keys can only be certain type.
# keys are commonly strings and number.

# in python we can combine string and number keys in a dictionary.
d[10]=100
print(d[10])

# we can print all keys of the dictionary using keys function.
print(d.keys())
# we can print all values of the dictionary using values function.
print(d.values())
# we can print both keys and values of the dictionary using item function.
print(d.items())

# how to iterate over key value pairs?
for key, value in d.items():
    print("key: ")
    print(key)
    print("value: ")
    print(value)
    print("")
# here key, value is a variable we can name it anything we want.

# if we print a key that is not in the dictionary, python will give us an error.
# but what if we dont want to get an error?
# we can use get method instead of square brakets[].
print(d.get("Shawki"))
print(d.get("hasnine"))

# we can also specify a default value for a key which does not exist.
print(d.get("shammo", "not found"))

# how to delete a key-value pair from the dictionary?
# we can use the del function.
del student["age"]
print(student)
# we can also use pop method.
name = student.pop("name")
print(student)
print(name)
# by using pop method, the key-value pair will be deleted from the dictionary.
# but if we write name = before pop method, the value will be saved as name variable.