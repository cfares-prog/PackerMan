using Godot;
using System;

public partial class Ghost : CharacterBody2D
{
	private AnimatedSprite2D animatedSprite;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		animatedSprite= GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		animatedSprite.Play("idle" + ((GD.Randi()% 4)+ 1));
        base._Ready();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}
