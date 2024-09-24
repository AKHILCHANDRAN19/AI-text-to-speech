# Import the necessary libraries
import os
import sys
from TTS.api import TTS

# Function to initialize TTS model
def initialize_tts(model_name):
    try:
        tts = TTS(model_name)
        print(f"TTS model '{model_name}' loaded successfully.")
        return tts
    except Exception as e:
        print(f"Error loading TTS model '{model_name}': {e}")
        sys.exit(1)

# Function to synthesize speech from text
def synthesize_speech(tts, text, output_file):
    try:
        tts.tts_to_file(text=text, file_path=output_file)
        print(f"Speech synthesized and saved to '{output_file}'.")
    except Exception as e:
        print(f"Error synthesizing speech: {e}")

# Function to get user input for text and voice selection
def get_user_input(available_voices):
    print("Available Voices:")
    for i, voice in enumerate(available_voices):
        print(f"{i + 1}: {voice}")

    # Select voice
    while True:
        try:
            choice = int(input("Select a voice by number: "))
            if 1 <= choice <= len(available_voices):
                selected_voice = available_voices[choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Input text, allow multi-line input until "done" is typed
    print("Enter the text you want to convert to speech (type 'done' when finished):")
    text_lines = []
    while True:
        line = input()
        if line.lower() == 'done':
            break
        text_lines.append(line)

    # Join all lines into a single string
    text = "\n".join(text_lines)
    return selected_voice, text

# Main function
def main():
    # Define the model
    model_name = "tts_models/en/ljspeech/tacotron2-DDC"
    
    # Initialize TTS model
    tts = initialize_tts(model_name)

    # Hardcoded list of available voices (update this list with actual voices)
    available_voices = ["Voice 1", "Voice 2", "Voice 3"]  # Replace with actual voice names

    # Get user input for text and voice
    selected_voice, text = get_user_input(available_voices)

    # Output file path in Downloads folder
    output_file = "/storage/emulated/0/Download/output_speech.wav"

    # Synthesize speech
    synthesize_speech(tts, text, output_file)

if __name__ == "__main__":
    main()
