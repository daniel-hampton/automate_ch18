#! python3
# formFiller.py = Automatically fills in the form.

import time
import pyautogui


form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
              'robocop': 4, 'comments': 'Tell Bob I said hi.'},
             {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
              'comments': 'n/a'},
             {'name': 'Carol', 'fear': 'puppets', 'source': 'amulet',
              'robocop': 1, 'comments': 'Please take the puppets out of the'
              + ' break room.'},
             {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
              'robocop': 5, 'comments': 'Protect the innocent. Serve the '
              + 'public trust. Uphold the law.'},
             ]
pyautogui.PAUSE = 0.5

# set these to the correct coordinates for your computer.
name_field = (832, 303)  # mouseNow says first click 814, 343
submit_button = (780, 675)
submit_button_color = (72, 137, 241)
submit_another_link = (900, 231)

for person in form_data:
    # give the user a chance to kill the script
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # wait until the form page is loaded
    while not pyautogui.pixelMatchesColor(submit_button[0], submit_button[1],
                                          submit_button_color):
        time.sleep(0.5)

    # fill out the name field
    print('Entering %s info...' % (person['name']))
    pyautogui.click(name_field[0], name_field[1])
    pyautogui.typewrite(person['name'] + '\t')

    # fill out the greatest fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')

    # fill out the source of wizard powers field.
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    # fill out the robocop field.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # fill out the additional comments field
    pyautogui.typewrite(person['comments'] + '\t')

    # click submit
    pyautogui.press('enter')

    # wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # click the submit another response link.
    pyautogui.click(submit_another_link[0], submit_another_link[1])
