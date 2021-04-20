import requests
import json


def get_answer():
    # get the input
    user_input = input()
    # check if input can be converted to int
    # if yes, return int
    if user_input.isnumeric():
        return int(user_input)
    # if not, call nlu server
    # return intent
    else:
        url = "http://localhost:5005/model/parse"
        mydata = json.dumps({"text": user_input})

        x = requests.post(url, data=mydata)

        # TODO: convert json to object/dict
        print(x.text)


questions_dict = {
    "A1": "How much of the time do you feel you are making progress towards accomplishing your goals?",
    "E1": "How often do you become absorbed in what you are doing?",
    "P1": "In general, how often do you feel joyful?",
    "N1": "In general, how often do you feel anxious?",
    "A2": "How often do you achieve the important goals you have set for yourself?",
    "M1": "In general, to what extent do you lead a purposeful and meaningful life?",
    "R1": "To what extent do you receive help and support from others when you need it?",
    "M2": "In general, to what extent do you feel that what you do in your life is valuable and worthwhile?",
    "E2": "In general, to what extent do you feel excited and interested in things?",
    "H2": "How satisfied are you with your current physical health?",
    "P2": "In general, how often do you feel positive?",
    "N2": "In general, how often do you feel angry?",
    "R2": "To what extent do you feel loved?",
    "R3": "How satisfied are you with your personal relationships?",
    "P3": "In general, to what extent do you feel contented?"
}

print("Hi, I am Quoca :) How should I call you?")

name = input()

print(
    f'''Nice to meet you, {name}. I am glad that you are interested in having a 
happier life - and I am pleased to help you in this journey! To start, I will ask you a series of questions.
Please answer them as honestly as you can.
Let's go?'''
)

start = True

for key in questions_dict:
    print(questions_dict[key])
    answer = get_answer()
