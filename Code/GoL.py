import copy
from Tkinter import *
def init_table():
    global A,COR,X,Y
    for i in range(len(COR)):
        X.append(COR[i][0])
        Y.append(COR[i][1])
    for k in range(len(X)):
        for i in range(N):
            for j in range(M):
                if j==X[k] and i==Y[k]:
                    A[i][j]=1
def glider():
    global COR
    COR=[[28,26],[29,27],[29,28],[28,28],[27,28]]
    tochoice()

def GGG():
    global A,COR,X,Y
    COR=[[14,26],[15,26],[14,27],[15,27],[22,27],[22,28],[23,28],[23,26],[24,26],
    [24,27],[30,28],[30,29],[30,30],[31,28],[32,29],[36,26],[37,26],[36,25],[37,24],
    [38,24],[38,25],[48,24],[49,24],[49,25],[48,25],[49,31],[49,32],[49,33],[50,31],
    [51,32],[38,36],[39,36],[40,36],[38,37],[39,38]]
    tochoice()

def small_exploder():
    global A,COR,X,Y
    COR=[[29,24],[29,25],[28,25],[30,25],[30,26],[28,26],[29,27]]
    tochoice()

def exploder():
    global A,COR,X,Y
    COR=[[29,20],[27,20],[31,20],[31,21],[27,21],[27,22],[31,22],[27,23],[27,24],
    [31,23],[31,24],[29,24]]
    tochoice()

def tumbler():
    global A,COR,X,Y
    COR=[[25,22],[26,22],[26,23],[25,23],[28,23],[28,22],[29,22],[29,23],[26,24],
    [26,25],[26,26],[28,24],[28,25],[28,26],[25,27],[29,27],[24,27],[30,27],[24,26],
    [24,25],[30,26],[30,25]]
    tochoice()

def lightweight_spaceship():
    global A,COR,X,Y
    COR=[[25,31],[25,29],[26,28],[27,28],[28,28],[29,28],[29,29],[29,30],[28,31]]
    tochoice()

def ten_cell_row():
    global A,COR,X,Y
    COR=[[24,27],[25,27],[26,27],[27,27],[28,27],[29,27],[30,27],[31,27],[32,27],[33,27]]
    tochoice()

def Kgalaxy():
    global A,COR,X,Y
    COR=[[23,23],[24,23],[25,23],[26,23],[27,23],[28,23],[23,22],[24,22],[25,22],
    [26,22],[27,22],[28,22],[24,25],[23,25],[24,26],[23,26],[24,27],[23,27],[24,28],
    [23,28],[24,29],[23,29],[24,30],[23,30],[26,30],[27,30],[28,30],[29,30],[30,30],
    [31,30],[26,29],[27,29],[28,29],[29,29],[30,29],[31,29],[31,27],[30,27],[30,26],
    [31,26],[31,25],[30,25],[30,24],[31,24],[31,23],[30,23],[30,22],[31,22]]
    tochoice()

def cross():
    global A,COR,X,Y
    COR=[[28,25],[29,25],[30,25],[27,25],[30,26],[30,27],[31,27],[32,27],[32,28],
    [32,29],[32,30],[31,30],[30,30],[30,31],[30,32],[29,32],[28,32],[27,32],[27,31],
    [27,30],[26,30],[25,30],[25,29],[25,28],[25,27],[26,27],[27,27],[27,26]]
    tochoice()

def star():
    global A,COR,X,Y
    COR=[[29,24],[30,24],[28,24],[28,26],[30,26],[32,26],[26,26],[32,28],[26,28],
    [26,30],[32,30],[24,28],[24,29],[24,30],[34,30],[34,29],[34,28],[32,32],[30,32],
    [28,32],[26,32],[28,34],[29,34],[30,34]]
    tochoice()
    
def start():
    global flag
    flag=True

def stop():
    global flag
    flag=False
        
def real_sim():
    global leaf,flag,speed
    if flag:
        next_state()
    leaf.after(speed*50,real_sim)

def next_state():
    global TEMP,A,frames,l
    TEMP=copy.deepcopy(A)
    show_state(A)
    frames+=1
    l.configure(text="Frames: %d" %frames)
    for i in range(N):
        for j in range(M):
            A[i][j]=neighbours(j,i,TEMP[i][j])

