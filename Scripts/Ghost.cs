using Godot;
using System;

public partial class Ghost : CharacterBody2D
{
	private Global manager;
	[Export]
	private string color = "red";
	[Export]
	private float baseSpeed = 100.0f;
	[Export]
	private Node movementAI;
	private AnimatedSprite2D animatedSprite;
	public Vector2 direction= Vector2.Zero;

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		animatedSprite= GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		animatedSprite.Play("idle" + ((GD.Randi()% 4)+ 1));

        manager = GetNode<Global>("/root/Global");
		manager.GhostFleeSig += DoFlee;
		manager.GhostChaseSig += DoChase;

		AddToGroup("Ghost", true);
        base._Ready();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta) {

		switch (direction)
		{
			case (1,0):
				animatedSprite.Play("right_" + color);
			break;
			case (-1,0):
				animatedSprite.Play("left_" + color);
			break;
			case (0,1):
				animatedSprite.Play("down_" + color);
			break;
			case (0,-1):
				animatedSprite.Play("up_" + color);
			break;
			default:
			break;
		}
		base._Process(delta);
	}

	// Called every frame at a fixed FPS. 'delta' is the elapsed time since the previous frame.
	public override void _PhysicsProcess(double delta) {
		Velocity = direction * baseSpeed * (float)delta;
		MoveAndSlide();
		base._PhysicsProcess(delta);
	}

	// temporary flee state enabler func
	public void DoFlee()
	{
		GD.Print($"{Name}: FLEE!!!");
	}
	// temporary chase state enabler func
	public void DoChase()
	{
		GD.Print($"{Name}: Chase.");
	}
}
