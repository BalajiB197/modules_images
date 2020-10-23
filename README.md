# Modules images

Project which helps in resizing, cropping and conversion of images using PIL library.

## Module1: jpg to png converted [ j2p ]
converts jpg images to png, which accepts image folder path and converts in a bulk all the images in that folder from jpg to png.  
CMD1 -> python my-app j2p './images/'  
CMD2 -> python __main__.py j2p './images/'


## Module2: png to jpg converted [ p2j ]
converts png images to jpg, which accepts image folder path and converts in a bulk all the images in that folder from png to jpg.  
CMD1 -> python my-app p2j './images/'  
CMD2 -> python __main__.py p2j './images/'

## Module3: resize image using __percentage__ value [res_p]
resize both png and jpg images to the given percent, which accepts image folder path and resizes in a bulk all the images in that folder to the specified percentage value.  
CMD1 -> python my-app res_p './images/' 0.5
CMD2 -> python __main__.py res_p './images/' 0.5  


## Module4: resize image by given __width__ value [res_w]
resize both png and jpg images to the given width, which accepts image folder path and resizes in a bulk all the images in that folder to the specified width value.   
CMD1 -> python my-app res_w './images/' --new_percent 400  
CMD2 -> python __main__.py res_w './images/' --new_percent 400  

## Module5: resize image by given __height__ value [res_w]
resize both png and jpg images to the given height, which accepts image folder path and resizes in a bulk all the images in that folder to the specified height value.   
CMD1 -> python my-app res_h './images/' --new_percent 400  
CMD2 -> python __main__.py res_h './images/' --new_percent 400 

## Module5: crop image by given __pixel__ value [crp_px]
crop centre both png and jpg images to the given pixel value, which accepts image folder path and crops in a bulk all the images in that folder to the specified pixel value.   
CMD1 -> python my-app cro_px './images/' --new_percent 224  
CMD2 -> python __main__.py cro_px './images/' --new_percent 224

##### Also accepts the percentage:  
CMD3 -> python my-app cro_px './images/' --new_percent 0.4 
CMD4 -> python __main__.py cro_px './images/' --new_percent 0.4
##### default is 0.5  
CMD5 -> python __main__.py crp_px './images/'

## Module6: helps in converting the folder scripts to one single folder
  
python -m zipfile -c my-app __main__.py   modules.py  
python -m zipfile -l my-app 

Reference:  
https://www.programiz.com/python-programming/methods/built-in/compile

