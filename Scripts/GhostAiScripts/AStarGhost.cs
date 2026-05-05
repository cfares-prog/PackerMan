using Godot;
using System;
using System.Collections.Generic;

public partial class AStarGhost : GhostMoveTemplate
{
	[Export] private int reviveDurationSeconds = 3;
	[Export] private float cellArrivalThreshold = 2.0f;

	private PackerMan packerMan;
	private readonly List<Vector2I> currentPath = new();
	private readonly List<Vector2I> chaseHistory = new();

	private Ghost.STATE previousState = Ghost.STATE.CHASE;
	private Vector2I chaseTargetCell = GhostAStarGrid.InvalidCell;
	private int pathIndex = -1;

	public override void _Ready()
	{
		base._Ready();

		packerMan = GetTree().GetFirstNodeInGroup("Player") as PackerMan;
		if (packerMan == null)
		{
			packerMan = GetNodeOrNull<PackerMan>("../../PackerMan");
		}

		ghost.timeTillRevived = reviveDurationSeconds;
		previousState = ghost.getState();
		if (previousState == Ghost.STATE.CHASE)
		{
			PushChaseHistory(GetGhostCell());
		}
	}

	public override void _PhysicsProcess(double delta)
	{
		Ghost.STATE currentState = ghost.getState();
		if (currentState != previousState)
		{
			HandleStateChanged(currentState);
			previousState = currentState;
		}

		switch (currentState)
		{
			case Ghost.STATE.CHASE:
				UpdateChasePath();
				FollowCurrentPath();
				base._PhysicsProcess(delta);
				break;
			case Ghost.STATE.FLEE:
				UpdateFleePath();
				FollowCurrentPath();
				base._PhysicsProcess(delta);
				break;
			case Ghost.STATE.REVIVE:
				currentPath.Clear();
				pathIndex = -1;
				ghost.direction = Vector2.Zero;
				time += delta;
				break;
		}
	}

	private void HandleStateChanged(Ghost.STATE newState)
	{
		if (newState == Ghost.STATE.CHASE)
		{
			currentPath.Clear();
			pathIndex = -1;
			chaseTargetCell = GhostAStarGrid.InvalidCell;
			PushChaseHistory(GetGhostCell());
			return;
		}

		if (newState == Ghost.STATE.FLEE)
		{
			BuildFleePath();
			return;
		}

		currentPath.Clear();
		pathIndex = -1;
	}

	private void UpdateChasePath()
	{
		if (packerMan == null)
		{
			ghost.direction = Vector2.Zero;
			return;
		}

		Vector2I ghostCell = GetGhostCell();
		Vector2I targetCell = GhostAStarGrid.GetClosestWalkableCell(GhostAStarGrid.WorldToCell(packerMan.GlobalPosition));

		PushChaseHistory(ghostCell);

		bool needsNewPath = currentPath.Count == 0
			|| pathIndex >= currentPath.Count
			|| chaseTargetCell != targetCell;

		if (!needsNewPath)
		{
			Vector2 targetCenter = GhostAStarGrid.CellToWorld(chaseTargetCell);
			if (ghost.GlobalPosition.DistanceTo(targetCenter) <= cellArrivalThreshold)
			{
				needsNewPath = true;
			}
		}

		if (needsNewPath)
		{
			RebuildPath(ghostCell, targetCell);
			chaseTargetCell = targetCell;
		}
	}

	private void UpdateFleePath()
	{
		if (currentPath.Count == 0 || pathIndex >= currentPath.Count)
		{
			BuildFleePath();
		}
	}

	private void BuildFleePath()
	{
		currentPath.Clear();
		pathIndex = -1;

		Vector2I currentCell = GetGhostCell();
		List<Vector2I> reversedHistory = new();

		if (chaseHistory.Count == 0)
		{
			reversedHistory.Add(currentCell);
		}
		else
		{
			for (int i = chaseHistory.Count - 1; i >= 0; i--)
			{
				reversedHistory.Add(chaseHistory[i]);
			}

			if (reversedHistory[0] != currentCell)
			{
				reversedHistory.Insert(0, currentCell);
			}
		}

		currentPath.AddRange(reversedHistory);
		pathIndex = currentPath.Count > 1 ? 1 : currentPath.Count;
	}

	private void RebuildPath(Vector2I startCell, Vector2I endCell)
	{
		currentPath.Clear();
		currentPath.AddRange(GhostAStarGrid.FindPath(startCell, endCell));

		if (currentPath.Count <= 1)
		{
			pathIndex = currentPath.Count;
			return;
		}

		pathIndex = currentPath[0] == startCell ? 1 : 0;
	}

	private void FollowCurrentPath()
	{
		if (currentPath.Count == 0 || pathIndex >= currentPath.Count)
		{
			ghost.direction = Vector2.Zero;
			return;
		}

		Vector2I ghostCell = GetGhostCell();
		while (pathIndex < currentPath.Count)
		{
			Vector2 waypoint = GhostAStarGrid.CellToWorld(currentPath[pathIndex]);
			if (ghost.GlobalPosition.DistanceTo(waypoint) > cellArrivalThreshold)
			{
				break;
			}

			pathIndex += 1;
		}

		if (pathIndex >= currentPath.Count)
		{
			ghost.direction = Vector2.Zero;
			return;
		}

		Vector2I nextCell = currentPath[pathIndex];
		Vector2I deltaCell = nextCell - ghostCell;
		if (deltaCell == Vector2I.Zero)
		{
			Vector2 offset = GhostAStarGrid.CellToWorld(nextCell) - ghost.GlobalPosition;
			ApplyDirection(offset);
			return;
		}

		ApplyDirection(deltaCell);
	}

	private void ApplyDirection(Vector2 vector)
	{
		if (Mathf.Abs(vector.X) > Mathf.Abs(vector.Y))
		{
			num = vector.X >= 0 ? 2u : 3u;
			return;
		}

		num = vector.Y >= 0 ? 1u : 0u;
	}

	private void PushChaseHistory(Vector2I cell)
	{
		if (chaseHistory.Count > 0 && chaseHistory[^1] == cell)
		{
			return;
		}

		chaseHistory.Add(cell);
		if (chaseHistory.Count > 5)
		{
			chaseHistory.RemoveAt(0);
		}
	}

	private Vector2I GetGhostCell()
	{
		return GhostAStarGrid.GetClosestWalkableCell(GhostAStarGrid.WorldToCell(ghost.GlobalPosition));
	}
}
