# CS446 Project: Segmentation of Gliomas from brain MRI
by Zhongyi Liu

# Project Description
Gliomas are Brain tumors that involve glial cells in the brain or spinal cord. Gliomas are classified as grades I to IV, where the grades indicate severity. The grades include grade 1 (benign, curable with complete surgical resection), grade II (low grade, undergo surgical resection, radiotherapy/chemotherapy, grade III/IV (high-grade glioma’s), and grade IV (glioblastoma). The task is to identify the location of the tumor, and its classification into three groups; edema (indicates inflammation), enhancing (indicates part of the tumor with active growth), and the necrotic core (dead tissue, generally in the center). 

The task of this course project is to find the location of gliomas as well as identifying the type of gliomas from 3D brain MRI. Detailed description and requirement can be found at https://relate.cs.illinois.edu/course/CS446-fa20/page/project/.

# Data
3D brain MRI dataset can be downloaded from https://uofi.box.com/s/hpzxkjghks7s5z0v9q2j33xzejo9iskb. Please put all downloaded image into the file "FA20_CS446_Project_Data".

# Algorithm
3D U-net was implemented to tackle the challenge since this algorithm has been widely applied in dealing with medical image segmentation. Based on the development of the package MedicalZoo (https://github.com/black0017/MedicalZooPytorch), the 3D U-net algorithm was trained with the provided dataset and dice loss was used as the evaluation metric. The training took place on Colab platform.

# Performance
Achieved dice loss of 68%.

