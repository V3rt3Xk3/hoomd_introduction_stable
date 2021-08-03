from time import time
from typing import Callable

class Benchmarking:

	@staticmethod
	def BenchmarkSimulation(function2Time: Callable, simLength: int, repetitions: int):		
		start = time()
		for i in range(0, repetitions):
			function2Time(simLength)
		end = time()
		return (end - start) / repetitions

	@staticmethod
	def BenchmarkSnapshot(function2Time: Callable, repetitions: int):		
		start = time()
		for i in range(0, repetitions):
			print("{}. Run".format(i))
			function2Time()
		end = time()
		return (end - start) / repetitions