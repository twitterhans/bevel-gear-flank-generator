from rest_framework import serializers


class MacroSerializer(serializers.Serializer):

    defRad = serializers.FloatField()
    nPinion = serializers.FloatField()
    nGear = serializers.FloatField()
    md = serializers.FloatField()
    pressAngle = serializers.FloatField()
    px = serializers.FloatField()
    gx = serializers.FloatField()
    backlashDef = serializers.FloatField()
    backlashDist = serializers.FloatField()
    backlashDistInv = serializers.FloatField()
    toothWidth = serializers.FloatField()
    inRadCone = serializers.FloatField()
    outRadCone = serializers.FloatField()
    noProfiles = serializers.FloatField()
    noPoints = serializers.FloatField()

