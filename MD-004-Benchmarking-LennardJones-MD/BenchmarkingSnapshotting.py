import os
import pandas

from Utilities.SimulationInterface import SimulationInterface
from Utilities.Benchmarking import Benchmarking
from Utilities.Utils import PandasUtility

simulationObject = SimulationInterface(numberOfParticles = 10000, LJsigma = 0.001, LJepsilon = 0.001)
simulationObject.RunSetup()
simulationObject.RunSimulation(runLength=600)

benchmarkDictionary = {}

avgTime = Benchmarking.BenchmarkSnapshot(simulationObject.TakeSnapshotNRestore, 10)
print("On average it took: {} seconds!".format(avgTime))
benchmarkDictionary["SnapshotNRestore"] = [avgTime]

# # WOW: Interestingly it seems lik i cannot add particles one ofter another.
# avgTime = Benchmarking.BenchmarkSnapshot(simulationObject.TakeSnapshotAlterNRestore, 10)
# print("On average it took: {} seconds!".format(avgTime))

# WOW: Instead I am computing things between snapshotting
def benchmarkRunSnapshotNAlterNRun():
	simulationObject.TakeSnapshotAlterNRestore()
	simulationObject.RunSimulation(1)

avgTime = Benchmarking.BenchmarkSnapshot(benchmarkRunSnapshotNAlterNRun, 10)
print("On average it took: {} seconds!".format(avgTime))
benchmarkDictionary["AlterNRestore"] = [avgTime]

avgTime = Benchmarking.BenchmarkSimulation(simulationObject.RunSimulation, 600, 10)
print("On average it took: {} seconds!".format(avgTime))
benchmarkDictionary["Run10Mins"] = [avgTime]

BenchmarkRun = pandas.DataFrame.from_dict(benchmarkDictionary, orient="columns")
print(BenchmarkRun)

current_path = os.path.dirname(__file__)
PandasUtility.to_csv(currentPath=current_path, fileName="BenchmarkRun.txt", dataFrame=BenchmarkRun)