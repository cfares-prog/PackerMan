using Godot;
using System;

public partial class PatrolGhost : GhostMoveTemplate
{
	// set num equal to 0 to move up, 1 to move down, 2 to move right or 3 to move left 
	//! THIS SCRIPT IS USED FOR COPY PASTE PURPOSES ONLY 
	//* Check The Directory Named "VariousPatrolGhostRoutes" For The Actually Usable PatrolGhost Scripts
	public uint[] initialMovArr= {}; public uint[]  loopMovArr= {}; public int initIdx, loopIdx;
	public override void _Ready() {
		initIdx= 0;
		loopIdx= 0;
		base._Ready();
	}
	public override void _PhysicsProcess(double delta)
	{
		if (time >= pickDirectionEveryXSeconds)
		{
			if (ghost.getState().Equals(Ghost.STATE.CHASE))
			{ /* CHASE logic */
				if (initIdx < initialMovArr.Length)
				{
					num= (uint)initialMovArr.GetValue(initIdx); initIdx+= 1;
				}
				else
				{
					num= (uint)loopMovArr.GetValue(loopIdx % loopMovArr.Length); loopIdx+= 1;
				}
			}
			else if (ghost.getState().Equals(Ghost.STATE.FLEE)) { /* FLEE logic */ }
			else if (ghost.getState().Equals(Ghost.STATE.REVIVE)) { /* REVIVE logic */ }
			time= 0;
		}
		base._PhysicsProcess(delta);
	}
}
