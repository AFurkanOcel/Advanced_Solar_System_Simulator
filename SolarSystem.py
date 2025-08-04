# Coder: A. Furkan ÖCEL
# Last Update: 05.04.2025

from vpython import * 
from math import *
import pygame # müzik eklemek için kullandım
import time # sleep() fonksiyonu için gerekli

scene = canvas(width=1520, height=665)

sound_level = 1
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5) # başlangıç seviyesini 0.5 ayarladım. bunu ses butonuyla Sound_Level fonksiyonuna erişerek artırıp azaltabiliyoruz
# müzik dosyasını yükleme ve çalıştırma
pygame.mixer.music.load("musics/Universe_Music.mp3")
pygame.mixer.music.play(loops=-1, start=15.0) # start=15 deyince müzik dosyasını 13.saniyesinden itibaren çalmaya başlıyor, loops=-1 deyince döngüyü sonsuz hale getiriyor
    
active_scene = 'SolarSystem'

Sun = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Sun.jpg", visible=True)
Mercury_Sun = sphere(radius=0.0035, texture="Images/Mercury.jpg", make_trail=False, trail_radius=0.002, visible=True)
Venus_Sun = sphere(radius=0.0087, texture="Images/Venus.jpg", make_trail=False, trail_radius=0.002, visible=True)
Earth_Sun = sphere(radius=0.0091, texture="Images/Earth.jpg", make_trail=False, trail_radius=0.002, visible=True)
Mars_Sun = sphere(radius=0.0048, texture="Images/Mars.jpg", make_trail=False, trail_radius=0.002, visible=True)
Jupiter_Sun = sphere(radius=0.1004, texture="Images/Jupiter.jpg", make_trail=False, trail_radius=0.002, visible=True)
Saturn_Sun = sphere(radius=0.0836, texture="Images/Saturn.jpg", make_trail=False, trail_radius=0.002, visible=True)
Uranus_Sun = sphere(radius=0.0364, texture="Images/Uranus.jpg", make_trail=False, trail_radius=0.002, visible=True)
Neptune_Sun = sphere(radius=0.0353, texture="Images/Neptune.jpg", make_trail=False, trail_radius=0.002, visible=True)

Earth = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Earth.jpg", visible=False)
Moon_Earth = sphere(radius=0.2723, texture="Images/Moon.jpg", make_trail=False, trail_radius=0.005, visible=False)
Earth_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Earth_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Mercury = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Mercury.jpg", visible=False)
Mercury_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Mercury_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Venus = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Venus.jpg", visible=False)
Venus_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Venus_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Mars = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Mars.jpg", visible=False)
Mars_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Mars_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Jupiter = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Jupiter.jpg", visible=False)
Jupiter_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Jupiter_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Saturn = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Saturn.jpg", visible=False)
Saturn_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Saturn_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Uranus = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Uranus.jpg", visible=False)
Uranus_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Uranus_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Neptune = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Neptune.jpg", visible=False)
Neptune_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Neptune_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Moon = sphere(pos=vector(0, 0, 0), radius=1, texture="Images/Moon.jpg", visible=False)
Moon_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Moon_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

orbit = False
paused = False
language = "English"

t_moon = 60
t_mercury = 240
t_venus = 120
t_earth = 300
t_mars = 0
t_jupiter = 90
t_saturn = 60
t_uranus = 180
t_neptune =270

time_SolarSystem = 0
time_Earth = 0
time_Mercury = 0
time_Venus = 0
time_Mars = 0
time_Jupiter = 0
time_Saturn = 0
time_Uranus = 0
time_Neptune = 0
time_Moon = 0

earth_year = 0
earth_day = 0
mercury_day = 0
venus_day = 0
mars_day = 0
jupiter_day = 0
saturn_day = 0
uranus_day = 0
neptune_day = 0
moon_day = 0  

def Loading_Scene():
    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

    time.sleep(3)

