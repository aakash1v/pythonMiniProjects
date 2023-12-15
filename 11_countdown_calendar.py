from tkinter import Tk, Canvas
from datetime import date, datetime

def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            print(current_event)
            event_date = datetime.strptime(current_event[1], '%d/%m/%y')
            current_event[1] = event_date.date()
            list_events.append(current_event)
    return list_events

def days_between_dates(date1, date2): 
    time_between = str(date1-date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]



root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold underline', text='My Countdown Calendar')
#c.create_text(100, 50, anchor='w', fill='pink', font='Courier 36 bold underline',text='Mk's Diary Dates')

events = get_events()
today = date.today()


vertical_space = 150

events.sort(key=lambda x: x[1])
for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = f'It is {days_until} days until {event_name}'
    if (int(days_until) <= 7):
        text_col = 'red'
    else:
        text_col = 'lightblue'
    c.create_text(100, vertical_space, anchor='w', fill=text_col,font='Arial 28 bold', text=display)
    vertical_space = vertical_space + 50
