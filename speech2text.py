import io
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'/users/amjad/SecretKey/Synclarity-9776378de904.json'
from google.cloud import speech
from google.cloud.speech import enums

output_filepath = "Transcripts/"
file_name  = "counter"
storage_uri = 'gs://grapheast/speech2text/{}.flac'.format(file_name)

def gc_long_running_recognize(storage_uri):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """
    transcript=''
    client = speech.SpeechClient()

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 48000


    # The language of the supplied audio
    language_code = "en-US"
    model = "default"
    use_enhanced = True
    enable_word_time_offsets = True
    phrases = ["In this Tutorial","image carousel","Press alt and drag"]
    #boost = 2
    #speech_contexts_element = {"phrases": phrases,"boost": boost}
    speech_contexts_element = {"phrases": phrases}
    #speech_contexts = [speech_contexts_element]
    speech_contexts=[speech.types.SpeechContext(phrases=["In this Tutorial","artboard"])]

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC

    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": encoding,
        "audio_channel_count":1,
        #"use_enhanced": use_enhanced,
        "model": model,
        "enable_word_time_offsets":enable_word_time_offsets,
        "speech_contexts": speech_contexts,

    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    for result in response.results:
        # First alternative is the most probable result
        transcript += result.alternatives[0].transcript
        #alternative = result.alternatives[0]
        #print(u"Transcript: {}".format(alternative.transcript))

    return transcript

def write_transcripts(transcript_filename,transcript):
    f= open(transcript_filename,"a")
    f.write(transcript)
    f.close()

if __name__ == "__main__":
    transcript = gc_long_running_recognize(storage_uri)
    transcript_filename = 'Transcripts/{}.txt'.format(file_name)
    write_transcripts(transcript_filename,transcript)
