def on_up_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -180
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    startNextLevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile4
    """),
    on_overlap_tile)

def on_b_pressed():
    mySprite.vy = -180
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile2(sprite2, location2):
    startNextLevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile7
    """),
    on_overlap_tile2)

def startNextLevel():
    global currentLevel, pacifist, myEnemy
    for value in sprites.all_of_kind(SpriteKind.enemy):
        value.destroy()
    currentLevel += 1
    if currentLevel == 1:
        scene.set_background_color(11)
        tiles.set_tilemap(tilemap("""
            level2
        """))
    elif currentLevel == 2:
        scene.set_background_color(9)
        tiles.set_tilemap(tilemap("""
            platformer1
        """))
    elif currentLevel == 3:
        scene.set_background_color(0)
        tiles.set_tilemap(tilemap("""
            level3
        """))
    elif currentLevel == 4:
        scene.set_background_color(0)
        tiles.set_tilemap(tilemap("""
            level4
        """))
    elif currentLevel == 5:
        if info.life() == 3:
            pacifist = 1
        if info.score() == 0:
            info.set_life(19)
            scene.set_background_color(8)
            tiles.set_current_tilemap(tilemap("""
                level5
            """))
            game.set_game_over_message(True, "PACIFIST ENDING?")
        else:
            startNextLevel()
    elif currentLevel == 6:
        if info.score() == 0 and (info.life() == 19 and pacifist == 1):
            info.set_score(50)
            info.set_life(1)
            scene.set_background_color(15)
            tiles.set_current_tilemap(tilemap("""
                level7
            """))
            game.show_long_text("Wow, I didn't think it could be done. You killed NO ENEMIES. Surprising, anyway good job, here have 50 score for your troubles. Quick question why did you put so much effort into this? ",
                DialogLayout.CENTER)
            game.splash("Now, will you sacrifice yourself to save the enemies from the dark?")
            game.set_game_over_message(True, "TRUE PACIFIST ENDING!!")
            game.set_game_over_message(False, "SACRIFICIAL ENDING")
        else:
            startNextLevel()
    elif info.score() == 14:
        scene.set_background_color(4)
        tiles.set_current_tilemap(tilemap("""
            level8
        """))
        game.show_long_text("How could you!? They were innocent, they were being controlled by someone. THEY HAD NO CHOICE!, but, now you have to suffer for them",
            DialogLayout.CENTER)
        game.set_game_over_message(False, "MASSACRE ENDING")
    else:
        game.over(True)
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        tile5
    """)):
        myEnemy = sprites.create(img("""
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                            2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 2 
                            2 5 2 2 2 2 2 2 2 2 2 2 2 2 5 2 
                            2 5 2 2 5 5 2 2 2 2 5 5 2 2 5 2 
                            2 5 2 2 2 2 5 2 2 5 2 2 2 2 5 2 
                            2 5 2 2 2 2 2 2 2 2 2 2 2 2 5 2 
                            2 5 2 2 2 5 2 2 2 2 5 2 2 2 5 2 
                            2 5 2 2 2 5 2 2 2 2 5 2 2 2 5 2 
                            2 5 2 2 2 2 2 2 2 2 2 2 2 2 5 2 
                            2 5 2 2 2 2 2 2 2 2 2 2 2 2 5 2 
                            2 5 2 2 2 5 5 5 5 5 5 2 2 2 5 2 
                            2 5 2 2 5 2 2 2 2 2 2 5 2 2 5 2 
                            2 5 2 2 2 2 2 2 2 2 2 2 2 2 5 2 
                            2 5 2 2 2 2 2 2 2 2 2 2 2 2 5 2 
                            2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 2 
                            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
            """),
            SpriteKind.enemy)
        myEnemy.vx = 30
        myEnemy.ay = 500
        tiles.place_on_tile(myEnemy, value2)

def on_overlap_tile3(sprite3, location3):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile2
    """),
    on_overlap_tile3)

def on_on_overlap(sprite4, otherSprite):
    otherSprite.destroy()
    if sprite4.bottom < otherSprite.y:
        sprite4.vy = -100
        info.change_score_by(1)
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

myEnemy: Sprite = None
pacifist = 0
currentLevel = 0
mySprite: Sprite = None
mySprite = sprites.create(img("""
        f f f f f f f f f f f f f f f f 
            f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 
            f 2 f f f f f f f f f f f f 2 f 
            f 2 f f f f f f f f f f f f 2 f 
            f 2 f f f f f f f f f f f f 2 f 
            f 2 f f 2 2 2 f f f 2 f f f 2 f 
            f 2 f f 2 f f 2 f 2 2 f f f 2 f 
            f 2 f f 2 f f 2 f f 2 f f f 2 f 
            f 2 f f 2 2 2 f f f 2 f f f 2 f 
            f 2 f f 2 f f f f f 2 f f f 2 f 
            f 2 f f 2 f f f f 2 2 2 f f 2 f 
            f 2 f f f f f f f f f f f f 2 f 
            f 2 f f f f f f f f f f f f 2 f 
            f 2 f f f f f f f f f f f f 2 f 
            f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 
            f f f f f f f f f f f f f f f f
    """),
    SpriteKind.player)
mySprite.ay = 500
controller.move_sprite(mySprite, 88, 0)
scene.camera_follow_sprite(mySprite)
info.set_life(3)
startNextLevel()

def on_on_update():
    for value3 in sprites.all_of_kind(SpriteKind.enemy):
        if value3.is_hitting_tile(CollisionDirection.BOTTOM):
            if value3.vx < 0 and value3.tile_kind_at(TileDirection.LEFT, assets.tile("""
                tile1
            """)):
                value3.vy = -150
            elif value3.vx > 0 and value3.tile_kind_at(TileDirection.RIGHT, assets.tile("""
                tile1
            """)):
                value3.vy = -150
        elif value3.is_hitting_tile(CollisionDirection.LEFT):
            value3.vx = 30
        elif value3.is_hitting_tile(CollisionDirection.RIGHT):
            value3.vx = -30
game.on_update(on_on_update)
