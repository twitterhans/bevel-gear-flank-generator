'''
import numpy as np
class Gear(jsonObject):

      # first path to be translated
      def sGear(self):
          #second part to be translated
         # it most return 3 arrays x y z

      def pGear(self):
          # third part to be translated
          # it most return 3 arrays x y z

      def involute_calculator():
          #fourth part to be translated
          # it most return 1 value
           def calcul( serializer: serializers.Serializer)-> float:
            sideTeeth = serializer.validated_data.get('sideTeeth')
            pinionTeeth = serializer.validated_data.get('pinionTeeth')
            return sideTeeth - pinionTeeth
'''
from rest_framework import serializers
import numpy as np
import time





class Gear:

    def __init__(self, defRad, nPinion, nGear, md, pressAngle, px, gx, backlashDef, backlashDist, backlashDistInv,
                 toothWidth, inRadCone, outRadCone, noProfiles, noPoints):
        print("love")
        pi = 4 * np.arctan(1)
        self.defRad = defRad
        self.nPinion = nPinion
        self.nGear = nGear
        self.md = md
        self.flagAng = True
        self.angIntersect = None
        self.pressAngle = pressAngle * (pi / 180)
        self.px = px
        self.gx = gx
        self.backlashDef = backlashDef
        self.backlashDist = backlashDist
        self.backlashDistInv = backlashDistInv
        self.toothWidth = toothWidth
        self.inRadCone = inRadCone
        self.outRadCone = outRadCone
        self.noProfiles = noProfiles
        self.noPoints = noPoints



        m = self.md * (self.outRadCone / self.defRad)


        backlash = self.backlashDef * (self.outRadCone / self.defRad)


        pitchAngleGear = np.arcsin(((m * self.nGear) / (2 * self.outRadCone)))
        pitchAnglePinion = np.arcsin(((m * self.nPinion) / (2 * self.outRadCone)))


        pitchAngleDefGear = np.arcsin((self.md * self.nGear) / (2 * self.defRad))
        pitchAngleDefPinion = np.arcsin((self.md * self.nPinion) / (2 * self.defRad))
        pitchCircleAngleDefGear = (1 / (np.sin(pitchAngleDefGear) * np.cos(self.pressAngle))) * np.arctan(
            np.sin(self.pressAngle) * np.tan(pitchAngleDefGear))
        pitchCircleAngleDefPinion = (1 / (np.sin(pitchAngleDefPinion) * np.cos(self.pressAngle))) * np.arctan(
            np.sin(self.pressAngle) * np.tan(pitchAngleDefPinion))
        baseAngleDefGear = np.arcsin(np.sin(pitchAngleDefGear) * np.cos(self.pressAngle))
        baseAngleDefPinion = np.arcsin(np.sin(pitchAngleDefPinion) * np.cos(self.pressAngle))
        toothAnglePcirBacklashDefPinion = ((pi * self.md / 2 + 2 * np.tan(
            self.pressAngle) * self.px * self.md - self.backlashDef * self.backlashDist) / (self.md * self.nPinion / 2))
        toothAnglePcirBacklashDefGear = ((pi * self.md / 2 + 2 * np.tan(
            self.pressAngle) * self.gx * self.md - self.backlashDef * (1 - self.backlashDist)) / (
                                                 self.md * self.nGear / 2))


        pitchCircleAngleGear = (1 / (np.sin(pitchAngleGear) * np.cos(self.pressAngle))) * np.arctan(
            np.sin(self.pressAngle) * np.tan(pitchAngleGear))
        pitchCircleAnglePinion = (1 / (np.sin(pitchAnglePinion) * np.cos(self.pressAngle))) * np.arctan(
            np.sin(self.pressAngle) * np.tan(pitchAnglePinion))
        baseAngleGear = np.arcsin(np.sin(pitchAngleGear) * np.cos(self.pressAngle))
        baseAnglePinion = np.arcsin(np.sin(pitchAnglePinion) * np.cos(self.pressAngle))
        cirPitchAngleGear = ((2 * np.pi) / self.nGear)
        cirPitchAnglePinion = ((2 * np.pi) / self.nPinion)
        toothAnglePcirBacklashPinion = (
                (np.pi * m / 2 + 2 * np.tan(self.pressAngle) * self.px * m - backlash * self.backlashDist) / (
                m * self.nPinion / 2))
        toothAnglePcirBacklashGear = (
                (np.pi * m / 2 + 2 * np.tan(self.pressAngle) * gx * m - backlash * (1 - self.backlashDist)) / (
                m * self.nGear / 2))
        self.SphericalGear(inRadCone, outRadCone, noProfiles, noPoints, pitchCircleAngleGear, baseAngleGear,toothAnglePcirBacklashGear, m, nGear, cirPitchAngleGear)
        self.SphericalPinion(inRadCone, outRadCone, noProfiles, noPoints, pitchCircleAnglePinion, baseAnglePinion, toothAnglePcirBacklashPinion, m, nPinion, cirPitchAnglePinion)

    def SphericalGear(self, inRadCone, outRadCone, noProfiles, noPoints,pitchCircleAngle, baseAngle, toothAnglePcirBacklash,m, n, cirPitchAngle):

        table = np.empty((0, 7))
        newLine = np.array(["\t\t", "\t\t", "\t\t", "\t\t", "\t\t", "\t\t\t\t\t", "radius"])
        table = np.vstack([table, newLine])
        l = 3
        i = 1
        self.flagAng = True

        for varRad in np.arange(inRadCone, outRadCone + 0.0000001, (outRadCone - inRadCone) / (noProfiles - 1)):

            x = (np.sin(pitchCircleAngle * np.sin(baseAngle)) * np.cos(pitchCircleAngle) - np.sin(pitchCircleAngle) * np.sin(
                baseAngle) * np.cos(
                pitchCircleAngle * np.sin(baseAngle))) * varRad
            y = (-1 * np.sin(pitchCircleAngle) * np.sin(pitchCircleAngle * np.sin(baseAngle)) - np.cos(pitchCircleAngle) * np.sin(
                baseAngle) * np.cos(
                pitchCircleAngle * np.sin(baseAngle))) * varRad
            z = (np.cos(baseAngle) * np.cos(pitchCircleAngle * np.sin(baseAngle))) * varRad

            if np.abs(y) > 0.0001:
                angForPoint = np.arctan(np.abs(x / y))
            else:
                angForPoint = np.pi / 2

            angAtPcircle = angForPoint


            self.ProfileTypeSpherical(varRad, baseAngle, toothAnglePcirBacklash, m, n, angAtPcircle)
            ldif = np.round((noPoints - 1 * 1 + 0.0000001 / self.angIntersect) + 0.5, 0)
            varin = (self.angIntersect / (noPoints - 1))

            counter = 1
            var = 0


            while counter <= noPoints:

                x = (np.sin(var * np.sin(baseAngle)) * np.cos(var) - np.sin(var) * np.sin(baseAngle) * np.cos(
                    var * np.sin(baseAngle))) * varRad
                y = (-1 * np.sin(var) * np.sin(var * np.sin(baseAngle)) - np.cos(var) * np.sin(baseAngle) * np.cos(
                    var * np.sin(baseAngle))) * varRad
                z = (np.cos(baseAngle) * np.cos(var * np.sin(baseAngle))) * varRad


                x1 = x * np.cos(angAtPcircle) - y * np.sin(angAtPcircle)
                y1 = y * np.cos(angAtPcircle) + x * np.sin(angAtPcircle)

                at = f"PNT_{i:02d}_1_{counter:02d}_X"
                ct = f"PNT_{i:02d}_1_{counter:02d}_Y"
                et = f"PNT_{i:02d}_1_{counter:02d}_Z"
                gt = np.sqrt(x1 ** 2 + y1 ** 2 + z ** 2)
                # Ajout des coordonnes dans le tableau de chaque point
                newLine = np.array([at, x1, ct, y1, et, z, gt])
                print(newLine)
                table = np.vstack([table, newLine])
                l += 1

                var += varin
                counter += 1

                if varRad == inRadCone:
                    x1 = x * np.cos(toothAnglePcirBacklash / 2 + angAtPcircle) - y * np.sin(
                        toothAnglePcirBacklash / 2 + angAtPcircle)
                    y1 = y * np.cos(toothAnglePcirBacklash / 2 + angAtPcircle) + x * np.sin(
                        toothAnglePcirBacklash / 2 + angAtPcircle)

                    x = -x1 * np.cos(toothAnglePcirBacklash / 2) + y1 * np.sin(toothAnglePcirBacklash / 2)
                    y = y1 * np.cos(toothAnglePcirBacklash / 2) + x1 * np.sin(toothAnglePcirBacklash / 2)

                    self.x1 = x * np.cos((-cirPitchAngle)) + y * np.sin((-cirPitchAngle))
                    self.y1 = y * np.cos((-cirPitchAngle)) - x * np.sin((-cirPitchAngle))

                    # rotation along Y axis
                    y = -y1 * np.cos(np.pi / 2) - z * np.sin(np.pi / 2)
                    z1 = z * np.cos(np.pi / 2) - y1 * np.sin(np.pi / 2)

            i += 1
        self.WriteFile('file1.txt', table, "Side Gear's Macro Coordinates")



    def SphericalPinion(self, inRadCone, outRadCone, noProfiles, noPoints,pitchCircleAngle, baseAngle, toothAnglePcirBacklash,m, n, cirPitchAngle):
        table = np.empty((0, 7))
        newLine = np.array(["\t\t", "\t\t", "\t\t", "\t\t", "\t\t", "\t\t\t\t\t", "radius"])
        table = np.vstack([table, newLine])
        l = 3
        i = 1
        self.flagAng = True

        for varRad in np.arange(inRadCone, outRadCone + 0.0000001, (outRadCone - inRadCone) / (noProfiles - 1)):

            self.radius = varRad
            self.var = pitchCircleAngle

            x = (np.sin(self.var * np.sin(baseAngle)) * np.cos(self.var) - np.sin(self.var) * np.sin(baseAngle) * np.cos(
                self.var * np.sin(baseAngle))) * self.radius
            y = (-1 * np.sin(self.var) * np.sin(self.var * np.sin(baseAngle)) - np.cos(self.var) * np.sin(baseAngle) * np.cos(
                self.var * np.sin(baseAngle))) * self.radius
            z = (np.cos(baseAngle) * np.cos(self.var * np.sin(baseAngle))) * self.radius

            if np.abs(y) > 0.0001:
                angForPoint = np.arctan(np.abs(x / y))
            else:
                angForPoint = np.pi / 2

            angAtPcircle = angForPoint




            self.ProfileTypeSpherical(varRad, baseAngle, toothAnglePcirBacklash, m, n, angAtPcircle)
            num = noPoints
            self.ldif = np.round((num - 1 * 1 + 0.0000001 / self.angIntersect) + 0.5, 0)
            varin = (self.angIntersect / (num - 1))

            counter = 1
            var = 0


            while counter <= noPoints:

                x = (np.sin(var * np.sin(baseAngle)) * np.cos(var) - np.sin(var) * np.sin(baseAngle) * np.cos(
                    var * np.sin(baseAngle))) * varRad
                y = (-1 * np.sin(var) * np.sin(var * np.sin(baseAngle)) - np.cos(var) * np.sin(baseAngle) * np.cos(
                    var * np.sin(baseAngle))) * varRad
                z = (np.cos(baseAngle) * np.cos(var * np.sin(baseAngle))) * varRad

                # Rotation along Y axis
                y1 = -y * np.cos(np.pi / 2) - z * np.sin(np.pi / 2)
                z1 = z * np.cos(np.pi / 2) - y * np.sin(np.pi / 2)

                if np.abs(x) > 0.0001:
                    self.angForPoint = np.arctan(np.abs(z1 / x))
                else:
                    angForPoint = np.pi / 2

                x1 = -x * np.cos(-angAtPcircle) + z1 * np.sin(-angAtPcircle)
                z2 = z1 * np.cos(-angAtPcircle) + x * np.sin(-angAtPcircle)

                at = f"PNT_{i:02d}_1_{counter:02d}_X"
                ct = f"PNT_{i:02d}_1_{counter:02d}_Y"
                et = f"PNT_{i:02d}_1_{counter:02d}_Z"
                gt = np.sqrt(x1 ** 2 + y1 ** 2 + z ** 2)
                # Ajout des coordonnes dans le tableau de chaque point
                newLine = np.array([at, x1, ct, y1, et, z2, gt])
                print(newLine)
                table = np.vstack([table, newLine])
                l += 1

                var += varin
                counter += 1

                if varRad == inRadCone:
                    x1 = x * np.cos(toothAnglePcirBacklash / 2 + angAtPcircle) - y * np.sin(
                        toothAnglePcirBacklash / 2 + angAtPcircle)
                    y1 = y * np.cos(toothAnglePcirBacklash / 2 + angAtPcircle) + x * np.sin(
                        toothAnglePcirBacklash / 2 + angAtPcircle)

                    x = -x1 * np.cos(toothAnglePcirBacklash / 2) + y1 * np.sin(toothAnglePcirBacklash / 2)
                    y = y1 * np.cos(toothAnglePcirBacklash / 2) + x1 * np.sin(toothAnglePcirBacklash / 2)

                    self.x1 = x * np.cos((-cirPitchAngle)) + y * np.sin((-cirPitchAngle))
                    self.y1 = y * np.cos((-cirPitchAngle)) - x * np.sin((-cirPitchAngle))

                    y = -y1 * np.cos(np.pi / 2) - z * np.sin(np.pi / 2)
                    z1 = z * np.cos(np.pi / 2) - y1 * np.sin(np.pi / 2)

            i += 1
        self.WriteFile('file2.txt', table, "Pinion Gear's Macro Coordinates")

    def ProfileTypeSpherical(self, varRad, baseAngle, toothAnglePcirBacklash, m, n, angAtPcircle):

        # global angIntersect, flagAng
        var = 0
        while self.flagAng:

            x = (np.sin(var * np.sin(baseAngle)) * np.cos(var) - np.sin(var) * np.sin(baseAngle) * np.cos(
                var * np.sin(baseAngle))) * varRad
            y = (-1 * np.sin(var) * np.sin(var * np.sin(baseAngle)) - np.cos(var) * np.sin(baseAngle) * np.cos(
                var * np.sin(baseAngle))) * varRad

            # Rotate x and y by half tooth_angle + angle at pcircle

            x1 = x * np.cos(toothAnglePcirBacklash / 2 + angAtPcircle) - y * np.sin(
                toothAnglePcirBacklash / 2 + angAtPcircle)

            if x1 > 0:
                x2 = x1
                if np.abs(x1) < 0.0000001:
                    self.angIntersect = var
                    self.flagAng = False
                var = var + 0.001
            else:
                if np.abs(x1) < 0.0000001:
                    if x2 < x1:
                        self.angIntersect = var
                        self.flagAng = False
                    else:
                        self.angIntersect = var - 0.000000001
                else:
                    var = var - 0.000000001
                    x2 = x1

                __all__ = ['Gear']

    def WriteFile(self, file, table, title):
        with open(file, 'w') as fichier:
            fichier.write('\t\t\t\t\t\t\t\t\t\t\t\t\t'+title+'\n\n')
            for line in table:
                lineText = '\t\t\t'.join(str(x) for x in line)
                fichier.write(lineText + '\n')
            fichier.close()
