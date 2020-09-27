with open('test.txt', 'a', encoding="utf-8") as writeFile:
    writeFile.writelines(['\n', '写一行文字\n', '再写入一行文字\n'])

with open('test.txt', encoding="utf-8") as txtFile:
    print(txtFile.readlines())