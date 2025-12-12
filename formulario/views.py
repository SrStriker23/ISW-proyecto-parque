from django.shortcuts import render
import json
from django.http import JsonResponse
from administracion.models import Response, Sector, Period
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    contexto = {
        'periodos': Period.objects.all(),
        'sectores': Sector.objects.all(),
    }

    return render(request,'formulario.html',contexto)

@csrf_exempt
def submitForm(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    body = json.loads(request.body.decode("utf-8"))

    # Buscar sector
    sector_id = body.get("sector")
    sector = Sector.objects.filter(id=sector_id).first()

    # Periodo actual para estadísticas
    now = datetime.now()
    period, _ = Period.objects.get_or_create(year=now.year, month=now.month)

    resp = Response.objects.create(
        sector=sector,
    period=period,
    nationality=body.get("nacionalidad"),
    age_group=body.get("edad"),
    motive=body.get("motivo"),
    rate_sendero=body.get("rate_sendero"),
    rate_info=body.get("rate_info"),
    rate_limpieza=body.get("rate_limpieza"),
    rate_personal=body.get("rate_personal"),
    comentario_positivo=body.get("comentario_positivo"),
    comentario_negativo=body.get("comentario_negativo"),
    comentario_general=body.get("comentario_general"),
    nps=body.get("nps"),
    anonymous=True,
    consent_given=body.get("consent", False),
    language=body.get("language", "es"),
    type=body.get("type", "full")
    )

    return JsonResponse({"status": "success", "id": resp.id})