import tkinter
import time
import random

# Crea la ventana y la asocia a la variable v
v = tkinter.Tk()


v.title("HAPPY FIGHTER")

presiono = False
carro1= None
i = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0
i8 = 0
j = 0
t = 0
t1 = 0
t2 = 0
t3 = 0
t4 = 0
count = 0
count2 = 0
count3 = 100
count4 = 100
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 100
count10 = 100
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 100
count16 = 80
count17 = 80
count18 = 100
sec3 = 0
sec4 = 0
sec5 = 0
sec6 = 0
sec7 = 0
sec8 = 0
posx1 = 50
posy1 =50
posx2 = 250
posy2 = 400
velrun=3
velgas=3
velmapa=5

# Primer nivel


def movimientofondo():
    global nivel1,dos,v,velmapa
    c4=0
    c5=0
    if(c4<5):
        nivel1.move(mapa1,0,velmapa)
        c4=c4+1
        c5=c5+1
        dos.after(1,movimientofondo)
    if(nivel1.coords(mapa1)[1]>3200):
        nivel1.move(mapa1,0,-nivel1.coords(mapa1)[1])



def start():
    global fondolvl1,i,j,carro,key,nivel1,carro1,t,carro2,posx1,posy1,posx2,posy2,z,movimiento,dos,carrito,runner,carro2,player1,player2,runner2,gas,gas2,gasolina,gaso,velo,carro3,fighter,fighterr,minivan
    
    dos = tkinter.Toplevel(v)
    v.iconify()
    nivel1= tkinter.Canvas(dos,bg="blue", width=1920, height=1000 )
    nivel1.pack()
    nivel1.bind("<KeyPress>",keydown)
    nivel1.bind("<KeyRelease>",keyup)
    nivel1.focus_set()
    nombre1=tkinter.Label(nivel1,bg="white",fg="black",textvariable=player1,borderwidth=5,font=("Arial",23)).place(x=20,y=30)
    nombre2=tkinter.Label(nivel1,bg="white",fg="black",textvariable=player2,borderwidth=5,font=("Arial",23)).place(x=1400,y=30)
    punticos=tkinter.Label(nivel1,bg="white",fg="black",text="Puntos",borderwidth=5,font=("Arial",23)).place(x=20,y=400)
    punticos=tkinter.Label(nivel1,bg="white",fg="black",text="Puntos",borderwidth=5,font=("Arial",23)).place(x=1400,y=400)
    gasolin=tkinter.Label(nivel1,bg="white",fg="black",text="Gasolina",borderwidth=5,font=("Arial",23)).place(x=20,y=570)
    gasolin=tkinter.Label(nivel1,bg="white",fg="black",text="Gasolina",borderwidth=5,font=("Arial",23)).place(x=1400,y=570)
    velo=tkinter.Label(nivel1,bg="white",fg="black",text="Velocidad",borderwidth=5,font=("Arial",23)).place(x=20,y=200)
    velo=tkinter.Label(nivel1,bg="white",fg="black",text="Velocidad",borderwidth=5,font=("Arial",23)).place(x=1400,y=200)
    carro1=nivel1.create_image(450,750,image=carro)
    mapa1=nivel1.create_image(770,380,image=fondolvl1)
    carrito=nivel1.create_image(1100,750,image=carro)
    runner = nivel1.create_image(350,0,image=carro2)
    runner2 = nivel1.create_image(950,0,image=carro2)
    fighter = nivel1.create_image(380,0,image=carro3)
    fighterr = nivel1.create_image(980,0,image=carro3)
    gas = nivel1.create_image(450,-800,image=gasolina)
    gas2 = nivel1.create_image(1100,-800,image=gasolina)
    choque(fighter)
    choque2(fighterr)
    choque3(runner)
    choque4(runner2)
    #minivan1()
    fightercar()
    fightercar2()
    #minivan(270,600)
    movimiento2()
    movimiento()
    movimientofondo()
    nivel1.lower(mapa1)
    puntos()
    puntos2()
    gaso()
    gaso2()
    velocidad1()
    velocidad2()
    key1player()
    key2player()
M=0
Z=0
A=0
B=0
def choque(enemigo):
    global nivel1,explosion,carro1,M,explosion1,count3,Z,count2,count5,explosion1
    if(nivel1.coords(carro1)[0]>=nivel1.coords(enemigo)[0] and nivel1.coords(carro1)[0]<=nivel1.coords(enemigo)[0]+50):
        if(nivel1.coords(carro1)[1]>=nivel1.coords(enemigo)[1] and nivel1.coords(carro1)[1]<=nivel1.coords(enemigo)[1]+50 ):
            if(M==0):
                M=1
                count3=count3-6
                count2 = count2-400
                count5 = 0
                nivel1.after(1000)
                
                
    else:
        M=0
        
            
            
  
    nivel1.after(10,choque,enemigo)

def choque2(enemigo):
    global nivel1,explosion,carrito,M,explosion1,count4,Z,count
    if(nivel1.coords(carrito)[0]>=nivel1.coords(enemigo)[0] and nivel1.coords(carrito)[0]<=nivel1.coords(enemigo)[0]+50):
        if(nivel1.coords(carrito)[1]>=nivel1.coords(enemigo)[1] and nivel1.coords(carrito)[1]<=nivel1.coords(enemigo)[1]+50 ):
            if(Z==0):
                explosion1 = nivel1.create_image(nivel1.coords(carrito)[0],nivel1.coords(carrito)[1],image=explosion)
                nivel1.delete(explosion1)
                Z=1
                count4=count4-6
                count = count-400
                nivel1.after(1000)
    else:
        Z=0
            
            
  
    nivel1.after(10,choque2,enemigo)
