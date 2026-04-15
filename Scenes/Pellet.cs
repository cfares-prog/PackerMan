using Godot;
using System;

public partial class Pellet : Area2D
{
	private Global gameManager;
	public override void _Ready()
    {
        BodyEntered += OnBodyEntered;// Connect body_entered signal
        gameManager = GetNode<Global>("/root/Global");// autoload
    }

    private void OnBodyEntered(Node2D body)
    {
        if (body.IsInGroup("Player"))
        {
            gameManager.AddScore(gameManager.PelletScore);
            QueueFree();
        }
    }
}
