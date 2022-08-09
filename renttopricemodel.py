#!/usr/bin/env python
# coding: utf-8

# In[190]:


import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


# In[177]:


Clean = pd.read_pickle('zillowmodelcleandata.pkl')


# In[178]:


#pickle.dump(Clean,open('zillowmodelcleandata.pkl','wb'))


# In[179]:


X = Clean[['zipcode','longitude','latitude','yearBuilt','livingArea','bathrooms','bedrooms','resoFacts.taxAnnualAmount','annualHomeownersInsurance']]


# In[180]:


X = X.rename(columns={'yearBuilt':'yearbuilt','livingArea':'livingarea','resoFacts.taxAnnualAmount': 'annualtax', 'annualHomeownersInsurance': 'annualinsurance'})


# In[181]:


y_ratio = Clean['rentZestimate']/Clean['price']


# In[182]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y_ratio, test_size=0.2, random_state=42)
print("Shape of the complete data set:", X.shape)
print("Shape of the train data set:", X_train.shape)
print("Shape of the test data set:", X_test.shape)


# In[183]:



regr = RandomForestRegressor(max_depth=20, random_state=42)


# In[184]:


analysis = Pipeline(steps=[
         ('scaler', StandardScaler()),
         ('regr',regr)])


# In[185]:


analysis.fit(X_train, y_train)


# In[186]:


y_pred = analysis.predict(X_test)


# In[187]:


r2_score(y_test, y_pred1)


# In[188]:


analysis.named_steps['regr'].feature_importances_


# In[189]:


pickle.dump(analysis,open('analysis.pkl','wb'))


# In[ ]:




