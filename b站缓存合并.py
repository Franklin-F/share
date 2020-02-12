import os
import re

path = "C:\\Users\\Franklin\\Desktop\\81148627"  # 手机的文件夹路,径需要修改
file_dir_list = []

for root, dirs, files in os.walk(path):
    if files is not None:
        for file_name in files:
            if file_name== 'audio.m4s' or file_name == 'video.m4s':
                # 将含有视频音频的文件夹进行保存
                number = root[len(path):]
                number = re.findall(r'^\\(\d{1,3})\\',number)[0]
                file_dir_list.append({"dir":root,"number":number})
            break
# print(file_dir_list)
try:
    os.mkdir(newpath := path+"\\all")
except:
    print('已经创建')
for i in file_dir_list:
    cmd_str = "ffmpeg -i {} -i {} -vcodec copy -acodec copy {} -y".format(i.get('dir')+'\\video.m4s',i.get('dir')+'\\audio.m4s',newpath+'\\'+i.get('number')+'.mp4')
    # print(cmd_str)
    os.system(cmd_str)
