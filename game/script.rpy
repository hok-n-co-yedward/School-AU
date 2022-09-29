# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define aoi = Character("Aoi", who_color="#FFFFFF")

#Transforms
transform my_left:
    xalign 1.5 yalign 1.0
transform my_right:
    xalign .1 yalign 1.0

transform bg_resolution:
    size (1920,1080)

transform aoi_half_size:
    size (2560,1440) crop(0,-600,2560,1440)
    on show:
        yalign 610 xalign 0.5

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene example_library_backdrop at bg_resolution

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show aoi_frown_1 at aoi_half_size, my_left

    # These display lines of dialogue.

    aoi "..."

    aoi "mid text test. mid text test. mid text test. mid text test. mid text test. mid text test. mid text test. mid text test.
    mid text test. mid text test. mid text test. mid text test. "

    aoi "Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test.
    Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test.
    Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test.
    Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test. Long text test.
    Long text test. Long text test. Long text test. Long text test. "

    # This ends the game.

    return
