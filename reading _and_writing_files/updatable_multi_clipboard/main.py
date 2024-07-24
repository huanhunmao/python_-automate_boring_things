import shelve, pyperclip, sys

# 更新剪切板内容，并  python main.py save <key> 这样运行和存储
# python main.py list
# command + v 就能看到存的东西

try:
    mcbShelf = shelve.open('mcb')

    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
        else:
            print("Error: Invalid command or key.")
    else:
        print("Usage: python script.py [save <key>|list|<key>]")

finally:
    mcbShelf.close()
