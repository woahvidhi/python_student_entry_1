from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import socket
import bs4
import requests

#code for buttons

def UpdateReset():
	entUpdateRno.delete(0,END)
	entUpdateMarks.delete(0,END)
	entUpdateRno.focus()
def AddReset():
	entAddRno.delete(0,END)
	entAddMarks.delete(0,END)
	entAddName.delete(0,END)
	entAddRno.focus()
def f1():
# to go to add page
	add.deiconify()
	root.withdraw()

def f2():
# to go to main page from add page
	root.deiconify()
	add.withdraw()
def f4():
#to go to view page
	view.deiconify()
	root.withdraw()
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql="select rno, name, marks from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		mdata=""
		for d in data:

			mdata = mdata + str(d[0])+ " " + d[1] + " => " + str(d[2]) + "\n"
		stData.insert(INSERT, mdata)
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Failure",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f5():
# to go to main page from view page
	view.withdraw()
	root.deiconify()
	stData.delete(1.0,END)

def f6():
# to go to update page
	root.withdraw()
	update.deiconify()

def f7():
# to go to main page from update page
	update.withdraw()
	root.deiconify()

def f9():
# to go to delete page
	root.withdraw()
	delete.deiconify()

def f10():
# to go to main page from delete page
	delete.withdraw()
	root.deiconify()
def f12():
# to go to graph page
	root.withdraw()
	graph.deiconify()

def f13():
# to go to main page from graph page
	graph.withdraw()
	root.deiconify()

# code for main page

root = Tk()
root.title("S.M.S.")
root.geometry("500x500+450+150")
root.configure(background = 'SlateBlue3')

btnAdd = Button(root, text = 'ADD', bg = '#00FFFF', foreground ='white',width = 10, font = ('Constantia', 18, 'bold'), command = f1)
btnView = Button(root, text = 'VIEW', bg = '#00CCFF', foreground ='white', width = 10, font = ('Constantia', 18, 'bold'), command = f4)
btnUpdate = Button(root, text = 'UPDATE', bg = '#0099FF', foreground ='white', width = 10, font = ('Constantia', 18, 'bold'), command = f6)
btnDelete = Button(root, text = 'DELETE', bg = '#0066FF', foreground ='white', width = 10, font = ('Constantia', 18, 'bold'), command = f9)
btnGraph = Button(root, text = 'GRAPH', bg = '#0033FF', foreground ='white', width = 10, font = ('Constantia', 18, 'bold'), command = f12)

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)

#***************************************************************

# functions for add page
def f3():
# to insert record into database

	import cx_Oracle
	con = None
	cursor = None
	try:
		name = None
		marks = None
		rno = None
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql="insert into student values ('%d','%s','%d')"
		rno=int(entAddRno.get())
		name=entAddName.get()
		marks=int(entAddMarks.get())
		args =(rno,name,marks)
		cursor.execute(sql % args)
		if rno<=0:
			con.rollback()
			msg = "Rno. can not be negative"
			messagebox.showerror("Failure",msg)
			entAddRno.delete(0,END)
			entAddRno.focus()
		elif marks<0 or marks>100:
			con.rollback()	
			msg = "Marks to be entered should be between 0 to 100 only"
			messagebox.showerror("Failure",msg)
			entAddMarks.delete(0,END)
			entAddMarks.focus()
		elif len(name)<2:
			con.rollback()
			msg = "Name has to be min. letters"
			messagebox.showerror("Failure",msg)
			entAddName.delete(0,END)
			entAddName.focus()
		elif not name.isalpha():
			con.rollback()
			msg = "Name should contain only letters"
			messagebox.showerror("Failure",msg)
			entAddName.delete(0,END)
			entAddName.focus()
		else:
			con.commit()
			msg = str(cursor.rowcount)+" record inserted" 
			messagebox.showinfo("Success",msg)
			AddReset()
	except ValueError:
		con.rollback()
		msg = "Only integers to be entered in marks and rno entry box"
		messagebox.showerror("Failure",msg)
		entAddMarks.delete(0,END)
		entAddRno.delete(0,END)
		entAddRno.focus()
	except cx_Oracle.DatabaseError:
		con.rollback()
		msg = "Rno. already exists"
		messagebox.showerror("Failure",msg)
		entAddRno.delete(0,END)
		entAddRno.focus()

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

# code for add page

add = Toplevel(root)
add.title('ADD S.')
add.geometry("500x500+450+150")
add.withdraw()
add.configure(background = 'SlateBlue3')

