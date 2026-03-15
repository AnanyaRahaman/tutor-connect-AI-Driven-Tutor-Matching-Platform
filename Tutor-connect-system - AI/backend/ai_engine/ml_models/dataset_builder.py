import pandas as pd

def build_training_data():

    data = {
        "subject_match":[1,1,0,1,0,1,1,0],
        "rating":[4.8,4.6,3.2,5.0,4.0,4.9,4.7,3.5],
        "price_diff":[5,10,25,3,15,6,4,20],
        "availability":[1,1,0,1,1,1,1,0],
        "experience":[5,4,2,7,3,6,8,1],
        "chosen":[1,1,0,1,0,1,1,0]
    }

    df = pd.DataFrame(data)

    return df