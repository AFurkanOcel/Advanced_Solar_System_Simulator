<h1 align="center">Advanced Solar System Simulator</h1>

<p align="center">
Interactive 3D solar system simulator built with Python, VPython and Pygame.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue"/>
  <img src="https://img.shields.io/badge/3D-VPython-orange"/>
  <img src="https://img.shields.io/badge/Audio-Pygame-green"/>
  <img src="https://img.shields.io/badge/Simulation-Orbits%20%26%20Rotation-purple"/>
  <img src="https://img.shields.io/badge/Interface-English%20%7C%20Turkish-red"/>
  <img src="https://img.shields.io/badge/License-MIT-brightgreen"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen"/>
</p>

---

## Project Overview

**Advanced Solar System Simulator** is an interactive astronomical visualization project that simulates the Sun, planets and the Moon in a 3D VPython environment.

The simulator focuses on visual learning by combining:

* Planetary orbit animation
* Planet self-rotation
* Axial tilt visualization with north/south arrows
* Scaled visual planet sizes
* Textured planet surfaces
* Bilingual interface support
* Background music and sound controls

The project is designed as a desktop/web-rendered VPython simulation where users can switch between the full Solar System view and individual planet views.

<img width="1800" alt="Solar System View" src="assets/screenshots/solar-system-view.png" />

---

## Project Structure

```text
Advanced_Solar_System_Simulator/
|-- SolarSystem.py
|-- README.md
|-- LICENSE
|-- .gitignore
|
|-- assets/
|   |-- textures/
|   |   |-- Sun.jpg
|   |   |-- Mercury.jpg
|   |   |-- Venus.jpg
|   |   |-- Earth.jpg
|   |   |-- Moon.jpg
|   |   |-- Mars.jpg
|   |   |-- Jupiter.jpg
|   |   |-- Saturn.jpg
|   |   |-- Uranus.jpg
|   |   |-- Neptune.jpg
|   |   |-- Space.jpg
|   |   |-- Universe.jpg
|   |   `-- other.png
|   |
|   |-- screenshots/
|   |   |-- solar-system-view.png
|   |   |-- earth-and-moon-view.png
|   |   |-- mercury-view.png
|   |   |-- venus-view.png
|   |   |-- mars-view.png
|   |   |-- jupiter-view.png
|   |   |-- saturn-view.png
|   |   |-- uranus-view.png
|   |   |-- neptune-view.png
|   |   `-- moon-view.png
|   |
|   `-- music/
|       `-- Universe_Music.mp3
```

### Main Files

| File / Folder | Description |
| --- | --- |
| `SolarSystem.py` | Main simulator source code |
| `assets/textures/` | Planet, Moon, Sun and space textures |
| `assets/screenshots/` | README screenshot images |
| `assets/music/` | Background music asset |

---

## Features

### 3D Solar System Simulation

* Sun and 8 planets rendered with texture images
* Planetary orbit animation around the Sun
* Scaled planet sizes for visual comparison
* Full Solar System scene and individual object scenes

### Planet Rotation and Axial Tilt

* Planets rotate around their own axes
* Axial tilt values are represented visually
* Red and blue arrows show north/south axis direction
* Retrograde rotation support for planets such as Venus and Uranus
* Moon axis visualization in Earth/Moon scenes

### Orbit Controls

* `Orbit:yes` displays orbital trails
* `Orbit:no` hides trails and axis arrows
* Solar System view shows planet orbit trails and compact axis arrows
* Earth view shows Moon orbit trail and Earth/Moon axis arrows

### Scene Navigation

Users can switch between:

* Solar System
* Earth
* Mercury
* Venus
* Mars
* Jupiter
* Saturn
* Uranus
* Neptune
* Moon

The active scene button is highlighted for easier navigation.

### Time Indicators

The simulator displays scene-specific time counters:

* Solar System view: year counter
* Planet views: day counter
* Moon view: Moon day counter

Time is scaled so the simulation remains observable and interactive.

### Bilingual Interface

The interface supports:

* English
* Turkish

Users can switch language directly from the simulator controls.

### Audio Support

* Background music playback using Pygame
* Sound button cycles between normal volume, increased volume and mute

---

## Simulation Model

The simulator uses simplified mathematical models to make planetary motion visually understandable while preserving realistic relationships such as orbit order, rotation speed differences and axial tilt direction.

### Orbital Motion

Planet positions are calculated with a parametric circular orbit model:

```text
x = center_x + orbit_radius * cos(theta)
z = center_z + orbit_radius * sin(theta)
y = 0
```

In VPython vector form:

```python
planet.pos = Sun.pos + vector(
    orbit_radius * cos(theta),
    0,
    orbit_radius * sin(theta)
)
```

The orbit angle is updated every frame:

```text
theta = theta - 2*pi / orbit_period
```

This creates continuous orbital movement around the Sun. The same idea is used for the Moon orbiting Earth.

### Rotation Around Own Axis

Each planet rotates around its own axis using:

```text
rotation_angle = spin_direction * 2*pi / rotation_period
```

Where:

| Term | Meaning |
| --- | --- |
| `spin_direction` | `1` for normal rotation, `-1` for retrograde rotation |
| `rotation_period` | Scaled number of frames required for one full rotation |
| `2*pi` | One complete rotation in radians |

This allows planets such as **Venus** and **Uranus** to rotate in a retrograde direction.

### Axial Tilt Calculation

Axial tilt is represented as a normalized direction vector. The simulator converts a tilt angle into a 3D axis vector:

```text
tilt_rad = radians(-tilt)
axis = normalize(vector(sin(tilt_rad), cos(tilt_rad), 0))
```

Equivalent code:

```python
def axis_from_tilt(tilt):
    tilt_rad = radians(-tilt)
    return norm(vector(sin(tilt_rad), cos(tilt_rad), 0))
```

This axis is used for:

* rotating the planet
* setting the visual up direction
* drawing red/blue north-south axis arrows

### Axis Arrow Visualization

The north and south arrows use the same axial tilt vector:

```text
north_arrow.axis = axis * arrow_length
south_arrow.axis = -axis * arrow_length
```

In the Solar System scene, arrow length is dynamically scaled so that large planets such as Jupiter and Saturn still keep visible axis indicators:

```text
arrow_length = max(planet_radius + 0.035, 0.10)
```

### Time Scaling

Real astronomical periods are scaled down to keep the simulation observable. For example:

| Object / Motion | Scaled Period Used |
| --- | --- |
| Earth orbit around Sun | `3155` frames |
| Moon orbit around Earth | `23605` frames |
| Earth self-rotation | `864` frames |
| Jupiter self-rotation | `357` frames |
| Neptune self-rotation | `580` frames |

The goal is not to reproduce real-time astronomy second by second, but to preserve relative motion patterns in an interactive 3D environment.

---

## Technologies Used

| Category | Technology |
| --- | --- |
| Language | Python |
| 3D Rendering | VPython |
| Math / Simulation | Python `math` module |
| Audio | Pygame Mixer |
| Assets | JPG textures, MP3 audio |
| Interface | VPython buttons |
| License | MIT |

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/AFurkanOcel/Advanced_Solar_System_Simulator.git
```

### 2. Open Project Folder

```bash
cd Advanced_Solar_System_Simulator
```

### 3. Install Dependencies

```bash
pip install vpython pygame
```

### 4. Run the Simulator

```bash
python SolarSystem.py
```

VPython opens the simulation in a browser-based 3D canvas or local VPython environment depending on your setup.

---

## Controls

| Control | Description |
| --- | --- |
| `Solar System` / planet buttons | Switch active scene |
| `Orbit:yes / Orbit:no` | Toggle orbit trails and axis arrows |
| `Pause / Run` | Pause or resume the simulation |
| `Middle Click` | Zoom |
| `Right Click` | Move camera |
| `Turkish / English` | Change interface language |
| Sound button | Cycle volume modes |

---

## Screenshots

### Solar System View

The main view shows the Sun and planets orbiting with textured surfaces.

<img width="1800" alt="Solar System View" src="assets/screenshots/solar-system-view.png" />

### Earth and Moon View

Earth scene with the Moon orbiting around it.

<img width="1800" alt="Earth and Moon View" src="assets/screenshots/earth-and-moon-view.png" />

### Planet Views

<p>
  <img width="400" alt="Mercury" src="assets/screenshots/mercury-view.png" />
  <img width="400" alt="Venus" src="assets/screenshots/venus-view.png" />
</p>

<p>
  <img width="400" alt="Mars" src="assets/screenshots/mars-view.png" />
  <img width="400" alt="Jupiter" src="assets/screenshots/jupiter-view.png" />
</p>

<p>
  <img width="400" alt="Saturn" src="assets/screenshots/saturn-view.png" />
  <img width="400" alt="Uranus" src="assets/screenshots/uranus-view.png" />
</p>

<p>
  <img width="400" alt="Neptune" src="assets/screenshots/neptune-view.png" />
  <img width="400" alt="Moon" src="assets/screenshots/moon-view.png" />
</p>

---

## Implementation Notes

* Planet data is centralized for axial tilt, rotation period and scene behavior.
* Scene transitions are managed through helper functions to reduce repeated code.
* Orbit trails are reset when scenes or orbit mode changes.
* Axis arrows are dynamically updated based on the active scene.
* Solar System axis arrows are compact so they remain visible without overwhelming the scene.

---

## Future Improvements

* Add Saturn ring visualization
* Add optional labels for planets
* Add adjustable simulation speed
* Add camera presets for each planet
* Add more detailed astronomical information panels
* Improve proportional distance scaling options

---

## Learning Outcomes

This project helped improve experience in:

* Python-based simulation development
* VPython 3D scene management
* Orbital motion and rotation logic
* Visualizing axial tilt and direction vectors
* Managing UI state in an interactive simulation
* Organizing media assets in a desktop/web-rendered application

---

## Author

**A. Furkan ÖCEL**

---

## License

This project is licensed under the terms included in the repository's `LICENSE` file.