def show_state(A):
    global c
    col_width=c.winfo_width()/WM
    row_height=c.winfo_height()/WN
    for i in range(N):
        for j in range(M):
            if A[i][j]:
                if sq[i][j]:
                    c.delete(sq[i][j])
                sq[i][j]=c.create_rectangle(j*col_width,i*row_height,(j+1)*col_width,(i+1)*row_height,fill="black")  
            else:
                c.delete(sq[i][j])
                sq[i][j]=None
    
def neighbours(x,y,state):
    global TEMP
    count=0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (y+i>0 and y+i<N and x+j>0 and x+j<M):
                if TEMP[y+i][x+j]==1 and (i<>0 or j<>0): count+=1
    if(state==1):
        if (count==2 or count==3): return 1
        else: return 0
    else:
        if count==3: return 1
        else: return 0

def tiles(event):
    global c
    col_width=c.winfo_width()/WM
    row_height=c.winfo_height()/WN
    j=event.x//col_width
    i=event.y//row_height
    if not sq[i][j]:
        sq[i][j]=c.create_rectangle(j*col_width,i*row_height,(j+1)*col_width,(i+1)*row_height,fill="black")
    else:
        c.delete(sq[i][j])
        sq[i][j]=None

def click(event):
    global X,Y,COR,c
    x, y = event.x, event.y
    y//=c.winfo_width()/WM
    x//=c.winfo_height()/WN
    if x<WM and y<WN:
        A=[x,y]
        COR.append(A)

def get_speed():
    global log,v,speed
    speed=v.get()
    log.destroy()
    
def check_same():
    global COR
    UN=unique(COR)
    D={}
    for i in range(len(UN)):
        D.update({i:howmany(UN[i],COR)})
    for i in range(len(UN)):
        if(D[i]%2==0):
            for j in range(D[i]):
                COR.remove(UN[i])
        else:
            for j in range(D[i]-1):
                COR.remove(UN[i])

def unique(l):
    w=[]
    for i in range(len(l)):
        j=0
        while j<i:
            if l[i]==l[j]: break
            j+=1
        if i==j: w.append(l[i])
    return w

def howmany(key,l):
    count=0
    for i in range(len(l)):
        if key==l[i]: count+=1
    return count

def again():
    global stick
    stick.destroy()
    enter_shape()

def enter_shape():
    global A,COR,c,X,Y,sq
    COR=[]
    root=Tk()
    root.title("Game of Life - Enter your shape")
    root.wm_geometry("+350+5")
    root.bind('<Button-1>',click)
    c=Canvas(root,width=600,height=600,highlightthickness=0,bd=0,bg='white')
    c.pack()
    c.bind("<Button-1>",tiles)
    Button(root,text="OK",bg="red",command=root.destroy).pack()
    root.mainloop()
    if COR<>[]:
        del COR[-1]
        check_same()
    if COR<>[]: choice()
        
def frame_sim():
    global X,Y,COR,A,frames,sq,l,c,leaf,wood,plant
    plant.destroy()
    init_table()
    sq=[[None for j in range(M)]for i in range(N)]
    frames=-1
    leaf=Tk()
    leaf.title("Game of Life")
    leaf.wm_geometry("+350+5")
    c=Canvas(leaf,width=600,height=600,highlightthickness=0,bd=0,bg='white')
    c.pack(side=TOP)
    Button(leaf,text="Next",bg="green",command=next_state).pack()
    Button(leaf,text="Menu",bg="blue",command=menu2).pack()
    l=Label(leaf,text="")
    l.pack()
    leaf.mainloop()

def continuous_sim():
    global X,Y,COR,A,frames,sq,l,c,leaf,wood,plant,flag,speed
    plant.destroy()
    X=[]
    Y=[]
    init_table()
    sq=[[None for j in range(M)]for i in range(N)]
    frames=-1
    flag=False
    speed=0
    while (speed<1 or speed>20):
        speed=sim_speed()
    speed=int(speed)
    leaf=Tk()
    leaf.title("Game of Life")
    leaf.wm_geometry("+350+5")
    c=Canvas(leaf,width=600,height=600,highlightthickness=0,bd=0,bg='white')
    c.pack(side=TOP)
    Button(leaf,text="Start",bg="green",command=start).pack()
    Button(leaf,text="Pause",bg="red",command=stop).pack()
    Button(leaf,text="Menu",bg="blue",command=menu2).pack()
    l=Label(leaf,text="")
    l.pack()
    leaf.after(speed*50,real_sim)
    leaf.mainloop()

