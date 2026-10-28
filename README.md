# Aura3D: Natural & Touchless 3D Viewer

> **Touchless 3D manipulation meets head-coupled motion parallax ("Fish-Tank VR") using a single RGB webcam.**

---

## Project Status

Early development (started October 2026, until December 2026).

| Component | Status |
|---|---|
| Basic 3D viewer (ModernGL window, vertex and fragment shaders, model/view/projection matrices) | Done |
| Off-axis projection driven by head position | Planned |
| Face and head tracking from the webcam | Planned |
| Hand-gesture manipulation (zoom, rotate, pan) | Planned |
| Gesture state machine and filtering | Planned |

The features below describe the target design.

---

## Problem Statement & Motivation
Inspecting models in conventional CAD, 3D modeling, and DCC software (Blender, SolidWorks, Maya) suffers from high cognitive friction:
* Inconsistent, non-standardized keyboard/mouse mappings across applications (`Shift + Middle Click`, `Alt + Right Click`, orbit rings).
* Cumbersome multi-button coordination required for simple rotate/pan/zoom inspection.
* Flat, static projection screens that lack natural depth cues and motion parallax.

**Aura3D** bridges this gap by introducing an accessible, ergonomic, and touchless interaction model. By pairing hand-tracking gestures with dynamic head-tracking perspective correction, inspecting a 3D asset becomes as natural as examining a physical object through a window.

---

## Core Features (planned)

### 1. Dynamic Head-Coupled Perspective ("Fish-Tank VR")
* **Real-time Face & Eye Tracking:** Tracks observer position $(X, Y, Z)$ relative to the display plane via standard webcam input.
* **Off-Axis Projection Matrix:** Dynamically recalculates an asymmetric frustum (`glFrustum` / custom perspective matrix) to render realistic motion parallax without dedicated VR headsets.

### 2. Natural Hand-Gesture Manipulation
* **Pinch-to-Zoom:** Measure Euclidean finger distance to fluidly scale and inspect fine mesh geometry.
* **Spatial Orbit & Rotation:** Translate palm and wrist pitch/yaw into intuitive model rotations.
* **Planar Translation (Pan):** Smooth viewport translation mapped directly to hand motion across the camera plane.
* **Gesture State Machine:** Temporal filtering to prevent jitter, accidental triggers, and false positives.

---

## Tech Stack

* **Language:** Python
* **Computer Vision & Tracking:** not chosen yet
* **3D Graphics:** ModernGL, moderngl-window
* **Linear Algebra & Transforms:** NumPy, PyGLM

---

## Getting Started

```bash
pip install -r requirements.txt
python main.py
```

The current version opens a window with a rotating colored cube.

---

## Course & Academic Scope
Developed for **CS3483 Multimodal Interface Design** at the **City University of Hong Kong (CityUHK)**.
