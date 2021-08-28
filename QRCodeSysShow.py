from time import *
import platform
import psutil
import qrcode
import matplotlib.pylab as pl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

tt = strftime('%D %H:%M:%S %p')
mc = f"Machine type: {platform.machine ()}"
pr = f"Processor type: {platform.processor ()}"
pl = f"Platform type: {platform.platform ()}"
os = f"Operating system: {platform.system ()}"
rl = f"Operating system release: {platform.release ()}"
ov = f"Operating system version: {platform.version ()}"
fc = f"Number of physical cores: {psutil.cpu_count (logical = False)}"
lc = f"Number of logical cores: {psutil.cpu_count (logical = True)}"
cf = f"Current CPU frequency: {psutil.cpu_freq ().current}"
mf = f"Min CPU frequency: {psutil.cpu_freq ().min}"
xf = f"Max CPU frequency: {psutil.cpu_freq ().max}"
cu = f"Current CPU utilization: {psutil.cpu_percent (interval = 1)}"
cc = f"Current CPU utilization [each]: {psutil.cpu_percent (interval = 1, percpu = True)}"
ri = f"Total RAM installed: {round (psutil.virtual_memory ().total / 1000000000, 2)} GB"
ra = f"Available RAM: {round (psutil.virtual_memory ().available / 1000000000, 2)} GB"
ru = f"Used RAM: {round (psutil.virtual_memory ().used / 1000000000, 2)} GB"
rg = f"RAM usage: {psutil.virtual_memory ().percent}%"

data1 = f"{tt}\n {mc}\n {pr}\n {pl}\n {os}\n {rl}\n {ov}\n {fc}\n {lc}\n "
data2 = f"{cf}\n {mf}\n {xf}\n {cu}\n {cc}\n {ri}\n {ra}\n {ru}\n {rg}\n "

data_tot = data1 + data2

img = qrcode.make(data_tot)


img.save('QRCodeSys.png')
print(data_tot + "\n QRCode created")

img = mpimg.imread('QRCodeSys.png')
image_plot = plt.imshow(img)
plt.show()







