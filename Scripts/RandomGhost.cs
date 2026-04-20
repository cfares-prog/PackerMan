using Godot;
using System;

public partial class RandomGhost : GhostMoveTemplate
{
	public override void _PhysicsProcess(double delta) {
		if (ghost.getState().Equals(Ghost.STATE.CHASE))
		{
			// CHASE logic
			if (time >= pickDirectionEveryXSeconds){
				num= GD.Randi() % 4;
				time= 0;
			}
		}
		else if (ghost.getState().Equals(Ghost.STATE.FLEE))
		{
			// FLEE logic
		}
		else if (ghost.getState().Equals(Ghost.STATE.REVIVE))
		{
			// REVIVE logic
		}
		base._PhysicsProcess(delta);
	}
}
