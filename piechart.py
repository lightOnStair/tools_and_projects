import turtle
turtle.speed(10)
turtle.hideturtle()
def vowelCount(astring):
    '''This function works as the argument of pieChart(),determines the
       individual vowel frequencies and returns the counts ina Python list
    '''
    #count the frequencies of a,e,i,o,u
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    freq_list = []
    for i in range(len(astring)):
        if astring[i] == "a" or astring[i] == "A":
            count_a += 1
        if astring[i] == "e" or astring[i] == "E":
            count_e += 1
        if astring[i] == "i" or astring[i] == "I":
            count_i += 1
        if astring[i] == "o" or astring[i] == "O":
            count_o += 1
        if astring[i] == "u" or astring[i] == "U":
            count_u += 1
    #put the result in a list in order
    freq_list += [count_a] + [count_e] + [count_i] + [count_o] + [count_u]
    return freq_list

def one_wedge(degree):
    '''to draw a wedge and fill it without specific color.'''
    turtle.begin_fill()
    turtle.right(90)
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(200,degree)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.end_fill()

def only_one_wedge():
    '''This function works in pieChart when there only exists one vowel,for
       avoiding leaving single straight line in the piechart and making the
       response clearer.
    '''
    turtle.penup()
    turtle.begin_fill()
    turtle.forward(200)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(200)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def char_mark(deg_list):
    '''This part work as a part in pieChart(), to mark the vowels letter that
       one wedge represents.
    '''
    i = 0
    vowel_lst = ['A','E','I','O','U']
    while i in range(5) :
        if deg_list[i] != 0:
            turtle.penup()
            turtle.left(deg_list[i] / 2)
            turtle.forward(100)
            turtle.write(vowel_lst[i],font=("Arial",15, "normal"),
            align = "center")
            turtle.right(180)
            turtle.forward(100)
            turtle.right(180 - deg_list[i] / 2)
            i += 1
        else:
            i += 1


def pieChart(flist):
    '''This function will generate a pieChart from a frequencies list of
       vowel
    '''
    # deal with special cases(when there is no or only one vowel)
    ssum = flist[0] + flist[1] + flist[2] + flist[3] + flist[4]
    if ssum == 0:
        turtle.color("black","white")
        only_one_wedge()
        turtle.write("no vowel detected", font=("Arial",15, "normal"),
        align = "center")
        return
    else:
        if flist[0] + flist[1] + flist[2] + flist[3] == 0:
            turtle.color("black","orange")
            only_one_wedge()
            turtle.write("U", font=("Arial",15, "normal"),align = "center")
            return
        if flist[1] + flist[2] + flist[3] + flist[4] == 0:
            turtle.color("black","yellow")
            only_one_wedge()
            turtle.write("A", font=("Arial",15, "normal"),align = "center")
            return
        if flist[2] + flist[3] + flist[4] + flist[0] == 0:
            turtle.color("black","grey")
            only_one_wedge()
            turtle.write("E", font=("Arial",15, "normal"),align = "center")
            return
        if flist[3] + flist[4] + flist[0] + flist[1] == 0:
            turtle.color("black","green")
            only_one_wedge()
            turtle.write("I", font=("Arial",15, "normal"),align = "center")
            return
        if flist[4] + flist[0] + flist[1] + flist[2] == 0:
            turtle.color("black","lightblue")
            only_one_wedge()
            turtle.write("O", font=("Arial",15, "normal"),align = "center")
            return

    # draw piechart in normal cases(when there are at least two vowel letters
    # showing up)
    prop_list = []
    for i in range(len(flist)):
        prop_list += [flist[i] / ssum]
    color_lst = ['yellow','grey','green','lightblue','orange']
    ii = 0
    while ii < 5:
        if prop_list[ii] != 0:
            turtle.color("black",color_lst[ii])
            one_wedge(360 * prop_list[ii])
            ii += 1
        else:
            ii += 1


    # to mark the vowel letters that every wedge represents. !note: one color
    # always corresponds to one vowel
    degree_list =[]
    for iii in range(len(prop_list)):
        degree_list += [360 * prop_list[iii]]
    turtle.right(90)
    char_mark(degree_list)

def legend():
    '''a simple legend for the piechart'''
    turtle.penup()
    turtle.setpos(0,350)
    turtle.write("yellow for A, grey for E, green for I, lightblue for O, orange for U",
    font = ("Arial",15, "normal"),align = "center")

def main():
    '''input a string in turtle window and return a piechart that reflects the
       propotion of vowels.
    '''
    pieChart(
    vowelCount(
    turtle.textinput(
    "vowel frequencies piechart generator","please in put a string:"
    )))
    legend()
    return

if __name__ == '__main__':
    main()
