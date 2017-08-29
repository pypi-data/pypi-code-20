from keras.preprocessing import sequence
from keras.datasets import imdb


def data(max_features=5000, maxlen=400):
    print('Loading data...')
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

    # subset the data
    x_train = x_train[:1000]
    y_train = y_train[:1000]
    x_test = x_test[:100]
    y_test = y_test[:100]

    print(len(x_train), 'train sequences')
    print(len(x_test), 'test sequences')

    print('Pad sequences (samples x time)')
    x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
    x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
    print('x_train shape:', x_train.shape)
    print('x_test shape:', x_test.shape)
    return (x_train, y_train, [1, 2, 3, "dummy_data"]), (x_test, y_test)