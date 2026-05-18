 #Stage 1 Rule based chatbot
qa_data =  {  
"library" : "The library is open from 8am on weekdays.",
"cafeteria" : "The cafeteria is located in the main building.",
"IT department": "You can contact IT at it-support@campus.edu",
"admissions": "Admission office is open from 9am to 4pm",
"hours": "We are open from 9am to 5pm.",
"location": "We are located on campus.",
"contact": "You can email us at something@mail.com",
}
def chatbot(user_input):
    user_input = user_input.lower()
    for key in qa_data:
        if key in user_input:
            return qa_data[key]
    return "Sorry, I don't understand your question. Please visit the school website @chatbot.eduhi"
#testing
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    print("Bot:", chatbot(msg))

