using Godot;
using System;

public partial class PackerMan : CharacterBody2D
{
    private Global manager;
	[Export] private float baseSpeed = 100.0f;
	[Export] private float vulTime = 3.0f;
	[Export] private float powerTime = 5.0f;
	[Export] private int ghostScore= 500;
	/*
		passThroughTime dictates in seconds packerman gets to passthrough ghosts 
		my very shitty atempt at a workarout to allow packer to not get stuck on ghosts hes eaten
		doesnt work >:(
		ah and packer now apparently can only eat a ghost if that ghost is moving TOWARDS packer
		or rather he never could do it any other way due to how collision checks are done
	*/
	[Export] private int passThroughTime= 1;
	private bool powerUp = false;
	private bool isHit = false;
	private bool isPlayerControlled = true;

	private Vector2 lastDirection= Vector2.Zero;
	private Vector2 direction= Vector2.Zero;
	private AnimatedSprite2D animatedSprite;
	public RayCast2D upRay;
	public RayCast2D downRay;
	public RayCast2D rightRay;
	public RayCast2D leftRay;

    public override void _Ready()
    {
		manager = GetNode<Global>("/root/Global");
		manager.PowerUpSig += PowerUpPacker;
		manager.PackerHitSig += ResetGame;

		animatedSprite= GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		animatedSprite.Play("idle");

		upRay= GetNode<RayCast2D>("ColBox/upRay");
		downRay= GetNode<RayCast2D>("ColBox/downRay");
		rightRay= GetNode<RayCast2D>("ColBox/rightRay");
		leftRay= GetNode<RayCast2D>("ColBox/leftRay");

		upRay.Enabled= false;
		downRay.Enabled= false;
		rightRay.Enabled= false;
		leftRay.Enabled= false;
		
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
		lastDirection= direction;
		// Get the input direction and handle the movement/deceleration.
		Vector2 direct= Vector2.Zero;

		if (isPlayerControlled){
			direct= Input.GetVector("left", "right", "up", "down");
		}

		switch (direct)
		{
			case (1,0):
				direction= Vector2.Right;
				upRay.Enabled= false;
				downRay.Enabled= false;
				rightRay.Enabled= true;
				leftRay.Enabled= false;
			break;
			case (-1,0):
				direction= Vector2.Left;
				upRay.Enabled= false;
				downRay.Enabled= false;
				rightRay.Enabled= false;
				leftRay.Enabled= true;
			break;
			case (0,1):
				direction= Vector2.Down;
				upRay.Enabled= false;
				downRay.Enabled= true;
				rightRay.Enabled= false;
				leftRay.Enabled= false;
			break;
			case (0,-1):
				direction= Vector2.Up;
				upRay.Enabled= true;
				downRay.Enabled= false;
				rightRay.Enabled= false;
				leftRay.Enabled= false;
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
					if (!powerUp)
					{// die
						PackerHit();
						manager.UpdateLife();
					}
					else
					{// aet ghost
						manager.AddScore(ghostScore);
						doPassthrough();
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
	public void goUp(){ direction= Vector2.Up;}
	public void goDown(){ direction= Vector2.Down;}
	public void goLeft(){ direction= Vector2.Left;}
	public void goRight(){ direction= Vector2.Right;}

	public void enablePlayerControl(){ isPlayerControlled = true; }
	public void disablePlayerControl(){ isPlayerControlled = false; }
	public bool isPoweredUp(){ return powerUp; }
	public async void doPassthrough()
	{
		SetCollisionLayerValue(2, false);
		await ToSignal(GetTree().CreateTimer(passThroughTime), SceneTreeTimer.SignalName.Timeout);
		SetCollisionLayerValue(2, true);
	}
	private void ResetGame()
	{
		manager.PackerHitSig -= ResetGame;
		manager.PowerUpSig -= PowerUpPacker;
	}
}
