import numpy as np

# PATH_TO_MODEL_CHECKPOINTS = "./model/save_epoch_1/ViolenceNet.ckpt"
PATH_TO_MODEL_CHECKPOINTS = "C:/Users/USER/Desktop/ai_test/인공지능_test/ViolenceDetection-master/model/save_epoch_1/ViolenceNet.ckpt"

'''
      To smooth the Judgement of Fight/NoneFight, count of neighbor frames
    (that has the value) should >= CHANGE_JUDGEMENT_THRESHOLD to change the
    judgement.
      Usually, this value is setted to the same as the frames Threshold that
    produce the Best Accuracy in Validation set.

    ex:
	NetOutput	Judgement
	  False		  False
	  True		  False
	  True		  False
	  True		  True
	  False		  True
	  Flase		  True
	  Flase		  False
'''
CHANGE_JUDGEMENT_THRESHOLD = 3

# 191211 Modify
DISPLAY_IMAGE_SIZE = 500
# DISPLAY_IMAGE_SIZE = 1000

BORDER_SIZE = 100
FIGHT_BORDER_COLOR = (0, 0, 255)
NO_FIGHT_BORDER_COLOR = (0, 255, 0)
