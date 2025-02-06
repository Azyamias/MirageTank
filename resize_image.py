def resize_image(surface, inter):
    if surface.size == inter.size:
        return surface, inter
    surface = surface.resize(inter.size)
    return surface, inter