def sim_speed():
    global log,v,speed
    log=Tk()
    log.title("Set Simulation Speed")
    log.wm_geometry("250x100+500+300")
    Label(log,text="Enter Simulation Speed 1(faster)->20(slower)").pack()
    v=StringVar()
    e=Entry(log,textvariable=v)
    e.pack()
    v.set(20)
    Button(log,text="OK",bg="red",command=get_speed).pack()
    log.mainloop()
    return float(speed)

def tochoice():
    global stick
    stick.destroy()
    choice()
    
def choice():
    global plant
    plant=Tk()
    plant.title("Choice")
    plant.wm_geometry("250x100+500+300")
    Label(plant,text="Choose from:").pack()
    Button(plant,text="Simulation frame by frame",bg="yellow",command=frame_sim).pack()
    Label(plant,text="or").pack()
    Button(plant,text="Continuous Simulation",bg="orange",command=continuous_sim).pack()
    plant.mainloop()

def choice2():
    global wood,stick
    wood.destroy()
    stick=Tk()
    stick.title("Choice")
    stick.wm_geometry("400x200+400+200")
    menubar=Menu(stick)
    osmenu=Menu(menubar,tearoff=0)
    osmenu.add_command(label="Tumbler",command=tumbler)
    osmenu.add_command(label="10 Cell Row",command=ten_cell_row)
    osmenu.add_command(label="Kor's Galaxy",command=Kgalaxy)
    osmenu.add_command(label="Cross",command=cross)
    osmenu.add_command(label="Star",command=star)
    menubar.add_cascade(label="Oscillators",menu=osmenu)
    spacemenu=Menu(menubar,tearoff=0)
    spacemenu.add_command(label="Glider",command=glider)
    spacemenu.add_command(label="Lightweight Spaceship",command=lightweight_spaceship)
    menubar.add_cascade(label="Spaceships",menu=spacemenu)
    expmenu=Menu(menubar,tearoff=0)
    expmenu.add_command(label="Small Exploder",command=small_exploder)
    expmenu.add_command(label="Exploder",command=exploder)
    menubar.add_cascade(label="Exploders",menu=expmenu)
    gunmenu=Menu(menubar,tearoff=0)
    gunmenu.add_command(label="Gosper's Glider Gun",command=GGG)
    menubar.add_cascade(label="Gosper's Glider Gun",menu=gunmenu)
    Label(stick,text="Choose from the above shapes\nor").pack()
    Button(stick,text="Enter your own shape",bg="orange",command=again).pack()
    stick.config(menu=menubar)
    stick.mainloop()

def about():
    root=Tk()
    root.title("About")
    root.wm_geometry("250x100+500+300")
    Label(root,text="Author: Nikos Roussos\nVersion: 3.1\nRelease Date: 06/05/2016").pack()
    Button(root,text="I don't care",bg="red",command=root.destroy).pack()
    root.mainloop()

def info():
    root=Tk()
    root.title("Instructions")
    root.wm_geometry("450x200+430+270")
    Label(root,text="The idea of Game of Life is that you have a surface split into squares").pack()
    Label(root,text="Every square has two states: dead or alive").pack()
    Label(root,text="\nRules:\n1-If a square is alive (black) and has 2 or 3 neighbouring squares alive, stays alive").pack()
    Label(root,text="2-If a square is dead (white) and has 3 neighbouring squares alive, becomes alive").pack()
    Label(root,text="3-In any other case the square stays/becomes dead").pack()
    Button(root,text="Got it!",bg="red",command=root.destroy).pack()
    root.mainloop()

def menu():
    global wood,A,X,Y
    X=[]
    Y=[]
    A=[[0 for j in range(M)]for i in range(N)]
    wood=Tk()
    wood.title("Game of Life - Menu")
    wood.wm_geometry("250x150+500+300")
    Label(wood,text="Welcome to a Game of Life Simulation!").pack()
    Button(wood,text="Begin",bg="green",command=choice2).pack()
    Button(wood,text="Instructions",bg="yellow",command=info).pack()
    Button(wood,text="About",bg="orange",command=about).pack()
    Button(wood,text="Exit",bg="red",command=wood.destroy).pack()
    wood.mainloop()

def menu2():
    global wood,leaf
    leaf.destroy()
    menu()

WN=60
WM=60
N=80
M=80
sq=[[None for j in range(M)]for i in range(N)]
menu()
