# Replace oldsubstr with newsubstry without using the startswith or endswith methods
def findAndReplace(text, oldsubstr, newsubstr):
    newtext = "" 
    text_i = 0
    old_i = 0
    while text_i < len(text):
        if text[text_i] == oldsubstr[old_i]:
            old_i += 1
            if old_i == len(oldsubstr):
                old_i = 0
            newtext += newsubstr
            text_i += len(oldsubstr)
        else:
            newtext += text[text_i]
            text_i += 1
    return newtext

def findAndReplaceList(lst, old_sublist, new_sublist):
    result = []
    i = 0
    while i < len(lst):
        if lst[i:i+len(old_sublist)] == old_sublist:
            result.extend(new_sublist)
            i += len(old_sublist)
        else:
            result.append(lst[i])
            i += 1
    return result


# multiple assert statements to test the function
assert findAndReplace("hello world", "hello", "goodbye") == "goodbye world"
assert findAndReplace("hello world", "world", "python") == "hello python"
assert findAndReplace("hello world", "hello", "hi") == "hi world"
assert findAndReplace("hello world", "world", "universe") == "hello universe"
assert findAndReplace("hello world there", "there", '') == "hello world "
assert findAndReplace(" ", " ", "hello world") == "hello world"