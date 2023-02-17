"""
File: babygraphics.py
Name: Matt
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    x_coordinate = int((width / len(YEARS)) * int(year_index))
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, canvas.winfo_width() - GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, canvas.winfo_height() - GRAPH_MARGIN_SIZE,
                       canvas.winfo_width() - GRAPH_MARGIN_SIZE, canvas.winfo_height() - GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, GRAPH_MARGIN_SIZE, 0, width=LINE_WIDTH, fill='black')
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i), 0,
                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH,
                           fill='black')

        canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + 5,
                           text=YEARS[i], anchor=tkinter.NW)

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    x = int(CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    y = int(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK

    for j in range(len(lookup_names)):
        for i in range(len(YEARS)-1):
            rank = name_data.get(lookup_names[j]).get(str(YEARS[i]))
            rank2 = name_data.get(lookup_names[j]).get(str(YEARS[i + 1]))
            print(YEARS[i])
            if str(YEARS[i]) in name_data[lookup_names[j]]:
                if rank is None or int(rank) > MAX_RANK:
                    y_start = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    y_start = int(rank) * y
                if rank2 is None or int(rank2) > MAX_RANK:
                    y_end = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    y_end = int(rank2) * y
            else:
                y_start = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                if rank2 is None or int(rank2) > MAX_RANK:
                    y_end = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    rank = str('*')
                else:   #想問助教，為什麼拿掉esle 下一行不work
                    y_end = int(rank2) * y

            canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i), y_start,
                               fill=COLORS[j % len(COLORS)], text=str(lookup_names[j]) + ', ' + str(rank),
                               anchor=tkinter.SW)
            canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i), y_start,
                               GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i) + x, y_end,
                               fill=COLORS[j % len(COLORS)], width=LINE_WIDTH)



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
