#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyopenms')


# In[2]:


from pyopenms import*


# In[23]:


vaka = AASequence.fromString("VAKA")
fullseq = vaka.getMonoWeight()
mass = vaka.getMonoWeight(Residue.ResidueType.Full, 2)
print(" Mass is", fullseq)
print("#------------------------------------#")
print("The peptide", str(vaka), "consists of the following amino acids:")
for aa in seq:
    print(aa.getName(), ":Its Mass= ", aa.getMonoWeight())





