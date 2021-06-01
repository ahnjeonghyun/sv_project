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
        #         id            = row[0],
        #         language_type = row[1],
        #         movie_url     = row[2]
        #         )

        # # #reward 생성
        # Reward.objects.create(
        #     id                 = row[0],
        #     language_id        = row[1],
        #     mobile_image_url   = row[2],
        #     pc_image_url       = row[3],
        #     mobile_reward_name = row[4],
        #     pc_reward_name     = row[5],
        #     reward_rate        = row[6]
        # )

        # quiz 생성
        # Quiz.objects.create(
        #         id          = row[0],
        #         language_id = row[1],
        #         quiz_seq    = row[2],
        #         content     = row[3],
        #         reward_id   = row[4]
        #        )

        # #answer생성
        # Answer.objects.create(
        #     language_id   = row[0],
        #     quiz_id       = row[1],
        #     answer        = row[2],
        #     answer_status = row[3],
        #     answer_seq    = row[4]
        # )