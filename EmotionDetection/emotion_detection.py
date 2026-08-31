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

    # Parsing the JSON response from the API
    response = json.loads(response.text)

    # Extracting emotion label and score from the response
    emotions = response['emotionPredictions'][0]['emotion']
    
    # Adding the dominant emotion to the dict
    max_key = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = max_key
    
    # Returning the emotion predictions
    return emotions