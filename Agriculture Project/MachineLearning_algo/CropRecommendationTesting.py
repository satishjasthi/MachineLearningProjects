import pandas as pd
import pickle
import numpy as np

class CropRecommendationTesting:
    def __init__(self,Saved_model_name):
        self.Saved_model_name = Saved_model_name

    def test(self):
        model = pickle.load(open(self.Saved_model_name, 'rb'))

        #testing for apple class
        print('Apple class testing ......')

        # test case 1
        test_case1 = [20,134,199,22,92,5,112]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'apple': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,20,195,21,90,5,100]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'apple': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [40,145,205,24,94,6,124]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'apple': print('Test case 3 sucess')
        else:print('Test case 1 Fail')


        #testing for Banana class
        print('Banana class testing ......')

        # test case 1
        test_case1 = [100,82,50,27,80,5,104]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'banana': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [80,70,45,25,75,5,90]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'banana': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [120,95,55,29,84,6,119]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'banana': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for blackgram class
        print('blackgram class testing ......')

        # test case 1
        test_case1 = [40,67,19,29,65,7,67]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'blackgram': print('Test case 1 sucess')
        else:print('Test case 3 Fail')

        # test case 2
        test_case2 = [20,55,15,25,60,6,60]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'blackgram': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [45,55,18,28,62,7,74]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'blackgram': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for chickpea class
        print('chickpea class testing ......')

        # test case 1
        test_case1 = [40,67,79,18,16,7,80]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'chickpea': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [20,55,75,17,14,5,65]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'chickpea': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [60,80,85,21,19,8,94]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'chickpea': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for coconut class
        print('coconut class testing ......')

        # test case 1
        test_case1 = [21,16,30,27,94,5,175]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'coconut': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,5,25,25,90,5,131]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'coconut': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [40,30,35,29,99,6,225]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'coconut': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for coffee class
        print('coffee class testing ......')

        # test case 1
        test_case1 = [101,28,29,25,58,6,158]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'coffee': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [80,15,25,23,50,6,115]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'coffee': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [120,40,35,27,69,7,199]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'coffee': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for cotton class
        print('cotton class testing ......')

        # test case 1
        test_case1 = [117,46,19,23,79,6,80]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'cotton': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [100,35,15,22,75,5,60]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'cotton': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [140,60,25,25,84,7,99]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'cotton': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for grapes class
        print('grapes class testing ......')

        # test case 1
        test_case1 = [23,132,200,23,81,6,69]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'grapes': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,120,195,8,80,5,65]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'grapes': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [40,145,205,41,83,6,74]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'grapes': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for jute class
        print('jute class testing ......')

        # test case 1
        test_case1 = [78,46,39,24,79,6,174]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'jute': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [60,35,35,23,70.88,6,150]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'jute': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [100,60,45,26,89,7,199]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'jute': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for kidneybeans class
        print('kidneybeans class testing ......')

        # test case 1
        test_case1 = [20,67,20,20,21,5,105]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'kidneybeans': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,55,15,15,18,5,60]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'kidneybeans': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [40,80,25,24,24,6,149]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'kidneybeans': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for lentil class
        print('lentil class testing ......')

        # test case 1
        test_case1 = [18,68,19,24,64,6,45]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'lentil': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,55,15,18,60,5,35]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'lentil': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [40,80,25,29,69,7,54]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'lentil': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for maize class
        print('maize class testing ......')

        # test case 1
        test_case1 = [100,60,25,26,74,7,109]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'maize': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [60,35,15,18,55,5,60]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'maize': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [77,48,19,22,65,6,84]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'maize': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for mango class
        print('mango class testing ......')

        # test case 1
        test_case1 = [40,40,35,35,54,6,100]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'mango': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,15,25,27,45,4,89]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'mango': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [20,27,29,31,50,5,94]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'mango': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for mothbeans class
        print('mothbeans class testing ......')

        # test case 1
        test_case1 = [40,60,25,32,64,9,74]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'mothbeans': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,35,15,24,40,3,30.9]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'mothbeans': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [21,48,20,28,53,6,51]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'mothbeans': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for mungbean class
        print('mungbean class testing ......')

        # test case 1
        test_case1 = [40,60,25,29,90,7,59]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'mungbean': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,35,15,27,80,6,36]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'mungbean': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [20,47,19,28,85,6,48]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'mungbean': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for muskmelon class
        print('muskmelon class testing ......')

        # test case 1
        test_case1 = [120,30,55,29,4,6,29]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'muskmelon': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [80,5,45,27,90,6,20]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'muskmelon': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [120,30,55,29,94,6,29]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'muskmelon': print('Test case 3 sucess')
        else:print('Test case 3 Fail')


        #testing for orange class
        print('orange class testing ......')

        # test case 1
        test_case1 = [40,30,15,34,94,8,119]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'orange': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,5,5,10,90,6,100]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'orange': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [19,16,10,22,92,7,110]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'orange': print('Test case 3 sucess')
        else:print('Test case 1 Fail')


        #testing for papaya class
        print('papaya class testing ......')

        # test case 1
        test_case1 = [70,70,55,43,94,6,248]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'papaya': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [31,46,45,24,91,6.5,41]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'papaya': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [49,59,50,33,92,6,142]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'papaya': print('Test case 3 sucess')
        else:print('Test case 1 Fail')


        #testing for pigeonpeas class
        print('pigeonpeas class testing ......')

        # test case 1
        test_case1 = [40,80,25,36,69,7,198]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'pigeonpeas': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,55,15,18,30,4,90]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'pigeonpeas': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [20,67,20,27,48,5,149]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'pigeonpeas': print('Test case 3 sucess')
        else:print('Test case 1 Fail')


        #testing for pomegranate class
        print('pomegranate class testing ......')

        # test case 1
        test_case1 = [40,30,45,24,95,7,112]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'pomegranate': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [0,5,35,18,85,5,102]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'pomegranate': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [18,18,40,21,90,6,107]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'pomegranate': print('Test case 3 sucess')
        else:print('Test case 1 Fail')


        #testing for rice class
        print('rice class testing ......')

        # test case 1
        test_case1 = [99,60,45,26,84,7,298]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'rice': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [60,35,35,20,80,5,182]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'rice': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [79,47,39,23,82,6,236]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'rice': print('Test case 3 sucess')
        else:print('Test case 1 Fail')


        #testing for watermelon class
        print('watermelon class testing ......')

        # test case 1
        test_case1 = [120,30,55,26,89,6,59]   
        result = model.predict(np.array(test_case1).reshape(1,7))
        if result[0] == 'watermelon': print('Test case 1 sucess')
        else:print('Test case 1 Fail')

        # test case 2
        test_case2 = [80,5,45,24,80,6,40]   
        result = model.predict(np.array(test_case2).reshape(1,7))
        if result[0] == 'watermelon': print('Test case 2 sucess')
        else:print('Test case 2 Fail')

        # test case 3
        test_case3 = [99,17,50,25,85,6,50]   
        result = model.predict(np.array(test_case3).reshape(1,7))
        if result[0] == 'watermelon': print('Test case 3 sucess')
        else:print('Test case 1 Fail')


        
            

if __name__ == "__main__":
    model = CropRecommendationTesting('Crop_recommendation_model.sav')

    model.test()