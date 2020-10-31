* [常用指令](#常用指令：)
    * [讀取圖片：`cv2.imread(path, flag)`](#讀取圖片：cv2.imread(path,-flag))
    * [顯示圖片：`cv2.imshow(window_name, image)`](#顯示圖片：cv2.imshow(window_name,-image))
    * [寫入圖片：`cv2.imwrite(filename, image)`](#寫入圖片：cv2.imwrite(filename,-image))
    * [視窗：`cv2.namedWindow(window_name, flag)` ](#視窗：cv2.namedWindow(window_name,-flag))

## 安裝測試
Raspberry Pi 安裝：`armv7l`
```sh
sudo apt install python-opencv
sudo apt install python3-opencv
```
Ubuntu MATE 安裝：`aarch64`  
原文連結：https://github.com/huzz/OpenCV-aarch64

```python
import cv2
```

## 常用指令：
### 讀取圖片：`cv2.imread(path, flag)`
`cv2.IMREAD_COLOR`：預設值，讀取 RGB 三個 channels 的彩色圖片  
`cv2.IMREAD_GRAYSCALE`：以灰階的格式來讀取圖片  
`cv2.IMREAD_UNCHANGED`：讀取圖片中所有的 channels，包含透明度的 channel

```python
img = cv2.imread('image.jpg')                               # 讀取圖檔
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)    # 以灰階的方式讀取圖檔
img.shape                                                   # 查看解析度、channel
```
詳細：https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/

---
### 顯示圖片：`cv2.imshow(window_name, image)`
```python
# 顯示圖片
cv2.imshow('My Image', img)
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
```
詳細：https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/?ref=lbp

---
### 寫入圖片：`cv2.imwrite(filename, image)`
```python
cv2.imwrite('output.jpg', img)
# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('output.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('output.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])
```
詳細：https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method/?ref=lbp

---
### 視窗：`cv2.namedWindow(window_name, flag)` 
flag 預設值：`cv2.WINDOW_AUTOSIZE + cv2.WINDOW_KEEPRATIO + cv2.WINDOW_GUI_EXPANDED`   
`cv2.WINDOW_NORMAL`：窗口大小可改变。  
`cv2.WINDOW_AUTOSIZE`：窗口大小不可改变。  
`cv2.WINDOW_FREERATIO`：自适应比例。  
`cv2.WINDOW_KEEPRATIO`：保持比例。  
```python
# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)
cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 參考網址：
[Python 與 OpenCV 基本讀取、顯示與儲存圖片教學](https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/)