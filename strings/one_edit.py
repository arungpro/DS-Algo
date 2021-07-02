'''
Write a function that returns whether two words are exactly "one edit" away using the following signature:

    bool OneEditApart(string s1, string s2);

An edit is:
-----------
- Inserting one character anywhere in the word (including at the beginning and end)
- Removing one character
- Replacing one character
Examples:
    OneEditApart("cat", "dog") = false
    OneEditApart("cat", "cats") = true
    OneEditApart("cat", "cut") = true
    OneEditApart("cat", "cast") = true
    OneEditApart("cat", "at") = true
    OneEditApart("cat", "act") = false
'''
def createStringDict(s):
    sDict = {}
    for ele in s:
        if ele in sDict.keys():
            sDict[ele] += 1
        else:
            sDict[ele] = 1
    return sDict

def oneEditApart(s1, s2):
    # case 1
    # General check. Removing one character or Insert 1 character
    onEdit = False
    if(s1.lengh == s2.length || s1.lengh == s2.length - 1 || s1.lengh == s2.length + 1):
        onEdit = True
    else:
        return onEdit
    

    