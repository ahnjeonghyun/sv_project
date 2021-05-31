import jwt
import json
import my_settings

from utils            import user_check

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Count

from quizes.models    import Reward, Quiz, UserAnswer
from users.models     import User, Language


class RewardLoadView(View):
    @user_check
    def get(self,request,quiz_num):
        try:
            user_language = request.user.language_id
            quiz = Quiz.objects.get(
                quiz_seq    = quiz_num,
                language_id = user_language,
            )

            result = {
                "status"            : "보상확인응답", 
                "quiz_num"          : quiz.quiz_seq,
                "mobile_reward"     : quiz.reward.mobile_reward_name,
                "mobile_reward_url" : quiz.reward.mobile_image_url,
                "PC_reward"         : quiz.reward.pc_reward_name,
                "PC_reward_url"     : quiz.reward.pc_image_url,
                "reward_rate"       : quiz.reward.reward_rate
            }

            return JsonResponse(result ,status = 200)

        except KeyError:
            return JsonResponse({'Message':'KeyError'},status = 400)

        except Quiz.DoesNotExist:
            return JsonResponse({'Message':'Quiz does not exist'},status = 400)

class QuizLoadView(View):
    @user_check
    def get(self, request, quiz_num):
        try:
            user = request.user

            quiz = Quiz.objects.get(
                quiz_seq    = quiz_num,
                language_id = user.language_id
            )

            answers = quiz.answer_set.all()

            result = {
                "quiz_num"  : quiz.quiz_seq,
                "quiz"      : quiz.content,
                "ans"       : {},
                "is_answer" : {}
            }

            for i in range(len(answers)):
                result["ans"][i+1]       = answers.get(answer_seq = i+1).answer
                result["is_answer"][i+1] = answers.get(answer_seq = i+1).answer_status

            return JsonResponse(result, status = 200)

        except KeyError:
            return JsonResponse({"Message":"KeyError"}, status = 400)
        except Quiz.DoesNotExist:
            return JsonResponse({'Message':'Quiz Does Not Exist'}, status = 400)

class AnswerCheckView(View):
    @user_check
    def post(self, request):
        data     = json.loads(request.body)
        user     = request.user
        answer   = data.get('answer',None)
        quiz_num = Quiz.objects.get(quiz_seq = data['quiz_num'],language_id = user.language_id)
        

        UserAnswer.objects.create(
            user_id   = user.id,
            quiz_id   = quiz_num.id,
            is_answer = answer
        )
        return JsonResponse({'result':'success'},status = 200)

class ResultCheckView(View):
    @user_check
    def get(self, request):
        user = request.user

        user_answer = UserAnswer.objects.filter(user_id = user.id)
        
        result = {
            "status"  : "결과확인응답",
            "correct" : user_answer.filter(is_answer = True).count(),
            "wrong"   : user_answer.filter(is_answer = False).count() + user_answer.filter(is_answer = None).count()
        }

        return JsonResponse(result, status = 200)