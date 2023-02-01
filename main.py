import re

data = '<div class="filter_items"><p>name </p><p>.....999</p></div>'

content = ['SNACKS', 'QALB NIRACHATH', 'BANANA FRY', 'MUTTAPPAM', 'EGG PUFF', 'SAMOSA', 'COIN PARIPPUVADA 2PCS', 'MUTTA BHAJJI', 'PAZHAM NIRACHATHU', 'CUTLETS', 'CHICKEN WINGS 6PCS', 'POCKET CHICKEN', 'UNNAKAI', 'MALAI CUTTING CHAI', 'HUB-E-MAKAN', 'COFFEE', 'BLACK COFFEE', 'MOHABATH', 'HORLICKS', 'BOOST', 'MILK']

n = len(content)

change_data_added_list = []
for items in content:
    if not items.isspace():
        changed_data = data.replace('name', items)
        change_data_added_list.append(changed_data)

# print(change_data_added_list)

read_me = open('ready.txt', 'w')
for i in change_data_added_list:
    read_me.write(i)
    read_me.write('\n')

read_me.write('\n')
# read_me.write('\n')
# read_me.write('\n')

read_me.close()