def choque3(enemigo):
    global nivel1,explosion,carro1,B,explosion1,count3,A,count2,count5
    if(nivel1.coords(carro1)[0]>=nivel1.coords(enemigo)[0] and nivel1.coords(carro1)[0]<=nivel1.coords(enemigo)[0]+50):
        if(nivel1.coords(carro1)[1]>=nivel1.coords(enemigo)[1] and nivel1.coords(carro1)[1]<=nivel1.coords(enemigo)[1]+50 ):
            if(A==0):
                explosion1 = nivel1.create_image(nivel1.coords(carro1)[0],nivel1.coords(carro1)[1],image=explosion)
                nivel1.delete(explosion1)
                A=1
                count3=count3-6
                count2 = count2-400
                count5 = 0
                nivel1.after(1000)
    else:
        A=0
            
            
  
    nivel1.after(10,choque3,enemigo)

def choque4(enemigo):
    global nivel1,explosion,carrito,A,explosion1,count4,B,count,count5
    if(nivel1.coords(carrito)[0]>=nivel1.coords(enemigo)[0] and nivel1.coords(carrito)[0]<=nivel1.coords(enemigo)[0]+50):
        if(nivel1.coords(carrito)[1]>=nivel1.coords(enemigo)[1] and nivel1.coords(carrito)[1]<=nivel1.coords(enemigo)[1]+50 ):
            if(B==0):
                explosion1 = nivel1.create_image(nivel1.coords(carrito)[0],nivel1.coords(carrito)[1],image=explosion)
                nivel1.delete(explosion1)
                B=1
                count4=count4-6
                count = count-400
                nivel1.after(1000)

    else:
        B=0

            
            
  
    nivel1.after(10,choque4,enemigo)


            
            

h=[]
def keyup(e):
  global x,h
  print(e.keycode)
  if(e.keycode in h):
    h.pop(h.index(e.keycode))
    #x.set(str(h))

def keydown(e):
  global x,h
  if not e.keycode in h:
    h.append(e.keycode)
    #x.set(str(h))
    
def key1player():
    """
    """
    global carro1,i,j,y,fondo,carro,start,nivel1,carrito,i2,h,velx
    #tecla = repr(event.char)
    #(tecla)
    if(68 in h):
        if(i < 165):
            nivel1.delete(carro1)
            i = i + velx
        
            carro1 = nivel1.create_image(450+i,750+j,image=carro)
            
            
        else:
            nivel1.delete(carro1)
            carro1 = nivel1.create_image(450+i,750+j,image=volteard)
                       
    if(65 in h):
        if(i >-145 ):
            nivel1.delete(carro1)
            i = i - velx
            
            carro1 = nivel1.create_image(450+i,750+j,image=carro)
        else:
            nivel1.delete(carro1)
            carro1 = nivel1.create_image(450+i,750+j,image=volteari)
    dos.after(30,key1player)
def key2player():
    """
    """
    global carro1,i,j,y,fondo,carro,start,nivel1,carrito,i2,h,velx

    if(76 in h):
        if(i2 < 150):
            nivel1.delete(carrito)
            i2 = i2 + velx
        
            carrito = nivel1.create_image(1100+i2,750+j,image=carro)
            
            
        else:
            nivel1.delete(carrito)
            carrito = nivel1.create_image(1100+i2,750+j,image=volteard)
                       
    if(74 in h):
        if(i2 >-165 ):
            nivel1.delete(carrito)
            i2 = i2 - velx
            
            carrito = nivel1.create_image(1100+i2,750+j,image=carro)
        else:
            nivel1.delete(carrito)
            carrito = nivel1.create_image(1100+i2,750+j,image=volteari)
    dos.after(30,key2player)

def movimiento():

    global dos,carro1,t,carro2,runner,posx1,posy1,posx2,posy2,start,z,start,t1,runner2,velrun
    if(t1<500):
        t1=t1+1
        nivel1.move(runner,0,velrun)
        nivel1.move(runner2,0,velrun)
    if(t1==500):
        pp = random.randint(270,600)
        pp1 = random.randint(900,1250)
        nivel1.move(runner,pp-nivel1.coords(runner)[0],-nivel1.coords(runner)[1])
        nivel1.move(runner2,pp1-nivel1.coords(runner2)[0],-nivel1.coords(runner2)[1])
        t1 = 0
    nivel1.after(10,movimiento)
def movimiento2():

    global dos,carro1,t,carro2,gas,posx1,posy1,posx2,posy2,start,z,start,t2,gas2,velgas
    if(t2<2000):
        t2=t2+1
        nivel1.move(gas,0,velgas)
        nivel1.move(gas2,0,velgas)
    if(t2==2000):
        nivel1.delete(gas)
        nivel1.delete(gas2)
        tt = random.randint(270,600)
        tt1 = random.randint(900,1250)
        gas = nivel1.create_image(tt,-800,image=gasolina)
        gas2 = nivel1.create_image(tt1,-800,image=gasolina)
        t2 = 0
    nivel1.after(10,movimiento2)

vely=2
def fightercar():
    global dos,carro1,t,carro2,runner,posx1,posy1,posx2,posy2,start,z,start,t1,runner2,velrun,fighter,nivel1,vely
    if(nivel1.coords(fighter)[1] <=1400):
        if(nivel1.coords(fighter)[0] < nivel1.coords(carro1)[0]):
            nivel1.move(fighter,1,vely)
        if(nivel1.coords(fighter)[0] > nivel1.coords(carro1)[0]):
            nivel1.move(fighter,-1,vely)
        if(nivel1.coords(fighter)[0] == nivel1.coords(carro1)[0]):
            nivel1.move(fighter,0,vely)
    if(nivel1.coords(fighter)[1] > 1400):
        
        gg = random.randint(270,600)
        nivel1.move(fighter,gg-nivel1.coords(fighter)[0],-nivel1.coords(fighter)[1])


    nivel1.after(10,fightercar)
