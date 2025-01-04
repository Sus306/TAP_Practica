import mcpi.minecraft as minecraft
import mcpi.block as block

# Conectar con el servidor de Minecraft
mc = minecraft.Minecraft.create()

# Publicar un mensaje en el chat
mc.postToChat("Hello Minecraft World")

# Obtener la posición del jugador y colocar un bloque de piedra
pos = mc.player.getTilePos()
mc.setBlock(pos.x + 3, pos.y, pos.z, block.STONE.id)
