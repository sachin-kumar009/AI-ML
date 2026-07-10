# Q1 
def countChar(S):
  return [S.count('A'),S.count('D')]

str = "AbaDd"
strCharCount = countChar(str)
print(strCharCount)
  

# Q2
def CountHead(S):
    ans = ""
    for ch in sorted(set(S)):
        if S.count(ch) > 1:
            ans += ch + str(S.count(ch)) + " "
    return ans.strip()

str = "prepbytes"
print(CountHead(str))

# Q3
def Count_Vowel(S):
    return S.lower().count('a') + S.lower().count('e') + S.lower().count('i') + S.lower().count('o') + S.lower().count('u')

str = "Prepbytes"
print(Count_Vowel(str))

# Q4
def Concatenate_Strings(S1, S2):
    return S1 + S2

str1 = "Prep"
str2 = "bytes"
print(Concatenate_Strings(str1, str2))

# Q5
def findLength(S):
    count = 0
    for i in S:
        count += 1
    return count

str = "CeDqe"
print(findLength(str))

# Q6
def Game_Winner(S):
    if S.count('A') > S.count('D'):
        return "Aditya"
    elif S.count('A') < S.count('D'):
        return "Danish"
    else:
        return "Draw"

str = "ADDAAADDDDD"
print(Game_Winner(str))

# Q7
def joinStrings(S, P):
    return "".join([S, P])

str1 = "PrepBytes"
str2 = "Technologies"
print(joinStrings(str1, str2))


# Q8
def joinStrings(S, P):
    return "".join([S, P])

str1 = "PrepBytes"
str2 = "Technologies"
print(joinStrings(str1, str2))

# Q9
def Plain_Check(S):
    return S == S[::-1]

str = "naman"
print(Plain_Check(str))


# Q10
def String_Match(S1, S2):
    return "YES" if S1 == S2 else "NO"

str1 = "Prepbytes"
str2 = "Prepbytes"
print(String_Match(str1, str2))

# Q11
def Replace(S, pattern, text):
    return S.replace(pattern, text)

str = "Hi, I am You."
print(Replace(str, "You", "Prepbytes"))

# Q12
def Split_the_String(S):
    return S.split()

str = "I am utkarsh raj"
print(Split_the_String(str))

# Q13
def Count_Vowels(S):
    S = S.lower()
    return S.count('a') + S.count('e') + S.count('i') + S.count('o') + S.count('u')

def Count_Consonants(S):
    return sum(ch.isalpha() for ch in S) - Count_Vowels(S)

str = "Prepbytes"
print(Count_Vowels(str))
print(Count_Consonants(str))