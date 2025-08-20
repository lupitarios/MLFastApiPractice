from transformers import pipeline


print("\n\n*** Sentiment Analysis using Hugging Face Transformers ***\n")
user_feeling = input("How do you feel today? ")
emotion_model = pipeline("text-classification", model = "j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
#emotion_model("I am so happy to see you!")  # Example usage
output_classification = emotion_model(user_feeling)
print(output_classification)

output_classification[0].sort(key=lambda x: x['score'], reverse=True)
print("\n\nSorted Output Classification:\n", output_classification[0])
print("\n\nTop Emotion:\n", output_classification[0][0])  #
# The output will be a list of dictionaries, each containing a label and a score.
# The label represents the emotion, and the score represents the confidence level of that emotion.
print("\n\nTop Emotion Label:\n", output_classification[0][0]['label'])  # Top emotion label