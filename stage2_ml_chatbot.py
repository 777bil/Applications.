#Stage 2 chatbot
import random
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 

# Training data
questions = [
    "When is the application deadline?",
    "When does the admission period end?",
    "What is the last day to apply?",
    "Are applications still open?",
    "What documents do I need to apply?",
    "Do I need a high school certificate?",
    "What should I submit for my applications?",
    "What are the required application documents?",
    "Are there robotics clubs?",
    "What student activities are available?",
    "How do I participate in campus events?",
    "How do i apply for dormitory?",
    "How can I get accomodation?",
    "What are the dorm fees?",
    "Where are the student dorms?",
    "Is there a library?",
    "Where is the faculty building or engineering building?",
    "What facilities are available for students?",
    "What is the minimum IELTS score?",
    "Do International students need English scores?",
    "What English test is accepted?",
    "Who can I  contact for more information?"
]

# Labels (intent)
answers = [
    "admission_deadline",
    "admission_deadline",
    "admission_deadline",
    "admission_deadline",
    "required_documents",
    "required_documents",
    "required_documents",
    "required_documents",
    "club_activities",
    "club_activities",
    "club_activities",
    "housing_information",
    "housing_information",
    "housing_information",
    "housing_information",
    "campus_facilities",
    "campus_facilities",
    "campus_facilities",
    "english_requirement",
    "english_requirement",
    "english_requirement",
    "contact_information"
]
#Map labels to responses
responses = {
    "admission_deadline": "The admission deadline depends on the application round. Please check the official university admission website for the most up-to date deadline.",
    "required_documents": "Applicants are required to submit academic transcripts, identification documents, and any required certificates such as high school equivalency certificate. Please refer to the official admission guidelines for detailed requirements.",
    "club_activities":"Students can join clubs and activities during orientation or through student affairs office. Available clubs and activities can be inquired from the student affairs office.",
    "housing_information": "Students may apply for on-campus housing through the university housing office. Availability and fees are provided on the official housing webpage.",
    "campus_facilities": "Campus facilities such as library,gym and computer labs are available to students. Facility locations and operating hours can be found on the university website.",
    "english_requirement":"Englsih proficiency is required for International programs. Accepted tests and minimum scores are specified in the official admission criteria.",
    "contact_information":"You can contact your faculty on this mail; contact@mail.com"
}


#convert text to numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Train supervised ML model
model = LogisticRegression()
model.fit(X, answers)

def get_response(user_input):
    X = vectorizer.transform([user_input])
    probs = model.predict_proba(X)[0]
    confidence = max(probs)
    predicted_index = np.argmax(probs)
    
    THRESHOLD = 0.6
    if confidence < THRESHOLD:
        return "I'm not confident about the answer to this, Please check the official school website (@campus.edu) for the most accurate and up to date information."
    tag = answers[predicted_index]
    for intent in answers["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])


#def chatbot_stage2(user_input):
   # vec = vectorizer.transform([user_input])
    #prediction = model.predict(vec)[0]
    #return responses[prediction]


# Test Stage 2
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    print("Bot:", get_response(msg))


