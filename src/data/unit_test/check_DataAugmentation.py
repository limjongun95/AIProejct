#!/usr/bin/python3

import os
import sys
import cv2
import skvideo.io
import numpy as np
import src.data.DataAugmenter as DataAugmenter
import src.data.ImageUtils as ImageUtils

'''
    Change the following variable if you have different data arrangement
'''
LIST_OF_VIDEOS = [
	"./datafile/noFights/no222_xvid.avi",
	"./datafile/fights/fi1_xvid.avi",
	"./datafile/fights/fi2_xvid.avi",
	"./datafile/noFights/no223_xvid.avi",
	"./datafile/fights/fi3_xvid.avi",
	"./datafile/noFights/no224_xvid.avi",
	"./datafile/noFights/no230_xvid.avi",
	"./datafile/fights/fi4_xvid.avi",
	"./datafile/noFights/no234_xvid.avi",
	"./datafile/noFights/no234_xvid.avi",
	"./datafile/noFights/no235_xvid.avi",
	"./datafile/fights/fi7_xvid.avi",
	"./datafile/noFights/no236_xvid.avi",
	"./datafile/fights/fi8_xvid.avi",
	"./datafile/fights/fi14_xvid.avi",
	"./datafile/noFights/no239_xvid.avi"

]


def PrintHelp():
	print("Usage:")
	print("\t $(ThisScript)")
	print("\t\t Note: If you're not put your data in 'data/Bermejo/hockey', you should edit this script")
	print("\t\t	  and change the data path.")
	print()

def PrintImageRange(title_, image_):
	minValue = np.min(image_)
	maxValue = np.max(image_)
	print(title_ + "(min, max) = (" + str(minValue) + ", " + str(maxValue) + ")")

def Check_DataAugmentation():
	canvas = np.zeros( [500, 1000, 3], dtype=np.uint8)

	for eachVideoPathFileName in LIST_OF_VIDEOS:
		batchOfImagesRGB = skvideo.io.vread(eachVideoPathFileName)
		batchOfAugmentedImages = DataAugmenter.Augment(batchOfImagesRGB)

		if batchOfImagesRGB.shape != batchOfAugmentedImages.shape:
			errorMessage = "Loaded image.shape = " + str(batchOfImagesRGB.shape) + "\n"
			errorMessage += "While augmentedImage.shape = " + str(augmentedImage.shape) + "\n"
			errorMessage += "Not Equal!"
			raise ValueError(errorMessage)

		w = batchOfImagesRGB.shape[2]
		h = batchOfImagesRGB.shape[1]

		i = 0
		while True:
			originalImage = batchOfImagesRGB[i]
			originalImage = cv2.cvtColor(originalImage, cv2.COLOR_RGB2BGR)
			canvas[:h, :w] = originalImage

			augmentedImage = batchOfAugmentedImages[i]
			augmentedImage = cv2.cvtColor(augmentedImage, cv2.COLOR_RGB2BGR)
			canvas[:h, 500:500+w] = augmentedImage
			
			cv2.imshow("Violence Detection", canvas)

			userResponse = cv2.waitKey(0)
			if userResponse == ord('n'):
				i += 1
				if i >= batchOfImagesRGB.shape[0]:
					break

			elif userResponse == ord('b'):
				i -= 1

			elif userResponse == ord('q'):
				raise StopIteration()



if __name__ == '__main__':
	if len(sys.argv) == 1:
		Check_DataAugmentation()


	else:
		PrintHelp()
