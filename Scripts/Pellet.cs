using Godot;
using System;

public partial class Pellet : Area2D
{
    [Export]
    private int score= 1000;
	private Global gameManager;
	public override void _Ready()
    {
        BodyEntered += OnBodyEntered;// Connect body_entered signal
        gameManager = GetNode<Global>("/root/Global");// autoload
        gameManager.PackerHitSig += ResetGame;
    }

    private void OnBodyEntered(Node2D body)
    {
        if (body.IsInGroup("Player"))
        {
            gameManager.AddScore(score);
            gameManager.PowerUp();
            QueueFree();
        }
    }

    private void ResetGame()
    {
        gameManager.PackerHitSig -= ResetGame;
    }
}
