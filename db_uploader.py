import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sv_blackdesert.settings")
django.setup()

from users.models  import *
from quizes.models import *
from admins.models import *

CSV_PATH_PRODUCTS = './quiz.csv'

with open(CSV_PATH_PRODUCTS) as in_file:

    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        #Language 생성
        # Language.objects.create(
        #         language_type = row[0],
        #         movie_url=row[1]
                # )

        # #reward 생성
        # Reward.objects.create(
        #     language_id = row[0],
        #     mobile_image_url = row[1],
        #     pc_image_url = row[2],
        #     mobile_reward_name = row[3],
        #     pc_reward_name = row[4],
        #     reward_rate = row[5]
        # )

        # quiz 생성
        # Quiz.objects.create(
        #         language_id = row[0],
        #         quiz_seq = row[1],
        #         content = row[2],
        #         reward_id = row[3]
        #        )

        # #answer생성
        # Answer.objects.create(
        #     language_id = row[0],
        #     quiz_id = row[1],
        #     answer = row[2],
        #     answer_status = row[3],
        #     answer_seq = row[4]
        # )