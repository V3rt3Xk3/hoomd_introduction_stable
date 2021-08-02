import os
import hoomd
import hoomd.md
from hoomd.lattice import unitcell
import gsd.hoomd
from Utilities.Utils import SysUtils, GSDUtils

# NOTE: General Sys setup
currentPath = os.path.dirname(__file__)

trajectoryPath = SysUtils.generateSnaptshotPath(currentPath, "trajectory.gsd")
toContinueGSD = SysUtils.generateSnaptshotPath(currentPath, "toContinueGSD.gsd")



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
hoomd.run(1e4)