def fightercar2():
    global dos,carro1,t,carrito,runner,posx1,posy1,posx2,posy2,start,z,start,t1,runner2,velrun,fighterr,nivel1,vely
    if(nivel1.coords(fighterr)[1] <=1400):
        if(nivel1.coords(fighterr)[0] < nivel1.coords(carrito)[0]):
            nivel1.move(fighterr,1,vely)
        if(nivel1.coords(fighterr)[0] > nivel1.coords(carrito)[0]):
            nivel1.move(fighterr,-1,vely)
        if(nivel1.coords(fighterr)[0] == nivel1.coords(carrito)[0]):
            nivel1.move(fighterr,0,vely)
    if(nivel1.coords(fighterr)[1] > 1400):
        ff = random.randint(900,1250)
        nivel1.move(fighterr,ff-nivel1.coords(fighterr)[0],-nivel1.coords(fighterr)[1])

    nivel1.after(10,fightercar2)



#Segundo nivel

        
def start2():
    global fondolvl2,i,j,carro,key2,nivel2,carro2,posx1,posy1,posx2,posy2,z,movimientofondo2,lvl3,carrito2,mapa2,player1,player2,fighter2,fighterr2,runner3,runner4,gas3,gas4,carro20
    lvl3 = tkinter.Toplevel(v)
    v.iconify()
    nivel2= tkinter.Canvas(lvl3,bg="blue", width=1920, height=1000 )
    nivel2.pack()
    #nivel2.bind("<KeyPress>", key2)
    nivel2.bind("<KeyPress>",keydown2)
    nivel2.bind("<KeyRelease>",keyup2)
    nivel2.focus_set()
    nombre3=tkinter.Label(nivel2,bg="white",fg="black",textvariable=player1,borderwidth=5,font=("Arial",23)).place(x=20,y=30)
    nombre4=tkinter.Label(nivel2,bg="white",fg="black",textvariable=player2,borderwidth=5,font=("Arial",23)).place(x=1400,y=30)
    punticos3=tkinter.Label(nivel2,bg="white",fg="black",text="Puntos",borderwidth=5,font=("Arial",23)).place(x=20,y=400)
    punticos4=tkinter.Label(nivel2,bg="white",fg="black",text="Puntos",borderwidth=5,font=("Arial",23)).place(x=1400,y=400)
    gasolin3=tkinter.Label(nivel2,bg="white",fg="black",text="Gasolina",borderwidth=5,font=("Arial",23)).place(x=20,y=570)
    gasolin4=tkinter.Label(nivel2,bg="white",fg="black",text="Gasolina",borderwidth=5,font=("Arial",23)).place(x=1400,y=570)
    velo3=tkinter.Label(nivel2,bg="white",fg="black",text="Velocidad",borderwidth=5,font=("Arial",23)).place(x=20,y=200)
    velo4=tkinter.Label(nivel2,bg="white",fg="black",text="Velocidad",borderwidth=5,font=("Arial",23)).place(x=1400,y=200)
    fighter2 = nivel2.create_image(360,0,image=carro3)
    fighterr2 = nivel2.create_image(940,0,image=carro3)
    runner3 = nivel2.create_image(320,0,image=carro20)
    runner4 = nivel2.create_image(990,0,image=carro20)
    carro2 =nivel2.create_image(450,750,image=carro)
    mapa2 =nivel2.create_image(770,380,image=fondolvl2)
    carrito2=nivel2.create_image(1100,750,image=carro)
    gas3 = nivel2.create_image(450,-800,image=gasolina)
    gas4 = nivel2.create_image(1100,-800,image=gasolina)

    movimiento3()
    movimiento4()
    fightercar3()
    fightercar4()
    gaso3()
    gaso4()
    velocidad3()
    velocidad4()
    puntos3()
    puntos4()
    key1player2()
    key2player2()
    movimientofondo2()
    nivel2.lower(mapa2)

    
def fightercar3():
    global lvl3,carro2,t,carro,posx1,posy1,posx2,posy2,start2,z,start,t1,runner2,velrun,fighter2,nivel2,vely
    if(nivel2.coords(fighter2)[1] <=1400):
        if(nivel2.coords(fighter2)[0] < nivel2.coords(carro2)[0]):
            nivel2.move(fighter2,1,vely)
        if(nivel2.coords(fighter2)[0] > nivel2.coords(carro2)[0]):
            nivel2.move(fighter2,-1,vely)
        if(nivel2.coords(fighter2)[0] == nivel2.coords(carro2)[0]):
            nivel2.move(fighter2,0,vely)
    if(nivel2.coords(fighter2)[1] > 1400):
        nivel2.delete(fighter2)
        gg2 = random.randint(270,600)
        fighter2 = nivel2.create_image(gg2,1,image=carro3)

    nivel2.after(10,fightercar3)
def fightercar4():
    global lvl3,carro1,t,carrito2,runner,posx1,posy1,posx2,posy2,start,z,start,t1,runner2,velrun,fighterr2,nivel2,vely
    if(nivel2.coords(fighterr2)[1] <=1400):
        if(nivel2.coords(fighterr2)[0] < nivel2.coords(carrito2)[0]):
            nivel2.move(fighterr2,1,vely)
        if(nivel2.coords(fighterr2)[0] > nivel2.coords(carrito2)[0]):
            nivel2.move(fighterr2,-1,vely)
        if(nivel2.coords(fighterr2)[0] == nivel2.coords(carrito2)[0]):
            nivel2.move(fighterr2,0,vely)
    if(nivel2.coords(fighterr2)[1] > 1400):
        nivel2.delete(fighterr2)
        ff2 = random.randint(900,1250)
        fighterr2 = nivel1.create_image(ff2,1,image=carro3)

    nivel2.after(10,fightercar4)
def movimiento3():

    global lvl3,carro20,t3,runner4,posx1,posy1,posx2,posy2,start,z,start,t4,runner3,velrun
    if(t3<500):
        t3=t3+1
        nivel2.move(runner3,0,velrun)
        nivel2.move(runner4,0,velrun)
    if(t3==500):
        nivel2.delete(runner3)
        nivel2.delete(runner4)
        pp2 = random.randint(270,600)
        pp10 = random.randint(900,1250)
        runner3 = nivel2.create_image(pp2,0,image=carro20)
        runner4 = nivel2.create_image(pp10,0,image=carro20)
        t3 = 0
    nivel2.after(10,movimiento3)
