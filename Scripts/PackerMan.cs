using Godot;
using System;

public partial class PackerMan : CharacterBody2D
{
	[Export]
	private int health= 100;
	[Export]
	private float baseSpeed = 100.0f;
	private Vector2 lastDirection= Vector2.Zero;
	private Vector2 direction= Vector2.Zero;
	private AnimatedSprite2D animatedSprite;

    public override void _Ready()
    {
		animatedSprite= GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		animatedSprite.Play("idle");
        base._Ready();
    }


	public override void _PhysicsProcess(double delta)
	{
		Position= (Vector2I)Position;
		lastDirection= direction;
		// Get the input direction and handle the movement/deceleration.
		switch (Input.GetVector("left", "right", "up", "down"))
		{
			case (1,0):
				direction= Vector2.Right;
				animatedSprite.Play("right");
			break;
			case (-1,0):
				direction= Vector2.Left;
				animatedSprite.Play("left");
			break;
			case (0,1):
				direction= Vector2.Down;
				animatedSprite.Play("down");
			break;
			case (0,-1):
				direction= Vector2.Up;
				animatedSprite.Play("up");
			break;
			default:
			break;
		}
		Velocity = direction * baseSpeed * (float)delta;
		MoveAndSlide();
	}
}
