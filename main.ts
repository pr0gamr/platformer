controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        mySprite.vy = -180
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile4`, function (sprite, location) {
    startNextLevel()
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -180
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile7`, function (sprite, location) {
    startNextLevel()
})
function startNextLevel () {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        value.destroy()
    }
    currentLevel += 1
    if (currentLevel == 1) {
        scene.setBackgroundColor(11)
        tiles.setTilemap(tilemap`level2`)
    } else if (currentLevel == 2) {
        scene.setBackgroundColor(9)
        tiles.setTilemap(tilemap`platformer1`)
    } else if (currentLevel == 3) {
        scene.setBackgroundColor(0)
        tiles.setTilemap(tilemap`level3`)
    } else if (currentLevel == 4) {
        scene.setBackgroundColor(0)
        tiles.setTilemap(tilemap`level4`)
    } else if (currentLevel == 5) {
        if (info.life() == 3) {
            pacifist = 1
        }
        if (info.score() == 0) {
            info.setLife(19)
            scene.setBackgroundColor(8)
            tiles.setCurrentTilemap(tilemap`level5`)
            game.setGameOverMessage(true, "PACIFIST ENDING?")
        } else {
            startNextLevel()
        }
    } else if (currentLevel == 6) {
        if (info.score() == 0 && (info.life() == 19 && pacifist == 1)) {
            info.setScore(50)
            info.setLife(1)
            scene.setBackgroundColor(15)
            tiles.setCurrentTilemap(tilemap`level7`)
            game.showLongText("Wow, I didn't think it could be done. You killed NO ENEMIES. Surprising, anyway good job, here have 50 score for your troubles. Quick question why did you put so much effort into this? ", DialogLayout.Center)
            game.splash("Now, will you sacrifice yourself to save the enemies from the dark?")
            game.setGameOverMessage(true, "TRUE PACIFIST ENDING!!")
            game.setGameOverMessage(false, "SACRIFICIAL ENDING")
        } else {
            startNextLevel()
        }
    } else if (info.score() == 14) {
        scene.setBackgroundColor(4)
        tiles.setCurrentTilemap(tilemap`level8`)
        game.showLongText("How could you!? They were innocent, they were being controlled by someone. THEY HAD NO CHOICE!, but, now you have to suffer for them", DialogLayout.Center)
        game.setGameOverMessage(false, "MASSACRE ENDING")
    } else {
        game.over(true)
    }
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    for (let value2 of tiles.getTilesByType(assets.tile`tile5`)) {
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        myEnemy.vx = 30
        myEnemy.ay = 500
        tiles.placeOnTile(myEnemy, value2)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile2`, function (sprite, location) {
    game.over(false)
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    if (sprite.bottom < otherSprite.y) {
        sprite.vy = -100
        info.changeScoreBy(1)
    } else {
        info.changeLifeBy(-1)
    }
})
let myEnemy: Sprite = null
let pacifist = 0
let currentLevel = 0
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.ay = 500
controller.moveSprite(mySprite, 88, 0)
scene.cameraFollowSprite(mySprite)
info.setLife(3)
startNextLevel()
game.onUpdate(function () {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        if (value.isHittingTile(CollisionDirection.Bottom)) {
            if (value.vx < 0 && value.tileKindAt(TileDirection.Left, assets.tile`tile1`)) {
                value.vy = -150
            } else if (value.vx > 0 && value.tileKindAt(TileDirection.Right, assets.tile`tile1`)) {
                value.vy = -150
            }
        } else if (value.isHittingTile(CollisionDirection.Left)) {
            value.vx = 30
        } else if (value.isHittingTile(CollisionDirection.Right)) {
            value.vx = -30
        }
    }
})
