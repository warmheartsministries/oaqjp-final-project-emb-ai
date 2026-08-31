import requests
import json

def emotion_detector(text_to_analyze):
    # URL of emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Constructing the request payload in expected format 
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)

    # If the response status code is 200, extract the emotions and scores
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        # Extracting emotion label and score from the response
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # Adding the dominant emotion to the dict
        max_key = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = max_key
    # If the response status code is 400, set the values of all keys to None
    elif response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        emotions['dominant_emotion'] = None
    
    # Returning the emotion predictions
    return emotions