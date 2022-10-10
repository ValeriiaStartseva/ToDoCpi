user_input = 'random'
data = list()  # Create a list of storing data
marked_items = list()  # Create a list of storing Done items


def showMenu():
    print('Menu:')
    print('1 - Add an item')
    print('2 - Remove an item')
    print('3 - Mark an item as done')
    print('4 - List items')
    print('5 - Exit')


while user_input != '5':

    showMenu()
    user_input = input('Enter your choice: ')

    if user_input == '1':  # adding item
        item = input('What is to be done?')
        data.append(item)
        print('Added item!', item)
    elif user_input == '2':  # remove item
        item = input('Which item you want to remove?')
        if item in data:
            data.remove(item)
            print('Removed item', item)
        else:
            print('Item does not exist in the to-do list!')
    elif user_input == '3':  # marked done
        item = input('Which is to be done?')
        if item in data:
            marked_items.append(item)
            data.remove(item)
            print('Item was done', item)
        else:
            print('Item does not exist in the to-do list!')
    elif user_input == '4':
        print('List of to-do items: ')
        for items in data:
            print(items)


