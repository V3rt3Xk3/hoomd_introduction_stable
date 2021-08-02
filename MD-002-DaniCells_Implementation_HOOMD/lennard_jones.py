import os
import numpy

from Utilities.Utils import SysUtils, GSDUtils

import hoomd
import hoomd.md
from hoomd.lattice import unitcell

import gsd.hoomd

# NOTE: General Sys setup
currentPath = os.path.dirname(__file__)

# NOTE: Initialize the execution context to control where HOOMD will execute the simulation. When no command line options are provided, HOOMD will auto-select a GPU if it exists, or run on the CPU.
hoomd.context.initialize("")

# NOTE: We are initializing a single UnitCell with a single particle, where the lattice vectors are a 100 microns each and the cell is in the middle
BiologicalUnitcell = unitcell(N=1, a1=[10,0,0], a2=[0,10,0], a3=[0,0,10], position=[[5,5,5]], type_name=["G1"], diameter=[0.5], mass=[1], charge=[0], moment_inertia=[0],orientation=[[1,0,0,0]])
hoomdSystemObject = hoomd.init.create_lattice(unitcell=BiologicalUnitcell, n=1)

# NOTE: Finding the neighbour particles 'efficiently'
neighbourList = hoomd.md.nlist.cell()

# NOTE: Specifying the Potential to calculate
lennard_jones_Potential = hoomd.md.pair.lj(r_cut=3.5, nlist=neighbourList)
# NOTE: Sigma is "1.78", because it gives an optimal distance of 2
lennard_jones_Potential.pair_coeff.set("G1","G1",epsilon = 2.0, sigma = 1.78)

# NOTE: Integrator
hoomd.md.integrate.mode_standard(dt=0.005)

allParticles = hoomd.group.all()
hoomd.md.integrate.langevin(group=allParticles, kT=0.2, seed=42)

# NOTE: Logging
logPath = SysUtils.generateLogPath(currentPath=currentPath, fileName="log-output.log")
hoomd.analyze.log(filename=logPath,
                  quantities=['potential_energy', 'temperature'],
                  period=100,
                  overwrite=True)

# NOTE: Dumping the snapshots
# WOW: There seems to be no equivalent method in the 3.0.0 beta
trajectoryPath = SysUtils.generateSnaptshotPath(currentPath, "trajectory.gsd")
hoomd.dump.gsd(trajectoryPath, period=1e3, group=allParticles, overwrite=True)

# NOTE: Running the simulation
hoomd.run(5e4)

# NOTE: I have the next code block repeating twice. So i spawn 2 new particles total.
toContinueGSD = SysUtils.generateSnaptshotPath(currentPath, "toContinueGSD.gsd")
hoomd.dump.gsd(toContinueGSD, period=None, group=hoomd.group.all(), overwrite=True)

with gsd.hoomd.open(toContinueGSD) as trajectoryFile:
    gsdSnapshot = trajectoryFile[-1]

GSDUtils.spawnParticle(gsdSnapshot,x=5,y=5,z=5)

toContinueGSD = SysUtils.generateSnaptshotPath(currentPath, "toContinueGSD.gsd")
with gsd.hoomd.open(toContinueGSD, mode='wb') as file:
    file.append(gsdSnapshot)
    

hoomd.context.initialize("")
hoomd.init.read_gsd(trajectoryPath,restart=toContinueGSD)


# NOTE: Finding the neighbour particles 'efficiently'
neighbourList = hoomd.md.nlist.cell()
# NOTE: Specifying the Potential to calculate
lennard_jones_Potential = hoomd.md.pair.lj(r_cut=3.5, nlist=neighbourList)
# NOTE: Sigma is "1.78", because it gives an optimal distance of 2
lennard_jones_Potential.pair_coeff.set("G1","G1",epsilon = 2.0, sigma = 1.78)
# NOTE: Integrator
hoomd.md.integrate.mode_standard(dt=0.005)
allParticles = hoomd.group.all()
hoomd.md.integrate.langevin(group=allParticles, kT=0.2, seed=42)



trajectoryPath = SysUtils.generateSnaptshotPath(currentPath, "trajectory.gsd")
hoomd.dump.gsd(trajectoryPath, period=1e3, group=hoomd.group.all(), overwrite=True)

# NOTE: Running the simulation
hoomd.run(5e4)

# NOTE: New particle again
toContinueGSD = SysUtils.generateSnaptshotPath(currentPath, "toContinueGSD.gsd")
hoomd.dump.gsd(toContinueGSD, period=None, group=hoomd.group.all(), overwrite=True)

with gsd.hoomd.open(toContinueGSD) as trajectoryFile:
    gsdSnapshot = trajectoryFile[-1]

GSDUtils.spawnParticle(gsdSnapshot,x=5,y=5,z=5)

toContinueGSD = SysUtils.generateSnaptshotPath(currentPath, "toContinueGSD.gsd")
with gsd.hoomd.open(toContinueGSD, mode='wb') as file:
    file.append(gsdSnapshot)

hoomd.context.initialize("")
hoomd.init.read_gsd(trajectoryPath,restart=toContinueGSD)


# NOTE: Finding the neighbour particles 'efficiently'
neighbourList = hoomd.md.nlist.cell()
# NOTE: Specifying the Potential to calculate
lennard_jones_Potential = hoomd.md.pair.lj(r_cut=3.5, nlist=neighbourList)
# NOTE: Sigma is "1.78", because it gives an optimal distance of 2
lennard_jones_Potential.pair_coeff.set("G1","G1",epsilon = 2.0, sigma = 1.78)
# NOTE: Integrator
hoomd.md.integrate.mode_standard(dt=0.005)
allParticles = hoomd.group.all()
hoomd.md.integrate.langevin(group=allParticles, kT=0.2, seed=42)



trajectoryPath = SysUtils.generateSnaptshotPath(currentPath, "trajectory.gsd")
hoomd.dump.gsd(trajectoryPath, period=1e3, group=hoomd.group.all(), overwrite=True)

# NOTE: Running the simulation
hoomd.run(5e4)