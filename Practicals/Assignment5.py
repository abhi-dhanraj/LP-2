import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today? ", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Priyanka. You can call me crazy if you want!", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good! How about you?", ]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's okay, never mind", ]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I help you?", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you? :)", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude! Seriously? You are asking me this?", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse ;)", ]
    ],
    [
        r"(.*) created ?",
        ["Abhishek created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pune, Maharashtra', ]
    ],
    [
        r"How is the weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot here in %1 man",
            "Too cold here in %1 man", "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is such an amazing company innit? But they are in huge loss these days :(", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2",
            "Damn it's raining cats and dogs here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a huge fan of football", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messi", "Ronaldo", "Neymar"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["W3 schools has many great articles with step-by-step explanation along with code, you can explore!"]
    ],
    [
        r"quit",
        ["Bye, take care! Work hard! :) ",
            "It was nice talking to you! See you soon :)"]
    ],
]


def chat():
    print("Hello there! This is chatbot by Abhishek! How can I serve you?")
    chat = Chat(pairs, reflections)
    chat.converse()


# initiate the conversation
if __name__ == "__main__":
    chat()
