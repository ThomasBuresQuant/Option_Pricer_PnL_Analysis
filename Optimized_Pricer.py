#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from datetime import datetime, timedelta


# In[2]:


class BSM_Pricer:
    def __init__(self,S,K,r,T,q,vol):
        self.S, self.K, self.T, self.r, self.q, self.vol = S, K, T, r, q, vol

    def Dr_Dq_F(self):
        S, K, T, r, q, vol = self.S, self.K, self.T, self.r, self.q, self.vol
        self.Dr=np.exp(-r*T)
        self.Dq=np.exp(-q*T)
        self.F = S*np.exp(r)
        return self.Dr, self.Dq, self.F

    def d1_d2(self):
        S, K, T, r, q, vol = self.S, self.K, self.T, self.r, self.q, self.vol
        self.d1=(np.log(S/K)+(r-q+0.5*vol**2)*T)/(vol*np.sqrt(T))
        self.d2=self.d1-vol*np.sqrt(T)

        if self.d2-self.d1-vol*np.sqrt(T)<1e-10:
            print('The formulas for d2 and d1 are correct.')
        else:
            print('The formulas for d2 and d1 are incorrect.')  
        return self.d1, self.d2

    def Underlying_BSM(self):
        S, K, T, r, q, vol = self.S, self.K, self.T, self.r, self.q, self.vol
        Z=np.random.normal(0,1)
        self.St = S*np.exp((r-q-0.5*vol**2)*T+vol*np.sqrt(T)*Z)
        return self.St

    def call_put(self):
        S, K, T, r, q, vol = self.S, self.K, self.T, self.r, self.q, self.vol
        N=norm.cdf

        if not hasattr(self, "Dq") or not hasattr(self, "Dr"):
            self.Dr_Dq_F()
        if not hasattr(self, "d1") or not hasattr(self, "d2"):
            self.d1_d2()
            
        self.call=S*self.Dq*N(self.d1)-K*self.Dr*N(self.d2)
        self.put=K*self.Dr*N(-self.d2)-S*self.Dq*N(-self.d1)

        if (self.call-self.put)-(S*self.Dq-K*self.Dr)<1e-10:
            print('The put call parity is respected.')
        else:
            print('The put call parity is violated.')
        return self.call,self.put

    def greeks(self):
        S, K, T, r, q, vol = self.S, self.K, self.T, self.r, self.q, self.vol
        phi=norm.pdf
        N=norm.cdf

        if not hasattr(self, "Dq") or not hasattr(self, "Dr"):
            self.Dr_Dq_F()
        if not hasattr(self, "d1") or not hasattr(self, "d2"):
            self.d1_d2()        
        
        self.delta_c=self.Dq*N(self.d1)
        self.delta_p=self.Dq*(N(self.d1)-1)
        self.gamma=(self.Dq*phi(self.d1))/(S*vol*np.sqrt(T))
        self.vega=S*self.Dq*phi(self.d1)*np.sqrt(T)
        self.theta_c=-((S*self.Dq*phi(self.d1)*vol)/(2*np.sqrt(T)))-r*K*self.Dr*N(self.d2)+q*S*self.Dq*N(self.d1)
        self.theta_p=-((S*self.Dq*phi(self.d1)*vol)/(2*np.sqrt(T)))+r*K*self.Dr*N(-self.d2)-q*S*self.Dq*N(-self.d1)
        self.rho_c=K*T*self.Dr*N(self.d2)
        self.rho_p=-K*T*self.Dr*N(-self.d2)
        self.dividend_rho_c=-T*S*self.Dq*N(self.d1)
        self.dividend_rho_p=T*S*self.Dq*N(-self.d1)
        return self.delta_c,self.delta_p,self.gamma,self.vega,self.theta_c,self.theta_p,self.rho_c,self.rho_p,self.dividend_rho_c,self.dividend_rho_p

    def run():
        self.Dr_Dq_F()
        self.d1_d2()
        self.Underlying_BSM()
        self.call_put()
        self.greeks()


# In[3]:


result = BSM_Pricer(100, 110, 0.05, 1, 0, 0.2)
result.Dr_Dq_F()
result.d1_d2()
result.Underlying_BSM()
result.call_put()
result.greeks()

