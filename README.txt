Contains a couple of programmes that can simplify the simulation of WAG in Dual Porosity NFR models using CMG IMEX.
CMG IMEX is a trademark of Computer Modelling Group LTD (http://www.cmgl.ca/).

The code does not directly change CMG IMEX, it rather works on the input and output files.
This code base is divided in 4 main gropus:
1 Cube ... allows alternating water-gas injection for a cuboid DP model
2 DP ... dual porosity simulations performed on 1 grid cell
3 Big ... generates a DP model that has entered size in x- and y-direction (z direction is constant), model can then be simulated as in 1
4 Random ... uses a model as generated in 3 and randomly fills entered percentage of fractures, model can then be simulated as in 1

All files only work if the are in the same folder as the .py-file. They work by double-clicking and the explinations provided here should be sufficient for their usage. 

Due to the similarity of the tasks many workflows function in a similar order. 
Workflow 1 provides the possibility to load the result of the previous simulation into a new simulation (e.g. to change injection fluids from water to gas).
Workflow 2 takes a simulation output file and calculates oil saturation in the fractures for each time step. Imo this is a much quicker and more efficient solution that the shipped reader.

Certain file names are used over and over again. Their explination can be found below. 
1a cutter ... cuts the last time step
1b get saturations ... takes values for the last time step from 1a and extracts saturation values
1c combiner ... combines 1b and 'all the rest', which is the rest of the code that CMG needs for the start of a simulation
2 get recovery ... takes a .out-file and extracts recovery factor for each timestep, already in .csv (to enable opening via MS Excel)
For sake of comparison of running times, get recovery is also written in Java.  
various writer-files act as helper functions for generations 
all the rest ... contains data that are the same for all simulations of this group; e.g. CMG-I/O data, grid data, relative permeability data,...