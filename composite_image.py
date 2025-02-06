from PIL import Image


def composite_image(surface, inter):
    out = Image.new('LA', surface.size)
    combined_pixel = out.load()
    for x in range(surface.width):
        for y in range(surface.height):
            surface_pixel = surface.getpixel((x, y))
            inter_pixel = inter.getpixel((x, y))
            alpha = 255 + inter_pixel - surface_pixel
            alpha = max(0, min(alpha, 255))
            if alpha == 0:
                out_pixel = 0
            else:
                out_pixel = int((inter_pixel * 255) / alpha + 0.5)
                out_pixel = max(0, min(out_pixel, 255))
            combined_pixel[x, y] = (out_pixel, alpha)
    return out
