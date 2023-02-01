f = open('raw.txt', 'r')

content = []

for i in f:
    print(i)
    content.append(i)



print(content)


raw_change = open('change.txt', 'a')

raw_change.write(f' content = {content} ')
raw_change.write('\n')
raw_change.write('\n')
raw_change.write('\n')


raw_change.close()

