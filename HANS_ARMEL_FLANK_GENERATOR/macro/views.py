from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import MacroSerializer
from django.http.response import JsonResponse
from django.http.response import Http404
from rest_framework.response import Response
from .Calculation import Gear


# Create your views here.

class MacroView(APIView):

    def post(self, request):
        data = request.data
        print(data)
        serializer = MacroSerializer(data=data)

        if serializer.is_valid():
            defRad = serializer.validated_data.get('defRad')
            nPinion = serializer.validated_data.get('nPinion')
            nGear = serializer.validated_data.get('nGear')
            md = serializer.validated_data.get('md')
            pressAngle = serializer.validated_data.get('pressAngle')
            px = serializer.validated_data.get('px')
            gx = serializer.validated_data.get('gx')
            backlashDef = serializer.validated_data.get('backlashDef')
            backlashDist = serializer.validated_data.get('backlashDist')
            backlashDistInv = serializer.validated_data.get('backlashDistInv')
            toothWidth = serializer.validated_data.get('toothWidth')
            inRadCone = serializer.validated_data.get('inRadCone')
            outRadCone = serializer.validated_data.get('outRadCone')
            noProfiles = serializer.validated_data.get('noProfiles')
            noPoints = serializer.validated_data.get('noPoints')
            gear_name = "Gear1"
            setattr(self, gear_name, Gear(defRad, nPinion, nGear, md, pressAngle, px, gx, backlashDef, backlashDist, backlashDistInv, toothWidth, inRadCone, outRadCone, noProfiles, noPoints))
            return JsonResponse("ok", safe=False, status=200)
        else:
            return JsonResponse(serializer.errors, safe=False, status=400)

    def delete(self, request):
        return JsonResponse("data deleted successfully", safe=False)

    def put(self, request):
        return JsonResponse("data modified successfully", safe=False)

    def get(self, request):
        return JsonResponse("data recievedget successfully", safe=False)