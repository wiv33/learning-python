import os

import numpy as np
import pandas as pd

DATA_IN_PATH = '../data_in/refine/'
TRAIN_CLEAN_DATA = 'train_clean.csv'


def rf(path):
    return "{}{}".format(DATA_IN_PATH, path)


train_data = pd.read_csv(rf(TRAIN_CLEAN_DATA))

""" word2vecㅇ의 경우 단어로 표현된 리스트를 입력값으로 넣어야 한다. """
reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

# 각 리뷰 == 하나의 문자열
# 문자열 => split
sentences = [rev.split() for rev in reviews]

# 학습 시 필요한 하이퍼파라미터
"""
num_features
    각 단어에 대해 임베딩된 벡터의 차원을 정한다.

min_word_count
    모델에 의미 잇는 단어를 가지고 학습하기 위해 적은 빈도 수의 단어들은 학습하지 않는다.

num_workers
    모델 학습 시 학습을 위한 프로세스 개수를 지정한다.
    
context
    word2vec을 수행하기 위한 컨텍스트 윈도 크기를 지정한다.

down_sampling
    word2vec 학습을 수행할 때 빠른 학습을 위해 정답 단어 라벨에 대한 다운샘플링 비율을 지정한다.
    0.001
    
"""
num_features = 300
min_word_count = 40
num_workers = 4
context = 10
down_sampling = 1e-3

# pip install gensim

import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

print('Training model...')

model = word2vec.Word2Vec(sentences=sentences,
                          workers=num_workers,
                          size=num_features,
                          min_count=min_word_count,
                          window=context,
                          sample=down_sampling)

# 모델 저장

model_name = '300features_40minwords_10context'
model.save(model_name)


def get_features(words, model, num_features):
    # 출력 벡터 초기화
    feature_vector = np.zeros((num_features), dtype=np.float32)

    num_words = 0

    # 어휘 사전 준비
    index2word_set = set(model.wv.index2word)

    for w in words:
        if w in index2word_set:
            num_words += 1

            feature_vector = np.add(feature_vector, model[w])
    feature_vector = np.divide(feature_vector, num_words)

    return feature_vector


def get_dataset(reviews, model, num_features):
    dataset = [get_features(s, model, num_features) for s in reviews]

    reviewFeatureVecs = np.stack(dataset)
    print(f'reviewFeatures shape is : {reviewFeatureVecs.shape}')
    return reviewFeatureVecs


test_data_vecs = get_dataset(sentences, model, num_features)

print(test_data_vecs.shape)

from sklearn.model_selection import train_test_split

X = test_data_vecs
y = np.array(sentiments)

TEST_SPLIT = .2
RANDOM_SEED = 42

# 학습 / 검증 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=TEST_SPLIT,
                                                    random_state=RANDOM_SEED)

from sklearn.linear_model import LogisticRegression

lgs = LogisticRegression(class_weight='balanced')
lgs.fit(X_train, y_train)

print(f'x_test len is {len(X_test)}')
predicted = lgs.predict(X_test)

from sklearn import metrics

fpr, tpr, _ = metrics.roc_curve(y_test, (lgs.predict_proba(X_test)[:, 1]))
auc = metrics.auc(fpr, tpr)

print("------------")
print("Accuracy: %f" % lgs.score(X_test, y_test))  # checking the accuracy
print("Precision: %f" % metrics.precision_score(y_test, predicted))
print("Recall: %f" % metrics.recall_score(y_test, predicted))
print("F1-Score: %f" % metrics.f1_score(y_test, predicted))
print("AUC: %f" % auc)
print(f'Accuracy : {lgs.score(X_test, y_test)}')

TEST_CLEAN_DATA = 'test_clean.csv'

test_data = pd.read_csv(rf(TEST_CLEAN_DATA))

test_review = list(test_data['review'])

test_sentences = [review.split() for review in test_review]

test_data_vecs = get_dataset(test_sentences, model, num_features)
print(f'test_data_vecs len is {len(test_data_vecs)}')
test_predicted = lgs.predict(test_data_vecs)
DATA_OUT_PATH = '../data_out/'

if not os.path.exists(DATA_OUT_PATH):
    os.makedirs(DATA_OUT_PATH)

ids = list(test_data['id'])
print(len(ids), len(test_predicted))
answer_dataset = pd.DataFrame({'id': ids, 'sentiment': test_predicted})
answer_dataset['id'] = answer_dataset['id'].apply(lambda x: x.replace('"', ''))
answer_dataset.to_csv(DATA_OUT_PATH + 'lgs_word2vec_answer.csv', index=False)

# kaggle competitions -c word2vec-nlp-tutorial -f lgs_word2vec_answer.csv -m "word2vec answer"
