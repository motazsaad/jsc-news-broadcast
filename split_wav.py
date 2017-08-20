import pydub
import os
from pydub import AudioSegment
from pydub import silence
import glob


wav_list = sorted(glob.glob(os.path.join('./wav/', '*.wav')))
for wav_file in wav_list:
    print('processing', wav_file)
    wav_seg = AudioSegment.from_wav(wav_file)
    chunks = silence.split_on_silence(wav_seg, min_silence_len=400,
                                      silence_thresh=-24, keep_silence=300)
    if not chunks:
        chunks = silence.split_on_silence(wav_seg)
    print('number of chuncks:{}'.format(len(chunks)))
    base_name, ext = os.path.basename(wav_file).split('.')
    if not os.path.exists('./wav_split/' + base_name):
        os.mkdir('./wav_split/' + base_name)
    for i, chunk in enumerate(chunks):
        out_file = "./wav_split/{}/{}_{}.wav".format(base_name, base_name, str(i).zfill(2))
        #print("exporting", out_file)
        chunk.export(out_file, format="wav")


#os.system('rm wav_split/*.wav')
# min_silence_len=1000, silence_thresh=-16, keep_silence=100
"""
    audio_segment - original pydub.AudioSegment() object
    min_silence_len - (in ms) minimum length of a silence to be used for
        a split. default: 1000ms
    silence_thresh - (in dBFS) anything quieter than this will be
        considered silence. default: -16dBFS
    keep_silence - (in ms) amount of silence to leave at the beginning
        and end of the chunks. Keeps the sound from sounding like it is
        abruptly cut off. (default: 100ms)
"""
