using Godot;
using System;

public partial class Ghost : CharacterBody2D
{
	[Export]
	private float baseSpeed = 100.0f;
	[Export]
	private Node movementAI;
	private AnimatedSprite2D animatedSprite;
	private Vector2 direction= Vector2.Zero;

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		animatedSprite= GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		animatedSprite.Play("idle" + ((GD.Randi()% 4)+ 1));
        base._Ready();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta) {

		base._Process(delta);
	}

	// Called every frame at a fixed FPS. 'delta' is the elapsed time since the previous frame.
	public override void _PhysicsProcess(double delta) {

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
		base._PhysicsProcess(delta);
	}
}
