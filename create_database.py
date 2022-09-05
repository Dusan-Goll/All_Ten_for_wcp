# TODO: * create lesson One --> DONE
#       * create lesson Two and Three --> DONE
#       * create lesson Four

import random
folderName = "lessons_database"


def lessonOne():
    combs = ["fj", "jf", "jj", "ff"]
    lineLength = 3 * len(combs) * 6  # = 72
    lines = []
    for i in range(2):  # number of lines
        line = ''
        while len(line) < lineLength:
            random.shuffle(combs)
            for comb in combs:
                line += comb + ' '
        line = line.rstrip()  # delete space at the end of text
        lines.append(line + '\n')

    file = open(f"{folderName}\\lesson_01_fj.txt", mode='w')
    file.writelines(lines)
    file.close()
    return lines


def lessonTwo():
    combsA = ["fjf", "jfj", "fjf", "jfj"]
    combsB = ["ffj", "jff", "fjj", "jjf", 'fff', 'jjj']
    lineLength = (len(combsA[0]) + 1) * 9 * 2  # (3+1)*9*2=72
    lines = []
    for i in range(2):  # number of lines
        line = ''
        while len(line) < lineLength:
            for comb in combsA:
                line += comb + ' '
            random.shuffle(combsB)
            for comb in combsB[1:]:
                line += comb + ' '
        line = line.rstrip()  # delete space at the end of text
        lines.append(line + '\n')

    file = open(f"{folderName}\\lesson_02_fjf.txt", mode='w')
    file.writelines(lines)
    file.close()
    return lines


def lessonThree():
    combsA = ["jfjf", "fjjf", "jffj", "fjfj"]
    combsB = ["fj", "jf"]
    combsC = ["fjf", "jfj"]
    lineLength = ((len(combsA[0]) + 1) * 4 + (len(combsB[0]) + 1) * 4
                  + (len(combsC[0]) + 1)) * 2  # ((4+1)*4+(2+1)*4+(3+1))*2=72
    lines = []
    for i in range(3):  # number of lines
        line = ''
        while len(line) < lineLength:
            random.shuffle(combsA)
            for comb in combsA:
                line += comb + ' '
            random.shuffle(combsB)
            for ix in range(2):
                for comb in combsB:
                    line += comb + ' '
            line += random.choice(combsC) + ' '
        lines.append(line.rstrip() + '\n')  # newline ending of line

    file = open(f"{folderName}\\lesson_03_fjjf.txt", mode='w')
    file.writelines(lines)
    file.close()
    return lines


def lessonFour():
    combs = ["dk", "kd", "dd", "kk"]
    lineLength = (len(combs[0]) + 1) * len(combs) * 6  # = 72
    lines = []
    for i in range(2):  # number of lines
        line = ''
        while len(line) < lineLength:
            random.shuffle(combs)
            for comb in combs:
                line += comb + ' '
        line = line.rstrip()  # delete space at the end of text
        lines.append(line + '\n')

    file = open(f"{folderName}\\lesson_04_dk.txt", mode='w')
    file.writelines(lines)
    file.close()
    return lines


# function call+
# linesLst = lessonFour()

# if __name__ == '__main__':
#     for row in linesLst:
#         print(row, end='')