def movimiento4():

    global lvl3,carro1,t3,carro2,gas3,posx1,posy1,posx2,posy2,start,z,start,t4,gas4,velgas
    if(t4<2000):
        t4=t4+1
        nivel2.move(gas3,0,velgas)
        nivel2.move(gas4,0,velgas)
    if(t4==2000):
        nivel2.delete(gas3)
        nivel2.delete(gas4)
        tt2 = random.randint(270,600)
        tt10 = random.randint(900,1250)
        gas3 = nivel2.create_image(tt2,-800,image=gasolina)
        gas4 = nivel2.create_image(tt10,-800,image=gasolina)
        t4 = 0
    nivel2.after(10,movimiento4)


def movimientofondo2():
    global nivel2,lvl3,v
    c6=0
    c7=0
    if(c6<5):
        nivel2.move(mapa2,0,velmapa)
        c6=c6+1
        c7=c7+1
        lvl3.after(1,movimientofondo2)
    if(nivel2.coords(mapa2)[1]>3200):
        nivel2.move(mapa2,0,-nivel2.coords(mapa2)[1])

def keyup2(e):
  global x,h
  print(e.keycode)
  if(e.keycode in h):
    h.pop(h.index(e.keycode))
    #x.set(str(h))

def keydown2(e):
  global x,h
  if not e.keycode in h:
    h.append(e.keycode)
    #x.set(str(h))

def key1player2():
    """
    """
    global carro2,i3,j,y,fondo,carro2,start2,nivel2,carrito2,i4,h,x,velx
    #tecla = repr(event.char)
    #print(tecla)
    if(68 in h):
        if(i3 < 220):
            nivel2.delete(carro2)
            i3 = i3 + velx
        
            carro2 = nivel2.create_image(450+i3,750+j,image=carro)
            
            
        else:
            nivel2.delete(carro2)
            carro2 = nivel2.create_image(450+i3,750+j,image=volteard)
                       
    if(65 in h):
        if(i3 >-190 ):
            nivel2.delete(carro2)
            i3 = i3 - velx
            
            carro2 = nivel2.create_image(450+i3,750+j,image=carro)
        else:
            nivel2.delete(carro2)
            carro2 = nivel2.create_image(450+i3,750+j,image=volteari)
    lvl3.after(30,key1player2)
def key2player2():
    global carro2,i3,j,y,fondo,carro2,start2,nivel2,carrito2,i4,h,x,velx

    if(76 in h):
        if(i4 < 200):
            nivel2.delete(carrito2)
            i4 = i4 + velx
        
            carrito2 = nivel2.create_image(1100+i4,750+j,image=carro)
            
            
        else:
            nivel2.delete(carrito2)
            carrito2 = nivel2.create_image(1100+i4,750+j,image=volteard)
                       
    if(74 in h):
        if(i4 >-220 ):
            nivel2.delete(carrito2)
            i4 = i4 - velx
            
            carrito2 = nivel2.create_image(1100+i4,750+j,image=carro)
        else:
            nivel2.delete(carrito2)
            carrito2 = nivel2.create_image(1100+i4,750+j,image=volteari)
    lvl3.after(30,key2player2)
#Nivel 3
velmapa2 = 7
def movimientofondo3():
    global nivel3,lvl4,v,velmapa2
    c8=0
    c9=0
    if(c8<5):
        nivel3.move(mapa3,0,velmapa2)
        c8=c8+1
        c9=c9+1
        lvl4.after(1,movimientofondo3)
    if(nivel3.coords(mapa3)[1]>3200):
        nivel3.move(mapa3,0,-nivel3.coords(mapa3)[1])
            
def start3():
    global fondolvl3,i,j,carro,key3,nivel3,carro3,posx1,posy1,posx2,posy2,z,movimientofondo3,lvl4,carrito3,mapa3,player1,player2,fighter3,fighterr3,carro30
    lvl4 = tkinter.Toplevel(v)
    v.iconify()
    nivel3= tkinter.Canvas(lvl4,bg="blue", width=1920, height=1000 )
    nivel3.pack()
    #nivel3.bind("<Key>", key3)
    nivel3.bind("<KeyPress>",keydown3)
    nivel3.bind("<KeyRelease>",keyup3)
    nivel3.focus_set()
    nombre5=tkinter.Label(nivel3,bg="white",fg="black",textvariable=player1,borderwidth=5,font=("Arial",23)).place(x=20,y=30)
    nombre6=tkinter.Label(nivel3,bg="white",fg="black",textvariable=player2,borderwidth=5,font=("Arial",23)).place(x=1400,y=30)
    punticos=tkinter.Label(nivel3,bg="white",fg="black",text="Puntos",borderwidth=5,font=("Arial",23)).place(x=20,y=400)
    punticos=tkinter.Label(nivel3,bg="white",fg="black",text="Puntos",borderwidth=5,font=("Arial",23)).place(x=1400,y=400)
    gasolin=tkinter.Label(nivel3,bg="white",fg="black",text="Gasolina",borderwidth=5,font=("Arial",23)).place(x=20,y=570)
    gasolin=tkinter.Label(nivel3,bg="white",fg="black",text="Gasolina",borderwidth=5,font=("Arial",23)).place(x=1400,y=570)
    velo=tkinter.Label(nivel3,bg="white",fg="black",text="Velocidad",borderwidth=5,font=("Arial",23)).place(x=20,y=200)
    velo=tkinter.Label(nivel3,bg="white",fg="black",text="Velocidad",borderwidth=5,font=("Arial",23)).place(x=1400,y=200)
    mapa3=nivel3.create_image(770,380,image=fondolvl3)
    carro3=nivel3.create_image(450,750,image=carro)
    carrito3 =nivel3.create_image(1100,750,image=carro)
    fighter3 = nivel3.create_image(380,0,image=carro30)
    fighterr3 = nivel3.create_image(980,0,image=carro30)

    fightercar6()
    fightercar5()
    gaso5()
    gaso6()
    puntos5()
    puntos6()
    velocidad5()
    velocidad6()
    key1player3()
    key2player3()
    movimientofondo3()
    nivel3.lower(mapa3)

