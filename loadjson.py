s__author__ = 'falko'

import sys
import json
#import time
from config import *


reload(sys)
sys.setdefaultencoding('utf-8')

def getJson(so, question):
    data = {}
    data["title"] = question.title
    data["url"] = question.url
    data["tags"] = question.tags
    data["question_body"] = question.body
    data["view_count"] = question.view_count
    data["question_creation_date"] = question.creation_date.isoformat()
    #***************************************************************************
    try:
        owner_id = question.owner.id
    except:
        owner_id = None
    #***************************************************************************
    if not owner_id is None:
        data["owner_id"] = owner_id
        #time.sleep (0.15)
        user = so.user(owner_id)
        try:
            data["owner_name"] = question.owner.display_name
        except:
            data["owner_name"] = None

        try:
            data["owner_age"] = user.age
        except :
            data["owner_age"] = None
        try:
            data["owner_location"] = user.owner_location
        except :
            data["owner_location"] = None
        try:
            data["owner_reputation"] = user.reputation
        except :
            data["owner_reputation"] = None
    else:
        data["owner_id"] = None
        data["owner_name"] = None
        data["owner_age"] = None
        data["owner_location"] = None
        data["owner_reputation"] = None
    #***************************************************************************
    try:
        data["accepted_answer_id"] = question.accepted_answer_id
    except:
        data["accepted_answer_id"] = None

    if not data["accepted_answer_id"] is None:
        answer = None
        try:
            answer = so.answer(question.accepted_answer_id)
        except:
            answer = None

        if not answer is None:
            answerer_id = answer.owner_id
            data["answerer_id"] = answerer_id
            data["answer_body"] = answer.body
            data["answer_creation_date"] = answer.creation_date.isoformat()
            #time.sleep (0.15)
            answerer = None
            try:
                answerer = so.user(answerer_id)
            except:
                answerer = None

            try:
                data["answerer_name"] = answerer.display_name
            except:
                data["answerer_name"] = None
            try:
                data["answerer_age"] = answerer.age
            except:
                data["answerer_age"] = None
            try:
                data["answerer_location"] = answerer.location
            except:
                data["answerer_location"] = None
            try:
                data["answerer_reputation"] = answerer.reputation
            except:
                data["answerer_reputation"] = None
        else:
            data["answerer_id"] = None
            data["answer_body"] = None
            data["answer_creation_date"] = None
            data["answerer_name"] = None
            data["answerer_age"] = None
            data["answerer_location"] = None
            data["answerer_reputation"] = None

    else:
        data["answerer_id"] = None
        data["answer_body"] = None
        data["answerer_name"] = None
        data["answer_creation_date"] = None
        data["answerer_age"] = None
        data["answerer_location"] = None
        data["answerer_reputation"] = None
    #***************************************************************************
    json_data = json.dumps(data)
    return json_data
