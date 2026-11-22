import sherpa_onnx, soundfile as sf, numpy as np, json
d="/home/claude/reel/sherpa-onnx-whisper-small/"
r=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d+"small-encoder.int8.onnx",decoder=d+"small-decoder.int8.onnx",tokens=d+"small-tokens.txt",language="id",task="transcribe",num_threads=2)
x,sr=sf.read("el16.wav",dtype="float32")
sil=[(2.357,2.757),(6.618,6.869),(10.138,10.562),(12.954,13.207),(21.222,21.554),(27.762,28.106),(33.125,33.391),(39.196,39.454)]
cuts=[0]+[ (a+b)/2 for a,b in sil]+[len(x)/sr]
for i in range(len(cuts)-1):
    s=r.create_stream(); s.accept_waveform(sr,x[int(cuts[i]*sr):int(cuts[i+1]*sr)]); r.decode_stream(s)
    print(i,round(cuts[i],2),round(cuts[i+1],2),s.result.text)
