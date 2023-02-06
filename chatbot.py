from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and response
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
    [
        r"(.*) your name ?",
        ["I do not have a specific name, but you can call MexBot and I am a chatbot  "]
    ],
    [
        r"how are you (.*) ?",
        ['I am doing very well', "I am great!",'I am doing good']
    ],
    [
        r"sorry (.*)",
        ['Its alright','Its ok, never mind','come on it is not a big deal','come on! why you are sorry!']
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["I am glad to hear that", "Nice to hear that", "Alright, great!",]
    ],
    [
        r"(hi|hey|hello|hola|holla|hi)(.*)",
        ["Hello","Hey there","hey! whats up",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can not refuse",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tetouan, Morocco',]
    ],
    [
        r"(.*)raining in (.*)",
        ['I have no idea because I do not have access to internet','I would suggest to check an online website',]
    ],
    [
        r"(.*)created(.*)",
        ["Soufiane Lamchoudi created me using Python's NLTK library, and my name is inspired from his nickname since people call him Mexudi",]
    ],
    [
        r"quit",
        ['It was nice talking to you, see you soon and take care']
    ],
    [
        r"(.*)",
        ['That is nice to hear','hmm interesting']
    ],
]
#test the reflection
print(reflections)