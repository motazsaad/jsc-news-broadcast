import argparse
import os
import shutil

from pydub import AudioSegment
from pydub import silence

my_min_silence_len = 450
my_keep_silence = 350

parser = argparse.ArgumentParser(description='split wav file based on the silence')
parser.add_argument('-i', '--infile', type=str,
                    help='input file.', required=True)


def export_chunks(chunks, wave_file):
    print('number of chucks:{}'.format(len(chunks)))
    base_name, ext = os.path.basename(wave_file).split('.')
    if not os.path.exists('./wav_split/' + base_name):
        print("making ", './wav_split/' + base_name)
        os.mkdir('./wav_split/' + base_name)
    else:
        print("removing ", './wav_split/' + base_name)
        shutil.rmtree('./wav_split/' + base_name)
        print("making ", './wav_split/' + base_name)
        os.mkdir('./wav_split/' + base_name)
    for i, chunk in enumerate(chunks):
        out_file = "./wav_split/{}/{}_{}.wav".format(base_name, base_name, str(i).zfill(2))
        chunk.export(out_file, format="wav")


if __name__ == '__main__':
    args = parser.parse_args()
    wav_file = args.infile
    print('processing', wav_file)
    wav_seg = AudioSegment.from_wav(wav_file)
    ans = 'y'
    threshold = 0
    while ans == 'y':
        threshold = input("please enter a threshold: ")
        chunks = silence.split_on_silence(wav_seg, silence_thresh=threshold,
                                          keep_silence=my_keep_silence,
                                          min_silence_len=my_min_silence_len)
        print('number of chucks:{}'.format(len(chunks)))
        ans = input('try another threshold? (y or n): ')
    export_chunks(chunks, wav_file)

# os.system('rm wav_split/*.wav')
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
