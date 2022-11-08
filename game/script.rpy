image orig:
    contains:
        "images/CG/bg.webp"
    contains:
        "images/CG/b1.webp"
    contains:
        "images/CG/c1.webp"
    contains:
        "images/CG/d1.webp"
    contains:
        "images/CG/b2.webp"
    contains:
        "images/CG/c2.webp"
    contains:
        "images/CG/d6.webp"

image oversample:
    contains:
        "images_x2/CG/bg@2.webp"
    contains:
        "images_x2/CG/b1@2.webp"
    contains:
        "images_x2/CG/c1@2.webp"
    contains:
        "images_x2/CG/d1@2.webp"
    contains:
        "images_x2/CG/b2@2.webp"
    contains:
        "images_x2/CG/c2@2.webp"
    contains:
        "images_x2/CG/d6@2.webp"

image oversample_fixed:
    contains:
        Image("images_x2/CG/bg@2.webp", optimize_bounds=False)
    contains:
        Image("images_x2/CG/b1@2.webp", optimize_bounds=False)
    contains:
        Image("images_x2/CG/c1@2.webp", optimize_bounds=False)
    contains:
        Image("images_x2/CG/d1@2.webp", optimize_bounds=False)
    contains:
        Image("images_x2/CG/b2@2.webp", optimize_bounds=False)
    contains:
        Image("images_x2/CG/c2@2.webp", optimize_bounds=False)
    contains:
        Image("images_x2/CG/d6@2.webp", optimize_bounds=False)

init python:
    def clear_cache():
        renpy.exports.flush_cache_file("images_x2/CG/b1@2.webp")
        renpy.exports.flush_cache_file("images_x2/CG/c1@2.webp")
        renpy.exports.flush_cache_file("images_x2/CG/d1@2.webp")
        renpy.exports.flush_cache_file("images_x2/CG/b2@2.webp")
        renpy.exports.flush_cache_file("images_x2/CG/c2@2.webp")
        renpy.exports.flush_cache_file("images_x2/CG/d6@2.webp")

label start:
    scene orig
    $ clear_cache()
    "Original"

    scene oversample
    "Oversample"

    scene orig
    $ clear_cache()
    "Original"

    scene oversample_fixed
    "Oversample fixed"

    return
