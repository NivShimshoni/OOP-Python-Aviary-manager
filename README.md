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
* **Finches:** Includes **Zebra Finch** and **Gouldian Finch**. [span_11](start_span)[span_12](start_span)[span_13](start_span)Features unique `nest_building` logic based on the bird's age[span_11](end_span)[span_12](end_span)[span_13](end_span).
* **Parrots:** Includes **Budgerigar** and **Lovebird**. [span_14](start_span)[span_15](start_span)[span_16](start_span)Features a `find_nestbox` method that generates a 2D square matrix based on development[span_14](end_span)[span_15](end_span)[span_16](end_span).

### 🏠 Housing & Environment
* **[span_17](start_span)[span_18](start_span)Cage Management:** Enforces species-specific housing (one type per cage) and monitors volume capacity based on bird requirements[span_17](end_span)[span_18](end_span).
* **[span_19](start_span)Bird-Room Wall:** A large-scale 2D grid that manages the placement of cages on a physical wall, ensuring they fit within the room's dimensions and do not overlap[span_19](end_span).

## 💻 Tech Stack
* **Language:** Python
* **[span_20](start_span)[span_21](start_span)Modules:** `datetime` (for age tracking) and `random` (for behavioral traits)[span_20](end_span)[span_21](end_span).

---
*Note: This project was developed as an academic assignment at Ben-Gurion University.*
