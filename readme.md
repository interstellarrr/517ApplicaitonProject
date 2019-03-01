CSE 517a Application Project Milestone 1
=========================================
- **Topic** : Distance To Fire Points - Linear Models

- **Team Members** : Yannan Gao,Weiran Liu,Minzi Zhang,Shaohua Zhang

# Table of Contents

## 1.Dataset Introduction
### >1.1 General Introduction
### >1.2 Statistical description
## 2. Data Visualization
## 3. Testing Models
### >3.1 Data Processing
#### >>3.1.1 Data Basic Processing
#### >>3.1.2 One-hot Encoding
#### >>3.1.3 Generating polynomial features
### >3.2 Regularizer for Ridge Regression
### >3.3 Comparing Different Linear Models
## 4. Tnterpreting of Data
----------

## **1.Dataset Introduction**
### **1.1 General Introduction**
- The dataset is from Kaggle distance-to-fire-points task

- Our task is to predict the distance to fire points for inholdings or neighboring lands that are outside their immediate jurisdiction, based on the data from basic descriptive information including inventory data.

- The dataset has in total 7438 labeled samples

- The data fields are:

Name | Meaning | Type
-----|---------|--------
Elevation | Elevation in meters | 
Aspect | Aspect in degrees azimuth | 
Slope | Slope in degrees | 
Horizontal_Distance_To_Hydrology | Horz Dist to nearest surface water features | 
Vertical_Distance_To_Hydrology | Vert Dist to nearest surface water features | 
Horizontal_Distance_To_Roadways | Horz Dist to nearest roadway | 
Hillshade_9am | Hillshade index at 9am, summer solstice | 
Hillshade_Noon | Hillshade index at noon, summer soltice | 
Hillshade_3pm | Hillshade index at 3pm, summer solstice | 
Soil_Type | based on the USFS Ecological Landtype Units (ELUs) for this study area. The first digit refers to the climatic zone, the second refers to the geologic. The third and fourth ELU digits are unique to the mapping unit and have no special meaning to the climatic or geologic zones.| 
Horizontal_Distance_To_Fire_Points | Horz Dist to nearest wildfire ignition |
--------
### **1.2 Statistical description**
- This part mainly contains statistical analysis towards features
- Here lists analysis of first three features:

Statistics | Elevation  |   Aspect    |    Slope 
---|------------|-------------|---------
count| 7438.000000 | 7438.000000 | 7438.000000
mean | 3237.099758 |  194.653536 | 13.145873
std  | 99.783831   |  115.218272 |  6.444191
min  | 2947.000000 |   0.000000  |  0.000000
25%  | 3167.000000 |   90.000000 |  8.000000
50%  | 3229.000000 |  199.500000 |  13.000000
75%  | 3309.000000 |  309.000000 |  17.000000
max  | 3489.000000 |  359.000000 |  43.000000

---

## **2.Data Visualization**
- Here is the correlation map among variables
![correlation](heatmap.png)
From above, some variables are relatively highly correlated, like Hillshade_9am with Hillshade_3pm,Hillshade_9am with aspect, Hillshade_3pm with aspect and so on.
## **3.Testing Models**
### **3.1 Data Processing**
#### **3.1.1 Basic Preprocessing**
 We used some basic data preprocseeing methods including:

- Quantify(Encoding descriptive features into dummy variable)
- Normalization: centering and unification, for continuous data only
- Split data into training and testing set
- We have 7438 samples in total, and we use 7438 of them as training set and the other 11157 as test set.

- Fill missing data (by taking average, on training and test set separately)
- Add 1 more bias dimension

#### **3.1.2 One-hot Encoding**
In order to test the proformance of different models with continuous and discrete features, we did 2 additional attempts:

- Separate the training and test set into:

    i) Training set with only continuous features

    ii) Training set with only discrete features

    iii) Test set with only continuous features

    iv) Test set with only discrete features
- One-hot encoding: Changing all continuous features into discrete features by one-hot encoding. 
>>Sample will have 203 dimensional all-discrete features after encoding instead of orginal 9.
#### **3.1.3 Generating polynomial features**
In order to add complexity to the model, we are considering nonlinear features of the input data by using polynomial features, which can get features’ high-order and interaction terms. 

- After testing, we decided to transform features into forth-order space, which could avoid overfitting.
>>Sample will have 715 dimensional all-discrete features after encoding instead of 203 (after on-hot encoding).

### **3.2 Regularizer for Ridge Regression**

We used telescope search to find the optimal regularizer coefficient for rigde regression. The accuracies for 10-fold validation and on test set are (using all original features):

In the next part, we will set 
> regularizer coefficient = 0.5 

when comparing different models.

### **3.3 Comparing Different Linear Models**

We tested the following models:

- OLS
- Ridge regression with square loss
- Linear SVM
- Logistic regression

And we collected proformance of these models in follwing cases:

- with all original features
- with only continuous features
- with only discrete features
- with only one-hot encoded discrete features
- with forth-order transform discrete features

It suggests that the linear model, Ridge regression with square loss, is the best among these methods based on our data.
