import PIL
import matplotlib.pyplot as plt
# Saving individual images for each z values
for i in range(0,74,1):
    reflectivity = data.variables['reflectivity'][i]
    im = plt.imshow(reflectivity, origin='lower')
    plt.title('reflectivity at z = ' + str(i))
    im.figure.savefig(r'C:\Users\bikra\Desktop\RA\Gif images'+'\\'+str(i)+'.jpg')
    plt.clf()


#Creating gif from images created above
image_frames = []
days = np.arange(0,74)
for i in days:
    new_frame = PIL.Image.open(r'C:\Users\bikra\Desktop\RA\Gif images'+'\\'+ str(i) + '.jpg')
    image_frames.append(new_frame)
   
image_frames[0].save('Reflectivity at z kilometers.gif', format = 'GIF',
                     append_images = image_frames[1: ],
                     save_all = True, duration = 100,
                     loop = 0)
