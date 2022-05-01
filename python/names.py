def save_to_file(text):

    with open('./names3.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(text))
        myfile.write('\n')

with open('data3.txt', 'r', encoding='utf-8') as file:
    data = file.read().replace(' ', '\n')
    data = data.split()
    save_to_file(data)
