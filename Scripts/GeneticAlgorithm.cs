using Godot;
using System;

public partial class GeneticAlgorithm : Node
{
	[Export]
	public PackerMan packer;
	[Export]
	public bool aiHasControl= false;
	
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		if (aiHasControl) packer.disablePlayerControl();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		//ususaly used for visuals
	}

	public override void _PhysicsProcess(double delta) {
		if (aiHasControl)
		{// code goes in here plz
			
		}
		base._PhysicsProcess(delta);
	}
}
