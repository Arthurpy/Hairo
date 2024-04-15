def get_user_oauth_token_from_django(request):
    if request.user.is_authenticated:
        user = request.user
        oauth_token = user.profile.oauth_token  # À adapter selon ta structure de modèle
        return oauth_token
    else:
        return None
