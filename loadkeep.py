import gkeepapi
import gpsoauth

def get_credentials():
    creds = []
    for line in open('secrets.txt', 'r'):
        creds.append(line.split('=')[1].replace('\n',''))
    return creds

def load(note_name):
    keep = gkeepapi.Keep()
    creds = get_credentials()
    print('user "' + creds[0] + '"')
    print('apppwd "' + creds[1] + '"')
    success = keep.login(creds[0], creds[1])

    note = keep.createNote('Todo', 'Eat breakfast')
    note.pinned = True
    note.color = gkeepapi.node.ColorValue.Red
    keep.sync()

def first_oauth():
    creds = get_credentials()
    gpsoauth.perform_oauth()

if __name__ == '__main__':
    load('hi')