lblAddRno = Label(add, text = 'Enter Rno', font = ('Constantia', 18, 'bold'),bg = 'SlateBlue3',fg = 'white' )
entAddRno =  Entry(add, bd= 5)
lblAddName = Label(add, text = 'Enter Name', bg = 'SlateBlue3',fg = 'white', font = ('Constantia', 18, 'bold'))
entAddName =  Entry(add, bd= 5)
lblAddMarks = Label(add, text = 'Enter Marks',bg = 'SlateBlue3',fg = 'white',  font = ('Constantia', 18, 'bold'))
entAddMarks = Entry(add, bd= 5)
btnAddSave = Button(add, text = 'SAVE',bg = '#0033FF',fg='white', font = ('Constantia', 18, 'bold'), command = f3)
btnAddBack = Button(add, text = 'BACK',bg = '#0066FF',  fg='white',font = ('Constantia', 18, 'bold'), command = f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

# code for temp

try:
	socket.create_connection(("www.google.com", 80))
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"#link
	a2 ="&q=" + 'mumbai'#city data
	a3 = "&appid=c6e315d09197cec231495138183954bd"#userid
	api_address= a1+a2+a3
	res1 = requests.get(api_address)

	data=res1.json()
	main=data['main']
	temp=main['temp']
except OSError as e:
	messagebox.showerror("Failure",e)

# code of quote

res=requests.get("http://www.brainyquote.com/quotes_of_the_day.html")
soup=bs4.BeautifulSoup(res.text,'lxml')
quote=soup.find('img',{"class":"p-qotd"})
text=quote['alt']

#code for display

lblquote = Label(root, text = "QOTD "+ text,bg = 'SlateBlue3',fg = 'white', font=("Constantia",10,"bold"))
lbltem = Label(root, text = "TEMPERATURE "+ str(temp),bg = 'SlateBlue3',fg = 'white', font=("Constantia",14,"bold"))

lblquote.pack(pady=10)
lbltem.pack(pady=10)

#***************************************************************

# code for view
view = Toplevel(root)
view.title('VIEW S.')
view.geometry("500x500+450+150")
view.withdraw()
view.configure(background = 'SlateBlue3')

stData= scrolledtext.ScrolledText(view, width=40, height=10,bg ='SkyBlue',foreground='black')
btnBack = Button(view, text="BACK", width=10,font=("Constantia",14,"bold"), command=f5,bg = '#0033FF', foreground='white')

stData.pack(pady=10)
btnBack.pack(pady=10)

#***************************************************************
#function for update page

def f8():
# to update database
	import cx_Oracle
	con = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "update student set marks = '%d' where rno = '%d' "
		rno = int(entUpdateRno.get())
		marks = int(entUpdateMarks.get())
		args = (marks, rno)
		cursor.execute(sql % args)
		if rno<=0:
			con.rollback()
			msg = "Rno. can not be negative"
			messagebox.showerror("Failure",msg)
			entUpdateRno.delete(0,END)
			entUpdateRno.focus()
		elif marks<0 or marks>100:
			con.rollback()	
			msg = "Marks to be entered should be between 0 to 100 only"
			messagebox.showerror("Failure",msg)
			entUpdateMarks.delete(0,END)
			entUpdateMarks.focus()
		else:
			con.commit()
			msg = str(cursor.rowcount)+" record inserted" 
			messagebox.showinfo("Success",msg)
			UpdateReset()
	except ValueError:
		con.rollback()
		msg = "Only integers to be entered in marks and rno entry box"
		messagebox.showerror("Failure",msg)
		UpdateReset()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

# code for update page

update = Toplevel(root)
update.title('UPDATE S.')
update.geometry("500x500+450+150")
update.withdraw()
update.configure(background = 'SlateBlue3')

lblUpdateRno = Label(update, text='Enter Rno', font = ('Constantia', 18, 'bold'),bg = 'SlateBlue', foreground='white')
entUpdateRno = Entry(update, bd = 5)
lblUpdateMarks = Label(update, text = 'Enter Marks', font = ('Constantia', 18, 'bold'),bg = 'SlateBlue', foreground='white')
entUpdateMarks = Entry(update, bd= 5)
btnUpdateSave = Button(update, text = 'SAVE', font = ('Constantia', 18, 'bold'), command = f8,bg = '#0033FF',fg='white')
btnUpdateBack = Button(update, text = 'BACK', font = ('Constantia', 18, 'bold'), command = f7 ,bg = '#0066FF',  fg='white')

lblUpdateRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblUpdateMarks.pack(pady=10)
entUpdateMarks.pack(pady=10)
btnUpdateSave.pack(pady=10)
btnUpdateBack.pack(pady=10)


#***************************************************************
#functions for delete page

def f11():
	import cx_Oracle
	con = None
	cursor = None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "delete from student where rno='%d'"
		rno = int(entDeleteRno.get())
		args=(rno)
		cursor.execute(sql%args)
		if rno<=0:
			con.rollback()
			msg = "Rno. can not be negative"
			messagebox.showerror("Failure",msg)
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
		elif cursor.rowcount == 0:
			con.rollback()
			msg = "Roll no. doesnt exist"
			messagebox.showerror("Failure",msg)
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
		else:
			con.commit()
			msg = str(cursor.rowcount)+" record deleted" 
			messagebox.showinfo("Success",msg)
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure",e)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
	except ValueError :
		con.rollback()
		msg = "Roll. no should be a integer"
		messagebox.showerror("Failure",msg)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

# code for delete page

delete = Toplevel(root)
delete.title('DELETE S.')
delete.geometry("500x500+450+150")
delete.withdraw()
delete.configure(background = 'SlateBlue3')

lblDeleteRno = Label(delete, text='Enter Rno', font = ('Constantia', 18, 'bold'),bg = 'SlateBlue', foreground='white')
entDeleteRno = Entry(delete, bd = 5)
btnDeleteSave = Button(delete, text = 'SAVE', font = ('Constantia', 18, 'bold'), command = f11,bg = '#0033FF',  fg='white')
btnDeleteBack = Button(delete, text = 'BACK', font = ('Constantia', 18, 'bold'), command = f10,bg = '#0066FF',  fg='white')

lblDeleteRno.pack(pady=10)
entDeleteRno.pack(pady=10)
btnDeleteSave.pack(pady=10)
btnDeleteBack.pack(pady=10)

#***************************************************************

# functions for graph page
def f14(n):
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql="select name, marks from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		stats = []
		tmarks = []
		tname = []
		for d in data:
			stats.append((d[1],d[0]))
			tmarks.append(d[1])
			tname.append(d[0])
		stats.sort(reverse = True)
		marks=[]
		name=[]
		for s in range(5):
			sdata = stats[s]
			marks.append(sdata[0])
			name.append(sdata[1])

		op = o.get()
		from matplotlib import pyplot as plt

		if op == 1:
			if n == 2:
				plt.bar(name, marks)	
				plt.grid()
				plt.title('REPORT')
				plt.xlabel('NAMES OF STUDENTS ---> ')
				plt.ylabel('MARKS OBTAINED ---> ')
				plt.show()
			else:
				plt.bar(tname, tmarks)
				plt.grid()
				plt.title('REPORT')
				plt.xlabel('NAMES OF STUDENTS  ---> ')
				plt.ylabel('MARKS OBTAINED  ---> ')
				plt.show()				
		else:
			if n == 2:
				plt.plot(name, marks, linewidth = 3, marker="o", markersize=10)
				plt.xlabel("NAMES OF STUDENTS  ---> ")
				plt.ylabel("MARKS OBTAINED ---> ")
				plt.title('REPORT')
				plt.grid()
				plt.show()
			else:
				plt.plot(tname, tmarks, linewidth = 3, marker="o", markersize=10)
				plt.xlabel("NAMES OF STUDENTS  ---> ")
				plt.ylabel("MARKS OBTAINED ---> ")
				plt.title('REPORT')
				plt.grid()
				plt.show()
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Failure",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()	
# code for graph page

graph = Toplevel(root)
graph.title('GRAPH S.')
graph.geometry("500x500+450+150")
graph.withdraw()
graph.configure(background = 'SlateBlue3')

o = IntVar()

rbGraphBar = Radiobutton(graph,bg='SlateBlue',fg='white', text="BAR GRAPH", font=('Constantia', 18, 'bold'), variable = o, value=1)
rbGraphLine = Radiobutton(graph,bg='SlateBlue',fg='white', text="LINE GRAPH", font=('Constantia', 18, 'bold'), variable = o, value=2)
btnGraphAll = Button(graph, text = 'OVER ALL', bg='#0099FF',fg='white',font = ('Constantia', 18, 'bold'), command = lambda:f14(1))
btnGraphFive = Button(graph, text = 'TOP FIVE', bg='#0066FF',fg='white',font = ('Constantia', 18, 'bold'), command = lambda:f14(2))
btnGraphBack = Button(graph, text = 'BACK',bg='#0033FF',fg='white', font = ('Constantia', 18, 'bold'), command = f13)

o.set(1)

rbGraphBar.pack(pady=10)
rbGraphLine.pack(pady=10)
btnGraphFive.pack(pady=10)
btnGraphAll.pack(pady=10)
btnGraphBack.pack(pady=10)






root.mainloop()