# Orbit-calculator

**Warning: This is only built for computer users.**

A website that calculates the orbit of a satellite around a selected body. To test my product, use this link: <https://phong765.github.io/Orbit-calculator/>
<img width="1882" height="867" alt="Screenshot 2026-07-10 111223" src="https://github.com/user-attachments/assets/8b023987-6576-47ec-82dd-b87b91d702ab" />
<img width="1902" height="867" alt="image" src="https://github.com/user-attachments/assets/a62e9ff7-2270-46d3-a005-eaa2113aab30" />
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/279b881f-4ace-43c9-af46-3f53e73d411f" />



## Overview of the project

This project is aimed at solving a problem I often face in my high school: when teaching a physics problem, most of my physics teachers at my school or in my country in general) didn't give students an idea of what the concepts look like in real life. Therefore, this program will give those who study orbits and circular motion a tool to test what they learn at school.  

Features include: 
* Choosing the object you want to orbit around
* Choosing your starting position and velocity vectors
* Gives parameters including eccentricity, orbital inclination, line of apsides angle, apogee, perigee, and orbit period.
* Graphs showing the orbit parameters
* Warnings when the orbit is too low or is invalid

## Working principle

The orbit and its parameters are calculated using the polar-coordinate orbit equation, and the orbital plane is determined by taking the cross product of the position and velocity vectors.

## Implementation

For the math, I write a Python script to handle the calculation and the plotting. And since this is a website, I turn it into a PyScript section in my HTML file, along with a CSS and JS file. And since this website only does one task, I feel that there's no need to build a backend-frontend architecture.
