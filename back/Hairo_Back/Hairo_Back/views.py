# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import User, Cours, FichierPDF, QCM, Resultat
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.http import JsonResponse
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialToken
from rest_framework import generics
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from .serializers import CoursSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import QCMSerializer, ResultatSerializer
from django.views.generic import ListView


def landing_page(request):
    return render(request, 'landing.html')


@csrf_exempt
def course_details_by_name(request):
    try:
        data = json.loads(request.body.decode('utf-8'))  # ensure decoding from bytes if needed
        course_name = data.get('courseName')
        if not course_name:
            return JsonResponse({'error': 'No course name provided'}, status=400)

        cours = Cours.objects.get(nom__iexact=course_name)  # Case insensitive search
        pdfs = cours.fichiers.all()
        pdf_data = [{
            'id': pdf.id,
            'nom': pdf.nom,
            'url': request.build_absolute_uri(pdf.fichier.url)  # Accessing the file url correctly
        } for pdf in pdfs]
        return JsonResponse({
            'nom': cours.nom,
            'pdfs': pdf_data
        }, safe=True)
    except Cours.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        # Log the exception to help with debugging
        print(f"Error in course_details_by_name: {str(e)}")
        return JsonResponse({'error': 'Server error'}, status=500)

@csrf_exempt
def ressources_pages(request):
    if request.method == 'POST':
        # Récupérer tous les cours de la base de données
        cours_list = Cours.objects.all()
        # Transformer les données en liste de dictionnaires
        cours_data = [{'id': cours.id, 'nom': cours.nom} for cours in cours_list]
        # Retourner les données en JSON
        return JsonResponse(cours_data, safe=False)
    else:
        # Si la méthode n'est pas POST, vous pouvez choisir de renvoyer une réponse appropriée
        return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def login_view(request):
    # Add logging
    data = json.loads(request.body)
    print("Data received:", data)

    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, 'your_secret_key', algorithm='HS256')

        return JsonResponse({'token': token})
    else:
        return JsonResponse({'error': 'Invalid Credentials'}, status=400)
    
def protected_view(request):
    if request.user is not None:
        return JsonResponse({'message': 'Welcome!'})
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=401)


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = User.objects.create_user(email=email, password=password)
        login(request, user)

        # Générer un jeton JWT
        token_payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(days=2)  # Expiration dans 2 jours
        }
        token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')

        # Stocker le jeton si nécessaire ou le renvoyer directement
        return JsonResponse({'token': token, 'message': 'User created successfully'})

    return render(request, 'signup.html')

@login_required
def agenda(request):
     # Récupérer le jeton d'accès OAuth de l'utilisateur depuis Django
    token = SocialToken.objects.get(account__user=request.user, account__provider='google')

    # Créer un objet Credentials à partir du jeton d'accès OAuth
    credentials = Credentials(token)

    # Créer un client Google Calendar à partir des credentials
    calendar_service = build('calendar', 'v3', credentials=credentials)

    # Récupérer la date de début et de fin de la semaine actuelle
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    # Récupérer les événements de la semaine actuelle
    events = calendar_service.events().list(
        calendarId='primary',
        timeMin=start_of_week.isoformat() + 'Z',
        timeMax=end_of_week.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    # Passer les événements au template
    context = {
        'events': events.get('items', [])
    }

    return JsonResponse(context)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({'message': 'Token is missing!'}, status=403)

        try:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            current_user = User.objects.get(id=data['id'])
        except:
            return JsonResponse({'message': 'Token is invalid!'}, status=403)

        return f(current_user, *args, **kwargs)

    return decorated


def send_token_response(user):
    token = generate_token_for(user)  # Générer le jeton d'authentification ici
    return JsonResponse({'token': token, 'message': 'Logged in successfully'})



class QCMViewSet(viewsets.ModelViewSet):
    queryset = QCM.objects.all()
    serializer_class = QCMSerializer

    def get_queryset(self):
        cours_id = self.request.query_params.get('cours_id')
        if cours_id is not None:
            return QCM.objects.filter(cours_id=cours_id)
        return super().get_queryset()

class ResultatViewSet(viewsets.ModelViewSet):
    queryset = Resultat.objects.all()
    serializer_class = ResultatSerializer

def get_all_qcms(request):
    qcms = QCM.objects.all()
    serializer = QCMSerializer(qcms, many=True)
    return JsonResponse(serializer.data, safe=False)

class QCMListView(ListView):
    model = QCM
    # Optionally specify a template or define how the data is rendered
    # template_name = 'qcm_list.html'
    
    def get_queryset(self):
        return QCM.objects.all()

 
def get_all_qcms(request):
    qcms = QCM.objects.all()
    serializer = QCMSerializer(qcms, many=True)
    return JsonResponse(serializer.data, safe=False)

def upload_pdf(request):
    user_id = request.user.id
    cours_nom = "Mes cours"
    pdf_file = request.FILES.get('file')
    if pdf_file and pdf_file.name.endswith('.pdf'):
        is_linked = (cours_nom == "Mes cours")
        cours, created = Cours.objects.get_or_create(
            nom=cours_nom,
            defaults={'is_linked_to_user': is_linked}
        )
        if is_linked:
            cours.user = request.user
            cours.save()

        FichierPDF.objects.create(
            cours=cours,
            nom=pdf_file.name,
            fichier=pdf_file
        )
        return JsonResponse({'message': 'PDF uploaded successfully'}, status=200)
    return JsonResponse({'message': 'Invalid file'}, status=400)


def create_qcm(request):
    if request.method == 'POST':
        json_generated =  generate_json(request.pdf_file, request.cours_id)
        if json_generated:
            QCM.objects.create(cours_id=request.cours_id, contenu_json=json_generated)
            return JsonResponse({'message': 'QCM created successfully'})
        else:
            return JsonResponse({'error': 'Error generating QCM JSON'}, status=500)
        
