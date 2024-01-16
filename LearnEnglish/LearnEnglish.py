import random

# English and Hebrew chars.
eng_chars = "abcdefghijklmnopqrstuvwxyz. "
heb_chars = "אבגדהוזחטיכלמנסעפצקרשתףץןךם"


def first_change():
    i = 0
    file = open("allwords_backup.txt", encoding="utf8")
    lines = file.readlines()
    file.close()
    file = open("temp.txt", "w+", encoding="utf8")
    for line in lines:
        if line != "\n":
            if i % 2 == 0:
                line = line.replace("\n", " ")
            file.write(line)
            i += 1
    file.close()


def set_words_to_arrays(lst):
    global eng
    global heb
    global eng_chars
    global heb_chars
    eng = []
    heb = []
    for num in lst:
        file = open("allwords.txt", encoding="utf8")
        lines = file.readlines()  # Split the lines.
        file.close()
        for x in range(int(num) - 5, int(num)):  # Read each line.
            # Replace things in the line.
            lines[x] = lines[x].replace("\n", "")
            lines[x] = lines[x].replace(" - ", "-")

            # Check for English and Hebrew words and place them in their array.
            for i in range(len(lines[x])):
                if lines[x][i] in eng_chars and lines[x][i + 2] in heb_chars:
                    eng.append(lines[x][:i + 1])
                    heb.append(lines[x][i + 1:])
                    break

        # Delete all the " " (Spaces) from the end of the words.
        for i in range(len(eng)):
            if eng[i][-1] == " ":
                eng[i] = eng[i][:-1]  # The space is at the end of the word.
            if heb[i][0] == " ":
                heb[i] = heb[i][1:]  # The space is at the start of the word.


def set_words_to_dictionary_from_array():
    # Create a dictionary and fill it with the words and their translate: ("English": "אנגלית").
    global eng
    global heb
    dic = {}
    for i in range(len(eng)):
        dic[eng[i]] = heb[i]
    return dic


def get_levels(num):
    file = open("level_list.txt", encoding="utf8")
    lines = file.readlines()
    line = lines[num-1]
    levels = line.split()
    return levels


def reset_words():
    storage = open("backup_storage.txt", encoding="utf8")
    lines = storage.readlines()
    storage.close()
    allwords = open("allwords.txt", "w", encoding="utf8")
    for line in lines:
        allwords.write(line)
    allwords.close()


def learn(dic):
    words = list(dic.items())
    wrong = 0
    question = list(range(0, len(words)))
    random.shuffle(question)
    while True:
        for i in question:
            print(f"{words[i][0]} = ", end="")
            if words[i][1] == input():
                print("Good")
            else:
                print("Bad")
                wrong += 1
        if wrong == 0:
            break
        else:
            print("Try again without wrong answers.")
            wrong = 0
    print("Level Complete.")


def learn_cards(dic):
    words = list(dic.items())
    wrong = 0
    question = list(range(0, len(words)))
    while True:
        random.shuffle(question)
        for i in question:
            print(f"{words[i][0]} = ", end="")
            if input() == "":
                print("Good")
            else:
                print("Bad")
                wrong += 1
        if wrong == 0:
            break
        else:
            print("Try again without wrong answers.")
            wrong = 0
    print("Level Complete.")


def set_level_list():
    file = open("level_list.txt", "w+", encoding="utf8")
    easy = [2]
    normal = [2, 4]
    hard = [2, 4, 8]
    units = 834
    lst = list(range(1,units+1))
    lst_str = list(map(str, lst))
    for i in lst:
        file.write(str(i))
        file.write("\n")
        for dvd in hard:
            if i % dvd == 0:
                file.write(" ".join(lst_str[i-dvd:i]))
                file.write("\n")
    file.close()
    # Try to merge between this two. /\ and \/
    file = open("level_list.txt")
    lines = file.readlines()
    file.close()
    file = open("new_level_list.txt", "w+")
    for line in lines:
        line = line.replace("\n", "")
        line = line.split(" ")
        line = [int(x)*5 for x in line]
        for item in line:
            file.write(str(item)+" ")
        file.write("\n")
    file.close()


def get_line_level_number():
    # Add +1 to the "level_number.txt"
    file = open("level_number.txt")                                              # Open the file.
    num = file.readlines()[0]                                                                         # Read the number.
    new_num = int(num.replace("\x00", ""))                                                              # Delete the "\x00".
    return new_num


def set_line_level_number():
    file = open("level_number.txt", "r+")                                              # Open the file.
    num = get_line_level_number()
    file.truncate(0)                                                                   # Delete the content of the file.
    file.write(str(num+1))                                                                      # Write the next number.
    file.close()                                                                                       # Close the file.


def stage():
    first = get_line_level_number()//15 + 1
    second = get_line_level_number()
    if second % 15 == 0:
        first -= 1
    if second > 15:
        second %= 15
        if second == 0:
            second += 1
    return [first, second]


# reset_words()
# set_level_list()


print(get_levels(get_line_level_number()))


while True:
    print(f"Stage {stage()[0]}/105 - {stage()[1]}/15")
    set_words_to_arrays(get_levels(get_line_level_number()))
    dic = set_words_to_dictionary_from_array()
    print(dic)                                                                                                 # Answers
    learn_cards(dic)
    set_line_level_number()

# ---------- Instructions: ----------
# Cards Mode:
# if you know the words, press "Enter"
# else - press any key and than "Enter"

# Normal Mode:
# if you know the word, write the translation of the word to Hebrew, and than press "Enter"
# else - press "Enter"
# Attention! You have to write even the punctuation " . , - " etc.


# both = {
#
# "-" ,
# "()" ,
# "..." ,
# "," ,
#
# }
