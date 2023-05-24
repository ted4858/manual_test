from pypylon import pylon
import platform
from datetime import datetime

def save_images(num_img_to_save):
    img = pylon.PylonImage()
    tlf = pylon.TlFactory.GetInstance()

    cam = pylon.InstantCamera(tlf.CreateFirstDevice())
    cam.Open()
    cam.StartGrabbing()
    for i in range(num_img_to_save):
        with cam.RetrieveResult(2000) as result:

            current_time = datetime.now().strftime("%Y%m%d_%H시%M분%S초")

            img.AttachGrabResultBuffer(result)

            if platform.system() == 'Windows':

                ipo = pylon.ImagePersistenceOptions()
                ipo.SetQuality(100)

                filename = "camera_img/{}_img_{}.jpeg".format(current_time, i+1)
                img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
            else:
                filename = "camera_img/{}_saved_pypylon_img_{}.png".format(current_time, i+1)
                img.Save(pylon.ImageFileFormat_Png, filename)

            img.Release()

    cam.StopGrabbing()
    cam.Close()
