words = ["abc","bc","a","b","e"]
target1 = "ae"
target2 = "abxz"
target3 = "deab"

def canConstruct(target,words):
    if target == "":
        return True
    if target not in words:
        return False
    for word in words:
        if target.startswith(word):
            result = canConstruct(target[len(word)],words)
        if result == True:
            return result
    return False



