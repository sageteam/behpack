def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return '{}/{}.{}'.format(instance.id, instance.sku, extension)


def upload_movie_location(instance, filename):
    return '{0}/{1}'.format(instance.id, filename)