import os
import signal
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'hashmicro_project/index.html')

@csrf_exempt
def uninstall(request):
    if request.method == 'POST':
        # Terminate the Django application
        try:
             os.kill(os.getpid(), signal.SIGTERM)
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': 'Failed to terminate application!'}, status=500)
        return JsonResponse({'status': 'success', 'message': 'Application terminated.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method!.'}, status=400)