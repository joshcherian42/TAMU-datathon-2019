import os


def init():

    os.chdir("../Data")
    
    global training_data
    training_data = os.path.join(os.getcwd(), "equip_failures_training_set.csv")
    global test_data
    training_data = os.path.join(os.getcwd(), "equip_failures_test_set.csv")
    global sample_submission
    sample_submission = os.path.join(os.getcwd(), "sample_submission.csv")
