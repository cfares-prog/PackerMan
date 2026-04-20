using Godot;
using System;

public partial class GhostMoveTemplate : Node
{
	[Export]
	public Ghost ghost;
	[Export]
	public double pickDirectionEveryXSeconds= 1;
	public double time;
	public uint num= 0;
	public override void _PhysicsProcess(double delta) {
		time += delta;

		// change num to change ghost direction

		switch (num)
		{
			case 0:
			ghost.goUp();
			break;
			case 1:
			ghost.goDown();
			break;
			case 2:
			ghost.goRight();
			break;
			case 3:
			ghost.goLeft();
			break;
			default:
			break;
		}
		base._PhysicsProcess(delta);
	}
}
