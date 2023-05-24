from pypylon import pylon
import platform
from datetime import datetime

class ImageSaver:
    def __init__(self):
        self.img = pylon.PylonImage()
        self.tlf = pylon.TlFactory.GetInstance()
        self.cam = None

    def cam_open(self):
        self.cam = pylon.InstantCamera(self.tlf.CreateFirstDevice())
        self.cam.Open()
        self.cam.StartGrabbing()

    def cam_close(self):
        self.cam.StopGrabbing()
        self.cam.Close()

    def save_images(self, num_img_to_save, img_num):
        for i in range(num_img_to_save):
            with self.cam.RetrieveResult(2000) as result:
                current_time = datetime.now().strftime("%Y%m%d_%H시%M분%S초")
                self.img.AttachGrabResultBuffer(result)

                if platform.system() == 'Windows':
                    ipo = pylon.ImagePersistenceOptions()
                    ipo.SetQuality(100)
                    if num_img_to_save == 1:
                        filename = "camera_img/{}_img_{}.jpeg".format(current_time, img_num)
                        self.img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
                    else:
                        filename = "camera_img/{}_img_{}_{}.jpeg".format(current_time, img_num, i)
                        self.img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
                else:
                    if num_img_to_save == 1:
                        filename = "camera_img/{}_saved_pypylon_img_{}.png".format(current_time, img_num)
                        self.img.Save(pylon.ImageFileFormat_Png, filename)
                    else:
                        filename = "camera_img/{}_saved_pypylon_img_{}.png".format(current_time, img_num, i)
                        self.img.Save(pylon.ImageFileFormat_Png, filename)

                self.img.Release()

# Usage:
# saver = ImageSaver()
# saver.cam_open()
# for i in range(400):
#     saver.save_images(1, i)
# saver.cam_close()

# from pypylon import pylon
# import platform
# from datetime import datetime

# def save_images(num_img_to_save):
#     img = pylon.PylonImage()
#     tlf = pylon.TlFactory.GetInstance()

#     cam = pylon.InstantCamera(tlf.CreateFirstDevice())
#     cam.Open()
#     cam.StartGrabbing()
#     for i in range(num_img_to_save):
#         with cam.RetrieveResult(2000) as result:

#             current_time = datetime.now().strftime("%Y%m%d_%H시%M분%S초")

#             img.AttachGrabResultBuffer(result)

#             if platform.system() == 'Windows':

#                 ipo = pylon.ImagePersistenceOptions()
#                 ipo.SetQuality(100)

#                 filename = "camera_img/{}_img_{}.jpeg".format(current_time, i+1)
#                 img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
#             else:
#                 filename = "camera_img/{}_saved_pypylon_img_{}.png".format(current_time, i+1)
#                 img.Save(pylon.ImageFileFormat_Png, filename)

#             img.Release()

#     cam.StopGrabbing()
#     cam.Close()