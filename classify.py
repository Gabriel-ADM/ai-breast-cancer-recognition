import pandas as pd
import os
import shutil

def extract_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def create_txt(folder, file_name, content):
    file_path = os.path.join(folder, file_name)
    
    with open(file_path, 'w') as file:
        file.write(content)

def move_image_folder(image_path, destination_folder):
    new_path = os.path.join(destination_folder, os.path.basename(image_path))
    shutil.move(image_path, new_path)

cancer_csv = extract_csv('train.csv')

train_labels_path = r'data\labels\train'
val_labels_path = r'data\labels\val'
train_imgs_path = r'data\images\train'
val_imgs_path = r'data\images\val'

positive_case_content = '0 0.500000 0.500000 1.000000 1.000000\n'
negative_content = ''

for index, diagnosis in cancer_csv.sample(frac=1).reset_index(drop=False).iterrows():
    image_name = f"{diagnosis['patient_id']}@{diagnosis['image_id']}"
    diagnosis_result = diagnosis['cancer']
    
    if index < 1000:
        if diagnosis_result == 1:
            move_image_folder(f'{image_name}.png', train_imgs_path)
            create_txt(train_labels_path, f"{image_name}.txt",positive_case_content)
        else:
            move_image_folder(f'{image_name}.png', train_imgs_path)
            create_txt(train_labels_path, f"{image_name}.txt",negative_content)
    else:
        if diagnosis_result == 1:
            move_image_folder(f'{image_name}.png', val_imgs_path)
            create_txt(val_labels_path, f"{image_name}.txt", positive_case_content)
        else:
            move_image_folder(f'{image_name}.png', val_imgs_path)
            create_txt(val_labels_path, f"{image_name}.txt",negative_content)
