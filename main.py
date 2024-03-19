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
import re
from collections import Counter

def transcribe_audio(file_path):
    """
    Transcribes the given audio file to text using Whisper.
    """
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

def extract_key_takeaways(transcript, top_n=10):
    """
    Extracts key takeaways from the transcript by identifying the most common nouns.
    This is a very basic heuristic approach focusing on word frequency.
    """
    # Remove non-alphabetic characters for simplicity, keep spaces and apostrophes
    clean_transcript = re.sub(r"[^a-zA-Z\s']", '', transcript)
    words = clean_transcript.lower().split()
    
    # Count the frequency of each word
    word_freq = Counter(words)
    
    # Identify the most common words as key takeaways (simple heuristic)
    common_words = word_freq.most_common(top_n)
    key_takeaways = [word for word, _ in common_words]
    return key_takeaways

def save_to_file(filename, takeaways):
    """
    Saves takeaways to a specified file.
    """
    with open(filename, 'w') as file:
        file.write("Key Takeaways:\n")
        for takeaway in takeaways:
            file.write(f"- {takeaway}\n")

# Path to your audio file
audio_file_path = "/Users/rahuldey/Downloads/Paul Risotti.m4a"

# Transcribe the audio file
transcript = transcribe_audio(audio_file_path)

# Extract key takeaways
takeaways = extract_key_takeaways(transcript)

# Save takeaways to a file
output_filename = "output.txt"
save_to_file(output_filename, takeaways)

print(f"Transcription and analysis complete. Key takeaways saved to {output_filename}.")
