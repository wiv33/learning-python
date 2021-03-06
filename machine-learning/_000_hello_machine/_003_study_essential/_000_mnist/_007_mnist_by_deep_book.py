﻿import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import utils, layers, models

print(tf.__version__)

# 신경망과 훈련 매개변수
EPOCHS = 50  # 200 to 50
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10  # output의 demension
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2  # 검증
DROPOUT = 0.3  # 30% 죽이겠다.

# MNIST 데이터셋 로드
# 검증

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
RESHAPED = 784

x_train = x_train.reshape(60000, RESHAPED)
x_test = x_test.reshape(10000, RESHAPED)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# 입력을 [0, 1] 사이로 정규화
# 파이썬의 숫자 타입
# int, float
x_train = x_train / 255.
x_test = x_test / 255.

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# 레이블을 원핫 인코딩
y_train = utils.to_categorical(y_train, NB_CLASSES)
y_test = utils.to_categorical(y_test, NB_CLASSES)

# 모델 구축
model = models.Sequential()

# chap.02 layer 추가하기
model.add(layers.Dense(N_HIDDEN,
                       input_shape=(RESHAPED, ),  # layers.Input(shape=RESHAPED, ))
                       name='dense_layer',
                       activation='relu'))

model.add(layers.Dropout(DROPOUT))
model.add(layers.Dense(N_HIDDEN,
                       name='dense_layer_2',
                       activation='relu'))

model.add(layers.Dropout(DROPOUT))
model.add(layers.Dense(NB_CLASSES,
                       name='dense_layer_3',
                       activation='softmax'))

plt.imshow(x_train[0].reshape(28, 28))
plt.show()

# 모델 컴파일
model.compile(optimizer="SGD",
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train,
          y_train,
          batch_size=BATCH_SIZE,
          epochs=EPOCHS,
          verbose=VERBOSE,
          validation_split=VALIDATION_SPLIT)

# 모델 평가
# a, b = ("a", "b")
test_loss, test_acc = model.evaluate(x_test, y_test)

test_loss

test_acc

model.summary()

# 지도학습에서의 학습
# x * w + b == 정답이랑 같은지?
# (0 * -0.07939142) + (0 * -0.01258871) + == 7번째 인덱스의 값이 1에 가까운지?

