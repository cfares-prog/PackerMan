using Godot;
using System;

public partial class PackerMan : CharacterBody2D
{
    private Global manager;
	[Export]
	private float baseSpeed = 100.0f;
	[Export]
	private float vulTime = 3.0f;
	[Export]
	private float powerTime = 5.0f;

	private bool powerUp = false;
	private bool isHit = false;

	private Vector2 lastDirection= Vector2.Zero;
	private Vector2 direction= Vector2.Zero;
	private AnimatedSprite2D animatedSprite;

    public override void _Ready()
    {
		manager = GetNode<Global>("/root/Global");
		manager.PowerUpSig += PowerUpPacker;

		animatedSprite= GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		animatedSprite.Play("idle");
		
		AddToGroup("Player", true);
        base._Ready();
    }

	//for display and visuals
	public override void _Process(double delta) {
		switch (direction)
		{
			case (1,0):
				animatedSprite.Play("right");
			break;
			case (-1,0):
				animatedSprite.Play("left");
			break;
			case (0,1):
				animatedSprite.Play("down");
			break;
			case (0,-1):
				animatedSprite.Play("up");
			break;
			default:
			break;
		}
		base._Process(delta);
	}

	// for physics logic
	public override void _PhysicsProcess(double delta)
	{
		Position= (Vector2I)Position;
		lastDirection= direction;
		// Get the input direction and handle the movement/deceleration.
		switch (Input.GetVector("left", "right", "up", "down"))
		{
			case (1,0):
				direction= Vector2.Right;
			break;
			case (-1,0):
				direction= Vector2.Left;
			break;
			case (0,1):
				direction= Vector2.Down;
			break;
			case (0,-1):
				direction= Vector2.Up;
			break;
			default:
			break;
		}

		Velocity = direction * baseSpeed * (float)delta;
		MoveAndSlide();

		if (!isHit)
		{
			for (int i = 0; i < GetSlideCollisionCount(); i++)
			{
				Node collider = (Node)GetSlideCollision(i).GetCollider();

				if (collider is Ghost)
				{
					// GD.Print($"{Name}: collided with {collider.Name}");
					if (powerUp)
					{
						// eat ghost

					}
					else
					{
						// lose life
						PackerHit();
						manager.UpdateLife();
					}
				}
			}
		}
	}
	public async void PowerUpPacker()
	{
		GD.Print($"{Name}: power");
		powerUp= true;
		manager.ScareGhost();
		await ToSignal(GetTree().CreateTimer(powerTime), SceneTreeTimer.SignalName.Timeout);
		powerUp= false;
		manager.CalmGhost();
	}
	public async void PackerHit()
	{
		GD.Print($"{Name}: hit");
		isHit= true;
		await ToSignal(GetTree().CreateTimer(vulTime), SceneTreeTimer.SignalName.Timeout);
		isHit= false;
	}

}
