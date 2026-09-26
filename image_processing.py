def downsample_rgb(grid, old_w, old_h, n):

    if n <= 0:
        raise ValueError("n must be greater than 0")

    new_grid = []

    for row in range(0, old_h, n):

        new_row = []

        for col in range(0, old_w, n):

            pixel = grid[row][col]

            new_row.append(pixel)

        new_grid.append(new_row)

    new_h = len(new_grid)
    new_w = len(new_grid[0])

    return new_grid, new_w, new_h


def quantize_rgb(grid, old_w, old_h, k):

    if k <= 0 or k >= 8:
        raise ValueError("k must be between 1 and 7")

    levels = 2 ** k

    new_grid = []

    for row in range(old_h):

        new_row = []

        for col in range(old_w):

            pixel = grid[row][col]

            new_pixel = []

            for channel in range(3):

                value = pixel[channel]

                # 8-bit -> k-bit
                level = int(
                    value * (levels - 1) / 255
                )

                # k-bit -> [0,255]
                quantized_value = int(
                    level * 255 / (levels - 1)
                )

                new_pixel.append(quantized_value)

            new_row.append(new_pixel)

        new_grid.append(new_row)

    return new_grid


def image_properties(image, dpi):

    if dpi <= 0:
        raise ValueError("DPI must be greater than 0")

    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    # Physical dimensions
    width_inches = width / dpi
    height_inches = height / dpi

    # Uncompressed memory
    bytes_per_channel = 1

    memory_bytes = (
        height
        * width
        * channels
        * bytes_per_channel
    )

    memory_kb = memory_bytes / 1024

    return width_inches, height_inches, memory_kb