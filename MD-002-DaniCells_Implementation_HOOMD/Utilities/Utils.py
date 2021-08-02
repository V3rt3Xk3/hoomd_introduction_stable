import os
import gsd.hoomd

import numpy

class GSDUtils:

    @staticmethod
    def spawnParticle(snapshot, newType="G1", x=5, y=5,z=5):
        # WOW: This is superwierd, I couldn't find a good way to copy a hoomd.Snapshot to gsd.hoomd.Snapshot. The only difference seems like, there is a validate method for the properties and the  class itself.
        # NOTE: All the particle properties need to be filled, or hoomd throws an error.
        snapshot.particles.N += 1

        snapshot.particles.types.append(newType)

        snapshot.particles.typeid = numpy.resize(snapshot.particles.typeid,(len(snapshot.particles.typeid)+1,))
        snapshot.particles.typeid[-1] = 0

        snapshot.particles.mass = numpy.resize(snapshot.particles.mass,(len(snapshot.particles.mass)+1,))
        snapshot.particles.mass[-1] = 1

        snapshot.particles.body = numpy.resize(snapshot.particles.body,(len(snapshot.particles.body)+1,))
        snapshot.particles.body[-1] = -1

        snapshot.particles.charge = numpy.resize(snapshot.particles.charge,(len(snapshot.particles.charge)+1,))
        snapshot.particles.charge[-1] = 0

        # NOTE: The new particles' position has to be corrected with the simulation box
        snapshot.particles.position = numpy.resize(snapshot.particles.position,(len(snapshot.particles.position)+1,3))
        snapshot.particles.position[-1] = snapshot.particles.position[0]
        print(snapshot.particles.position[0])
        snapshot.particles.position[0][0] -= 0.75
        if snapshot.particles.position[0][0] < -x:
            snapshot.particles.position[0][0] = 5 - (- snapshot.particles.position[0][0])
        print(snapshot.particles.position[0])
        print(snapshot.particles.position[-1])
        snapshot.particles.position[-1][0] = snapshot.particles.position[0][0] + 1.5
        if snapshot.particles.position[-1][0] > x:
            snapshot.particles.position[-1][0] = 0 + (snapshot.particles.position[-1][0] - 5)
        print(snapshot.particles.position[-1])

        snapshot.particles.diameter = numpy.resize(snapshot.particles.diameter,(len(snapshot.particles.diameter)+1,))
        snapshot.particles.diameter[-1] = 0.5

        snapshot.particles.orientation = numpy.resize(snapshot.particles.orientation,(len(snapshot.particles.orientation)+1,4))
        snapshot.particles.orientation[0] = snapshot.particles.orientation[-1]

        snapshot.particles.velocity = numpy.resize(snapshot.particles.velocity,(len(snapshot.particles.velocity)+1,3))
        snapshot.particles.velocity[0] = snapshot.particles.velocity[-1]

        snapshot.particles.moment_inertia = numpy.resize(snapshot.particles.moment_inertia,(len(snapshot.particles.moment_inertia)+1,3))
        snapshot.particles.moment_inertia[-1] = snapshot.particles.moment_inertia[0]

        snapshot.particles.angmom = numpy.resize(snapshot.particles.angmom,(len(snapshot.particles.angmom)+1,4))
        snapshot.particles.angmom[0] = snapshot.particles.angmom[-1]

        snapshot.particles.image = numpy.resize(snapshot.particles.image,(len(snapshot.particles.image)+1,3))
        snapshot.particles.image[-1] = snapshot.particles.image[0]


    @staticmethod
    def createSnapshot(gsdSnapshot, hoomdSnapshot):
        # WOW: This is superwierd, I couldn't find a good way to copy a hoomd.Snapshot to gsd.hoomd.Snapshot. The only difference seems like, there is a validate method for the properties and the  class itself.
        gsdSnapshot.particles.N = hoomdSnapshot.particles.N
        gsdSnapshot.particles.types = hoomdSnapshot.particles.types
        gsdSnapshot.particles.typeid = hoomdSnapshot.particles.typeid
        gsdSnapshot.particles.mass = hoomdSnapshot.particles.mass
        gsdSnapshot.particles.position = hoomdSnapshot.particles.position
        gsdSnapshot.particles.orientation = hoomdSnapshot.particles.orientation
        gsdSnapshot.particles.velocity = hoomdSnapshot.particles.velocity
        gsdSnapshot.configuration.box = hoomdSnapshot.configuration.box

    @staticmethod
    def saveSnapshot(fileName, gsdSnapshot, hoomdSnapshot):
        # WOW: This is superwierd, I couldn't find a good way to copy a hoomd.Snapshot to gsd.hoomd.Snapshot. The only difference seems like, there is a validate method for the properties and the  class itself.
        gsdSnapshot.particles.N = hoomdSnapshot.particles.N
        gsdSnapshot.particles.types = hoomdSnapshot.particles.types
        gsdSnapshot.particles.typeid = hoomdSnapshot.particles.typeid
        gsdSnapshot.particles.mass = hoomdSnapshot.particles.mass
        gsdSnapshot.particles.position = hoomdSnapshot.particles.position
        gsdSnapshot.particles.orientation = hoomdSnapshot.particles.orientation
        gsdSnapshot.particles.velocity = hoomdSnapshot.particles.velocity
        gsdSnapshot.configuration.box = hoomdSnapshot.configuration.box

        # NOTE: Saving the snapshot
        currentPath = os.path.dirname(__file__)
        snapshotPath = SysUtils.generateSnaptshotPathFromUtils(currentPath=currentPath, fileName=fileName)
        with gsd.hoomd.open(name=snapshotPath, mode='xb') as file:
            file.append(gsdSnapshot)


class SysUtils:

    @staticmethod
    def generateSnaptshotPath(currentPath, fileName):
        # HACK: Generating the savePath

        if (currentPath == ""):
            file_path = "./snapshots/" + fileName
        elif (currentPath != ""):
            file_path = currentPath + '/snapshots/' + fileName

        return file_path
    
    @staticmethod
    def generateSnaptshotPathFromUtils(currentPath, fileName):
        # HACK: Generating the savePath

        if (currentPath == ""):
            file_path = "./../snapshots/" + fileName
        elif (currentPath != ""):
            file_path = currentPath + '/../snapshots/' + fileName

        return file_path

    @staticmethod
    def generateLogPath(currentPath, fileName):
        # HACK: Generating the savePath

        if (currentPath == ""):
            file_path = "./snapshots/" + fileName
        elif (currentPath != ""):
            file_path = currentPath + '/snapshots/' + fileName

        return file_path