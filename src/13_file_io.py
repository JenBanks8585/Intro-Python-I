import io

"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
print("With variable first ")
print('__________________________________')
f = open('src/foo.txt', 'r')
print(f.name)
f.close()

# using with
print('*********************************')
print("Reading contents one line each ")
print('__________________________________')
with open('src/foo.txt', 'r') as fa:
    fa_conts = fa.read()
    print(fa_conts)

print('*********************************')
print("Reading contents all in one line")
print('__________________________________')
with open('src/foo.txt', 'r') as fa:
    fa_conts = fa.readlines()
    print(fa_conts)

print('*********************************')
print("Reading contents one line at a time")
print('__________________________________')
with open('src/foo.txt', 'r') as fa:
    fa_conts = fa.readline()
    print(fa_conts)


print('*********************************')
print("Reading contents by iteration")
print('__________________________________')
with open('src/foo.txt', 'r') as fa:
    for line in fa:
        print (line) #, end = ')


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
print('*********************************')
print("Creating a file for writing")
g = open('bar.txt', 'w')
print(g.name)
g.close()

print('*********************************')
print("Creating file using with")
print('__________________________________')
with open('src/bar2.txt', 'w') as ga:
    print(ga.name)

print('*********************************')
print("Writing on file using with")
print('__________________________________')
with open('src/bar2.txt', 'w') as gb:
    gb.write("This is a sample text \n")
    gb.write("What should I write \n")
    gb.write("Who will read this? \n")

