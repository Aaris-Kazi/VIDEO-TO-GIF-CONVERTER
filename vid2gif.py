import imageio
import os

def gifmaker(inputPath, targetFormat):
    output = os.path.split(inputPath)[0] + targetFormat
    print(f'converting{inputPath} \n to {output}')
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(output, fps = fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frames{frames}')
        
    print('Done!')
    writer.close()


clip = os.path.abspath('For_GIF.mp4')
print(clip)
gifmaker(clip, '.gif')