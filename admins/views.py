import json
import bcrypt
import jwt
import my_settings

from django.views  import View
from django.http   import JsonResponse
from django.db.models import Count

from admins.models import Admin
from quizes.models import Quiz, UserAnswer
from users.models  import User, Language

class AdminSigninView(View):
    def post(self,request):
        try:
            data      = json.loads(request.body)
            password  = data['password']
            admin     = Admin.objects.get(pk = 1)
            
            if not bcrypt.checkpw(password.encode('utf-8'), admin.password.encode('utf-8') ):
                return JsonResponse({'Message' : 'Invalid_paasword'}, status = 400)
            
            encode_jwt = jwt.encode({'admin_id' : admin.id}, my_settings.SECRET_KEY['secret'], my_settings.ALGORITHM)
            return JsonResponse({'token' : encode_jwt}, status = 200)

        except KeyError:
            return JsonResponse({'Message' : 'KeyError'}, status = 400)

class AdminChartView(View):
    def get(self, request):
        users = User.objects.all()
        quiz = Quiz.objects.all()
        useranswers = UserAnswer.objects.all()

        result ={
            "result" : "success",
            "user" :{
                    "total"  : users.count(),
                    "ko"     : users.filter(language_id = 1).count(),
                    "en"     : users.filter(language_id = 2).count(),
                    "ru"     : users.filter(language_id = 3).count(),
                    "th"     : users.filter(language_id = 4).count(),
                    "tu"     : users.filter(language_id = 5).count(),
                    "pt"     : users.filter(language_id = 6).count(),
                    "zh"     : users.filter(language_id = 7).count(),
                    "ja"     : users.filter(language_id = 8).count(),
                    "PC"     : users.filter(device_type = "PC").count(),
                    "Mobile" : users.filter(device_type = "Mobile").count()
                },
                "1" : {},
                "2" : {},
                "3" : {},
                "4" : {},
                "5" : {},
                "6" : {},
                "7" : {},
                "8" : {},
                "9" : {},
                "10" : {},
                "11" : {},
                "12" : {},
                "13" : {},
                "14" : {},
                "15" : {},
            }

        for i in range(1,16):
            true  = 0
            false = 0
            none  = 0
            for j in Quiz.objects.filter(quiz_seq = i):
                true  += j.useranswer_set.filter(is_answer = True).count()
                false += j.useranswer_set.filter(is_answer = False).count()
                none  += j.useranswer_set.filter(is_answer = None).count()
        
            result[str(i)]['정답']  = true
            result[str(i)]['오답']  = false
            result[str(i)]['미참여'] = none
                
        return JsonResponse(result, status = 200)