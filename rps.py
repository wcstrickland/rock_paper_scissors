import random
import tkinter
from PIL import ImageTk, Image


# valid options list used for random computer selection
options = ["rock", "paper", "scissors"]

# dictionary for matching image name to index in image list
image_options = {"rock": 0, "paper": 1, "scissors": 2}


# nested dictionary system to establish relationship between 3
rules = {
    "rock": {"paper": "Loses", "scissors": "Wins"},
    "paper": {"rock": "Wins", "scissors": "Loses"},
    "scissors": {"rock": "Loses", "paper": "Wins"}
}


def _load_images():
    """
    loads images from an image file. using list of option words as an
    iterable to pick matching filenames from a folder.
    :param :
    :return:
    """
    for word in options:
        # grab image by word from list matching filename
        name = 'images/{}.png'.format(word)
        # open, resize, and convert to tk PhotoImage
        image = Image.open(name)
        image = image.resize((300, 270), Image.ANTIALIAS)
        image_object = ImageTk.PhotoImage(image)
        # append to list of images initialized around l 185
        images.append(image_object)


def _check(x, y):
    """
    when passed "rps" arguments checks to see winner
    :param x: player 1 "rps"
    :param y: player 2 "rps"
    :return: a string with result "x wins or looses" or "draw"
    """
    if x and y in rules:
        if x == y:
            return "draw"
        else:
            # uses arguments as indices of nested libraries to determine relationship
            check_result = rules[x][y]
            return x + " " + check_result
    else:
        return "invalid input"


def _computer_turn():
    """
    randomly selects rock, paper or scissors and populates the computer
    canvas with corresponding image
    :return: object produced from random selection, importantly the same one
    used to select object
    """
    # randomly selects from rps in options and binds to object
    random_choice = random.choice(options)
    # object is used as look up in dictionary and the result indexes a list of images
    random_image_object = images[image_options[random_choice]]
    # image populates computer canvas
    computer_choice_frame.create_image(50, 10, image=random_image_object, anchor='nw')
    # object is returned rather than random choice to keep result and image congruent
    return random_choice


def _recolor(x):
    """
    sets the result box to red for loss, green for win, and white for draw
    :param x: the return of a check() from a button press
    :return:
    """
    if "Win" in x:
        result.configure(background='green')
    elif "Lose" in x:
        result.configure(background='red')
    else:
        result.configure(background='white')


def _press_rock():
    """
    checks an argument of rock against a random selection using "check()"
    bypasses need for passing arguments to allow button binding
    :return: .set()s a result text entry in gui with return of performed check
    """
    press_rock_result = _check("rock", _computer_turn())
    result_text.set(press_rock_result)
    _recolor(press_rock_result)
    rock_image_object = images[image_options["rock"]]
    player_choice_frame.create_image(50, 10, image=rock_image_object, anchor='nw')


def _press_paper():
    """
    checks an argument of rock against a random selection using "check()"
    bypasses need for passing arguments to allow button binding
    :return: .set()s a result text entry in gui with return of performed check
    """
    press_paper_result = _check("paper", _computer_turn())
    result_text.set(press_paper_result)
    _recolor(press_paper_result)
    paper_image_object = images[image_options["paper"]]
    player_choice_frame.create_image(50, 10, image=paper_image_object, anchor='nw')


def _press_scissors():
    """
    checks an argument of rock against a random selection using "check()"
    bypasses need for passing arguments to allow button binding
    :return: .set()s a result text entry in gui with return of performed check
    """
    # runs check() of scissors against random computer input
    press_scissors_result = _check("scissors", _computer_turn())
    # populates the result field with return of check()
    result_text.set(press_scissors_result)
    # recolor()s according to result
    _recolor(press_scissors_result)
    # creates image object for scissors input via dictionary key
    scissors_image_object = images[image_options["scissors"]]
    # and finally populates the player canvas with the image
    player_choice_frame.create_image(50, 10, image=scissors_image_object, anchor='nw')


def _play_again():
    """
    resets the game to starting state(currently only clears result_text)
    :return:
    """
    global computer_choice_frame
    global player_choice_frame
    # reset result box
    result_text.set("")
    # reset color
    _recolor("draw")
    # destroy and recreate canvas for player and computer
    computer_choice_frame.destroy()
    computer_choice_frame = tkinter.Canvas(main_window, relief="sunken", borderwidth=1)
    computer_choice_frame.grid(row=0, column=1, sticky='ew', columnspan=1, rowspan=1)
    player_choice_frame.destroy()
    player_choice_frame = tkinter.Canvas(main_window, relief="sunken", borderwidth=1)
    player_choice_frame.grid(row=1, column=1, sticky='ew', columnspan=1, rowspan=1)


# $$$$$$$$$$$$  MAIN WINDOW

main_window = tkinter.Tk()
main_window.title("Rock Paper Scissors")
main_window.geometry('590x600+500+300')
main_window['padx'] = 10

# ############# WEIGHTS

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=200)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)

main_window.rowconfigure(0, weight=200)
main_window.rowconfigure(1, weight=200)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=1)


# ###########   CHOICE CANVAS

computer_choice_frame = tkinter.Canvas(main_window, relief="sunken", borderwidth=1)
computer_choice_frame.grid(row=0, column=1, sticky='ew', columnspan=1, rowspan=1)

computer_choice_label = tkinter.Label(main_window, text="computer")
computer_choice_label.grid(row=0, column=0, sticky='ew')

player_choice_frame = tkinter.Canvas(main_window, relief="sunken", borderwidth=1)
player_choice_frame.grid(row=1, column=1, sticky='ew', columnspan=1, rowspan=1)

player_choice_label = tkinter.Label(main_window, text="player")
player_choice_label.grid(row=1, column=0, sticky='ew')


# $$$$$$$$$$$$$$ CHOICE BUTTONS

rock_button = tkinter.Button(main_window, text="ROCK", command=_press_rock)
paper_button = tkinter.Button(main_window, text="PAPER", command=_press_paper)
scissors_button = tkinter.Button(main_window, text="SCISSORS", command=_press_scissors)
play_again_button = tkinter.Button(main_window, text="PLAY AGAIN", command=_play_again)

rock_button.grid(row=2, column=1, sticky='ne')
paper_button.grid(row=2, column=1, sticky='n')
scissors_button.grid(row=2, column=1, sticky='nw')
play_again_button.grid(row=3, column=1, sticky='sew')

# #################### RESULT BOXES

result_label_frame = tkinter.LabelFrame(main_window, text="result")
result_label_frame.grid(row=1, column=2, columnspan=2)
# initializes string variable object to be referenced in Entry widget
result_text = tkinter.StringVar()
result = tkinter.Entry(result_label_frame, textvariable=result_text)
result.grid(row=1, column=2, columnspan=2, sticky='sw')

# ########### LOAD IMAGES

# initializes list for load_images() to .append to
images = []
# calls load_images() function on folder: images
_load_images()

main_window.mainloop()