def SolarSystem_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'SolarSystem'
    button_SolarSystem.background = color.green
    button_Earth.background = color.white
    button_Mercury.background = color.white
    button_Venus.background = color.white
    button_Mars.background = color.white
    button_Jupiter.background = color.white
    button_Saturn.background = color.white
    button_Uranus.background = color.white
    button_Neptune.background = color.white
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = True
    Mercury_Sun.visible = True
    Venus_Sun.visible = True
    Earth_Sun.visible = True
    Mars_Sun.visible = True
    Jupiter_Sun.visible = True
    Saturn_Sun.visible = True
    Uranus_Sun.visible = True
    Neptune_Sun.visible = True
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = True
        Venus_Sun.make_trail = True
        Earth_Sun.make_trail = True
        Mars_Sun.make_trail = True
        Jupiter_Sun.make_trail = True
        Saturn_Sun.make_trail = True
        Uranus_Sun.make_trail = True
        Neptune_Sun.make_trail = True
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Earth_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Earth'
    button_SolarSystem.background = color.white
    button_Earth.background = color.green
    button_Mercury.background = color.white
    button_Venus.background = color.white
    button_Mars.background = color.white
    button_Jupiter.background = color.white
    button_Saturn.background = color.white
    button_Uranus.background = color.white
    button_Neptune.background = color.white
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = True
    Moon_Earth.visible = True
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail()
        Moon_Earth.make_trail = True
        Earth_North_Arrow.visible = True
        Earth_South_Arrow.visible = True
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Mercury_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Mercury'
    button_SolarSystem.background = color.white
    button_Earth.background = color.white
    button_Mercury.background = color.green
    button_Venus.background = color.white
    button_Mars.background = color.white
    button_Jupiter.background = color.white
    button_Saturn.background = color.white
    button_Uranus.background = color.white
    button_Neptune.background = color.white
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = True
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = True
        Mercury_South_Arrow.visible = True
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Venus_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Venus'
    button_SolarSystem.background = color.white
    button_Earth.background = color.white
    button_Mercury.background = color.white
    button_Venus.background = color.green
    button_Mars.background = color.white
    button_Jupiter.background = color.white
    button_Saturn.background = color.white
    button_Uranus.background = color.white
    button_Neptune.background = color.white
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = True
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = True
        Venus_South_Arrow.visible = True
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Mars_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Mars'
    button_SolarSystem.background = color.white
    button_Earth.background = color.white
    button_Mercury.background = color.white
    button_Venus.background = color.white
    button_Mars.background = color.green
    button_Jupiter.background = color.white
    button_Saturn.background = color.white
    button_Uranus.background = color.white
    button_Neptune.background = color.white
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum    

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = True
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = True
        Mars_South_Arrow.visible = True
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Jupiter_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Jupiter'
    button_SolarSystem.background = color.white
    button_Earth.background = color.white
    button_Mercury.background = color.white
    button_Venus.background = color.white
    button_Mars.background = color.white
    button_Jupiter.background = color.green
    button_Saturn.background = color.white
    button_Uranus.background = color.white
    button_Neptune.background = color.white
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = True
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = True
        Jupiter_South_Arrow.visible = True
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Saturn_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Saturn'
    button_SolarSystem.background = color.white
    button_Earth.background = color.white
    button_Mercury.background = color.white
    button_Venus.background = color.white
    button_Mars.background = color.white
    button_Jupiter.background = color.white
    button_Saturn.background = color.green
    button_Uranus.background = color.white
    button_Neptune.background = color.white
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = True
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = True
        Saturn_South_Arrow.visible = True
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Uranus_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Uranus'
    button_SolarSystem.background = color.white
    button_Earth.background = color.white
    button_Mercury.background = color.white
    button_Venus.background = color.white
    button_Mars.background = color.white
    button_Jupiter.background = color.white
    button_Saturn.background = color.white
    button_Uranus.background = color.green
    button_Neptune.background = color.white
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = True
    Neptune.visible = False
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = True
        Uranus_South_Arrow.visible = True
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Neptune_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Neptune'
    button_SolarSystem.background = color.white
    button_Earth.background = color.white
    button_Mercury.background = color.white
    button_Venus.background = color.white
    button_Mars.background = color.white
    button_Jupiter.background = color.white
    button_Saturn.background = color.white
    button_Uranus.background = color.white
    button_Neptune.background = color.green
    button_Moon.background = color.white

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = True
    Moon.visible = False

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = True
        Neptune_South_Arrow.visible = True
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

def Moon_Scene():
    global active_scene # bunu yazmak zorundayım yoksa active_scene i algılamıyor
    active_scene = 'Moon'
    button_SolarSystem.background = color.white
    button_Earth.background = color.white
    button_Mercury.background = color.white
    button_Venus.background = color.white
    button_Mars.background = color.white
    button_Jupiter.background = color.white
    button_Saturn.background = color.white
    button_Uranus.background = color.white
    button_Neptune.background = color.white
    button_Moon.background = color.green

    Loading_Scene() # Loading_Scene i burada çağırıyorum çünkü buton renkleri değiştikten sonra çalışsın istiyorum

    Sun.visible = False
    Mercury_Sun.visible = False
    Venus_Sun.visible = False
    Earth_Sun.visible = False
    Mars_Sun.visible = False
    Jupiter_Sun.visible = False
    Saturn_Sun.visible = False
    Uranus_Sun.visible = False
    Neptune_Sun.visible = False
    Earth.visible = False
    Moon_Earth.visible = False
    Mercury.visible = False
    Venus.visible = False
    Mars.visible = False
    Jupiter.visible = False
    Saturn.visible = False
    Uranus.visible = False
    Neptune.visible = False
    Moon.visible = True

    if orbit == True: # bu sahneye geçerken kuyruk oluşumu sıfırdan başlasın diye böyle yapıyorum
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail() # önceki sahnede olan kuyrukları da silmemiz gerekiyor
        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = True
        Moon_South_Arrow.visible = True

