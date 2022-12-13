import os
import cv2

# %%
# 比較画像作成
# 使用する画像読み込み
filenames_list = os.listdir("comparison_images")

# 幅調整、横に画像を結合
def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)for im in im_list]
    return cv2.hconcat(im_list_resize)

list_img = []

for i in range(0, len(filenames_list)):

    img = cv2.imread(os.path.join("comparison_images" ,filenames_list[i]))

    list_img.append(img)

# 横に画像を結合
im_v_resize = hconcat_resize_min(list_img)

cv2.imwrite("comparison_images.png", im_v_resize)
