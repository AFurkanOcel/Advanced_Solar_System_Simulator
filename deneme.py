from vpython import *

scene.width  = 1400
scene.height = 800
scene.background = color.black

# 1) Dünya – kuzey kutbu +y yönünde, ama eksen eğik
tilt = -23.44 # +23.44 yapınca dünya sola değil sağa yatık oluyor
tilt_rad = radians(tilt)

# Eğik ekseni tanımla (z ekseni etrafında eğilmiş bir +y vektörü)
axis_tilted = vector(sin(tilt_rad), cos(tilt_rad), 0)

earth = sphere(
    pos=vector(0, 0, 0),
    radius=1,
    texture="Images/Earth.jpg",
    up=axis_tilted
)

# 2) Kuzey kutbu yönünde ok
axis_arrow_north = arrow(
    pos=earth.pos,
    axis=norm(axis_tilted)*1.5, # 1.5 ile çarparak okun uzunlugunu artırıyoruz
    color=color.red,
    shaftwidth=0.05
)

# 3) Güney kutbu yönünde ok (ters yön)
axis_arrow_south = arrow(
    pos=earth.pos,
    axis=norm(-axis_tilted)*1.5, # 1.5 ile çarparak okun uzunlugunu artırıyoruz
    color=color.blue,
    shaftwidth=0.05
)

# 4) Sürekli kendi eğik ekseninde dönüş
spin_deg_per_frame = 1 # -1 yapınca dünya ters yönde dönüyor
spin_rad = radians(spin_deg_per_frame)

while True:
    rate(60)
    earth.rotate(
        angle=spin_rad,
        axis=axis_tilted,
        origin=earth.pos
    )
    axis_arrow_north.rotate(
        angle=spin_rad,
        axis=axis_tilted,
        origin=earth.pos
    )
    axis_arrow_south.rotate(
        angle=spin_rad,
        axis=axis_tilted,
        origin=earth.pos
    )
