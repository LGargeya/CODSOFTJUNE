import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql 

tasks=[] #to store all the tasks entered

#adding task

def add_task():
    
    task_string=">"+task_field.get()
    #print(task_string)
    if len(task_string.strip()) == 1:
        messagebox.showinfo('Error','Field is empty')
    else:
        tasks.append(task_string)
        #print(task_string)
        the_cursor.execute('insert into tasks values (?)',(task_string,))
        
        list_update()  
        # deleting the entry in the entry field  
        task_field.delete(0, 'end')  
#updating the list

def list_update():  
    # calling the function to clear the list  
    clear_list()  
    # iterating through the strings in the list  
    for task in tasks:  
        #
        #  to insert the tasks in the list box

        task_listbox.insert('end',task)

# defining the function to delete a task from the list  
def delete_task():   
    try:  
        # getting the selected entry from the list box  
        the_value = task_listbox.get(task_listbox.curselection())  
        # checking if the stored value is present in the tasks list  
        if the_value in tasks:  
            # removing the task from the list  
            tasks.remove(the_value)  
            # calling the function to update the list  
            list_update()  
            # using the execute() method to execute a SQL statement  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        # displaying the message box with 'No Item Selected' message for an exception  
        messagebox.showinfo('Error', 'Please select a task to delete...')  

# function to delete all tasks from the list  
def delete_all_tasks():  
    # displaying a message box to ask user for confirmation  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    # if the value turns to be True  
    if message_box == True:  
        # using while loop to iterate through the tasks list until it's empty   
        while(len(tasks) != 0):  
            # using the pop() method to pop out the elements from the list  
            tasks.pop()  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('delete from tasks')  
        # calling the function to update the list  
        list_update()  

# function to clear the list  
def clear_list():  
    # using the delete method to delete all entries from the list box  
    task_listbox.delete(0, 'end')  

# function to close the application  
def close():  
    # printing the elements from the tasks list  
    print(tasks)  
    # using the destroy() method to close the application  
    guiWindow.destroy()

def retrieve_database():  
    # using the while loop to iterate through the elements in the tasks list  
    while(len(tasks) != 0):  
        # using the pop() method to pop out the elements from the list  
        tasks.pop()  
    # iterating through the rows in the database table  
    for row in the_cursor.execute('select title from tasks'):  
        # using the append() method to insert the titles from the table to the list  
        tasks.append(row[0])  

#----------------------------------------------------------------------------------

# main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class  
    guiWindow = tk.Tk()  
    # setting the title of the window  
    guiWindow.title("To-Do List")  
    # setting the geometry of the window  
    guiWindow.geometry("600x600+600+150")  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    # setting the background color to #26648E  
    guiWindow.configure(bg = "#26648E")  

# using the connect() method to connect to the database  
the_connection = sql.connect('listOfTasks.db')  
# creating an object of the cursor class  
the_cursor = the_connection.cursor()  
# using the execute() method to execute a SQL statement  
the_cursor.execute('create table if not exists tasks (title text)')  

# defining frames using the tk.Frame() widget  
header_frame = tk.Frame(guiWindow, bg = "#4F8FC0")  
functions_frame = tk.Frame(guiWindow, bg = "#7df599")  
listbox_frame = tk.Frame(guiWindow, bg = "#7df599") 
# using the pack() method to place the frames in the application  
header_frame.pack(fill = "both")  
functions_frame.pack(side = "left", expand = True, fill = "both")  
listbox_frame.pack(side = "right", expand = True, fill = "both")   

# defining a label using the ttk.Label() widget  
header_label = ttk.Label(  
    header_frame,  
    text = "Your To-Do List",  
    font = ("Sans", "30"),  
    background = "#4F8FC0",  
    foreground = "#FFE3B3"  
)  
# using the pack() method to place the label in the application  
header_label.pack(padx = 20, pady = 20)  

# defining another label using the ttk.Label() widget  
task_label = ttk.Label(  
    functions_frame,  
    text = "Enter your task:",  
    font = ("Sans", "14", "bold"),  
    background = "#7df599",  
    foreground = "#778899",

)  
# using the place() method to place the label in the application  
task_label.place(x = 30, y = 40)

# defining an entry field using the ttk.Entry() widget  
# Create a custom style for the rounded entry field
style = ttk.Style()
style.configure("Rounded.TEntry", borderwidth=1, relief="solid", padding=(10, 10))
task_field = ttk.Entry(  
    functions_frame,  
    font = ("Sans Serif", "14"),  
    width = 19,  
    background = "#7df599",  
    foreground = "#A52A2A",
    style="Rounded.TEntry"  
)  
# using the place() method to place the entry field in the application  
task_field.place(x = 30, y = 70)   

# adding buttons to the application using the ttk.Button() widget  
# Create a custom style for the rounded buttons
style = ttk.Style()
style.configure(
    "Rounded.TButton",
    relief="flat",
    borderwidth=1,
    padding=(5, 5),
    background="#7df599",  
    font=("Helvetica", 12),
)

add_button = ttk.Button(  
    functions_frame,  
    text = "+ Add a Task",  
    width = 24, 
    style="Rounded.TButton", 
    command = add_task  
)  
del_button = ttk.Button(  
    functions_frame,  
    text = "- Delete a Task",  
    width = 24,  
    style="Rounded.TButton",
    command = delete_task  
)  
del_all_button = ttk.Button(  
    functions_frame,  
    text = "-Delete All Tasks",  
    width = 24, 
    style="Rounded.TButton", 
    command = delete_all_tasks  
)  
exit_button = ttk.Button(  
    functions_frame,  
    text = "~Exit",  
    width = 24, 
    style="Rounded.TButton", 
    command = close  
)  
# using the place() method to set the position of the buttons in the application  
add_button.place(x = 30, y = 120)  
del_button.place(x = 30, y = 160)  
del_all_button.place(x = 30, y = 200)  
exit_button.place(x = 30, y = 240)  

# defining a list box using the tk.Listbox() widget  

task_listbox = tk.Listbox(
    listbox_frame,
    width=30,
    height=14,
    font=("Sans Serif", "12","bold"),
    selectmode='SINGLE',
    background="#FFFFFF",
    foreground="#000000",
    selectbackground="#2a91bf",
    selectforeground="#FFFFFF"
)
# using the place() method to place the list box in the application  
task_listbox.place(x = 15, y = 63)  

# calling some functions  
retrieve_database()  
list_update()  
# using the mainloop() method to run the application  
guiWindow.mainloop()  
# establishing the connection with database  
the_connection.commit()  
the_cursor.close()  
