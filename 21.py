# str2 = '''
# hello class!!
# welcome
# start the test'''
# str2 = "hello class!!\nweelcome\nstart the test"
# print(str2)
# str = input("Enter a string : ")

# str1 = "hello"
# str2 = " wolrd"
# str3 = "14"
# str4 = str1+str2
# print(str4)
# str5 = str1+str3
# print(str5)


# from itertools import count


# word = input("Enter a string : ")

# l = len(word)
# print(l)
# count = 0
# for i in word:
#     count = count + 1
#     if count == l:
#         print(i)
#     else:
#         print(i, end=",")

# word = input("Enter a stirng : ")
# l = len(word)

# i = 0
# while (i < l):
#     print(word[i], end=",")
#     i = i + 1

# str1 = input("Enter a string : ")
# str2 = str1[::]
# print(str2)

# str1 = input("Enter a string : ")
# str2 = ""
# for i in str1:
#     str2 = str2+i

# print(str2)
# ls = ["apple", "aaa"]
# ls.sort()
# print(ls)

text = (input("Enter : ")).split(" ")
str = ""
for i in text:
    if text.count(i) >= 2:
        str += i
print(str)
