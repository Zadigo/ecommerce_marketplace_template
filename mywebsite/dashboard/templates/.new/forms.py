   def _update_old_images(self):
        """
        Updates existing images to the database
        if the user has changed their values
        """
        incoming_keys = self.data.getlist('image-key')
        if incoming_keys:
            images = models.Image.objects.filter(id__in=incoming_keys)

            if images.exists():
                names = self.data.getlist('image-name')
                urls = self.data.getlist('image-url')
                variants = self.data.getlist('image-variant')

                for i, image in enumerate(images):
                    try:
                        name = names[i]
                    except:
                        raise exceptions.ValidationError(
                            _("Le nom n'est pas valide"))

                    # try:
                    #     variant = variants[i]
                    # except:
                    #     variant = 'Noir'
                    variant = self._check_if_none(variants, i, default='Noir')

                    # try:
                    #     url = urls[i]
                    # except:
                    #     url = None
                    url = self._check_if_none(urls, i)

                    image.name = name
                    image.variant = variant
                    image.url = url

                models.Image.objects.bulk_update(
                    images, ['name', 'variant', 'url'])
                return images

    def _create_new_images(self, instance, old_items=None):
        """
        Creates new images to the database when the user
        has added new fields to the existing ones
        """
        has_new_images = self.data.getlist('new-image-url', [])

        if has_new_images:
            names = self.data.getlist('new-image-name')
            variants = self.data.getlist('new-image-variant')

            has_same_lengths = self._check_has_same_lengths(
                has_new_images, names, variants
            )

            if has_same_lengths:
                items = []
                for i, url in enumerate(has_new_images):
                    if names[i]:
                        items.append(
                            models.Image(
                                name=names[i],
                                url=url,
                                variant=variants[i]
                            )
                        )

                try:
                    with transaction.atomic():
                        new_images = models.Image.objects.bulk_create(items)
                except:
                    self.add_error(None, _("Une erreur est survenue - FIE-SA"))
                else:
                    if old_items:
                        items = list(old_items) + new_images
                    else:
                        items = new_images
                    instance.images.set(items)
            else:
                self.add_error(None, _("Une erreur est survenue - FIE-LE"))
