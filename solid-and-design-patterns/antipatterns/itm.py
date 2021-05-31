# ITM: initialize then modify

def initial_version():
    # create empty list
    col = []
    i = 0

    # for each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        print('%d:"%s"'%(i, name))
        col.append((name, []))


def remove_comments():
    col = []
    i = 0

    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        print('%d:"%s"'%(i, name))
        col.append((name, []))


def remove_counter():
    col = []

    for i, t in enumerate(tr_elements[0]):
        name = t.text_content()
        print('%d:"%s"'%(i, name))
        col.append((name, []))


def remove_print():
    col = []

    for t in tr_elements[0]:
        name = t.text_content()
        col.append((name, []))


def remove_variable():
    col = []

    for t in tr_elements[0]:
        col.append((t.text_content(), []))


def list_comprehension():
    col = [(t.text_content(), []) for t in tr_elements[0]]
