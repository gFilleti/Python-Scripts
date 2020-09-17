#!/usr/bin/env python
# coding: utf-8

# In[148]:


class Expr:
    pass


# In[149]:


class Times (Expr):
    
    def __init__(self, l, r):
        self.l = l
        self.r = r
    
    def __str__(self):
        return "( {} * {} )".format(str(self.l), str(self.r))
    
    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)


# In[150]:


class Plus (Expr):
    
    def __init__(self, l,r):
        self.l = l
        self.r = r
        
    def __str__(self):
        return "( {} + {} )".format(str(self.l), str(self.r))
    
    def eval(self,env):
        return self.l.eval(env) + self.r.eval(env)


# In[151]:


class Const (Expr):
    
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return str(self.val)
    
    def eval(self, env):
        return self.val


# In[152]:


class Var (Expr) :
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def eval(self, name):
        return env[self.name]
        


# In[153]:


e1 = Times(Const(3), Plus(Var("y"), Var("x")))


# In[154]:


e2 = Plus(Times(Const(3), Var('y')), Var("x"))


# In[155]:


e1


# In[156]:


print(e1)


# In[157]:


print(e2)


# In[163]:


env = { "x" : 2, "y" : 4}


# In[159]:


env["x"]


# In[160]:


env["y"]


# In[161]:


e1.eval(env)


# In[162]:


e2.eval(env)


# In[ ]:




