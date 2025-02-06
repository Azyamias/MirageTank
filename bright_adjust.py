from PIL import ImageEnhance


def bright_adjust(surface, inter):
    enhancer_surface = ImageEnhance.Brightness(surface)
    surface = enhancer_surface.enhance(1.3)
    enhancer_inter = ImageEnhance.Brightness(inter)
    inter = enhancer_inter.enhance(0.5)
    return surface, inter
