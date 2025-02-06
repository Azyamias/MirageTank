import resize_image as ri
from PIL import Image
import os
import composite_image as ci
import bright_adjust
import time

start_tme = time.time()
os.makedirs("out", exist_ok=True)
file = os.listdir("surface")
if not file:
    print("文件夹surface中不存在文件")
    exit()
else:
    surface_path = os.path.join("surface", file[0])
    if not surface_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        print(f"文件{surface_path}不是图片格式")
        exit()
    else:
        surface = Image.open(surface_path).convert('L')
file = os.listdir("inter")
if not file:
    print("文件夹inter中不存在文件")
    exit()
else:
    inter_path = os.path.join("inter", file[0])
    if not inter_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        print(f"文件{inter_path}不是图片格式")
        exit()
    else:
        inter = Image.open(inter_path).convert('L')
surface, inter = bright_adjust.bright_adjust(surface, inter)
surface, inter = ri.resize_image(surface, inter)
out = ci.composite_image(surface, inter)
out.save('out/out.png')
end_time = time.time()
print(f"程序执行完毕，用时{int(end_time - start_tme + 0.5)}秒")