print('The futur price of the underlying is {}$ !'.format(round(result.St,2)))
print('The value of the call is {} and the value of the put is {} !'.format(round(result.call,2),round(result.put,2)))
print('The greeks value for delta_c,delta_p,gamma,vega,theta_c,theta_p,rho_c,rho_p,dividend_rho_c,dividend_rho_p are {}, {}, {}, {}, {}, {}, {}, {}, {}, {} !'.format(round(result.delta_c,2),round(result.delta_p,2),round(result.gamma,2),round(result.vega,2),round(result.theta_c,2),round(result.theta_p,2),round(result.rho_c,2),round(result.rho_p,2),round(result.dividend_rho_c,2),round(result.dividend_rho_p,2)))


# In[50]:


portfolio_0 = BSM_Pricer(100, 101, 0.275, 0.055, 0, 0.2)
portfolio_0.Underlying_BSM()
portfolio_0.call_put()
portfolio_0.greeks()

portfolio = [BSM_Pricer(98, 101, 0.255, 0.053, 0, 0.21),
    BSM_Pricer(102, 101, 0.285, 0.057, 0, 0.19)
]
for option in portfolio:
    option.Underlying_BSM()
    option.call_put()
    option.greeks()
    print('The futur price of the underlying is {}$ !'.format(round(option.St,2)))
    print('The value of the call is {} and the value of the put is {} !'.format(round(option.call,2),round(option.put,2)))
    print('The greeks value for delta_c,delta_p,gamma,vega,theta_c,theta_p,rho_c,rho_p,dividend_rho_c,dividend_rho_p are {}, {}, {}, {}, {}, {}, {}, {}, {}, {} !'.format(round(option.delta_c,2),round(option.delta_p,2),round(option.gamma,2),round(option.vega,2),round(option.theta_c,2),round(option.theta_p,2),round(option.rho_c,2),round(option.rho_p,2),round(option.dividend_rho_c,2),round(option.dividend_rho_p,2)))


# In[52]:


class greeks_effect:
    def __init__ (self,option,portfolio_0):
        self.dS = option.S - portfolio_0.S
        self.dvol = option.vol - portfolio_0.vol
        self.dT = option.T - portfolio_0.T
        self.dr = option.r - portfolio_0.r
        self.dcall = option.call - portfolio_0.call
        
        self.delta_c = portfolio_0.delta_c
        self.gamma = portfolio_0.gamma
        self.vega = portfolio_0.vega
        self.theta_c = portfolio_0.theta_c
        self.rho_c = portfolio_0.rho_c

    def d_option(self):
        self.dV_call_predict = self.delta_c*self.dS + (1/2)*self.gamma*(self.dS**2)+self.vega*self.dvol+self.theta_c*self.dT+self.rho_c*self.dr
        self.dV_call_reel = self.dcall
        return self.dV_call_predict, self.dV_call_reel


# In[73]:


results = []

for option in portfolio:
    greeks_effect_result=greeks_effect(option,portfolio_0)
    greeks_effect_result.d_option()
    print('The predicted change in price is {} and the acutal change in price is {}.'.format(round(greeks_effect_result.dV_call_predict,3),round(greeks_effect_result.dV_call_reel,3)))
    
    results.append([option.S,
        greeks_effect_result.dV_call_predict,
        greeks_effect_result.dV_call_reel
    ])
    
    df_model=pd.DataFrame(result, columns=['S','dV_call_predict','dV_call_reel'])
    df_model['error'] = (abs((greeks_effect_result.dV_call_predict - greeks_effect_result.dV_call_reel))/abs(greeks_effect_result.dV_call_reel))*100
    print('The % of error from the model is : {}%'.format(round(Error,2)))

max_error = df_model['error'].mean()
print('The maximum error of the model is : {}'.format(max_error))


# In[1]:


# mean_error = df_model['error'].mean(skipna=True)
# max_error = df_model['error'].max(skipna=True)

# print(f"\nAverage error = {mean_error:.2f}%")
# print(f"Maximum error = {max_error:.2f}%")


# In[ ]:





# In[ ]:





# In[ ]:




