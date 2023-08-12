# coding=utf-8

import dashscope
from dashscope import Generation
from http import HTTPStatus
import json

dashscope.api_key = 'YOUR-API-KEY'

def getHistory(qqNum):
    with open("history.json", "r") as f:
        data = json.load(f)
        if str(qqNum) in data:
            history = data[str(qqNum)]
            return history
        else:
            history = data['0']
            newID = {str(qqNum): history}
            data.update(newID)
            return history

def request(in_history,question):
    in_prompt = question
    if in_prompt == "exit":
        return None
    response=Generation.call(
        model = 'qwen-v1',
        prompt = in_prompt,
        history = in_history
    )
    if response.status_code==HTTPStatus.OK:
        answer = response.output['text']
        newChat = {"user": in_prompt, "bot": answer}
        return newChat

def saveHistory(history, newChat, qqNum):
    history.append(newChat)
    newData = {str(qqNum): history}
    with open("history.json", "r+") as f:
        data = json.load(f)
        if str(qqNum) in data:
            data[str(qqNum)] = newData[str(qqNum)]
        else:
            data.update(newData)
        f.seek(0)
        json.dump(data, f, ensure_ascii = False, indent = 4)
        f.truncate()

def chat(question,qqNum):
    history = getHistory(qqNum)
    newChat = request(history,question)
    if newChat is None:
        return "qwen错误！！"
    saveHistory(history, newChat, qqNum)
    return newChat['bot']
