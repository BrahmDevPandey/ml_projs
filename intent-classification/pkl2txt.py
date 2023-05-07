import spacy
import numpy as np
import pickle


intents = {1: 'admission_process',
            2: 'academics',
            3: 'general',
            4: 'greeting',
            5: 'hod',
            6: 'fee_structure',
            7: 'random',
            8: 'placement',
            9: 'miscellaneous'}

nlp = spacy.load("en_core_web_sm")
with open("question-classifier.pkl", "rb") as file:
  classifier = pickle.load(file)

# a simple function to determine the intent of a question
def findIntent(query):
  doc = nlp(query)
  keywords_str = ""

  # find the keywords
  for token in doc:
    if not token.is_stop and not token.is_punct and not token.pos_ == 'PRON' and token.text.lower():
      keywords_str += token.lemma_ + " "  # add to keyword_str

  test_data = np.array(nlp(keywords_str).vector).reshape(1, -1)
  
  # predict the class of this vector
  res = classifier.predict(test_data)[0]
  return intents[res]


# print(findIntent("how many companies visit the campus"))
