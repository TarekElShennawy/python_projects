element_list = ['h1','h2','h3','h4','h5','h6',
                'p', 'hr', 'a', 'ul', 'ol',
                'li', 'img', 'div', 'span']
a = 0
id_nr = 0
class_nr = 0
element_nr = 0

#Ask the user for the number of identifiers
print("How many selectors?")
selectors_nr = input()


i = 0
while i != int(selectors_nr):
    selector_input = input()
    word_list = selector_input.split()
    character_list = list(selector_input)
    
    for character in character_list:
        if character == "#":
            id_nr += 1
        elif character == ".":
            class_nr += 1
            
    for word in word_list:
        if word in element_list:
            element_nr += 1

    priority_level = str(id_nr) + str(class_nr) + str(element_nr)
    print("The priority level is " + priority_level)
    i += 1
