import cv2
import numpy as np

# İki resmin yüklenmesi
image1 = cv2.imread("goz1.jpg")  # goz1.jpg
image2 = cv2.imread("goz2.jpg")  # goz4.jpg


# height = max(image1.shape[0], image2.shape[0])
# width = max(image1.shape[1], image2.shape[1])
# image1 = cv2.resize(image1, (width, height))
# image2 = cv2.resize(image2, (width, height))

# Panoramik birleştirici nesnesinin oluşturulması
stitcher = cv2.Stitcher_create()

# Resimleri birleştirme işlemi
status, panorama = stitcher.stitch([image1, image2])

# Panoramik resmin gösterilmesi
if status == cv2.Stitcher_OK:
    cv2.imshow('Panorama', panorama)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Panorama birleştirilemedi!')