def Switch_Orbit():
    global orbit
    if orbit == False:
        orbit = True
        Mercury_Sun.make_trail = True
        Venus_Sun.make_trail = True
        Earth_Sun.make_trail = True
        Mars_Sun.make_trail = True
        Jupiter_Sun.make_trail = True
        Saturn_Sun.make_trail = True
        Uranus_Sun.make_trail = True
        Neptune_Sun.make_trail = True
        Moon_Earth.make_trail = True
        if active_scene == 'Earth':
            Earth_North_Arrow.visible = True
            Earth_South_Arrow.visible = True
        elif active_scene == 'Mercury':
            Mercury_North_Arrow.visible = True
            Mercury_South_Arrow.visible = True
        elif active_scene == 'Venus':
            Venus_North_Arrow.visible = True
            Venus_South_Arrow.visible = True
        elif active_scene == 'Mars':
            Mars_North_Arrow.visible = True
            Mars_South_Arrow.visible = True
        elif active_scene == 'Jupiter':
            Jupiter_North_Arrow.visible = True
            Jupiter_South_Arrow.visible = True
        elif active_scene == 'Saturn':
            Saturn_North_Arrow.visible = True
            Saturn_South_Arrow.visible = True
        elif active_scene == 'Uranus':
            Uranus_North_Arrow.visible = True
            Uranus_South_Arrow.visible = True
        elif active_scene == 'Neptune':
            Neptune_North_Arrow.visible = True
            Neptune_South_Arrow.visible = True
        elif active_scene == 'Moon':
            Moon_North_Arrow.visible = True
            Moon_South_Arrow.visible = True

        if language == 'English':
            button_Orbit.text = 'Orbit:yes'
        else:
            button_Orbit.text = 'Yörünge:var'
    else:
        orbit = False
        Earth_North_Arrow.visible = False
        Earth_South_Arrow.visible = False
        Mercury_North_Arrow.visible = False
        Mercury_South_Arrow.visible = False
        Venus_North_Arrow.visible = False
        Venus_South_Arrow.visible = False
        Mars_North_Arrow.visible = False
        Mars_South_Arrow.visible = False
        Jupiter_North_Arrow.visible = False
        Jupiter_South_Arrow.visible = False
        Saturn_North_Arrow.visible = False
        Saturn_South_Arrow.visible = False
        Uranus_North_Arrow.visible = False
        Uranus_South_Arrow.visible = False
        Neptune_North_Arrow.visible = False
        Neptune_South_Arrow.visible = False
        Moon_North_Arrow.visible = False
        Moon_South_Arrow.visible = False

        Mercury_Sun.make_trail = False
        Venus_Sun.make_trail = False
        Earth_Sun.make_trail = False
        Mars_Sun.make_trail = False
        Jupiter_Sun.make_trail = False
        Saturn_Sun.make_trail = False
        Uranus_Sun.make_trail = False
        Neptune_Sun.make_trail = False
        Moon_Earth.make_trail = False
        Mercury_Sun.clear_trail()
        Venus_Sun.clear_trail()
        Earth_Sun.clear_trail()
        Mars_Sun.clear_trail()
        Jupiter_Sun.clear_trail()
        Saturn_Sun.clear_trail()
        Uranus_Sun.clear_trail()
        Neptune_Sun.clear_trail()
        Moon_Earth.clear_trail()

        if language == 'English':
            button_Orbit.text = 'Orbit:no'
        else:
            button_Orbit.text = 'Yörünge:yok'

def Pause_Run():
    global paused
    if paused == False:
        paused = True
        if language == 'English':
            button_Pause.text = 'Run'
        else:
            button_Pause.text = 'Çalıştır'
    else:
        paused = False
        if language == 'English':
            button_Pause.text = 'Pause'
        else:
            button_Pause.text = 'Durdur'

def English_To_Turkish():
    global language
    language = "Turkish"
    button_SolarSystem.text = "Güneş Sistemi"
    button_Earth.text = "Dünya"
    button_Mercury.text = "Merkür"
    button_Venus.text = "Venüs"
    button_Mars.text = "Mars"
    button_Jupiter.text = "Jüpiter"
    button_Saturn.text = "Satürn"
    button_Uranus.text = "Uranüs"
    button_Neptune.text = "Neptün"
    button_Moon.text = "Ay"
    if orbit == False:
        button_Orbit.text = 'Yörünge:yok'
    else:
        button_Orbit.text = 'Yörünge:var'
    if paused == False:
        button_Pause.text = 'Durdur'
    else:
        button_Pause.text = 'Çalıştır'
    button_Click.text = 'Orta Tık = Zoom     Sağ Tık = Hareket'
    if active_scene == 'SolarSystem': 
        button_Time.text = f'Yıl: {earth_year}' + '   ' + '(1 Yıl = 0,000001 Dünya Yılı)'
    elif active_scene == 'Earth':
        button_Time.text = f'Gün: {earth_day}' + '   ' + '(1 Gün = 0,0001 Dünya Günü)'
    elif active_scene == 'Mercury':
        button_Time.text = f'Gün: {mercury_day}' + '   ' + '(1 Gün = 0,0001 Merkür Günü)'
    elif active_scene == 'Venus':
        button_Time.text = f'Gün: {venus_day}' + '   ' + '(1 Gün = 0,0001 Venüs Günü)'
    elif active_scene == 'Mars':
        button_Time.text = f'Gün: {mars_day}' + '   ' + '(1 Gün = 0,0001 Mars Günü)'
    elif active_scene == 'Jupiter':
        button_Time.text = f'Gün: {jupiter_day}' + '   ' + '(1 Gün = 0,0001 Jüpiter Günü)'
    elif active_scene == 'Saturn':
        button_Time.text = f'Gün: {saturn_day}' + '   ' + '(1 Gün = 0,0001 Satürn Günü)'
    elif active_scene == 'Uranus':
        button_Time.text = f'Gün: {uranus_day}' + '   ' + '(1 Gün = 0,0001 Uranüs Günü)'
    elif active_scene == 'Neptune':
        button_Time.text = f'Gün: {neptune_day}' + '   ' + '(1 Gün = 0,0001 Neptün Günü)'
    elif active_scene == 'Moon':
        button_Time.text = f'Gün: {moon_day}' + '   ' + '(1 Gün = 0,0001 Ay Günü)'

