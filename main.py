from image_processing import downsample_rgb, quantize_rgb, image_properties


import cv2
import numpy as np


# ========== SAMPLING ========== 

# image = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130, 140, 150, 160]
# ])

# image = cv2.imread("images/test.jpg")
# image = cv2.imread("images/test2.png")
import cv2

from image_processing import (
    downsample_rgb,
    quantize_rgb,
    image_properties
)


def main():

    # ======================Load image====================

    # image = np.array([
    #     [10, 20, 30, 40],
    #     [50, 60, 70, 80],
    #     [90, 100, 110, 120],
    #     [130, 140, 150, 160]
    # ])

    # image = cv2.imread("images/test.jpg")
    # image = cv2.imread("images/test2.png")
    image = cv2.imread("images/test3.png")

    if image is None:
        print("Error: image could not be loaded.")
        return

    old_h, old_w, channels = image.shape

    grid = image.tolist()

    print("Original image:")
    print("Width :", old_w)
    print("Height:", old_h)
    print("Channels:", channels)


    # ====================IMAGE SAMPLING======================

    print("\n========== SAMPLING ==========")

    n = 2

    new_grid, new_w, new_h = downsample_rgb(
        grid,
        old_w,
        old_h,
        n
    )

    print("Sampling factor:", n)
    print("Old size:", old_w, "x", old_h)
    print("New size:", new_w, "x", new_h)


    # =====================IMAGE QUANTIZATION=====================

    print("\n========== QUANTIZATION ==========")

    k = 4

    quantized_grid = quantize_rgb(
        grid,
        old_w,
        old_h,
        k
    )

    print("Bit depth:", k)
    print("Number of levels:", 2 ** k)

    print("\nBefore quantization:")

    for row in range(3):
        for col in range(3):

            print(
                f"Pixel [{row}][{col}]:",
                grid[row][col]
            )

    print("\nAfter quantization:")

    for row in range(3):
        for col in range(3):

            print(
                f"Pixel [{row}][{col}]:",
                quantized_grid[row][col]
            )


    # ====================IMAGE PROPERTIES======================

    print("\n========== IMAGE PROPERTIES ==========")

    dpi = 300

    width_inches, height_inches, memory_kb = image_properties(
        image,
        dpi
    )

    print("DPI:", dpi)

    print("Physical width:", width_inches,"inches" )

    print("Physical height:",height_inches,"inches")

    print("Uncompressed memory:",memory_kb,"KB")


if __name__ == "__main__":
    main()




# test3 image

"""

r g b


[
    [
        [145, 193, 168], 
        [92, 161, 155], 
        [79, 155, 158], 
        [69, 142, 149], 
        [41, 126, 131], 
        [49, 134, 140], 
        [79, 150, 145]
    ], 
    
    [
        [150, 197, 175], 
        [112, 178, 164], 
        [100, 170, 170], 
        [94, 161, 158], 
        [68, 142, 134], 
        [60, 138, 138], 
        [79, 153, 154]
    ], 
    
    [
        [131, 195, 183], 
        [129, 192, 183], 
        [110, 180, 171], 
        [107, 174, 163], 
        [101, 167, 151], 
        [87, 155, 147], 
        [87, 158, 149]
    ], 
    
    [
        [125, 192, 198], 
        [150, 206, 209], 
        [113, 181, 171], 
        [113, 174, 163], 
        [116, 176, 159], 
        [96, 166, 149], 
        [96, 167, 150]
    ], 
    
    [
        [152, 202, 217], 
        [135, 202, 197], 
        [97, 174, 166], 
        [94, 172, 171], 
        [125, 187, 178], 
        [102, 171, 153], 
        [102, 169, 154]
    ], 
    
    [
        [136, 188, 211], 
        [95, 182, 194], 
        [84, 173, 180], 
        [89, 177, 185], 
        [119, 189, 192], 
        [106, 176, 159], 
        [104, 169, 154]], 
        [[46, 101, 119], 
        [43, 132, 150], 
        [66, 158, 176], 
        [118, 189, 206], 
        [107, 187, 185], 
        [102, 174, 165], 
        [106, 172, 163]
    ]
]

"""
