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


def lessonFive():
    combsA = ["dkj", "dkf", "djk", "dfk", "kdj", "kdf", "kjd", "kfd",
              "jdk", "fdk", "jkd", "fkd"]
    combsB = ["dkd", "djd", "dfd", "kdk", "kjk", "kfk"]
    combsC = ["fdj", "fkj", "jdf", "jkf", "djf", "dfj", "kjf", "kfj"]
    lineLength = (len(combsA[0]) + 1) * (6 + 2 + 1) * 2  # (3+1)*9*2=72
    lines = []
    for i in range(3):  # number of lines
        line = ''
        while len(line) < lineLength:
            random.shuffle(combsA)
            for comb in combsA[:6]:
                line += comb + ' '
            random.shuffle(combsB)
            for comb in combsB[:2]:
                line += comb + ' '
            line += random.choice(combsC) + ' '
        line = line.rstrip()  # delete space at the end of text
        lines.append(line + '\n')

    file = open(f"{folderName}\\lesson_05_dkj.txt", mode='w')
    file.writelines(lines)
    file.close()
    return lines


def quatroTwoOneOne(first, second, minors):
    comb = [first, first, second, random.choice(minors)]
    random.shuffle(comb)
    comb_str = ''
    for letter in comb:
        comb_str += letter
    return comb_str


def quatroOneTwoOne(duo, minors):
    random.shuffle(minors)
    minorA = minors.pop()
    minorB = minors.pop()
    comb = [random.choice(duo), minorA, minorA, minorB]
    random.shuffle(comb)
    comb_str = ''
    for letter in comb:
        comb_str += letter
    return comb_str


def sextuplet(majors, minors):
    a, b = majors
    c, d = minors
    comb = [a, a, b, b, c, d]
    random.shuffle(comb)
    comb_str = ''
    for letter in comb:
        comb_str += letter
    return comb_str


def lessonSix():
    letters = ['d', 'k', 'f', 'j']
    lineLength = (4 + 1) * (6 * 2 + 1) + (6 + 1) * 1  # =72
    lines = []
    for i in range(3):  # number of lines
        line = ''
        while len(line) < lineLength:
            for ix in range(2):
                line += quatroTwoOneOne('d', 'k', ('f', 'j')) + ' '\
                        + quatroTwoOneOne('k', 'd', ('f', 'j')) + ' '\
                        + random.choice(['dkdk', 'kdkd']) + ' '\
                        + quatroTwoOneOne('d', 'k', ('f', 'j')) + ' '\
                        + quatroTwoOneOne('k', 'd', ('f', 'j')) + ' '
                for inx in range(4):
                    random.shuffle(letters)
                    line += letters.pop()
                letters = ['d', 'k', 'f', 'j']
                line += ' '
            line += quatroOneTwoOne(('d', 'k'), ['f', 'j']) + ' '
            line += sextuplet(['d', 'k'], ['f', 'j']) + ' '
        lines.append(line.rstrip() + '\n')  # newline ending of line

    file = open(f"{folderName}\\lesson_06_dkfj.txt", mode='w')
    file.writelines(lines)
    file.close()
    return lines


# function call+
linesLst = lessonSix()

# if __name__ == '__main__':
#     for row in linesLst:
#         print(row, end='')
