using Godot;
using System;

public partial class AStarGhost : GhostMoveTemplate
{
	// set num equal to 0 to move up, 1 to move down, 2 to move right or 3 to move left 
	public override void _Ready()
	{
		base._Ready();
	}

	public override void _PhysicsProcess(double delta) 
	{
		if (time >= pickDirectionEveryXSeconds)
		{
			if (ghost.getState().Equals(Ghost.STATE.CHASE)) { /* CHASE logic */ }
			else if (ghost.getState().Equals(Ghost.STATE.FLEE)) { /* FLEE logic */ }
			else if (ghost.getState().Equals(Ghost.STATE.REVIVE)) { /* REVIVE logic */ }
			time= 0;
		}
		base._PhysicsProcess(delta);
	}
}