def Turkish_To_English():
    global language
    language = "English"
    button_SolarSystem.text = "Solar System"
    button_Earth.text = "Earth"
    button_Mercury.text = "Mercury"
    button_Venus.text = "Venus"
    button_Mars.text = "Mars"
    button_Jupiter.text = "Jupiter"
    button_Saturn.text = "Saturn"
    button_Uranus.text = "Uranus"
    button_Neptune.text = "Neptune"
    button_Moon.text = "Moon"
    if orbit == False:
        button_Orbit.text = 'Orbit:no'
    else:
        button_Orbit.text = 'Orbit:yes'
    if paused == False:
        button_Pause.text = 'Pause'
    else:
        button_Pause.text = 'Run'
    button_Click.text = 'Middle Click = Zoom     Right Click = Move'
    if active_scene == 'SolarSystem': 
        button_Time.text = f'Year: {earth_year}' + '   ' + '(1 Year = 0,000001 Earth Year)'
    elif active_scene == 'Earth':
        button_Time.text = f'Day: {earth_day}' + '   ' + '(1 Day = 0,0001 Earth Day)'
    elif active_scene == 'Mercury':
        button_Time.text = f'Day: {mercury_day}' + '   ' + '(1 Day = 0,0001 Mercury Day)'
    elif active_scene == 'Venus':
        button_Time.text = f'Day: {venus_day}' + '   ' + '(1 Day = 0,0001 Venus Day)'
    elif active_scene == 'Mars':
        button_Time.text = f'Day: {mars_day}' + '   ' + '(1 Day = 0,0001 Mars Day)'
    elif active_scene == 'Jupiter':
        button_Time.text = f'Day: {jupiter_day}' + '   ' + '(1 Day = 0,0001 Jupiter Day)'
    elif active_scene == 'Saturn':
        button_Time.text = f'Day: {saturn_day}' + '   ' + '(1 Day = 0,0001 Saturn Day)'
    elif active_scene == 'Uranus':
        button_Time.text = f'Day: {uranus_day}' + '   ' + '(1 Day = 0,0001 Uranus Day)'
    elif active_scene == 'Neptune':
        button_Time.text = f'Day: {neptune_day}' + '   ' + '(1 Day = 0,0001 Neptune Day)'
    elif active_scene == 'Moon':
        button_Time.text = f'Day: {moon_day}' + '   ' + '(1 Day = 0,0001 Moon Day)'

def Sound_Level():
    global sound_level
    if sound_level == 1:
        sound_level = 2
        button_Sound.text = "<))"
        pygame.mixer.music.set_volume(1.0)
    elif sound_level == 2:
        sound_level = 0
        button_Sound.text = '<'
        pygame.mixer.music.set_volume(0.0)
    else:
        sound_level = 1
        button_Sound.text = '<)'
        pygame.mixer.music.set_volume(0.5)

def nothing(): # bu fonksiyonu button_Click ve button_Time için yazdım. aslında buton değiller fakat bind komutu kullanılmak zorunda, o nedenle boyle bir cozum buldum
    1==1

button_SolarSystem = button(text='Solar System', pos=scene.title_anchor, background=color.green, bind=SolarSystem_Scene)
button_Earth = button(text='Earth', pos=scene.title_anchor, bind=Earth_Scene)
button_Mercury = button(text='Mercury', pos=scene.title_anchor, bind=Mercury_Scene)
button_Venus = button(text='Venus', pos=scene.title_anchor, bind=Venus_Scene)
button_Mars = button(text='Mars', pos=scene.title_anchor, bind=Mars_Scene)
button_Jupiter = button(text='Jupiter', pos=scene.title_anchor, bind=Jupiter_Scene)
button_Saturn = button(text='Saturn', pos=scene.title_anchor, bind=Saturn_Scene)
button_Uranus = button(text='Uranus', pos=scene.title_anchor, bind=Uranus_Scene)
button_Neptune = button(text='Neptune', pos=scene.title_anchor, bind=Neptune_Scene)
button_Moon = button(text='Moon', pos=scene.title_anchor, bind=Moon_Scene)

button_Orbit = button(text='Orbit:no', pos=scene.title_anchor, background=hat(vector(120,120,120)), color=color.white, bind=Switch_Orbit)

button_Pause = button(text='Pause', pos=scene.title_anchor, background=hat(vector(120,120,120)), bind=Pause_Run)

button_Click = button(text='Middle Click = Zoom     Right Click = Move', pos=scene.title_anchor, background=hat(vector(240,239,184)), bind=nothing)

button_Time = button(text=f'Year: {earth_year}' + '   ' + '(1 Year = 0,000001 Earth Year)', pos=scene.title_anchor, background=color.black, color=color.white, bind=nothing)

