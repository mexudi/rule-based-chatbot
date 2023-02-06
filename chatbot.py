from ntlk.chat.util import Chat, reflections

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
        r"I am (.*) (good|well|okay|ok)"
    ]
]