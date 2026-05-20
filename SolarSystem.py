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
pygame.mixer.music.load("assets/music/Universe_Music.mp3")
pygame.mixer.music.play(loops=-1, start=15.0) # start=15 deyince müzik dosyasını 13.saniyesinden itibaren çalmaya başlıyor, loops=-1 deyince döngüyü sonsuz hale getiriyor
    
active_scene = 'SolarSystem'

Sun = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Sun.jpg", visible=True)
Mercury_Sun = sphere(radius=0.0035, texture="assets/textures/Mercury.jpg", make_trail=False, trail_radius=0.002, visible=True)
Venus_Sun = sphere(radius=0.0087, texture="assets/textures/Venus.jpg", make_trail=False, trail_radius=0.002, visible=True)
Earth_Sun = sphere(radius=0.0091, texture="assets/textures/Earth.jpg", make_trail=False, trail_radius=0.002, visible=True)
Mars_Sun = sphere(radius=0.0048, texture="assets/textures/Mars.jpg", make_trail=False, trail_radius=0.002, visible=True)
Jupiter_Sun = sphere(radius=0.1004, texture="assets/textures/Jupiter.jpg", make_trail=False, trail_radius=0.002, visible=True)
Saturn_Sun = sphere(radius=0.0836, texture="assets/textures/Saturn.jpg", make_trail=False, trail_radius=0.002, visible=True)
Uranus_Sun = sphere(radius=0.0364, texture="assets/textures/Uranus.jpg", make_trail=False, trail_radius=0.002, visible=True)
Neptune_Sun = sphere(radius=0.0353, texture="assets/textures/Neptune.jpg", make_trail=False, trail_radius=0.002, visible=True)

Earth = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Earth.jpg", visible=False)
Moon_Earth = sphere(radius=0.2723, texture="assets/textures/Moon.jpg", make_trail=False, trail_radius=0.005, visible=False)
Earth_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Earth_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Mercury = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Mercury.jpg", visible=False)
Mercury_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Mercury_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Venus = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Venus.jpg", visible=False)
Venus_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Venus_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Mars = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Mars.jpg", visible=False)
Mars_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Mars_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Jupiter = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Jupiter.jpg", visible=False)
Jupiter_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Jupiter_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Saturn = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Saturn.jpg", visible=False)
Saturn_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Saturn_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Uranus = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Uranus.jpg", visible=False)
Uranus_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Uranus_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Neptune = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Neptune.jpg", visible=False)
Neptune_North_Arrow = arrow(pos=vector(0,1,0), axis=vector(0,1,0), length=0.4, color=color.red, visible=False)
Neptune_South_Arrow = arrow(pos=vector(0,-1,0), axis=vector(0,-1,0), length=0.4, color=color.blue, visible=False)

Moon = sphere(pos=vector(0, 0, 0), radius=1, texture="assets/textures/Moon.jpg", visible=False)
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

def axis_from_tilt(tilt):
    tilt_rad = radians(-tilt)
    return norm(vector(sin(tilt_rad), cos(tilt_rad), 0))

PLANET_AXES = {
    'Mercury': {'tilt': 0.03, 'period': 50670, 'spin_direction': 1, 'body': Mercury, 'solar_body': Mercury_Sun, 'north_arrow': Mercury_North_Arrow, 'south_arrow': Mercury_South_Arrow},
    'Venus': {'tilt': 177.36, 'period': 209952, 'spin_direction': -1, 'body': Venus, 'solar_body': Venus_Sun, 'north_arrow': Venus_North_Arrow, 'south_arrow': Venus_South_Arrow},
    'Earth': {'tilt': 23.44, 'period': 864, 'spin_direction': 1, 'body': Earth, 'solar_body': Earth_Sun, 'north_arrow': Earth_North_Arrow, 'south_arrow': Earth_South_Arrow},
    'Mars': {'tilt': 25.19, 'period': 886, 'spin_direction': 1, 'body': Mars, 'solar_body': Mars_Sun, 'north_arrow': Mars_North_Arrow, 'south_arrow': Mars_South_Arrow},
    'Jupiter': {'tilt': 3.13, 'period': 357, 'spin_direction': 1, 'body': Jupiter, 'solar_body': Jupiter_Sun, 'north_arrow': Jupiter_North_Arrow, 'south_arrow': Jupiter_South_Arrow},
    'Saturn': {'tilt': 26.73, 'period': 383, 'spin_direction': 1, 'body': Saturn, 'solar_body': Saturn_Sun, 'north_arrow': Saturn_North_Arrow, 'south_arrow': Saturn_South_Arrow},
    'Uranus': {'tilt': 97.77, 'period': 620, 'spin_direction': -1, 'body': Uranus, 'solar_body': Uranus_Sun, 'north_arrow': Uranus_North_Arrow, 'south_arrow': Uranus_South_Arrow},
    'Neptune': {'tilt': 28.32, 'period': 580, 'spin_direction': 1, 'body': Neptune, 'solar_body': Neptune_Sun, 'north_arrow': Neptune_North_Arrow, 'south_arrow': Neptune_South_Arrow},
    'Moon': {'tilt': 6.68, 'period': 23587, 'spin_direction': 1, 'body': Moon, 'solar_body': None, 'north_arrow': Moon_North_Arrow, 'south_arrow': Moon_South_Arrow},
}

