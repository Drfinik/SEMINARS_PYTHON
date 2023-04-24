# Задача №27. 
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# my_string = input("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells")
# my_string = "She sells, sea shells on the sea shore. The shells\
#  that she sells are sea shells! I'm sure So if she sells sea \
# shells on the sea shore? I'm sure that\n the shells are sea \
# shore shells"
# result = [i.strip('.,?!\n').lower() for i in my_string.split()]
# result = set(result)
# print(result)
# print(len(result))


# str_split = input("Enter some text: ").lower().split()
# str_cnt = {}
# for i in str_split:   
#     str_cnt[i] = str_cnt.get(i, 0) + 1

# print(f"Number of words in the text is: {len(str_cnt)}")


# import string


# my_string = "She sells, sea shells on the sea shore. The shells that she sells are sea shells! I'm sure So if she sells sea shells on the sea shore? I'm sure that the shells are sea shore shells".lower()
# for ch in string.punctuation:
#     my_string = my_string.replace(ch,' ')
    
# result = set(my_string.split)
# print(result)
# print(len(result))

n = int(input())
max_number = -1
while n !=0:
    if n > max_number:
        max_number = n
    n = int(input())

