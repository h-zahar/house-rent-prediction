import numpy as np
import pickle
import sklearn

locations = open('locations.txt', 'r').read().split("', '")

model = pickle.load(open('model.pkl', 'rb'))

def data_preprocessing(Location, Area, Bed, Bath):
    index = locations.index(Location)
    x = np.zeros(len(locations))
    x[0] = Area
    x[1] = Bed
    x[2] = Bath

    if index >= 0:
        x[index] = 1

    return x

def prediction(Location, Area, Bed, Bath):
    x = data_preprocessing(Location, Area, Bed, Bath)
    features = [x]
    prediction = model.predict(features)
    result = prediction[0]

    return result

def main():
    print(prediction('Matikata Cantonment Dhaka',1250, 3, 3))

if __name__ == "__main__":
    main()