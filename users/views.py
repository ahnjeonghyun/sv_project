import jwt
import json
import my_settings

from django.views   import View
from django.http    import JsonResponse

from users.models   import User, Language

class SignupView(View):
    def post(self,request):
        try:
            data          = json.loads(request.body)
            nickname      = data.get('nickname',None)
            language_type = data.get('language',None)
            device_type   = data.get('platform',None)

            if not (nickname or language_type or device_type):
                return JsonResponse({'Message':'Data Input Error'},status = 400)
            
            language = Language.objects.get(language_type = language_type)

            user,is_true = User.objects.get_or_create(
                nickname    = nickname,
                language_id = language.id,
                defaults={'device_type':device_type})

            if not is_true:
                return JsonResponse({'Message':'Duplicate Nickname'},status = 400)

            token = jwt.encode(
                {
                    'user_id'          : user.id,
                    'user_nickname'    : user.nickname,
                    'user_language'    : user.language.id,
                    'user_device_type' : user.device_type
                },
                my_settings.SECRET_KEY['secret'], my_settings.ALGORITHM)

            return JsonResponse({'token': token},status = 200)

        except KeyError:
            return JsonResponse({'Message':'KeyError'},status = 400)

class UserMovieView(View):
    def get(self, request):
        try:
            language = request.GET.get('language',None)
            language_type = Language.objects.get(language_type = language)

            return JsonResponse({'movie-url':language_type.movie_url},status = 200)

        except KeyError:
            return JsonResponse({'Key':'Error'},status=400)
        except Language.DoesNotExist:
            return JsonResponse({'Message':'Invalid language'},status = 400)