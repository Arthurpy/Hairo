from django.utils.deprecation import MiddlewareMixin
import jwt
from django.http import JsonResponse
from django.contrib.auth import get_user_model

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.headers.get('Authorization')
        if token:
            try:
                payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
                user_id = payload.get('user_id')
                User = get_user_model()
                user = User.objects.get(id=user_id)
                request.user = user
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token expired'}, status=403)
            except (jwt.DecodeError, User.DoesNotExist):
                return JsonResponse({'error': 'Invalid token'}, status=401)
        else:
            request.user = None
