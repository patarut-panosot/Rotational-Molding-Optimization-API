# Rotational Molding Production Scheduling Optimization API
A Python API for creating programs to optimize rotational molding production line scheduling using Gurobi solver.
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to use](#how-to-use)
## General info
This is an implementation of the linear programs developed during a research class at IUSB mathematical department in spring 2020.
The team members are Dane Campbell, Loise Frey, Sherley Frye, Phillip Marmorino, Patarut Panosot, and Jordan Winkler, with Dr. Peter Connor as the advisor.
The API can be used to build a program that outputs an optimized production schedule for a rotational molding production line.
## Technologies
The project is created with:
* Python version: 3.7
* Gurobi version: 9.0.1
* Numpy version: 1.16.4
* Pandas version: 0.24.2
* openpyxl version: 2.6.2

Note that all softwares except for Gurobi are opensource.
Gurobi requires paid commercial license or free academic license.
## How to use
The file opt_models.py contains two class definitions; MaxProfit and ProductionSchedule.
To use them, first create an instance with the number of molding arms, mounts per arm, and production run time (in hours).
The class methods then are used to read input data (demand, inventory, profit, mold, etc.) as Pandas DataFrames, build a linear program, run an optimizer on the linear program, then output the production allocation (MaxProfit) or production schedule (ProductionSchedule).
Example usage is available in the file example_opt_models.py.
