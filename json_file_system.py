"""json file system"""
import json

class PathEnd(Exception):
    pass

def user_input():
    """
    Gets input
    :return: list
    """
    return input('$ ').split()[1].split('/')

def read_json(path):
    """
    Reads json file
    :param path: path to the file
    :return: dict
    """
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def file_system(data:dict, inputt:list):
    """

    :param data:
    :param input:
    :return:
    """
    temp = data
    for direct in inputt:
        temp = get_from_key(temp, direct)
    return temp

def get_from_key(data, key):
    """
    Gets data using key
    :param data: dict
    :param key: key
    """
    if isinstance(data, dict):
        return data[key]
    elif isinstance(data, list):
        return data[int(key)]
    else:
        raise PathEnd()

def update(path, new_data):
    """
    Updates the path
    """
    for direct in new_data:
        if direct == '..':
            path.pop()
        else:
            path.append(direct)


def main():
    """
    Main function
    """
    print('To use json file system you need to write "cd" and then one of the given paths in the list.\n'
          'If the direction you enter is dict, you will get a list of dict key that you are to use to go further.\n'
          'If the direction you enter is list, you will get the range of list`s indexes like [0...n].\n'
          'If you already know the path, you can input it using "/" like "users/user/id/...".\n'
          'If you want to come back to a previous stage of your path, you can use "cd ..".\n'
          'To finish the program you can use next command "do exit"')
    data = read_json('file.json')
    path = []

    while True:


        try:

            current = file_system(data, path)
            if isinstance(current, dict):
                print(list(current.keys()))
            elif isinstance(current, list):
                if current and (isinstance(current[0], dict) or isinstance(current[0], list)):
                    print(f"[0...{len(current) - 1}]")
                else:
                    print(current)
            else:
                print(current)
            print("/".join(path))
            user = user_input()
            if user[0] == 'exit':
                break
            update(path, user)
        except KeyError:
            print('Wrong key!')
            path.pop()
        except ValueError:
            print('Wrong input!')
            path.pop()
        except IndexError:
            print('Wrong index! Maybe you forgot to type "cd"?')
            path.pop()
        except PathEnd:
            path.pop()
            print("End!")


if __name__ =='__main__':
    main()
