using Godot;
using System;

public partial class Teleport : Area2D
{
	private Global manager;
	private Marker2D destination;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		destination = GetNode<Marker2D>("dest");
		BodyEntered += TeleportBody;

        manager = GetNode<Global>("/root/Global");
		manager.PackerHitSig += ResetGame;
	}

	public void TeleportBody(Node2D body)
	{
		GD.Print("tp Left");
		GD.Print(destination.GlobalPosition);
		if (body is PackerMan || body is Ghost)
		{
			body.SetPhysicsProcess(false);
			body.GlobalPosition= destination.GlobalPosition;
			body.SetPhysicsProcess(true);
		}
	}

	public void ResetGame()
	{
		BodyEntered -= TeleportBody;
		manager.PackerHitSig -= ResetGame;
	}
}
