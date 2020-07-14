'''import pandas as pd
import pickle

knn_pickel_filename = '../knn_model.pkl'
gnb_pickel_filename = '../gnb_model.pkl'
DT_pickel_filename = '../DT_model.pkl'
selected_features_filename = '/selected_features.csv'

with open(knn_pickel_filename, 'rb') as file:
    mod = pickle.load(file)



def usr_input(causes):
    d = "itching,skin_rash,nodal_skin_eruptions,continuous_sneezing,shivering,chills,joint_pain,stomach_pain,acidity,ulcers_on_tongue,muscle_wasting,vomiting,burning_micturition,spotting_ urination,fatigue,weight_gain,anxiety,cold_hands_and_feets,mood_swings,weight_loss,restlessness,lethargy,patches_in_throat,irregular_sugar_level,cough,high_fever,sunken_eyes,breathlessness,sweating,dehydration,indigestion,headache,yellowish_skin,dark_urine,nausea,loss_of_appetite,pain_behind_the_eyes,back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,yellowing_of_eyes,acute_liver_failure,fluid_overload,swelling_of_stomach,swelled_lymph_nodes,malaise,blurred_and_distorted_vision,phlegm,throat_irritation,redness_of_eyes,sinus_pressure,runny_nose,congestion,chest_pain,weakness_in_limbs,fast_heart_rate,pain_during_bowel_movements,pain_in_anal_region,bloody_stool,irritation_in_anus,neck_pain,dizziness,cramps,bruising,obesity,swollen_legs,swollen_blood_vessels,puffy_face_and_eyes,enlarged_thyroid,brittle_nails,swollen_extremeties,excessive_hunger,extra_marital_contacts,drying_and_tingling_lips,slurred_speech,knee_pain,hip_joint_pain,muscle_weakness,stiff_neck,swelling_joints,movement_stiffness,spinning_movements,loss_of_balance,unsteadiness,weakness_of_one_body_side,loss_of_smell,bladder_discomfort,foul_smell_of urine,continuous_feel_of_urine,passage_of_gases,internal_itching,toxic_look_(typhos),depression,irritability,muscle_pain,altered_sensorium,red_spots_over_body,belly_pain,abnormal_menstruation,dischromic _patches,watering_from_eyes,increased_appetite,polyuria,family_history,mucoid_sputum,rusty_sputum,lack_of_concentration,visual_disturbances,receiving_blood_transfusion,receiving_unsterile_injections,coma,stomach_bleeding,distention_of_abdomen,history_of_alcohol_consumption,fluid_overload,blood_in_sputum,prominent_veins_on_calf,palpitations,painful_walking,pus_filled_pimples,blackheads,scurring,skin_peeling,silver_like_dusting,small_dents_in_nails,inflammatory_nails,blister,red_sore_around_nose,yellow_crust_ooze"
    heds = d.split(sep=',')
    temp = pd.DataFrame(columns=heds,index=['A'])
    for i in temp.columns:
    #for j in causes:
        if i in causes :
            temp.xs('A')[i] = '1'
        else:
            temp.xs('A')[i] = '0'
    f = temp.reset_index(drop=True)
    return f

def cause(str):
    causes = str.split(",")
    da = usr_input(causes)

    selected_features= pd.read_csv(selected_features_filename)
    sf = selected_features['selected_features'].tolist()
    test_data_new = da[sf]
    X_test = test_data_new.iloc[:,:]
    #X_test
    selected_features = pd.read_csv('selected_features.csv')
    sf = selected_features['selected_features'].tolist()
    test_data_new = da[sf]
    X_test = test_data_new.iloc[:, :-1]
    with open(knn_pickel_filename, 'rb') as file:
        knn_classifier = pickle.load(file)

    with open(gnb_pickel_filename, 'rb') as file:
        gnb_classifier = pickle.load(file)

    with open(DT_pickel_filename, 'rb') as file:
        dt_classifier = pickle.load(file)

    k_pred_test = knn_classifier.predict(X_test)
    gnb_pred = gnb_classifier.predict(X_test)
    dt_pred = dt_classifier.predict(X_test)
    dis = [k_pred_test, gnb_pred, dt_pred]
    append_new(da.loc[0])
    return dis

from csv import writer
def append_new(t):
    with open('New.csv', 'a+',newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(t)

'''

