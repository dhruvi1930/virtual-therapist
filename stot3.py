from sklearn.preprocessing import LabelEncoder
from keras.models import model_from_json
import os
import record
import pandas as pd
import librosa
import glob
import keras
import numpy as np


def voice1():
    lb = LabelEncoder()
    # emo1=['sad', 'happy', 'angry']
    emo2 = ['female_happy', 'female_angry', 'male_happy', 'male_angry', 'female_sad', 'male_sad']
    lb.fit_transform(emo2)
    json_file = open(r'E:/sem7/project/virtual/speeash14.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(r"E:/sem7/project/virtual/speeash14.h5")
    opt = keras.optimizers.rmsprop(lr=0.00001, decay=1e-6)
    loaded_model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    record.record()
    X, sample_rate = librosa.load('recoutput.wav', res_type='kaiser_fast', duration=2.5, sr=22050 * 2, offset=0.5)
    sample_rate = np.array(sample_rate)
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)
    featurelive = mfccs
    livedf2 = featurelive
    livedf2 = pd.DataFrame(data=livedf2)
    livedf2 = livedf2.stack().to_frame().T
    twodim = np.expand_dims(livedf2, axis=2)
    livepreds = loaded_model.predict(twodim, batch_size=32, verbose=1)
    livepreds1 = livepreds.argmax(axis=1)
    liveabc = livepreds1.astype(int).flatten()
    livepredictions = (lb.inverse_transform((liveabc)))
    return livepredictions