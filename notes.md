## Important things to consider:
// Use to check different positions of something(often string)
for letter in range(len(s) - 1): // Need -1 as without it can lead to index error because it needs to check that it can +1 the index to check the other part
    if s[letter] == s[letter + 1]:
Using .lower() returns a new string so need to set it to a variable even if its same variable that I am currently using.
Using not in will if a value is absent from a collection while something like != will only check if the values are different. Ex: for item in something: or for item not in something:






























