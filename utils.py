import json
import jwt
import my_settings

from django.http      import JsonResponse

from users.models     import User, Language
from admins.models    import Admin

def user_check(func):
    def decorator(self, request, *args, **kwargs):
        try:
            encoded_token = request.headers['Authorization']
            decoded_token = jwt.decode(encoded_token, my_settings.SECRET_KEY['secret'], my_settings.ALGORITHM)

            if decoded_token.get('user_id',None):

                user = User.objects.get(
                    id          = decoded_token['user_id'],
                    nickname    = decoded_token['user_nickname'],
                    language_id = decoded_token['user_language'],
                    device_type = decoded_token['user_device_type']
                )
                request.user = user

                return func(self, request, *args, **kwargs)
            
            elif decoded_token.get('admin_id',None):

                user = User.objects.get(
                    id = decoded_token['admin_id'],
                )

                request.user = user

                return func(self, request, *args, **kwargs)

        except User.DoesNotExist:
            return JsonResponse({"message":"UNKNOWN_USER"}, status = 401)

        except KeyError:
            return JsonResponse({"message":"INVALID_LOGIN"}, status = 401)

        except jwt.DecodeError:
            return JsonResponse({"message":"INVALID_TOKEN"}, status = 401)

    return decorator