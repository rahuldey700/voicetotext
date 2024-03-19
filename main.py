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

def extract_key_insights_and_quotes(transcript):
    """
    Extracts key insights and quotes from the transcript.
    This is a heuristic approach that looks for sentences with quotation marks for quotes
    and sentences that may signify insight based on certain keywords.
    """
    # Split transcript into sentences
    sentences = re.split(r'(?<=[.!?])\s+', transcript)
    
    insights = []
    quotes = []
    
    # Keywords that might indicate insightful sentences
    insight_keywords = ['importantly', 'notably', 'key point', 'remember', 'highlight']
    
    for sentence in sentences:
        # Check for direct quotes
        if '"' in sentence or "“" in sentence or "‘" in sentence:
            quotes.append(sentence)
        # Check for sentences containing insight keywords
        elif any(keyword in sentence.lower() for keyword in insight_keywords):
            insights.append(sentence)
    
    return insights, quotes

def save_to_file(filename, insights, quotes):
    """
    Saves insights and quotes to a specified file.
    """
    with open(filename, 'w') as file:
        file.write("Key Insights:\n")
        for insight in insights:
            file.write(f"- {insight}\n")
        
        file.write("\nKey Quotes:\n")
        for quote in quotes:
            file.write(f"- {quote}\n")

# Path to audio file
audio_file_path = "/Users/rahuldey/Downloads/Paul Risotti.m4a"

# Transcribe the audio file
transcript = transcribe_audio(audio_file_path)

# Extract key insights and quotes
insights, quotes = extract_key_insights_and_quotes(transcript)

# Save insights and quotes to a file
output_filename = "output.txt"
save_to_file(output_filename, insights, quotes)

print(f"Transcription and analysis complete. Insights and quotes saved to {output_filename}.")

