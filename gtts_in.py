#!/usr/bin/env python3
#!/Users/amjad/py-stuff/speech2text/env/
import os
import argparse
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'/users/amjad/SecretKey/Synclarity-9776378de904.json'
#-------------------------------
def synthesize_text_file(text_file):
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    with open(text_file, 'r') as f:
        text = f.read()
        input_text = texttospeech.types.SynthesisInput(text=text)
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-IN',
        name='en-IN-Wavenet-A',
        #ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE
        )

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
        pitch= 0
        )

    response = client.synthesize_speech(input_text, voice, audio_config)
    with open('output2.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

def synthesize_ssml_file(ssml_file):
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    with open(ssml_file, 'r') as f:
        ssml = f.read()
        input_text = texttospeech.types.SynthesisInput(ssml=ssml)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-IN',
        name='en-IN-Wavenet-A',
        #ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE
        )

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
        pitch= .3,
        speaking_rate= .9,
        #effects_profile_id=['large-home-entertainment-class-device']
        )

    response = client.synthesize_speech(input_text, voice, audio_config)
    with open('output1.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output1.mp3"')


#-------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--text',
                       help='The text file from which to synthesize speech.')
    group.add_argument('--ssml',
                       help='The ssml file from which to synthesize speech.')

    args = parser.parse_args()

    if args.text:
        synthesize_text_file(args.text)
    else:
        synthesize_ssml_file(args.ssml)

 # commandline >> python3 gtts_in.py --ssml scripts/ge-pr-0016.xml
