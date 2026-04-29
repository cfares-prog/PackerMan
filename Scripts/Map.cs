using Godot;
using System;

public partial class Map : Node2D
{
    private Global gameManager;
	
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		
        // Connect to the global signal
        gameManager = GetNode<Global>("/root/Global");

		gameManager.PackerHitSig += ResetGame;
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}

	private void ResetGame()
	{
		gameManager.PackerHitSig -= ResetGame;
		GetTree().ReloadCurrentScene();
	}

}