vely2=4
def fightercar5():
    global lvl4,carro1,t,carro3,runner,posx1,posy1,posx2,posy2,start,z,start,t1,runner2,velrun,fighter3,nivel1,vely
    if(nivel3.coords(fighter3)[1] <=1400):
        if(nivel3.coords(fighter3)[0] < nivel3.coords(carro3)[0]):
            nivel3.move(fighter3,1,vely2)
        if(nivel3.coords(fighter3)[0] > nivel3.coords(carro3)[0]):
            nivel3.move(fighter3,-1,vely2)
        if(nivel3.coords(fighter3)[0] == nivel3.coords(carro3)[0]):
            nivel3.move(fighter3,0,vely2)
    if(nivel3.coords(fighter3)[1] > 1400):
        nivel3.delete(fighter3)
        gg3 = random.randint(270,600)
        fighter3 = nivel3.create_image(gg3,1,image=carro30)

    nivel3.after(10,fightercar5)
def fightercar6():
    global lvl4,carro1,t,carrito3,runner,posx1,posy1,posx2,posy2,start,z,start,t1,runner2,velrun,fighterr3,nivel1,vely
    if(nivel3.coords(fighterr3)[1] <=1400):
        if(nivel3.coords(fighterr3)[0] < nivel3.coords(carrito3)[0]):
            nivel3.move(fighterr3,1,vely2)
        if(nivel3.coords(fighterr3)[0] > nivel3.coords(carrito3)[0]):
            nivel3.move(fighterr3,-1,vely2)
        if(nivel3.coords(fighterr3)[0] == nivel3.coords(carrito3)[0]):
            nivel3.move(fighterr3,0,vely2)
    if(nivel3.coords(fighterr3)[1] > 1400):
        nivel3.delete(fighterr3)
        ff3 = random.randint(900,1250)
        fighterr3 = nivel3.create_image(ff3,1,image=carro30)

    nivel3.after(10,fightercar6)


def keyup3(e):
  global x,h
  print(e.keycode)
  if(e.keycode in h):
    h.pop(h.index(e.keycode))
    #x.set(str(h))

def keydown3(e):
  global x,h
  if not e.keycode in h:
    h.append(e.keycode)
    #x.set(str(h))

def key1player3():
    """
    """
    global carro3,i5,j,y,fondo,carro3,start3,nivel3,carrito3,i6,h,velx
    if(68 in h):
        if(i5 < 180):
            nivel3.delete(carro3)
            i5 = i5 + velx
        
            carro3 = nivel3.create_image(450+i5,750+j,image=carro)
            
            
        else:
            nivel3.delete(carro3)
            carro3 = nivel3.create_image(450+i5,750+j,image=volteard)
                       
    if(65 in h):
        if(i5 >-165 ):
            nivel3.delete(carro3)
            i5 = i5 - velx
            
            carro3 = nivel3.create_image(450+i5,750+j,image=carro)
        else:
            nivel3.delete(carro3)
            carro3 = nivel3.create_image(450+i5,750+j,image=volteari)
    lvl4.after(30,key1player3)
        
def key2player3():
    global carro3,i5,j,y,fondo,carro3,start3,nivel3,carrito3,i6,h,velx
    if(76 in h):
        if(i6 < 155):
            nivel3.delete(carrito3)
            i6 = i6 + velx
        
            carrito3 = nivel3.create_image(1100+i6,750+j,image=carro)
            
            
        else:
            nivel3.delete(carrito3)
            carrito3 = nivel3.create_image(1100+i6,750+j,image=volteard)
                       
    if(74 in h):
        if(i6 >-200 ):
            nivel3.delete(carrito3)
            i6 = i6 - velx
            
            carrito3= nivel3.create_image(1100+i6,750+j,image=carro)
        else:
            nivel3.delete(carrito3)
            carrito3 = nivel3.create_image(1100+i6,750+j,image=volteari)
    lvl4.after(30,key2player3)
#Nivel4
def start4():
    global fondolvl4,i,j,carro,key4,nivel4,carro4,posx1,posy1,posx2,posy2,z,movimientofondo4,lvl5,carrito4,mapa4,player1,player2
    lvl5 = tkinter.Toplevel(v)
    v.iconify()
    nivel4= tkinter.Canvas(lvl5,bg="blue", width=1920, height=1000 )
    nivel4.pack()
    #nivel4.bind("<Key>", key4)
    nivel4.bind("<KeyPress>",keydown4)
    nivel4.bind("<KeyRelease>",keyup4)
    nivel4.focus_set()
    nombre1=tkinter.Label(nivel4,bg="white",fg="black",textvariable=player1,borderwidth=5,font=("Arial",23)).place(x=20,y=30)
    nombre2=tkinter.Label(nivel4,bg="white",fg="black",textvariable=player2,borderwidth=5,font=("Arial",23)).place(x=1400,y=30)
    punticos=tkinter.Label(nivel4,bg="white",fg="black",text="Puntos",borderwidth=5,font=("Arial",23)).place(x=20,y=400)
    punticos=tkinter.Label(nivel4,bg="white",fg="black",text="Puntos",borderwidth=5,font=("Arial",23)).place(x=1400,y=400)
    gasolin=tkinter.Label(nivel4,bg="white",fg="black",text="Gasolina",borderwidth=5,font=("Arial",23)).place(x=20,y=570)
    gasolin=tkinter.Label(nivel4,bg="white",fg="black",text="Gasolina",borderwidth=5,font=("Arial",23)).place(x=1400,y=570)
    velo=tkinter.Label(nivel4,bg="white",fg="black",text="Velocidad",borderwidth=5,font=("Arial",23)).place(x=20,y=200)
    velo=tkinter.Label(nivel4,bg="white",fg="black",text="Velocidad",borderwidth=5,font=("Arial",23)).place(x=1400,y=200)
    carro4=nivel4.create_image(450,750,image=carro)
    mapa4=nivel4.create_image(770,380,image=fondolvl2)
    carrito4=nivel4.create_image(1100,750,image=carro)
    gaso7()
    gaso8()
    puntos7()
    puntos8()
    velocidad7()
    velocidad8()
    key1player4()
    key2player4()
    movimientofondo4()
    nivel4.lower(mapa4)

