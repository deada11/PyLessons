import os.path

answer = open('answer.txt', 'w')
for cur_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith('.py'):
            answer.write(cur_dir + '\n')
            break
answer.close()