button_TurFlag = button(text='Türkçe', pos=scene.title_anchor, background=color.red, color=color.white, bind=English_To_Turkish)
button_EngFlag = button(text='English', pos=scene.title_anchor, background=color.blue, color=color.white, bind=Turkish_To_English)

button_Sound = button(text='<)', pos=scene.title_anchor, background=color.orange, color=color.white, bind=Sound_Level)

while True:
    if paused == False:
        rate(100)
        
        # 1 yıl 31,55 saniye olsun (31,55s = 0,000001day, 1 yıl 8765,82saat yani 31,55 milyon saniye)
        t_mercury -= 2 * pi / 757.3 # 3155 * 0,24 (0,24yıl = merkürün güneş etrafında 1 turu)
        t_venus -= 2 * pi / 1956.1 # 3155 * 0,62 (0,62yıl = venüsün güneş etrafında 1 turu)
        t_earth -= 2 * pi / 3155 # 3155 * 1 (1yıl = dünyanın güneş etrafında 1 turu)
        t_mars -= 2 * pi / 5931.4 # 3155 * 1,88 (1,88yıl = marsın güneş etrafında 1 turu)
        t_jupiter -= 2 * pi / 37418.3 # 3155 * 11,86 (11,86yıl = jupiterin güneş etrafında 1 turu)
        t_saturn -= 2 * pi / 92946.3 # 3155 * 29,46 (29,46yıl = satürnün güneş etrafında 1 turu)
        t_uranus -= 2 * pi / 265051 # 3155 * 84,01 (84,01yıl = uranüsün güneş etrafında 1 turu)
        t_neptune -= 2 * pi / 519944 # 3155 * 164,8 (164,8yıl = neptünün güneş etrafında 1 turu)
        Sun.rotate(angle=2 * pi / 23328, axis=vector(0, 1, 0)) # güneşin 1 günü = 27 dünya günü (8,64 * 27 = 233,28)
        Mercury_Sun.pos = Sun.pos + vector(1.6 * cos(t_mercury), 0, 1.6 * sin(t_mercury)) # merkürün güneş etrafında dönmesi
        Venus_Sun.pos = Sun.pos + vector(2.0 * cos(t_venus), 0, 2.0 * sin(t_venus)) # venüsün güneş etrafında dönmesi
        Earth_Sun.pos = Sun.pos + vector(2.4 * cos(t_earth), 0, 2.4 * sin(t_earth)) # dünyanın güneş etrafında dönmesi
        Mars_Sun.pos = Sun.pos + vector(2.8 * cos(t_mars), 0, 2.8 * sin(t_mars)) # marsın güneş etrafında dönmesi
        Jupiter_Sun.pos = Sun.pos + vector(3.2 * cos(t_jupiter), 0, 3.2 * sin(t_jupiter)) # jüpiterin güneş etrafında dönmesi
        Saturn_Sun.pos = Sun.pos + vector(3.6 * cos(t_saturn), 0, 3.6 * sin(t_saturn)) # satürnnün güneş etrafında dönmesi
        Uranus_Sun.pos = Sun.pos + vector(4.0 * cos(t_uranus), 0, 4.0 * sin(t_uranus)) # uranüsün güneş etrafında dönmesi
        Neptune_Sun.pos = Sun.pos + vector(4.4 * cos(t_neptune), 0, 4.4 * sin(t_neptune)) # neptünün güneş etrafında dönmesi

        # 1 gün 8,64 saniye olsun (8,64s = 0,0001day, 1 dünya günü 24 saat aldım aslında 23,93 saat sonrasında düzeltebilirsin)
        t_moon -= 2 * pi / 23605 # 864 * 27,4 (27,4gün = ayın dünya etrafında 1 turu aslında 27,32 gün sonrasında düzeltebilirsin)
        Earth.rotate(angle=2 * pi / 864, axis=vector(0, 1, 0)) 
        Moon_Earth.rotate(angle=2 * pi / 23605, axis=vector(0, 1, 0)) # ayın kendi etrafında dönmesi
        Moon_Earth.pos = Earth.pos + vector(2.5 * cos(t_moon), 0, 2.5 * sin(t_moon)) # ayın dünya etrafında dönmesi
        Earth_North_Arrow.rotate(angle=2 * pi / 864, axis=vector(0, 1, 0)) 
        Earth_South_Arrow.rotate(angle=-2 * pi / 864, axis=vector(0, -1, 0))

        # 1 merkür günü 506,70 saniye olsun (506,7s = 0,0001mercuryday, 1 merkür günü 1407,5 saat yani 5,067 milyon saniye)
        Mercury.rotate(angle=2 * pi / 50670, axis=vector(0,1,0))
        Mercury_North_Arrow.rotate(angle=2 * pi / 50670, axis=vector(0, 1, 0)) 
        Mercury_South_Arrow.rotate(angle=-2 * pi / 50670, axis=vector(0, -1, 0))
        
        # 1 venüs günü 2099,52 saniye olsun (2099,52s = 0,0001venusday, 1 venüs günü 5832 saat yani 20,9952 milyon saniye)
        Venus.rotate(angle=2 * pi / 209952, axis=vector(0,1,0))
        Venus_North_Arrow.rotate(angle=2 * pi / 209952, axis=vector(0, 1, 0)) 
        Venus_South_Arrow.rotate(angle=-2 * pi / 209952, axis=vector(0, -1, 0))

        # 1 mars günü 8,86 saniye olsun (8,86 saniye = 0,0001marsday, 1 mars günü 24,62 saat yani 88632 saniye)
        Mars.rotate(angle=2 * pi / 886, axis=vector(0,1,0))
        Mars_North_Arrow.rotate(angle=2 * pi / 886, axis=vector(0, 1, 0)) 
        Mars_South_Arrow.rotate(angle=-2 * pi / 886, axis=vector(0, -1, 0))

        # 1 jüpiter günü 3,57 saniye olsun (3,57 saniye = 0,0001jupiterday, 1 jüpiter günü 9,93 saat yani 35748 saniye)
        Jupiter.rotate(angle=2 * pi / 357, axis=vector(0,1,0))
        Jupiter_North_Arrow.rotate(angle=2 * pi / 357, axis=vector(0, 1, 0)) 
        Jupiter_South_Arrow.rotate(angle=-2 * pi / 357, axis=vector(0, -1, 0))

        # 1 satürn günü 3,83 saniye olsun (3,83 saniye = 0,0001saturnday, 1 satürn günü 10,66 saat yani 38376 saniye)
        Saturn.rotate(angle=2 * pi / 383, axis=vector(0,1,0))
        Saturn_North_Arrow.rotate(angle=2 * pi / 383, axis=vector(0, 1, 0)) 
        Saturn_South_Arrow.rotate(angle=-2 * pi / 383, axis=vector(0, -1, 0))

        # 1 uranüs günü 6,20 saniye olsun (6,20 saniye = 0,0001uranusday, 1 uranüs günü 17,24 saat yani 62064  saniye)
        Uranus.rotate(angle=2 * pi / 620, axis=vector(0,1,0))
        Uranus_North_Arrow.rotate(angle=2 * pi / 620, axis=vector(0, 1, 0)) 
        Uranus_South_Arrow.rotate(angle=-2 * pi / 620, axis=vector(0, -1, 0))

        # 1 neptün günü 5,80 saniye olsun (5,80 saniye = 0.0001neptuneday, 1 neptün günü 16,11 saat yani 57996 saniye)
        Neptune.rotate(angle=2 * pi / 580, axis=vector(0,1,0))
        Neptune_North_Arrow.rotate(angle=2 * pi / 580, axis=vector(0, 1, 0)) 
        Neptune_South_Arrow.rotate(angle=-2 * pi / 580, axis=vector(0, -1, 0))

        # 1 ay günü 235,87 saniye olsun (235,87 saniye = 0,0001moonday, 1 ay günü 655,2 saat yani 2,3587 milyon saniye)
        Moon.rotate(angle=2 * pi / 23587, axis=vector(0,1,0))
        Moon_North_Arrow.rotate(angle=2 * pi / 23587, axis=vector(0, 1, 0)) 
        Moon_South_Arrow.rotate(angle=-2 * pi / 23587, axis=vector(0, -1, 0))

        if active_scene == 'SolarSystem': 
            time_SolarSystem += 1
            if time_Earth > 0 or time_Mercury > 0 or time_Venus > 0 or time_Mars > 0 or time_Jupiter > 0 or time_Saturn > 0 or time_Uranus > 0 or time_Neptune > 0 or time_Moon > 0: # bunu yapıyoruz çünkü diğer sahnelerden bu sahneye geçince yıl sayısı 1 artana kadar önceki yazı kalıyor
                time_Earth = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için earth_year artmaz
                time_Mercury = 0
                time_Venus = 0
                time_Mars = 0
                time_Jupiter = 0
                time_Saturn = 0
                time_Uranus = 0
                time_Neptune = 0
                time_Moon = 0 
                earth_year = 0 # earth_year ı da sıfıra eşitliyoruz çünkü tekrar bu sahneye geldiğimizde yıl sayısı sıfırdan başlasın istedim
                if language == 'English':
                    button_Time.text = f'Year: {earth_year}' + '   ' + '(1 Year = 0,000001 Earth Year)'
                else:
                    button_Time.text = f'Yıl: {earth_year}' + '   ' + '(1 Yıl = 0,000001 Dünya Yılı)'
            if time_SolarSystem% 3155 == 0:
                earth_year +=1
                if language == 'English':
                    button_Time.text = f'Year: {earth_year}' + '   ' + '(1 Year = 0,000001 Earth Year)'
                else:
                    button_Time.text = f'Yıl: {earth_year}' + '   ' + '(1 Yıl = 0,000001 Dünya Yılı)'

        if active_scene == 'Earth':
            time_Earth += 1
            if time_SolarSystem > 0 or time_Mercury > 0 or time_Venus > 0 or time_Mars > 0 or time_Jupiter > 0 or time_Saturn > 0 or time_Uranus > 0 or time_Neptune > 0 or time_Moon > 0: # bunu yapıyoruz çünkü diğer sahnelerden bu sahneye geçince gün sayısı 1 artana kadar önceki yazı kalıyor
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için earth_day artmaz
                time_Mercury = 0
                time_Venus = 0
                time_Mars = 0
                time_Jupiter = 0
                time_Saturn = 0
                time_Uranus = 0
                time_Neptune = 0
                time_Moon = 0 
                earth_day = 0 # earth_day i de sıfıra eşitliyoruz çünkü tekrar bu sahneye geldiğimizde gün sayısı sıfırdan başlasın istedim
                if language == 'English':
                    button_Time.text = f'Day: {earth_day}' + '   ' + '(1 Day = 0,0001 Earth Day)'
                else:
                    button_Time.text = f'Gün: {earth_day}' + '   ' + '(1 Gün = 0,0001 Dünya Günü)'
            if time_Earth % 864 == 0:
                earth_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {earth_day}' + '   ' + '(1 Day = 0,0001 Earth Day)'
                else:
                    button_Time.text = f'Gün: {earth_day}' + '   ' + '(1 Gün = 0,0001 Dünya Günü)'

        if active_scene == 'Mercury':
            time_Mercury += 1
            if time_SolarSystem > 0 or time_Earth > 0 or time_Venus > 0 or time_Mars > 0 or time_Jupiter > 0 or time_Saturn > 0 or time_Uranus > 0 or time_Neptune > 0 or time_Moon > 0:
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için mercury_day artmaz
                time_Earth = 0
                time_Venus = 0
                time_Mars = 0
                time_Jupiter = 0
                time_Saturn = 0
                time_Uranus = 0
                time_Neptune = 0
                time_Moon = 0 
                mercury_day = 0
                if language == 'English':
                    button_Time.text = f'Day: {mercury_day}' + '   ' + '(1 Day = 0,0001 Mercury Day)'
                else:
                    button_Time.text = f'Gün: {mercury_day}' + '   ' + '(1 Gün = 0,0001 Merkür Günü)'
            if time_Mercury % 50670 == 0:
                mercury_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {mercury_day}' + '   ' + '(1 Day = 0,0001 Mercury Day)'
                else:
                    button_Time.text = f'Gün: {mercury_day}' + '   ' + '(1 Gün = 0,0001 Merkür Günü)'

        if active_scene == 'Venus':
            time_Venus += 1
            if time_SolarSystem > 0 or time_Earth > 0 or time_Mercury > 0 or time_Mars > 0 or time_Jupiter > 0 or time_Saturn > 0 or time_Uranus > 0 or time_Neptune > 0 or time_Moon > 0:
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için venus_day artmaz
                time_Earth = 0
                time_Mercury = 0
                time_Mars = 0
                time_Jupiter = 0
                time_Saturn = 0
                time_Uranus = 0
                time_Neptune = 0
                time_Moon = 0 
                venus_day = 0
                if language == 'English':
                    button_Time.text = f'Day: {venus_day}' + '   ' + '(1 Day = 0,0001 Venus Day)'
                else:
                    button_Time.text = f'Gün: {venus_day}' + '   ' + '(1 Gün = 0,0001 Venüs Günü)'
            if time_Venus % 209952 == 0:
                venus_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {venus_day}' + '   ' + '(1 Day = 0,0001 Venus Day)'
                else:
                    button_Time.text = f'Gün: {venus_day}' + '   ' + '(1 Gün = 0,0001 Venüs Günü)'

        if active_scene == 'Mars':
            time_Mars += 1
            if time_SolarSystem > 0 or time_Earth > 0 or time_Mercury > 0 or time_Venus > 0 or time_Jupiter > 0 or time_Saturn > 0 or time_Uranus > 0 or time_Neptune > 0 or time_Moon > 0:
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için mars_day artmaz
                time_Earth = 0
                time_Mercury = 0
                time_Venus = 0
                time_Jupiter = 0
                time_Saturn = 0
                time_Uranus = 0
                time_Neptune = 0
                time_Moon = 0 
                mars_day = 0
                if language == 'English':
                    button_Time.text = f'Day: {mars_day}' + '   ' + '(1 Day = 0,0001 Mars Day)'
                else:
                    button_Time.text = f'Gün: {mars_day}' + '   ' + '(1 Gün = 0,0001 Mars Günü)'
            if time_Mars % 886 == 0:
                mars_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {mars_day}' + '   ' + '(1 Day = 0,0001 Mars Day)'
                else:
                    button_Time.text = f'Gün: {mars_day}' + '   ' + '(1 Gün = 0,0001 Mars Günü)'

        if active_scene == 'Jupiter':
            time_Jupiter += 1
            if time_SolarSystem > 0 or time_Earth > 0 or time_Mercury > 0 or time_Venus > 0 or time_Mars > 0 or time_Saturn > 0 or time_Uranus > 0 or time_Neptune > 0 or time_Moon > 0:
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için jupiter_day artmaz
                time_Earth = 0
                time_Mercury = 0
                time_Venus = 0
                time_Mars = 0
                time_Saturn = 0
                time_Uranus = 0
                time_Neptune = 0
                time_Moon = 0 
                jupiter_day = 0
                if language == 'English':
                    button_Time.text = f'Day: {jupiter_day}' + '   ' + '(1 Day = 0,0001 Jupiter Day)'
                else:
                    button_Time.text = f'Gün: {jupiter_day}' + '   ' + '(1 Gün = 0,0001 Jüpiter Günü)'
            if time_Jupiter % 357 == 0:
                jupiter_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {jupiter_day}' + '   ' + '(1 Day = 0,0001 Jupiter Day)'
                else:
                    button_Time.text = f'Gün: {jupiter_day}' + '   ' + '(1 Gün = 0,0001 Jüpiter Günü)'

        if active_scene == 'Saturn':
            time_Saturn += 1
            if time_SolarSystem > 0 or time_Earth > 0 or time_Mercury > 0 or time_Venus > 0 or time_Mars > 0 or time_Jupiter > 0 or time_Uranus > 0 or time_Neptune > 0 or time_Moon > 0:
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için saturn_day artmaz
                time_Earth = 0
                time_Mercury = 0
                time_Venus = 0
                time_Mars = 0
                time_Jupiter = 0
                time_Uranus = 0
                time_Neptune = 0
                time_Moon = 0 
                saturn_day = 0
                if language == 'English':
                    button_Time.text = f'Day: {saturn_day}' + '   ' + '(1 Day = 0,0001 Saturn Day)'
                else:
                    button_Time.text = f'Gün: {saturn_day}' + '   ' + '(1 Gün = 0,0001 Satürn Günü)'
            if time_Saturn % 383 == 0:
                saturn_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {saturn_day}' + '   ' + '(1 Day = 0,0001 Saturn Day)'
                else:
                    button_Time.text = f'Gün: {saturn_day}' + '   ' + '(1 Gün = 0,0001 Satürn Günü)'

        if active_scene == 'Uranus':
            time_Uranus += 1
            if time_SolarSystem > 0 or time_Earth > 0 or time_Mercury > 0 or time_Venus > 0 or time_Mars > 0 or time_Jupiter > 0 or time_Saturn > 0 or time_Neptune > 0 or time_Moon > 0:
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için uranus_day artmaz
                time_Earth = 0
                time_Mercury = 0
                time_Venus = 0
                time_Mars = 0
                time_Jupiter = 0
                time_Saturn = 0
                time_Neptune = 0
                time_Moon = 0 
                uranus_day = 0
                if language == 'English':
                    button_Time.text = f'Day: {uranus_day}' + '   ' + '(1 Day = 0,0001 Uranus Day)'
                else:
                    button_Time.text = f'Gün: {uranus_day}' + '   ' + '(1 Gün = 0,0001 Uranüs Günü)'
            if time_Uranus % 620 == 0:
                uranus_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {uranus_day}' + '   ' + '(1 Day = 0,0001 Uranus Day)'
                else:
                    button_Time.text = f'Gün: {uranus_day}' + '   ' + '(1 Gün = 0,0001 Uranüs Günü)'

        if active_scene == 'Neptune':
            time_Neptune += 1
            if time_SolarSystem > 0 or time_Earth > 0 or time_Mercury > 0 or time_Venus > 0 or time_Mars > 0 or time_Jupiter > 0 or time_Saturn > 0 or time_Uranus > 0 or time_Moon > 0:
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için neptune_day artmaz
                time_Earth = 0
                time_Mercury = 0
                time_Venus = 0
                time_Mars = 0
                time_Jupiter = 0
                time_Saturn = 0
                time_Uranus = 0
                time_Moon = 0 
                neptune_day = 0
                if language == 'English':
                    button_Time.text = f'Day: {neptune_day}' + '   ' + '(1 Day = 0,0001 Neptune Day)'
                else:
                    button_Time.text = f'Gün: {neptune_day}' + '   ' + '(1 Gün = 0,0001 Neptün Günü)'
            if time_Neptune % 580 == 0:
                neptune_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {neptune_day}' + '   ' + '(1 Day = 0,0001 Neptune Day)'
                else:
                    button_Time.text = f'Gün: {neptune_day}' + '   ' + '(1 Gün = 0,0001 Neptün Günü)'

        if active_scene == 'Moon':
            time_Moon += 1
            if time_SolarSystem > 0 or time_Earth > 0 or time_Mercury > 0 or time_Venus > 0 or time_Mars > 0 or time_Jupiter > 0 or time_Saturn > 0 or time_Uranus > 0 or time_Neptune > 0:
                time_SolarSystem = 0 # diğer timeları sıfıra eşitliyoruz çünkü böyle yapmazsak diğer timelardan en az biri hep sıfırdan büyük olucağı için moon_day artmaz
                time_Earth = 0
                time_Mercury = 0
                time_Venus = 0
                time_Mars = 0
                time_Jupiter = 0
                time_Saturn = 0
                time_Uranus = 0
                time_Neptune = 0 
                moon_day = 0
                if language == 'English':
                    button_Time.text = f'Day: {moon_day}' + '   ' + '(1 Day = 0,0001 Moon Day)'
                else:
                    button_Time.text = f'Gün: {moon_day}' + '   ' + '(1 Gün = 0,0001 Ay Günü)'
            if time_Moon % 23587 == 0:
                moon_day += 1
                if language == 'English':
                    button_Time.text = f'Day: {moon_day}' + '   ' + '(1 Day = 0,0001 Moon Day)'
                else:
                    button_Time.text = f'Gün: {moon_day}' + '   ' + '(1 Gün = 0,0001 Ay Günü)'