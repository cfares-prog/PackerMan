extends Area2D
@onready var sprite_2d: Sprite2D = $Sprite2D

func _on_body_entered(body: Node2D) -> void:
	print("+1 Pellet")
	queue_free()
