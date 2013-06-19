def carga_fondo(name, colorkey=None):
    fullname = os.path.join('img', name)
    try:
        image = pygame.image.load(fullname) 
    except pygame.error, message: 
        print 'No se puede cargar la imagen:', name
        raise SystemExit, message
    image = image.convert()
    return image, image.get_rect()
