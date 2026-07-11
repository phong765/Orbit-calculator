# Orbit-calculator

**Warning: This is only built for computer users.**

A website that calculates the orbit of a satellite around a selected body. To test my product, use this link: <https://phong765.github.io/Orbit-calculator/>
<img width="1882" height="867" alt="Screenshot 2026-07-10 111223" src="https://github.com/user-attachments/assets/8b023987-6576-47ec-82dd-b87b91d702ab" />
<img width="1902" height="867" alt="image" src="https://github.com/user-attachments/assets/a62e9ff7-2270-46d3-a005-eaa2113aab30" />
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/279b881f-4ace-43c9-af46-3f53e73d411f" />

My GitHub also includes the raw Python file for the calculation.

## Overview of the project

This project is aimed at solving a problem I often face in my high school: when teaching a physics problem, most of my physics teachers at my school or in my country in general) didn't give students an idea of what the concepts look like in real life. Therefore, this program will provide those who study orbits and circular motion with a tool to test and visualize their learning in school.  

Features include: 
* Choosing the object you want to orbit around
* Choosing your starting position and velocity vectors
* Gives parameters including eccentricity, orbital inclination, line of apsides angle, apogee, perigee, and orbit period.
* Graphs showing the orbit parameters
* Warnings when the orbit is too low or is invalid

## Working principle

The orbit and its parameters are calculated using the polar-coordinate orbit equation and its derivations, and the orbital plane is determined by taking the cross product of the position and velocity vectors. My work is based on this document: [orbits.pdf](https://github.com/user-attachments/files/29911772/orbits.pdf)


## Implementation

For the math, I write a Python script to handle the calculation and the plotting. And since this is a website, I turn it into a PyScript section in my HTML file, along with a CSS file and JS script. And since this website only does one task, I feel that there's no need to build a backend-frontend architecture. However, this means that the website will take a few seconds to load the script before the users are able to use it.

## Processing flow
<img width="1702" height="627" alt="image" src="https://github.com/user-attachments/assets/74a60956-671b-489b-b0a4-eaabfeb2e813" />
## Technical quirks
* Why do I have to add a 1ms delay for the scrolling function: to make sure that the results are fully rendered, otherwise it will scroll to an undesirable place.
* What are the references for my coordinate system: the origin will be the Earth's center, the Z-axis will run through the poles and the XY-plane will be the equatorial plane. The great thing about this is that the exact position of the X and Y axes isn't very important since the Earth is a sphere that rotates.
* How accurate it is: since my calculation ignores the effects from other bodies and aerodynamic drag, this is just a rough approximation aimed at showing the basics of orbital mechanics. It can't solve the two-body problem or determine the orbit of a satellite when it travels through the Solar System and beyond 
## Acknowledgements
* Libraries that I use: PyScript, Matplotlib, and NumPy.
* AI usage: I use Copilot for autocomplete and Gemini for code layout polishing and helping me with hard problems.


