
import os
import zipfile
import shutil
import patoolib

dir_list = os.listdir()

for file in dir_list:
    # Finding all .zip files
    if(file.endswith(".zip")):
        if(os.path.isdir('zipped-folders')==False):
            os.mkdir('zipped-folders')

        # Copying the zip file inside folder to extarct
        shutil.copy(file, 'zipped-folders')

        zip_name = os.getcwd() + "\\" +str(file)

        # extracting zip to rar
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall('.\\zipped-folders\\rars')

        # temp_rars_location = os.getcwd() + "\\zipped-folders\\rars\\"

        # for rar_file in os.listdir(temp_rars_location):
        #     shutil.copy(temp_rars_location + "\\" + rar_file , os.getcwd() + "\\zipped-folders\\rars")


        for rar_name in os.listdir('.\\zipped-folders\\rars'):
            print(rar_name)
            if(rar_name.endswith(".rar")):
                rar_dir = os.getcwd() + "\\zipped-folders\\rars\\" + rar_name
                final_output_pdfs_dir = os.getcwd() + "\\zipped-folders"
                # extracting rar file
                patoolib.extract_archive(rar_dir, outdir=final_output_pdfs_dir)

        shutil.rmtree(os.getcwd() + "\\zipped-folders\\rars\\")
        os.remove(os.getcwd() + "\\zipped-folders\\"+file)


    # Finding all .rar files
    elif(file.endswith(".rar")):
        if(os.path.isdir('rar-folders')==False):
            os.mkdir('rar-folders')

        # Copying the zip file inside folder to extarct
        shutil.copy(file, 'rar-folders')

        final_output_pdfs = os.getcwd() + "\\rar-folders"

        rar_dir = os.getcwd() + "\\rar-folders\\" + file
        
        # extracting rar file
        patoolib.extract_archive(rar_dir, outdir=final_output_pdfs)

        os.remove(os.getcwd() + "\\rar-folders\\"+file)





# Appending .pdf at end if not present
zip_dir = os.getcwd() + "\\zipped-folders\\"

for file in os.listdir(zip_dir):
    if(len(file.split('.'))==1):

        source_name = zip_dir + "\\" + file
        target_name = source_name + ".pdf"

        os.rename(source_name, target_name)


# Appending .pdf at end if not present
rar_dir = os.getcwd() + "\\rar-folders\\"

for file in os.listdir(rar_dir):
    if(len(file.split('.'))==1):

        source_name = rar_dir + "\\" + file
        target_name = source_name + ".pdf"

        os.rename(source_name, target_name)
        





    

            