SOLAR_SYSTEM_PLANETS = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def initialize_planet_axes():
    for data in PLANET_AXES.values():
        data['axis'] = axis_from_tilt(data['tilt'])
        data['body'].up = data['axis']
        if data['solar_body'] != None:
            data['solar_body'].up = data['axis']
        data['north_arrow'].shaftwidth = 0.05
        data['south_arrow'].shaftwidth = 0.05
    Moon_Earth.up = PLANET_AXES['Moon']['axis']

def hide_all_axis_arrows():
    for data in PLANET_AXES.values():
        data['north_arrow'].visible = False
        data['south_arrow'].visible = False

def show_axis_arrows(names):
    for name in names:
        PLANET_AXES[name]['north_arrow'].visible = True
        PLANET_AXES[name]['south_arrow'].visible = True

def apply_orbit_visibility():
    hide_all_axis_arrows()
    if orbit == False:
        return
    if active_scene == 'SolarSystem':
        show_axis_arrows(SOLAR_SYSTEM_PLANETS)
    elif active_scene == 'Earth':
        show_axis_arrows(['Earth', 'Moon'])
    elif active_scene in PLANET_AXES:
        show_axis_arrows([active_scene])
    update_axis_arrows()

def update_axis_arrows():
    for name, data in PLANET_AXES.items():
        if active_scene == 'SolarSystem':
            if name not in SOLAR_SYSTEM_PLANETS:
                continue
            body = data['solar_body']
            arrow_length = max(body.radius + 0.035, 0.10)
            shaftwidth = 0.005
        elif active_scene == 'Earth' and name == 'Moon':
            body = Moon_Earth
            arrow_length = 0.45
            shaftwidth = 0.018
        elif active_scene == name:
            body = data['body']
            arrow_length = 1.5
            shaftwidth = 0.05
        else:
            continue

        data['north_arrow'].pos = body.pos
        data['north_arrow'].axis = data['axis'] * arrow_length
        data['north_arrow'].shaftwidth = shaftwidth
        data['south_arrow'].pos = body.pos
        data['south_arrow'].axis = -data['axis'] * arrow_length
        data['south_arrow'].shaftwidth = shaftwidth

def rotate_on_axis(body, data):
    spin_angle = data['spin_direction'] * 2 * pi / data['period']
    body.rotate(angle=spin_angle, axis=data['axis'], origin=body.pos)

def rotate_planets_on_axes():
    for data in PLANET_AXES.values():
        rotate_on_axis(data['body'], data)
        if data['solar_body'] != None:
            rotate_on_axis(data['solar_body'], data)

SOLAR_TRAIL_BODIES = [Mercury_Sun, Venus_Sun, Earth_Sun, Mars_Sun, Jupiter_Sun, Saturn_Sun, Uranus_Sun, Neptune_Sun]
ALL_TRAIL_BODIES = SOLAR_TRAIL_BODIES + [Moon_Earth]
SCENE_BODIES = {
    'SolarSystem': [Sun, Mercury_Sun, Venus_Sun, Earth_Sun, Mars_Sun, Jupiter_Sun, Saturn_Sun, Uranus_Sun, Neptune_Sun],
    'Earth': [Earth, Moon_Earth],
    'Mercury': [Mercury],
    'Venus': [Venus],
    'Mars': [Mars],
    'Jupiter': [Jupiter],
    'Saturn': [Saturn],
    'Uranus': [Uranus],
    'Neptune': [Neptune],
    'Moon': [Moon],
}
ALL_BODIES = [Sun, Mercury_Sun, Venus_Sun, Earth_Sun, Mars_Sun, Jupiter_Sun, Saturn_Sun, Uranus_Sun, Neptune_Sun, Earth, Moon_Earth, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Moon]

def clear_all_trails():
    for body in ALL_TRAIL_BODIES:
        body.clear_trail()

def set_solar_trails(enabled):
    for body in SOLAR_TRAIL_BODIES:
        body.make_trail = enabled

def set_moon_trail(enabled):
    Moon_Earth.make_trail = enabled

def hide_all_bodies():
    for body in ALL_BODIES:
        body.visible = False

