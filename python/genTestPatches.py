from PIL import Image
import numpy as np
import cv2
import os




def getTestPatches(imId):
    objId = 5

    base_path = '/Users/apurvnigam/study_ucl/term1/MScThesis/hinterstoisser/'
    # base_path = '../'

    test_filepath = base_path + 'test/{:02d}/testImages/{:04d}/test{:04d}_{:02d}{:02d}.txt'
    test_RGBPatch_path = base_path+'test/{:02d}/testImages/{:04d}/testPatchesRGB/'
    test_DepthPatch_path = base_path + 'test/{:02}/testImages/{:04d}/testPatchesDepth/'
    seg_output_path = base_path + 'test/{:02}/testImages/{:04d}/segout{:04d}.png'


    if not os.path.isdir(test_RGBPatch_path.format(objId,imId)):
        os.makedirs(test_RGBPatch_path.format(objId,imId))
    if not os.path.isdir(test_DepthPatch_path.format(objId,imId)):
        os.makedirs(test_DepthPatch_path.format(objId,imId))

    rgb_image_path = base_path+ 'test/05/rgb/%04d.png'%(imId)
    rgbData = cv2.imread(rgb_image_path,-1)

    dep_image_path = base_path + 'test/05/depth/%04d.png'%(imId)
    depData = cv2.imread(dep_image_path, -1)

    segOut = cv2.imread(seg_output_path.format(objId,imId,imId))
    indices = np.where(np.all(segOut == 1,axis=2))
    coords = zip(indices[0], indices[1])

    w=20
    h=20
    outFile = open(test_filepath.format(objId,imId,imId,w,h), 'w')

    for pix in coords:
        # for c in indices[1]:
        r= pix[0]
        c= pix[1]
        rgbSubImg = rgbData[r-h : r+h, c-w :c+w];
        # rgbSubImg = cv2.resize(rgbSubImg, (227, 227))
        cv2.imwrite(test_RGBPatch_path.format(objId,imId)+'%03d%03d.png'%(r,c),rgbSubImg)
        #
        depSubImg = depData[r - h: r + h, c - w:c + w];
        # depSubImg = cv2.resize(depSubImg, (227, 227))
        cv2.imwrite(test_DepthPatch_path.format(objId,imId)+'%03d%03d.png' % (r, c), depSubImg)
        outFile.write('%03d%03d.png\n'%(r,c))


imId=0

# for i in range(1,2,10):
#     print i
getTestPatches(1146)