import json


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Twitte

@login_required
def api_add_twitte(request):
    data = json.loads(request.body)
    body = data['body']

    twitte = Twitte.objects.create(body = body, created_by = request.user)

    return JsonResponse({'success': True})