def keyup4(e):
  global x,h
  print(e.keycode)
  if(e.keycode in h):
    h.pop(h.index(e.keycode))
    #x.set(str(h))

def keydown4(e):
  global x,h
  if not e.keycode in h:
    h.append(e.keycode)
    #x.set(str(h))
    
velx = 10
def key1player4():
    """
    """
    global carro4,i8,j,y,fondo,carro4,start4,nivel4,carrito4,i7,h,velx
    if(68 in h):
        if(i7 < 230):
            nivel4.delete(carro4)
            i7 = i7 + velx
        
            carro4 = nivel4.create_image(450+i7,750+j,image=carro)
            
            
        else:
            nivel4.delete(carro4)
            carro4 = nivel4.create_image(450+i7,750+j,image=volteard)
                       
    if(65 in h):
        if(i7 >-200 ):
            nivel4.delete(carro4)
            i7 = i7 - velx
            
            carro4 = nivel4.create_image(450+i7,750+j,image=carro)
        else:
            nivel4.delete(carro4)
            carro4 = nivel4.create_image(450+i7,750+j,image=volteari)
    lvl5.after(30,key1player4)
        
def key2player4():
    global carro4,i7,j,y,fondo,carro4,start4,nivel4,carrito4,i8,h,velx
    if(76 in h):
        if(i8 < 155):
            nivel4.delete(carrito4)
            i8 = i8 + velx
        
            carrito4 = nivel4.create_image(1100+i8,750+j,image=carro)
            
            
        else:
            nivel4.delete(carrito4)
            carrito4 = nivel4.create_image(1100+i8,750+j,image=volteard)
                       
    if(74 in h):
        if(i8 >-200 ):
            nivel4.delete(carrito4)
            i8 = i8 - velx
            
            carrito4= nivel4.create_image(1100+i8,750+j,image=carro)
        else:
            nivel4.delete(carrito4)
            carrito4 = nivel4.create_image(1100+i8,750+j,image=volteari)
    lvl5.after(30,key2player4)

def movimientofondo4():
    global nivel4,lvl5,v,velmapa2
    c10=0
    c11=0
    if(c10<5):
        nivel4.move(mapa4,0,velmapa2)
        c10=c10+1
        c11=c11+1
        lvl5.after(1,movimientofondo4)
    if(nivel4.coords(mapa4)[1]>3200):
        nivel4.move(mapa4,0,-nivel4.coords(mapa4)[1])



##def minivan1():
##    global dos,minivan,nivel,start
##    if(nivel1.coords(minivan)[1] <= 850):
##        if(nivel1.coords(minivan)[0] <=1000 and minivan.coords(minivan)[0] >= 780):
##           cc = random.randit(-9,9)
##           cc2= random.randit(1,6)
##           nivel1.move(minivan,cc,cc2)
##        if(nivel1.coords(minivan)[0] > 1000):
##            cc = random.randit(-9,0)
##            cc2= random.randit(1,6)
##            nivel1.move(minivan,cc,cc2)
##        if(nivel1.coords(minivan)[0] < 700):
##            cc = random.randit(0,9)
##            cc2= random.randit(1,6)
##            nivel1.move(minivan,cc,cc2)
##    if(nivel1.coords(minivan)[1] < 800):
##        nivel1.delete(minivan)
##        x=random.randint(270,600)
##        minivan = nivel1.create_image(x,1,image=minivan)
##    nivel1.after(10,minivan1)
##            


# Gasolina cada nivel

# Gasolina nivel1

velgaso = 2
def gaso():
    global count3,velmapa,velgas,velrun,count4,points,vely,velx,velgaso
    if(count3>=0):
        
        textGasolina= tkinter.Label(dos,borderwidth=5,font=("Arial",22),width=6)
        textGasolina.config(text= str(count3))
        textGasolina.place(x=20,y=620)
        count3=count3-velgaso
        nivel1.after(500,gaso)
    else:
        velmapa=0
        pierde=nivel1.create_image(450,350,image=gameover)
        gana=nivel1.create_image(1090,350,image=win)
        velrun=0
        velgas=0
        points=0
        vely = 0
        velx = 0
        velgaso = 0
        
def gaso2():
    global count4,velmapa,velgas,velrun,count3,points,gasolin,vely,velx,velgaso
    if(count4>=0):
        textGasolina= tkinter.Label(dos,borderwidth=5,font=("Arial",22),width=6)
        textGasolina.config(text= str(count4))
        textGasolina.place(x=1400,y=620)
        count4=count4-velgaso
        nivel1.after(500,gaso2)
    else:
        velmapa=0
        pierde=nivel1.create_image(1090,350,image=gameover)
        gana=nivel1.create_image(450,350,image=win)
        velrun=0
        velgas=0
        points=0
        vely = 0
        velx = 0
        velgaso = 0

#Gasolina nivel 2

def gaso3():
    global count9,velmapa,velgas,velrun,count4,points,velgaso,vely,velx
    if(count9>=0):
        
        textGasolina3= tkinter.Label(lvl3,borderwidth=5,font=("Arial",22),width=6)
        textGasolina3.config(text= str(count9))
        textGasolina3.place(x=20,y=620)
        count9=count9-velgaso
        nivel2.after(500,gaso3)
    else:
        velmapa=0
        pierde=nivel2.create_image(450,350,image=gameover)
        gana=nivel2.create_image(1090,350,image=win)
        velrun=0
        velgas=0
        points=0
        velgaso = 0
        vely = 0
        velx = 0
        
