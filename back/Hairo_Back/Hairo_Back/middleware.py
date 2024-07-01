import jwt
from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from .models import User  # Assurez-vous que User est importé

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is None:
            return
        
        token = token.split(' ')[1]
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            request.user = User.objects.get(id=user_id)
        except jwt.DecodeError:
            print(f"Failed to decode JWT: {token}")
            return JsonResponse({'error': 'Invalid token format'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
