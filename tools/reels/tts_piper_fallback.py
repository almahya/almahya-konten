import wave, numpy as np, json, soundfile as sf
from piper import PiperVoice
from piper.config import SynthesisConfig
from scenes import SCENES
v=PiperVoice.load("vits-piper-id_ID-news_tts-medium/id_ID-news_tts-medium.onnx",config_path="vits-piper-id_ID-news_tts-medium/id_ID-news_tts-medium.onnx.json")
sr=v.config.sample_rate; out=[]; times=[]; t=0
gap=np.zeros(int(sr*0.35),dtype=np.float32)
cfg=SynthesisConfig(length_scale=0.92)
for s in SCENES:
    chunks=[c.audio_float_array for c in v.synthesize(s["tts"],syn_config=cfg)]
    x=np.concatenate(chunks+[gap]).astype(np.float32); out.append(x)
    times.append((t,t+len(x)/sr)); t+=len(x)/sr
sf.write("voice.wav",np.concatenate(out),sr)
json.dump(times,open("times.json","w")); print([round(b-a,1) for a,b in times],sr,round(t,1))
