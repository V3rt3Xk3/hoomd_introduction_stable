import math
from random import random
from Utilities.Utils import SysUtils

import os

import hoomd
import hoomd.md
from hoomd.lattice import sc

class SimulationInterface(object):

	def __init__(self, numberOfParticles = 10000, LJsigma = 1.78, LJepsilon = 2):
		"""
		Initializes the variables of our simple Simulation Object

		Args:
			numberOfParticles (int, optional): Number of particles to use in the simulation with a standard "Simple Cubic" lattice. Defaults to 10000.
		"""
		self.currentPath = os.path.dirname(__file__)
		self.numberOfParticles = numberOfParticles
		self.unitcellRepetitionsPerAxis = math.ceil(self.numberOfParticles**(1/3))
		self.hoomdSystemObject = None
		self.LJsigma = LJsigma
		self.LJepsilon = LJepsilon

	def RunSetup(self,snapshotInterval=1800):
		hoomd.context.initialize("")

		self.hoomdSystemObject = hoomd.init.create_lattice(unitcell=sc(a=2.0), n=self.unitcellRepetitionsPerAxis)

		neighbourList = hoomd.md.nlist.cell()
		lennard_jones_Potential = hoomd.md.pair.lj(r_cut=3.5, nlist=neighbourList)
		# NOTE: This sigma value renders the LJ function useless, but because of the "r_cut" it still should be computed.
		lennard_jones_Potential.pair_coeff.set("A","A",epsilon = self.LJepsilon, sigma = self.LJsigma)

		hoomd.md.integrate.mode_standard(dt=0.005)

		allParticles = hoomd.group.all()
		hoomd.md.integrate.langevin(group=allParticles, kT=0.2, seed=42)

		logPath = SysUtils.generateSavePathFromUtilities(currentPath=self.currentPath, fileName="log-output.log")
		hoomd.analyze.log(filename=logPath,
				  quantities=['potential_energy', 'temperature'],
				  period=100,
				  overwrite=True)
		
		trajectoryPath = SysUtils.generateSavePathFromUtilities(self.currentPath, "trajectory.gsd")
		hoomd.dump.gsd(trajectoryPath, period=snapshotInterval, group=allParticles, overwrite=True)

		return self.hoomdSystemObject

	def RunSimulation(self, runLength = 3600):
		hoomd.run(runLength)
		return

	def TakeSnapshotNRestore(self):
		snapshot = self.hoomdSystemObject.take_snapshot()
		self.hoomdSystemObject.restore_snapshot(snapshot)

	def TakeSnapshotAlterNRestore(self):
		snapshot = self.hoomdSystemObject.take_snapshot()

		numberOfParticles = snapshot.particles.N
		snapshot.particles.resize(numberOfParticles+1)
		# NOTE: The position is consequence of the
		positionVector3D = []
		for i in range(3):
			positionVector3D.append((random()*self.unitcellRepetitionsPerAxis*2-self.unitcellRepetitionsPerAxis))
		snapshot.particles.position[numberOfParticles] = [positionVector3D[i] for i in range(len(positionVector3D))]

		self.hoomdSystemObject.restore_snapshot(snapshot)