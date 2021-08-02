# hoomd-blue Questions

## Questions on the go
* I couldn't find a way to spawn a new particle into the lattice
  * This also means, that if we have to re-initialize the system, that would be scientifically incorrect as the thermodynamics are set randomly
* In the python code, the CellCycle Checkpoints are checked at every timestep / In Hoomd I cannot do that
* We might be able to tweak the masses of the particles / particle types to avoid explosion / implosion of the system
* We definitely have a trade-off in self developed code from analogue systems to semi digital systems.
  * In the python2 code, the cells can have any size, compound secretion levels or so
  * In the hoomd system, it seems like we have to specify ditinct Types

## Approaches i tried to spawn a particle
* Reinitialized the system with new UNITCELL
  * Error: System cannot be reinitialized
* Edit hoomd system data
  * Value error, attributes cannot be set
* Edit the GSD Snapshot file
  * Snapshot doesn't have "broadcast box" property
  * Finally figured out, that saving the file and using the GSD to "restart" could solve it, but no. Again: "Cannot reinitialize more than once"