import os

from Utilities.Utils import SysUtils

import hoomd
import hoomd.md

# NOTE: General Sys setup
currentPath = os.path.dirname(__file__)

# NOTE: Initialize the execution context to control where HOOMD will execute the simulation. When no command line options are provided, HOOMD will auto-select a GPU if it exists, or run on the CPU.
hoomd.context.initialize("")

# NOTE: Initialize a n by n by n simple cubic lattice of particles. The lattice initializer by default creates all particles named type "A", and with 0 velocity.
hoomd.init.create_lattice(unitcell=hoomd.lattice.sc(a=2.0), n=5)

# NOTE: Finding the neighbour particles 'efficiently'
neighbourList = hoomd.md.nlist.cell()

# NOTE: Specifying the Potential to calculate
lennard_jones_Potential = hoomd.md.pair.lj(r_cut=2.5, nlist=neighbourList)
lennard_jones_Potential.pair_coeff.set("A","A",epsilon = 1.0, sigma = 1.0)

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
hoomd.dump.gsd(trajectoryPath, period=2e3, group=allParticles, overwrite=True)

# NOTE: Running the simulation
hoomd.run(1e4)