from externals.tortoise.tortoise.utils.audio import load_voices
import spacy

nlp = spacy.load("en_core_web_sm")

def generate_audio_stream(text, tts, voice_samples):
    print(f"Generating audio stream...: {text}")
    voice_samples, conditioning_latents = load_voices([voice_samples])
    stream = tts.tts_stream(
        text,
        voice_samples=voice_samples,
        conditioning_latents=conditioning_latents,
        verbose=True,
        stream_chunk_size=40  # Adjust chunk size as needed
    )
    for audio_chunk in stream:
        yield audio_chunk


def split_text(text, max_length=200):
    doc = nlp(text)
    chunks = []
    chunk = []
    length = 0

    for sent in doc.sents:
        sent_length = len(sent.text)
        if length + sent_length > max_length:
            chunks.append(' '.join(chunk))
            chunk = []
            length = 0
        chunk.append(sent.text)
        length += sent_length + 1

    if chunk:
        chunks.append(' '.join(chunk))

    return chunks