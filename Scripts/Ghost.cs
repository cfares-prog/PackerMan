using Godot;
using System;

public partial class Ghost : CharacterBody2D
{
	public enum STATE { CHASE, FLEE, REVIVE};
	
	private Global manager;
	[Export]
	public int timeTillRevived= 10;

	[Export(PropertyHint.Enum, "red,pink,cyan,orange,green,yellow,blue,purple,crimson,forest,gold,aqua")] 
	public string baseColor { get; private set; }= "red";
	[Export] private float baseSpeed = 100.0f;
	private AnimatedSprite2D animatedSprite;
	public Vector2 direction= Vector2.Zero;
	private string color;
	private STATE state= STATE.CHASE;

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		animatedSprite= GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		animatedSprite.Play("idle" + ((GD.Randi()% 4)+ 1));

        manager = GetNode<Global>("/root/Global");
		manager.GhostFleeSig += DoFlee;
		manager.GhostChaseSig += DoChase;
		manager.PackerHitSig += ResetGame;

		color= baseColor;

		AddToGroup("Ghost", true);
        base._Ready();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta) {
		if (state.Equals(STATE.CHASE))
		{
			color= baseColor;
		}
		else if (state.Equals(STATE.FLEE))
		{
			color= "withdraw";
		}
		else if (state.Equals(STATE.REVIVE))
		{
			color= "dead";
		}
		
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
		Velocity = direction * baseSpeed ;
		MoveAndSlide();
		for (int i = 0; i < GetSlideCollisionCount(); i++)
		{
			Node collider = (Node)GetSlideCollision(i).GetCollider();

			if (collider is PackerMan packer){ if (packer.isPoweredUp()){ DoRevive(); } }
		}
	}

	// flee state enabler func
	public async void DoFlee()
	{
		GD.Print($"{Name}: FLEE!!!");
		state= STATE.FLEE;
		SetCollisionMaskValue(3, true);
	}
	// chase state enabler func
	public async void DoChase()
	{
		GD.Print($"{Name}: Chase.");
		state= STATE.CHASE;
		SetCollisionMaskValue(3, true);
	}
	// chase state enabler func
	public async void DoRevive()
	{
		GD.Print($"{Name}: Dead.");
		state= STATE.REVIVE;
		SetCollisionMaskValue(3, false);
		await ToSignal(GetTree().CreateTimer(timeTillRevived), SceneTreeTimer.SignalName.Timeout);
		DoChase();
	}
	public void goUp(){ direction= Vector2.Up; }
	public void goDown(){ direction= Vector2.Down; }
	public void goLeft(){ direction= Vector2.Left;}
	public void goRight(){ direction= Vector2.Right;}
	public STATE getState(){ return state;}

	public void ResetGame()
	{
		manager.GhostFleeSig -= DoFlee;
		manager.GhostChaseSig -= DoChase;
		manager.PackerHitSig -= ResetGame;
	}

}
