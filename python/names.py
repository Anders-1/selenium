def save_to_file(text):

    with open('./names4.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(text))
        myfile.write('\n')

with open('python\data4.txt', 'r', encoding='utf-8') as file:
    data = file.read().replace(' ', '\n')
    data = data.split()
    save_to_file(data)

# Command (bash) to get final.txt from names.txt:
# sort names.txt | uniq -c | sort -nr > final.txt
