import os
import shutil
import mimetypes
import magic

def create_folders(store):
    os.makedirs(f'{store}\\Application\\Don\'t know', exist_ok=True)
    os.makedirs(f'{store}\\Audio\\Don\'t know', exist_ok=True)
    os.makedirs(f'{store}\\Image\\Don\'t know', exist_ok=True)
    os.makedirs(f'{store}\\Inode\\Don\'t know', exist_ok=True)
    os.makedirs(f'{store}\\Text\\Don\'t know', exist_ok=True)
    os.makedirs(f'{store}\\Video\\Don\'t know', exist_ok=True)
    os.makedirs(f'{store}\\Don\'t know\\Don\'t know', exist_ok=True)

def get_all_file(root):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if '.' not in name:
                all_file.append(os.path.join(path, name))

def copy_da(file_location,file_variant,store):
    
    file_name=file_location.split('\\')[-1]

    if file_variant.split('/')[0] == 'image':
        if file_variant.split('/')[1] == 'jpeg':
            shutil.copy2(file_location, f"{store}\\Image\\{file_name}.jpg")
        elif file_variant.split('/')[1] == 'png':
            shutil.copy2(file_location, f"{store}\\Image\\{file_name}.png")
        elif file_variant.split('/')[1] == 'tiff':
            shutil.copy2(file_location, f"{store}\\Image\\{file_name}.tiff")
        elif file_variant.split('/')[1] == 'webp':
            shutil.copy2(file_location, f"{store}\\Image\\{file_name}.webp")
        else:
            shutil.copy2(file_location, f"{store}\\Image\\{file_name}.jpg")

    elif file_variant.split('/')[0] == 'text':
        if file_variant.split('/')[1] == 'plain':
            shutil.copy2(file_location, f"{store}\\Text\\{file_name}.vcf")
        elif file_variant.split('/')[1] == 'xml':
            shutil.copy2(file_location, f"{store}\\Text\\{file_name}.xml")
        else :
            shutil.copy2(file_location, f"{store}\\Text\\{file_name}.jpg")


    elif file_variant.split('/')[0] == 'application':
        if file_variant.split('/')[1] == 'font-sfnt':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.ttf")
        elif file_variant.split('/')[1] == 'msword':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.doc")
        elif file_variant.split('/')[1] == 'octet-stream':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.lha")
        elif file_variant.split('/')[1] == 'pdf':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.pdf")
        elif file_variant.split('/')[1] == 'vnd.ms-powerpoint':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.ppt")
        elif file_variant.split('/')[1] == 'vnd.openxmlformats-officedocument.presentationml.presentation':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.pptx")
        elif file_variant.split('/')[1] == 'vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.xlsx")
        elif file_variant.split('/')[1] == 'vnd.openxmlformats-officedocument.wordprocessingml.document':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.docx")
        elif file_variant.split('/')[1] == 'x-gzip':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.gz")
        elif file_variant.split('/')[1] == 'x-tar':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.tar")
        elif file_variant.split('/')[1] == 'zip':
            shutil.copy2(file_location, f"{store}\\Application\\{file_name}.zip")
        else:
            shutil.copy2(file_location, f"{store}\\Application\\Don't know\\{file_name}")


    elif file_variant.split('/')[0] == 'audio':
        if file_variant.split('/')[1] == 'mpeg':
            shutil.copy2(file_location, f"{store}\\Audio\\{file_name}.mp3")
        elif file_variant.split('/')[1] == 'ogg':
            shutil.copy2(file_location, f"{store}\\Audio\\{file_name}.oga")
        else:
            shutil.copy2(file_location, f"{store}\\Audio\\Don't know\\{file_name}")


    elif file_variant.split('/')[0] == 'video':
        if file_variant.split('/')[1] == 'mp4':
            shutil.copy2(file_location, f"{store}\\Video\\{file_name}.mp4")
        elif file_variant.split('/')[1] == 'quicktime':
            shutil.copy2(file_location, f"{store}\\Video\\{file_name}.mov")
        else:
            shutil.copy2(file_location, f"{store}\\Video\\Don't know\\{file_name}")
    else:
        shutil.copy2(file_location, f"{store}\\Don't know\\{file_name}")

all_file=[]
root=input("Enter the Itunes backup location :")
store=input("Enter the location to store your data :")
get_all_file(root)
create_folders(store)

file=0
for x in all_file:
    z=str(magic.from_file(x,mime=True)).strip()
    print(f"{file} : {z}")
    copy_da(x,z,store)
    file+=1


# https://gist.github.com/JCloudYu/66616fbc15e64e7bf941f4bf80bd4173
# https://www.iana.org/assignments/media-types/media-types.xhtml

# application/font-sfnt -- ttf
# application/msword  -- doc
# application/octet-stream -- lha
# application/pdf -- pdf
# application/vnd.ms-powerpoint -- ppt
# application/vnd.openxmlformats-officedocument.presentationml.presentation -- pptx
# application/vnd.openxmlformats-officedocument.spreadsheetml.sheet  -- xlsx
# application/vnd.openxmlformats-officedocument.wordprocessingml.document -- docx
# application/x-gzip  -- gz
# application/x-sqlite3 -- dont'know
# application/x-tar -- tar 
# application/zip -- zip 
# audio/mpeg  -- mp3
# audio/ogg -- oga
# audio/x-hx-aac-adts -- don't know
# audio/x-m4a -- don't know
# image/jpeg -- jpg
# image/png -- png
# image/tiff -- tiff
# image/webp -- webp
# inode/x-empty -- don't know
# text/plain -- log
# text/vcard -- vcf
# text/xml -- xml
# video/mp4 -- mp4
# video/quicktime -- mov