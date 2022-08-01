from  PIL import Image
import os
from getpass import getuser

downloadsFolder = "//fe00fsc1212.bsh.corp.bshg.com/fredirect$/"+ getuser() +"/Downloads/"
picturesFolder = "//fe00fsc1212.bsh.corp.bshg.com/fredirect$/"+ getuser() +"/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

