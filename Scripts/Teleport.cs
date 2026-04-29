using Godot;
using System;

public partial class Teleport : Area2D
{
	private Marker2D destination;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		destination = GetNode<Marker2D>("dest");
		BodyEntered += TeleportBody;
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
}
