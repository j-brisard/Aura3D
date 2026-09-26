# Aura3D: Natural & Touchless 3D Viewer

> **Touchless 3D manipulation meets head-coupled motion parallax ("Fish-Tank VR") using a single RGB webcam.**

---

## 📌 Problem Statement & Motivation
Inspecting models in conventional CAD, 3D modeling, and DCC software (Blender, SolidWorks, Maya) suffers from high cognitive friction:
* Inconsistent, non-standardized keyboard/mouse mappings across applications (`Shift + Middle Click`, `Alt + Right Click`, orbit rings).
* Cumbersome multi-button coordination required for simple rotate/pan/zoom inspection.
* Flat, static projection screens that lack natural depth cues and motion parallax.

**Aura3D** bridges this gap by introducing an accessible, ergonomic, and touchless interaction model. By pairing hand-tracking gestures with dynamic head-tracking perspective correction, inspecting a 3D asset becomes as natural as examining a physical object through a window.

---

## 🎯 Core Features

### 1. Dynamic Head-Coupled Perspective ("Fish-Tank VR")
* **Real-time Face & Eye Tracking:** Tracks observer position $(X, Y, Z)$ relative to the display plane via standard webcam input.
* **Off-Axis Projection Matrix:** Dynamically recalculates an asymmetric frustum (`glFrustum` / custom perspective matrix) to render realistic motion parallax without dedicated VR headsets.

### 2. Natural Hand-Gesture Manipulation
* **Pinch-to-Zoom:** Measure Euclidean finger distance to fluidly scale and inspect fine mesh geometry.
* **Spatial Orbit & Rotation:** Translate palm and wrist pitch/yaw into intuitive model rotations.
* **Planar Translation (Pan):** Smooth viewport translation mapped directly to hand motion across the camera plane.
* **Gesture State Machine:** Temporal filtering to prevent jitter, accidental triggers, and false positives.

---

## 💻 Tech Stack

* **Language:** Python
* **Computer Vision & Tracking:** TBD
* **3D Graphics Engine:** ModernGL, GLFW
* **Linear Algebra & Transforms:** NumPy

---

## 👥 Course & Academic Scope
Developed for **CS3483 Multimodal Interface Design** at the **City University of Hong Kong (CityUHK)**.
