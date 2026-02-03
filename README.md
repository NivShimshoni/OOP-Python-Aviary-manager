# 🦜 Aviary Habitat Management System

## 🚀 Project Overview
This project is a sophisticated management system for an avian habitat, developed as part of my **Electrical Engineering** studies at **Ben-Gurion University of the Negev**. It simulates a complex environment consisting of a Bird-Room, various cage types, and multiple bird species with unique biological and behavioral traits.

The core of the project focuses on **Object-Oriented Programming (OOP)**, ensuring robust data handling, spatial awareness, and automated biological calculations.

## 🛠 Engineering & Programming Concepts
* **Advanced Class Hierarchy:** Implemented a multi-level inheritance structure (Bird → Finch/Parrot → Specific Species) to manage shared attributes and specialized behaviors.
* **Operator Overloading:** Customized Python comparison operators (`==`, `>`, `<`) to enable logical sorting of birds based on species and color complexity.
* **Spatial Logic & Grid Mapping:** Developed a 2D grid representation of a habitat wall with zero-overlap constraints and resolution-based positioning (10cm units).
* **Input Integrity & Validation:** Robust error handling using `ValueError` and `TypeError` for IDs, birth dates, and volume requirements.
* **Automated Calculations:** Dynamic age calculation (Years/Months/Days) and random trait generation for singing/tweeting strengths.

## 🏗 System Architecture

### 🦜 The Birds
The system manages two main families:
* **Finches:** Includes **Zebra Finch** and **Gouldian Finch**. Features unique `nest_building` logic based on the bird's age.
* **Parrots:** Includes **Budgerigar** and **Lovebird**. Features a `find_nestbox` method that generates a 2D square matrix based on development.

### 🏠 Housing & Environment
* **Cage Management:** Enforces species-specific housing (one type per cage) and monitors volume capacity based on bird requirements.
* **Bird-Room Wall:** A large-scale 2D grid that manages the placement of cages on a physical wall, ensuring they fit within the room's dimensions and do not overlap.

## 💻 Tech Stack
* **Language:** Python
* **Modules:** `datetime` (for age tracking) and `random` (for behavioral traits).

---
*Note: This project was developed as an academic assignment at Ben-Gurion University.*

## 🎓 Academic Integrity
This repository is published with the explicit permission of the course instructor, **Haya Idan**, from the Department of Electrical & Computer Engineering at Ben-Gurion University of the Negev. 

The project is shared for portfolio purposes to demonstrate my software engineering development and the application of OOP principles.