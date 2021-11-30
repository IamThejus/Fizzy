# GUI For Fizzy

from main import*
from tkinter import*
from tkinter import messagebox

# Functions

def save_student_details():
	roll=en_roll.get()
	name=en_stname.get()
	gen=en_gen.get()
	bg=en_bg.get()
	fam=en_fam.get()
	passw=get_credentials()['Pass']
	student_details(roll,name,gen,bg,fam,passw)
	messagebox.showinfo('Fizzy System Info','The deatails entered have been successfully saved in student details')

def save_cred():
    passw=en_pass.get()
    name=en_name.get()
    ocp=en_ocp.get()
    create_credentials(passw,name,ocp)
    create_database(passw)
    create_table_studnet(passw)
    user_script(name)
    messagebox.showinfo('Fizzy System Info','The credentials you have entered has been saved successfully.\nA new database called Fizzy has been created.')
    cred_window.destroy()

def save_in_txt():
	passw=get_credentials()['Pass']
	show_student_details(passw)
	messagebox.showinfo('Fizzy System Info','The students deatails has been saved in a text format named Students Deatails.txt')

# Check Credentials


if check_credentials()==True:
	credentials=get_credentials()
	passw=credentials['Pass']
	try:
		create_table_studnet(passw)
	except:
		pass
else:
	create_folders()
	# Creating window for getting credentials
	cred_window=Tk()
	cred_window.geometry('300x100')
	cred_window.title('Fizzy Credentials')

	# Creating Widgets
	l_name=Label(cred_window,text='Name')
	l_ocp=Label(cred_window,text='Occupation')
	l_pass=Label(cred_window,text='Mysql Password')
	
	en_name=Entry(cred_window,width=30)
	en_ocp=Entry(cred_window,width=30)
	en_pass=Entry(cred_window,width=30)
	
	cred_button=Button(cred_window,text='Save',command=save_cred)

	# Postioning For Widgets
	l_name.grid(column=1,row=1)
	l_ocp.grid(column=1,row=2)
	l_pass.grid(column=1,row=3)
	en_name.grid(column=2,row=1)
	en_ocp.grid(column=2,row=2)
	en_pass.grid(column=2,row=3)
	cred_button.grid(column=1,row=4)
	cred_window.mainloop()

# Main Window

# Creating window
main_window=Tk()
main_window.geometry('380x140')
main_window.title('Fizzy')


# Creating Widgets
l_roll=Label(main_window,text='Roll No.')
l_name=Label(main_window,text='Name')
l_gen=Label(main_window,text='Gender(M/F)')
l_bg=Label(main_window,text='Blood Group')
l_fam=Label(main_window,text='Family Members No.')

en_roll=Entry(main_window,width=30)
en_stname=Entry(main_window,width=30)
en_gen=Entry(main_window,width=30)
en_bg=Entry(main_window,width=30)
en_fam=Entry(main_window,width=30)

save_stud=Button(main_window,text='Save Deatails',command=save_student_details)
save_txt=Button(main_window,text='Save In Txt',command=save_in_txt)

# Postioning Widgets
l_roll.grid(column=1,row=1)
l_name.grid(column=1,row=2)
l_gen.grid(column=1,row=3)
l_bg.grid(column=1,row=4)
l_fam.grid(column=1,row=5)

en_roll.grid(column=2,row=1)
en_stname.grid(column=2,row=2)
en_gen.grid(column=2,row=3)
en_bg.grid(column=2,row=4)
en_fam.grid(column=2,row=5)

save_stud.grid(column=1,row=6)
save_txt.grid(column=2,row=6)


main_window.mainloop()