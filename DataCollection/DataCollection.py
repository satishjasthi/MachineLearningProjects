import pandas as pd
import sqlite3
import tqdm
import itertools

#connecting to sql 
con = sqlite3.connect("mental_health.sqlite")

#We have 3 tables(Survey_year,questions and answers) in sql file so we making diffrent datasets 
raw_data_questions = pd.read_sql_query("select * from Question" , con)
raw_data_answers = pd.read_sql_query("select * from Answer",con)

con.close()

#by using this raw datasets we will make anothor dataset which makes easy to build model
#craeting a empty dataset which contains all the question id as columns and users as rows
questionid_list = list(raw_data_questions['questionid'])
question_col = ['Q%s' % (x,) for x in questionid_list]
col = ['user_id']+question_col
dataset = pd.DataFrame(columns=col)
dataset['user_id'] = raw_data_answers['UserID'].unique()

# Adding answers to each user to the questions he answered , if the user didnt answers we will add not avaliable to that question
main_list = []
# questionid_list is a list of all question id
for i in tqdm.tqdm(questionid_list):
    values_list = []
    # range of number of users
    for w in range(1,4219):
        # if user answers the question then values_list is append with answeres value otherwise not avalaible
        if list(raw_data_answers['AnswerText'][(raw_data_answers['UserID']==w)&(raw_data_answers['QuestionID']==i)].values) != []:
            value = raw_data_answers['AnswerText'][(raw_data_answers['UserID']==w)&(raw_data_answers['QuestionID']==i)].values
            values = list(value)[0]
            values_list.append(values)
        else:
            values_list.append('Not_avaliable')
    #each values_list of users will be append into maimain_list so that we can add those values into dataframe          
    main_list.append(list(values_list))     

# adding each list of main_list to each person in datset   
index = 0
for i in question_col:
    dataset[i] = main_list[index]
    index = index+1

#Adding survey_id which is the survey year to the dataset

survey_list=[]
for i in range(1,4219):
    survey_year = raw_data_answers['SurveyID'][raw_data_answers['UserID']==i].values[0]
    survey_list.append(survey_year)
dataset['survey_id'] = survey_list  

#now we will select features which are importent to predict mental illness
#by seeing the rraw_data_questions we can pic importent questions that can help
columns = ['user_id',"Q1",'Q2','Q3','Q5','Q6','Q8','Q10','Q13','Q16','Q21','Q22','Q32','Q34','Q50','Q64','Q65','Q68','Q69','Q76','Q77','Q89','Q93','Q97','Q98','Q33']
mentall_illness_dataset = dataset[columns]

#converting this dataframe into csv file so we can use it anywhere
mentall_illness_dataset.to_csv('Mentall_illness_dataset.csv')

dataset.to_csv('Mentall_illness_dataset')