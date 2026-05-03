using Godot;
using System;

public partial class GhostMoveTemplate : Node
{
	// set num equal to 0 to move up, 1 to move down, 2 to move right or 3 to move left 
	[Export] public Ghost ghost;//* is the ghost being controlled 
	//& 1. needs to be assigned after attaching script to a node 
	//& 2. the node we attach the script to is just used to hold script in the case of any extentions of this class
	[Export] public double pickDirectionEveryXSeconds= 1;
	// by default picks a new direction every 1 second (or rather whenever time >= pickDirectionEveryXSeconds)
	[Export] private bool isAllowedToRun= true; // by default allows controller to run
	public double time; public uint num= 0;// by default moves up infinitely
	public override void _Ready() {
		SetProcess(isAllowedToRun);
		SetPhysicsProcess(isAllowedToRun);
		base._Ready();
	}
	public override void _PhysicsProcess(double delta) 
	{
		time += delta;
		switch (num)
		{
			case 0: ghost.goUp(); break;
			case 1: ghost.goDown(); break;
			case 2: ghost.goRight(); break;
			case 3: ghost.goLeft(); break;
			default: break;
		}
		base._PhysicsProcess(delta);
	}
}