def gaso4():
    global count10,velmapa,velgas,velrun,count3,points,gasolin,velgaso,vely,velx,lvl3
    if(count10>=0):
        textGasolina4= tkinter.Label(lvl3,borderwidth=5,font=("Arial",22),width=6)
        textGasolina4.config(text= str(count10))
        textGasolina4.place(x=1400,y=620)
        count10=count10-velgaso
        nivel2.after(500,gaso4)
    else:
        velmapa=0
        pierde=nivel2.create_image(1090,350,image=gameover)
        gana=nivel2.create_image(450,350,image=win)
        velrun=0
        velgas=0
        points=0
        velgaso = 0
        vely = 0
        velx = 0

# GASOLINA NIVEL 3


def gaso5():
    global count15,velmapa2,velgas,velrun,count16,points,vely2,velx,velgaso
    if(count15>=0):
        
        textGasolina5= tkinter.Label(lvl4,borderwidth=5,font=("Arial",22),width=6)
        textGasolina5.config(text= str(count15))
        textGasolina5.place(x=20,y=620)
        count15=count15-velgaso
        nivel3.after(500,gaso5)
    else:
        velmapa2=0
        pierde=nivel3.create_image(450,350,image=gameover)
        gana=nivel3.create_image(1090,350,image=win)
        velrun=0
        velgas=0
        points=0
        vely2 = 0
        velx = 0
        velgaso = 0
        
def gaso6():
    global count15,velmapa2,velgas,velrun,count16,points,gasolin,vely2,velx,velgaso
    if(count16>=0):
        textGasolina6= tkinter.Label(lvl4,borderwidth=5,font=("Arial",22),width=6)
        textGasolina6.config(text= str(count16))
        textGasolina6.place(x=1400,y=620)
        count16=count16-velgaso
        nivel3.after(500,gaso6)
    else:
        velmapa2=0
        pierde=nivel3.create_image(1090,350,image=gameover)
        gana=nivel3.create_image(450,350,image=win)
        velrun=0
        velgas=0
        points=0
        vely2 = 0
        velx = 0
        velgaso = 0

#Gasolina nivel 4

def gaso7():
    global count17,velmapa2,velgas,velrun,count18,points,velgaso,vely2,velx,lvl5
    if(count17>=0):
        
        textGasolina7= tkinter.Label(lvl5,borderwidth=5,font=("Arial",22),width=6)
        textGasolina7.config(text= str(count17))
        textGasolina7.place(x=20,y=620)
        count17=count17-velgaso
        nivel4.after(500,gaso7)
    else:
        velmapa2=0
        pierde=nivel4.create_image(450,350,image=gameover)
        gana=nivel4.create_image(1090,350,image=win)
        velrun=0
        velgas=0
        points=0
        velgaso = 0
        vely2 = 0
        velx = 0
        
def gaso8():
    global count17,velmapa2,velgas,velrun,count18,points,gasolin,velgaso,vely2,velx
    if(count18>=0):
        textGasolina8= tkinter.Label(lvl5,borderwidth=5,font=("Arial",22),width=6)
        textGasolina8.config(text= str(count18))
        textGasolina8.place(x=1400,y=620)
        count18=count18-velgaso
        nivel4.after(500,gaso8)
    else:
        velmapa2=0
        pierde=nivel4.create_image(1090,350,image=gameover)
        gana=nivel4.create_image(450,350,image=win)
        velrun=0
        velgas=0
        points=0
        velgaso = 0
        vely2 = 0
        velx = 0
    
#puntos cada nivel        
            

points=200    
def puntos():
    global count,points
    textGasolina= tkinter.Label(dos,borderwidth=5,font=("Arial",23))
    textGasolina.config(text= str(count))
    textGasolina.place(x=1400,y=450)
    count+=points
    nivel1.after(1000,puntos)
def puntos2():
    global count2,points
    textGasolina= tkinter.Label(dos,borderwidth=5,font=("Arial",23))
    textGasolina.config(text= str(count2))
    textGasolina.place(x=20,y=450)
    count2=count2+points
    nivel1.after(1000,puntos2)
def puntos3():
    global sec3,points
    textGasolina3= tkinter.Label(lvl3,borderwidth=5,font=("Arial",23))
    textGasolina3.config(text= str(sec3))
    textGasolina3.place(x=1400,y=450)
    sec3+=points
    nivel2.after(1000,puntos3)
def puntos4():
    global sec4,points
    textGasolina4= tkinter.Label(lvl3,borderwidth=5,font=("Arial",23))
    textGasolina4.config(text= str(sec4))
    textGasolina4.place(x=20,y=450)
    sec4=sec4+points
    nivel2.after(2000,puntos4)
def puntos5():
    global sec5,points
    textGasolina5= tkinter.Label(lvl4,borderwidth=5,font=("Arial",23))
    textGasolina5.config(text= str(sec5))
    textGasolina5.place(x=1400,y=450)
    sec5+=points
    nivel3.after(1000,puntos5)
def puntos6():
    global sec6,points
    textGasolina6= tkinter.Label(lvl4,borderwidth=5,font=("Arial",23))
    textGasolina6.config(text= str(sec6))
    textGasolina6.place(x=20,y=450)
    sec6=sec6+points
    nivel3.after(2000,puntos6)
def puntos7():
    global sec7,points
    textGasolina7= tkinter.Label(lvl5,borderwidth=5,font=("Arial",23))
    textGasolina7.config(text= str(sec7))
    textGasolina7.place(x=1400,y=450)
    sec7+=points
    nivel4.after(1000,puntos3)
def puntos8():
    global sec8,points
    textGasolina8= tkinter.Label(lvl5,borderwidth=5,font=("Arial",23))
    textGasolina8.config(text= str(sec8))
    textGasolina8.place(x=20,y=450)
    sec8=sec8+points
    nivel4.after(1000,puntos4)




# Velocidad del carro en el mapa

def velocidad1():
    global count5
    if(count5>201):
        count5=count5+0
    else:
            textVelocidad=tkinter.Label(dos,borderwidth=5,font=("Arial",22),width=6)
            textVelocidad.config(text= str(count5))
            textVelocidad.place(x=20,y=250)
            count5=count5+30
            nivel1.after(500,velocidad1)
