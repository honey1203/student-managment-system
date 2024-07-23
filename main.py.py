from tkinter import*
from tkinter import ttk
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("student management sytem")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="grey",fg="black")
        title.pack(side=TOP,fill=X)  
        
  #========Manage Frame=================================  
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=21,y=99,width=449,height=559)
        
        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold")) 
        m_title.grid(row=0,columnspan=2,pady=15)
        
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold")) 
        lbl_roll.grid(row=1,column=0,pady=8,padx=10,sticky="W")
        
        txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE) 
        txt_Roll.grid(row=1,column=1,pady=8,padx=10,sticky="W")
        
        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold")) 
        lbl_name.grid(row=2,column=0,pady=8,padx=10,sticky="W")
        
        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE) 
        txt_name.grid(row=2,column=1,pady=8,padx=10,sticky="W")
        
        lbl_email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold")) 
        lbl_email.grid(row=3,column=0,pady=8,padx=10,sticky="W")
        
        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE) 
        txt_email.grid(row=3,column=1,pady=8,padx=10,sticky="W")
        
        lbl_gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold")) 
        lbl_gender.grid(row=4,column=0,pady=8,padx=10,sticky="W")
        
        
        
        lbl_contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold")) 
        lbl_contact.grid(row=5,column=0,pady=8,padx=10,sticky="W")
        
        txt_contact=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE) 
        txt_contact.grid(row=5,column=1,pady=8,padx=10,sticky="W")
        
        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold")) 
        lbl_dob.grid(row=6,column=0,pady=8,padx=10,sticky="W")
        
        txt_dob=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE) 
        txt_dob.grid(row=6,column=1,pady=8,padx=10,sticky="W")
        
        lbl_address=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold")) 
        lbl_address.grid(row=7,column=0,pady=8,padx=10,sticky="W")
        
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=518,width=420,)
        
      
        
        
        
        
        
        
        
           
  #========Detail Frame=================================       
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=99,width=800,height=559) 

        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold")) 
        lbl_search.grid(row=0,column=0,pady=8,padx=10,sticky="W")
        
        
        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",15,"bold"))

        combo_search['values']=("Name","Roll No.","Enrollment")
        combo_search.grid(row=0,column=1,padx=10,pady=10)
        
        txt_search=Entry(Detail_Frame,width=20,font=("times new roman",15,"bold"),bd=5,relief=GROOVE) 
        txt_search.grid(row=0,column=2,pady=10,padx=10,sticky="W")
        
        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)
        
    
    
    
root=Tk()
ob=Student(root)
root.mainloop()