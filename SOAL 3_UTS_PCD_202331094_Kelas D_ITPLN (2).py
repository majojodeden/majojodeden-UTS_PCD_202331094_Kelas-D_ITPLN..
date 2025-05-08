#!/usr/bin/env python
# coding: utf-8

#  ## 202331094_Maajid Dhirottsaha
#  

# ## gambar grayscale

# In[6]:


import cv2
import matplotlib.pyplot as plt

# Baca gambar berwarna
img = cv2.imread('photo5.jpeg')  # gunakan nama file yang sesuai

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tampilkan gambar asli dan grayscale
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Gambar Grayscale")
plt.axis("off")

plt.tight_layout()
plt.show()


# In[8]:


import cv2
import matplotlib.pyplot as plt

# Baca gambar berwarna
img = cv2.imread('photo5.jpeg')  # gunakan nama file yang sesuai

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tampilkan gambar asli dan grayscale
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Gambar Grayscale")
plt.axis("off")

plt.tight_layout()
plt.show()


# ## Maajid Dhirottsaha_202331094
# 

# ## Gambar Gray yang Dicerahkan dan Gambar gray Diperkontras

# In[10]:


import cv2
import matplotlib.pyplot as plt
import numpy as np

# Baca gambar dan ubah ke grayscale
img = cv2.imread('photo5.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -----------------------------
# Tingkatkan KECERAHAN
# -----------------------------
# Tambahkan nilai tetap (misalnya 50) ke seluruh piksel
bright = cv2.add(gray, 50)

# -----------------------------
# Tingkatkan KONTRAS
# -----------------------------
# Konversi ke float agar bisa dikalikan
contrast = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)

# -----------------------------
# Tampilkan hasil
# -----------------------------
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title("Gambar Gray")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(bright, cmap='gray')
plt.title("Gambar Gray yang Dicerahkan")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(contrast, cmap='gray')
plt.title("Gambar Gray yang Diperkontras")
plt.axis("off")

plt.tight_layout()
plt.show()


# ## Maajid Dhirottsaha_202331094

# ## Gambar Gray yang Dicerahkan dan Diperkontras

# In[12]:


import cv2
import matplotlib.pyplot as plt

# Baca gambar dan ubah ke grayscale
img = cv2.imread('photo5.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gabungkan peningkatan kecerahan dan kontras
# alpha = kontras, beta = kecerahan
enhanced = cv2.convertScaleAbs(gray, alpha=1.5, beta=50)

# Tampilkan hasil
plt.figure(figsize=(6, 6))
plt.imshow(enhanced, cmap='gray')
plt.title("Gambar Gray yang Dicerahkan dan Diperkontras")
plt.axis("off")
plt.show()


# ## 202331094_Maajid Dhirottsaha

# In[ ]:




