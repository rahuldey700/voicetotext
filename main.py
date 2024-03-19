# import whisper
# from collections import Counter
# import re

# def transcribe_audio(file_path):
#     """
#     Transcribes the given audio file to text using Whisper.
#     """
#     model = whisper.load_model("base")
#     result = model.transcribe(file_path)
#     return result["text"]

# def extract_key_takeaways(transcript, top_n=5):
#     """
#     Extracts key takeaways from the transcript by identifying the most common nouns.
#     This is a very basic heuristic approach.
#     """
#     # Remove non-alphabetic characters for simplicity
#     clean_transcript = re.sub(r'[^a-zA-Z\s]', '', transcript)
#     words = clean_transcript.lower().split()
    
#     # Simple heuristic to focus on nouns, assuming they might be key subjects
#     # This could be improved with proper NLP techniques
#     common_words = Counter(words).most_common(top_n)
#     key_takeaways = [word for word, _ in common_words]
#     return key_takeaways

# # Path to your audio file (e.g., "meeting_audio.mp3")
# audio_file_path = "/Users/rahuldey/Downloads/Paul Risotti.m4a"

# # Transcribe the audio file
# transcript = transcribe_audio(audio_file_path)
# print("Transcript:", transcript)

# # Extract key takeaways
# takeaways = extract_key_takeaways(transcript)
# print("Key Takeaways:", takeaways)

import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

audio_file_path = "/Users/rahuldey/Downloads/Paul Risotti.m4a"
transcript = transcribe_audio(audio_file_path)
print("Transcript:", transcript) 

from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

summary = summarize_text(transcript)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def extract_themes(text, top_n=5):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    
    # Filter out stop words and non-alphabetic words
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
    
    # Count and return the most common words
    most_common_words = Counter(filtered_words).most_common(top_n)
    return [word for word, _ in most_common_words]

themes = extract_themes(transcript)

def save_results(filename, transcript, summary, themes):
    with open(filename, 'w') as file:
        file.write("Transcription:\n\n")
        file.write(transcript)
        file.write("\n\nSummary:\n\n")
        file.write(summary)
        file.write("\n\nKey Themes:\n\n")
        file.write('\n'.join(themes))

output_filename = "analysis_output.txt"
save_results(output_filename, transcript, summary, themes)

print(f"Analysis complete. Results saved to {output_filename}.")
