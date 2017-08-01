wordlist = ["orange", "mango", "apple", "fig", "coconut"]
character = "o"
newlist=[]

for x in wordlist:
    if (x.count("o") != 0):
        newlist.append(x)

print newlist
