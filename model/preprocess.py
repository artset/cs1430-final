"""
Project 4 - CNNs
CS1430 - Computer Vision
Brown University
"""

import os
import random
import numpy as np
from PIL import Image
import tensorflow as tf

import hyperparameters as hp

class Datasets():
    """ Class for containing the training and test sets as well as
    other useful data-related information. Contains the functions
    for preprocessing.
    """
    def __init__(self, data_path):
        self.data_path = data_path

        # Setup data generators
        # TRAIN DATA
        self.train_data = self.get_data(os.path.join(self.data_path, "train/"), True, True)
        # TEST DATA
        self.test_data = self.get_data(os.path.join(self.data_path, "test/"), False, False)

    def preprocess_fn(self, img):
        """ Preprocess function for ImageDataGenerator. """
        img = img / 255.
        return img

    def get_data(self, path, shuffle, augment):
        """ Returns an image data generator which can be iterated
        through for images and corresponding class labels.

        Arguments:
            path - Filepath of the data being imported, such as
                   "../data/train" or "../data/test"
            shuffle - Boolean value indicating whether the data should
                      be randomly shuffled.
            augment - Boolean value indicating whether the data should
                      be augmented or not.

        Returns:
            An iterable image-batch generator
        """
        if augment:
            # Use the arguments of ImageDataGenerator()
            # to augment the data. Leave the
            # preprocessing_function argument as is unless
            # you have written your own custom preprocessing
            # function (see custom_preprocess_fn()).
            #
            # Documentation for ImageDataGenerator: https://bit.ly/2wN2EmK
            #
            # ============================================================
            data_gen = tf.keras.preprocessing.image.ImageDataGenerator(
                preprocessing_function=self.preprocess_fn, 
                horizontal_flip=True, 
                zoom_range=[.5, 1.0],
                fill_mode='nearest')
            # ============================================================
        else:
            # Don't modify this
            data_gen = tf.keras.preprocessing.image.ImageDataGenerator(
                preprocessing_function=self.preprocess_fn)

        # model takes 256x256
        img_size = hp.img_size

        # Form image data generator from directory structure
        data_gen = data_gen.flow_from_directory(
            path,
            target_size=(img_size, img_size),
            # save_to_dir=os.path.join(self.data_path, "preprocess/"),
            batch_size=hp.batch_size,
            shuffle=shuffle)
  
        return data_gen
