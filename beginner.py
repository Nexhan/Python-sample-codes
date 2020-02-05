#Separation of list from a dictionary

#separation of English and French word from a dictionary
#making a list of separated English and french word
language = {
    "hello":"Bonjour",
    "tea":"the",
    "coffee":"cafe"
}

English= []           #empty list to add a English language
French=[]           #empty list to add a French language

for Eng in language.keys():
    English.append(Eng)

print(English)

for fren in language.values():
    French.append(fren)

print(French)