def velocidad2():
    global count6
    if(count6>201):
        count6=count6+0
    else:
            textVelocidad=tkinter.Label(dos,borderwidth=5,font=("Arial",22),width=6)
            textVelocidad.config(text= str(count5))
            textVelocidad.place(x=1400,y=250)
            count6=count6+30
            nivel1.after(500,velocidad2)
def velocidad3():
    global count7
    if(count7>201):
        count7=count7+0
    else:
            textVelocidad3=tkinter.Label(lvl3,borderwidth=5,font=("Arial",22),width=6)
            textVelocidad3.config(text= str(count7))
            textVelocidad3.place(x=20,y=250)
            count7=count7+30
            nivel2.after(500,velocidad3)
def velocidad4():
    global count8
    if(count8>201):
        count8=count8+0
    else:
            textVelocidad4=tkinter.Label(lvl3,borderwidth=5,font=("Arial",22),width=6)
            textVelocidad4.config(text= str(count8))
            textVelocidad4.place(x=1400,y=250)
            count8=count8+30
            nivel2.after(500,velocidad4)
def velocidad5():
    global count11
    if(count11>201):
        count11=count11+0
    else:
            textVelocidad5=tkinter.Label(lvl4,borderwidth=5,font=("Arial",22),width=6)
            textVelocidad5.config(text= str(count11))
            textVelocidad5.place(x=20,y=250)
            count11=count11+30
            nivel3.after(500,velocidad5)
def velocidad6():
    global count12
    if(count12>201):
        count12=count12+0
    else:
            textVelocidad6=tkinter.Label(lvl4,borderwidth=5,font=("Arial",22),width=6)
            textVelocidad6.config(text= str(count12))
            textVelocidad6.place(x=1400,y=250)
            count12=count12+30
            nivel3.after(500,velocidad6)
def velocidad7():
    global count13
    if(count13>201):
        count13=count13+0
    else:
            textVelocidad7=tkinter.Label(lvl5,borderwidth=5,font=("Arial",22),width=6)
            textVelocidad7.config(text= str(count13))
            textVelocidad7.place(x=20,y=250)
            count13=count13+30
            nivel4.after(500,velocidad7)
def velocidad8():
    global count14
    if(count14>201):
        count14=count14+0
    else:
            textVelocidad8=tkinter.Label(lvl5,borderwidth=5,font=("Arial",22),width=6)
            textVelocidad8.config(text= str(count14))
            textVelocidad8.place(x=1400,y=250)
            count14=count14+30
            nivel4.after(500,velocidad8)
        
            
#widgets
pantalla = tkinter.PhotoImage(file="fondo.png")

d = tkinter.Canvas(v, bg="blue", width=1024, height=768)

st = tkinter.Label(d,image=pantalla)
bot = tkinter.Button(d,text="Nivel 1",bg="blue",fg="white",command=start,cursor="hand2",
                     relief="raised", borderwidth=5,font=("Time new roman",26)).place(x=1100,y=100)
bot2 = tkinter.Button(d,text="Nivel 2",bg="blue",fg="white",command=start2,cursor="hand2",
                      relief="raised", borderwidth=5,font=("Time new roman",26)).place(x=1100,y=250)
bot3 = tkinter.Button(d,text="Nivel 3",bg="blue",fg="white",command=start3,cursor="hand2",
                      relief="raised", borderwidth=5,font=("Time new roman",26)).place(x=1100,y=400)
bot4 = tkinter.Button(d,text="Nivel 4",bg="blue",fg="white",command=start4,cursor="hand2",
                      relief="raised", borderwidth=5,font=("Time new roman",26)).place(x=1100,y=550)
bot5 = tkinter.Button(d,text="Nivel 5",bg="blue",fg="white",cursor="hand2",
                      relief="raised", borderwidth=5,font=("Time new roman",26)).place(x=1100,y=700)
c = tkinter.Label(d,text="CHAMPIONS RACE",bg="black",fg="white",width=50,relief="raised", borderwidth=10,font=("Arial",36)).place(x=70,y=0)

# Liga el evento key al canvas

#d.bind("<Key>", key)


# Pone el foco en el canvas

d.focus_set()


# Empaqueta (muestra) los widgets
d.pack()
st.pack()
# Dibuja algo en el canvas
# Carga una imagen
player1 = tkinter.StringVar()
player2 = tkinter.StringVar()
caja = tkinter.Entry(d,textvariable=player1,font=("Arial",14)).place(x=100,y=160)
caja2 = tkinter.Entry(d,textvariable=player2,font=("Arial",14)).place(x=100,y=320)
player1nombre = tkinter.Label(d,text="Jugador1 nombre:",font=("Arial",14)).place(x=100,y=120)
player1nombre = tkinter.Label(d,text="Jugador2 nombre:",font=("Arial",14)).place(x=90,y=280)
carro = tkinter.PhotoImage(file="carro5.png")
carro2 = tkinter.PhotoImage(file="carro6.png")
carro20 = tkinter.PhotoImage(file="carro6.png")
carro3 = tkinter.PhotoImage(file="carro7.png")
carro30 = tkinter.PhotoImage(file="carro7.png")
carro4 = tkinter.PhotoImage(file="carro8.png")
gasolina = tkinter.PhotoImage(file="gasolina.png")
volteard = tkinter.PhotoImage(file="vd.png")
volteari = tkinter.PhotoImage(file="vi.png")
explosion = tkinter.PhotoImage(file="explosion1.png")
fondolvl1 = tkinter.PhotoImage(file="fondo1.png")
fondolvl2 = tkinter.PhotoImage(file="mapa2.png")
fondolvl3 = tkinter.PhotoImage(file="lvl3.png")
fondolvl4 = tkinter.PhotoImage(file="lvl4.png")
gameover = tkinter.PhotoImage(file="gameover.png")
win = tkinter.PhotoImage(file="win.png")

st= d.create_rectangle(10,10,200,200,outline="black",fill="blue")
mapa1=d.create_image(500,400,image=fondolvl1)
carro1=d.create_image(450,750,image=carro)
carrito=d.create_image(850,800,image=carro)

# Ciclo para escuchar los eventos

v.mainloop()
