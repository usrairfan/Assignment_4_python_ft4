# string concatetion (aka how to put strings togather)
# suppose we want to create a astring that says "subscribe to"____"
# youtuber = "Usra_Irfan"# some string variable

# a few ways to do this
# print("subscribe to"+" " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")
adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input ("femous person: ")
madlib = f"Computer programming is so {adj}! It makes me so excited all the time becouse \
I love to {verb1}.Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)