def show_scene_bodies(scene_name):
    hide_all_bodies()
    for body in SCENE_BODIES[scene_name]:
        body.visible = True

def configure_scene(scene_name):
    show_scene_bodies(scene_name)
    set_solar_trails(orbit and scene_name == 'SolarSystem')
    set_moon_trail(orbit and scene_name == 'Earth')
    clear_all_trails()
    apply_orbit_visibility()
    sync_ui()

ACTIVE_BUTTON_COLOR = color.green
PASSIVE_BUTTON_COLOR = color.white
CONTROL_BUTTON_COLOR = hat(vector(110, 110, 110))
INFO_BUTTON_COLOR = hat(vector(230, 230, 210))
TIME_BUTTON_COLOR = color.black

SCENE_NAMES = ['SolarSystem', 'Earth', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Moon']
SCENE_LABELS = {
    'English': {
        'SolarSystem': 'Solar System',
        'Earth': 'Earth',
        'Mercury': 'Mercury',
        'Venus': 'Venus',
        'Mars': 'Mars',
        'Jupiter': 'Jupiter',
        'Saturn': 'Saturn',
        'Uranus': 'Uranus',
        'Neptune': 'Neptune',
        'Moon': 'Moon',
    },
    'Turkish': {
        'SolarSystem': 'Güneş Sistemi',
        'Earth': 'Dünya',
        'Mercury': 'Merkür',
        'Venus': 'Venüs',
        'Mars': 'Mars',
        'Jupiter': 'Jüpiter',
        'Saturn': 'Satürn',
        'Uranus': 'Uranüs',
        'Neptune': 'Neptün',
        'Moon': 'Ay',
    },
}

TIME_TEXT = {
    'English': {
        'SolarSystem': ('Year', '1 Year = 0,000001 Earth Year'),
        'Earth': ('Day', '1 Day = 0,0001 Earth Day'),
        'Mercury': ('Day', '1 Day = 0,0001 Mercury Day'),
        'Venus': ('Day', '1 Day = 0,0001 Venus Day'),
        'Mars': ('Day', '1 Day = 0,0001 Mars Day'),
        'Jupiter': ('Day', '1 Day = 0,0001 Jupiter Day'),
        'Saturn': ('Day', '1 Day = 0,0001 Saturn Day'),
        'Uranus': ('Day', '1 Day = 0,0001 Uranus Day'),
        'Neptune': ('Day', '1 Day = 0,0001 Neptune Day'),
        'Moon': ('Day', '1 Day = 0,0001 Moon Day'),
    },
    'Turkish': {
        'SolarSystem': ('Yıl', '1 Yıl = 0,000001 Dünya Yılı'),
        'Earth': ('Gün', '1 Gün = 0,0001 Dünya Günü'),
        'Mercury': ('Gün', '1 Gün = 0,0001 Merkür Günü'),
        'Venus': ('Gün', '1 Gün = 0,0001 Venüs Günü'),
        'Mars': ('Gün', '1 Gün = 0,0001 Mars Günü'),
        'Jupiter': ('Gün', '1 Gün = 0,0001 Jüpiter Günü'),
        'Saturn': ('Gün', '1 Gün = 0,0001 Satürn Günü'),
        'Uranus': ('Gün', '1 Gün = 0,0001 Uranüs Günü'),
        'Neptune': ('Gün', '1 Gün = 0,0001 Neptün Günü'),
        'Moon': ('Gün', '1 Gün = 0,0001 Ay Günü'),
    },
}

def get_scene_counter(scene_name):
    if scene_name == 'SolarSystem':
        return earth_year
    if scene_name == 'Earth':
        return earth_day
    if scene_name == 'Mercury':
        return mercury_day
    if scene_name == 'Venus':
        return venus_day
    if scene_name == 'Mars':
        return mars_day
    if scene_name == 'Jupiter':
        return jupiter_day
    if scene_name == 'Saturn':
        return saturn_day
    if scene_name == 'Uranus':
        return uranus_day
    if scene_name == 'Neptune':
        return neptune_day
    if scene_name == 'Moon':
        return moon_day
    return 0

def update_scene_buttons():
    if 'SCENE_BUTTONS' not in globals():
        return
    for scene_name, scene_button in SCENE_BUTTONS.items():
        scene_button.background = ACTIVE_BUTTON_COLOR if scene_name == active_scene else PASSIVE_BUTTON_COLOR

def update_ui_text():
    if 'SCENE_BUTTONS' not in globals():
        return
    labels = SCENE_LABELS[language]
    for scene_name, scene_button in SCENE_BUTTONS.items():
        scene_button.text = labels[scene_name]

    if language == 'English':
        button_Orbit.text = 'Orbit:yes' if orbit else 'Orbit:no'
        button_Pause.text = 'Run' if paused else 'Pause'
        button_Click.text = 'Middle Click = Zoom     Right Click = Move'
    else:
        button_Orbit.text = 'Yörünge:var' if orbit else 'Yörünge:yok'
        button_Pause.text = 'Çalıştır' if paused else 'Durdur'
        button_Click.text = 'Orta Tık = Zoom     Sağ Tık = Hareket'

    label, description = TIME_TEXT[language][active_scene]
    button_Time.text = f'{label}: {get_scene_counter(active_scene)}   ({description})'

def apply_button_style():
    if 'button_Orbit' not in globals():
        return
    button_Orbit.background = CONTROL_BUTTON_COLOR
    button_Orbit.color = color.white
    button_Pause.background = CONTROL_BUTTON_COLOR
    button_Pause.color = color.white
    button_Click.background = INFO_BUTTON_COLOR
    button_Click.color = color.black
    button_Time.background = TIME_BUTTON_COLOR
    button_Time.color = color.white
    button_TurFlag.background = hat(vector(180, 40, 40))
    button_TurFlag.color = color.white
    button_EngFlag.background = hat(vector(45, 80, 170))
    button_EngFlag.color = color.white
    button_Sound.background = hat(vector(210, 135, 35))
    button_Sound.color = color.white

def sync_ui():
    update_scene_buttons()
    update_ui_text()
    apply_button_style()

def Loading_Scene():
    hide_all_bodies()
    set_solar_trails(False)
    set_moon_trail(False)
    if orbit:
        clear_all_trails()
    hide_all_axis_arrows()
    sync_ui()
    time.sleep(3)

def switch_scene(scene_name):
    global active_scene
    active_scene = scene_name
    Loading_Scene()
    configure_scene(scene_name)

def SolarSystem_Scene():
    switch_scene('SolarSystem')

def Earth_Scene():
    switch_scene('Earth')

def Mercury_Scene():
    switch_scene('Mercury')

def Venus_Scene():
    switch_scene('Venus')

def Mars_Scene():
    switch_scene('Mars')

def Jupiter_Scene():
    switch_scene('Jupiter')

def Saturn_Scene():
    switch_scene('Saturn')

def Uranus_Scene():
    switch_scene('Uranus')

def Neptune_Scene():
    switch_scene('Neptune')

def Moon_Scene():
    switch_scene('Moon')

def Switch_Orbit():
    global orbit
    orbit = not orbit
    configure_scene(active_scene)

def Pause_Run():
    global paused
    paused = not paused
    sync_ui()

def English_To_Turkish():
    global language
    language = "Turkish"
    sync_ui()

def Turkish_To_English():
    global language
    language = "English"
    sync_ui()

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

SCENE_BUTTONS = {
    'SolarSystem': button_SolarSystem,
    'Earth': button_Earth,
    'Mercury': button_Mercury,
    'Venus': button_Venus,
    'Mars': button_Mars,
    'Jupiter': button_Jupiter,
    'Saturn': button_Saturn,
    'Uranus': button_Uranus,
    'Neptune': button_Neptune,
    'Moon': button_Moon,
}

button_Orbit = button(text='Orbit:no', pos=scene.title_anchor, background=hat(vector(120,120,120)), color=color.white, bind=Switch_Orbit)

button_Pause = button(text='Pause', pos=scene.title_anchor, background=hat(vector(120,120,120)), bind=Pause_Run)

button_Click = button(text='Middle Click = Zoom     Right Click = Move', pos=scene.title_anchor, background=hat(vector(240,239,184)), bind=nothing)

button_Time = button(text=f'Year: {earth_year}' + '   ' + '(1 Year = 0,000001 Earth Year)', pos=scene.title_anchor, background=color.black, color=color.white, bind=nothing)

button_TurFlag = button(text='Türkçe', pos=scene.title_anchor, background=color.red, color=color.white, bind=English_To_Turkish)
button_EngFlag = button(text='English', pos=scene.title_anchor, background=color.blue, color=color.white, bind=Turkish_To_English)

button_Sound = button(text='<)', pos=scene.title_anchor, background=color.orange, color=color.white, bind=Sound_Level)

initialize_planet_axes()
update_axis_arrows()
sync_ui()

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
        Moon_Earth.pos = Earth.pos + vector(2.5 * cos(t_moon), 0, 2.5 * sin(t_moon)) # ayın dünya etrafında dönmesi

        # Gezegenler gerçek eksen eğikliklerine yakın eksenlerde, mevcut simülasyon hızlarıyla döner.
        rotate_planets_on_axes()
        rotate_on_axis(Moon_Earth, PLANET_AXES['Moon'])
        update_axis_arrows()

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
