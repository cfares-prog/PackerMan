using Godot;
using System.Collections.Generic;

public static class GhostAStarGrid
{
	public static readonly Vector2I InvalidCell = new(-9999, -9999);

	private const int Width = 28;
	private const int Height = 31;
	private const int TileSize = 16;
	private const int HalfTile = TileSize / 2;

	private static readonly string[] MazeRows =
	{
		"############################",
		"#............##............#",
		"#.####.#####.##.#####.####.#",
		"#.####.#####.##.#####.####.#",
		"#.####.#####.##.#####.####.#",
		"#..........................#",
		"#.####.##.########.##.####.#",
		"#.####.##.########.##.####.#",
		"#......##....##....##......#",
		"######.#####.##.#####.######",
		"######.#####.##.#####.######",
		"######.##..........##.######",
		"######.##.###..###.##.######",
		"######.##.#......#.##.######",
		"..........#......#..........",
		"######.##.#......#.##.######",
		"######.##.########.##.######",
		"######.##..........##.######",
		"######.#####.##.#####.######",
		"######.#####.##.#####.######",
		"#............##............#",
		"#.####.#####.##.#####.####.#",
		"#.####.#####.##.#####.####.#",
		"#...##................##...#",
		"###.##.##.########.##.##.###",
		"###.##.##.########.##.##.###",
		"#......##....##....##......#",
		"#.##########.##.##########.#",
		"#.##########.##.##########.#",
		"#..........................#",
		"############################"
	};

	private static readonly Vector2I[] Directions =
	{
		Vector2I.Up,
		Vector2I.Down,
		Vector2I.Left,
		Vector2I.Right,
	};

	public static List<Vector2I> FindPath(Vector2I start, Vector2I goal)
	{
		start = GetClosestWalkableCell(start);
		goal = GetClosestWalkableCell(goal);

		if (start == InvalidCell || goal == InvalidCell)
		{
			return new List<Vector2I>();
		}

		if (start == goal)
		{
			return new List<Vector2I> { start };
		}

		PriorityQueue<Vector2I, int> frontier = new();
		Dictionary<Vector2I, Vector2I> cameFrom = new();
		Dictionary<Vector2I, int> costSoFar = new();

		frontier.Enqueue(start, 0);
		cameFrom[start] = start;
		costSoFar[start] = 0;

		while (frontier.Count > 0)
		{
			Vector2I current = frontier.Dequeue();
			if (current == goal)
			{
				break;
			}

			foreach (Vector2I next in GetNeighbors(current))
			{
				int newCost = costSoFar[current] + 1;
				if (costSoFar.TryGetValue(next, out int knownCost) && newCost >= knownCost)
				{
					continue;
				}

				costSoFar[next] = newCost;
				cameFrom[next] = current;
				frontier.Enqueue(next, newCost + Heuristic(next, goal));
			}
		}

		if (!cameFrom.ContainsKey(goal))
		{
			return new List<Vector2I> { start };
		}

		List<Vector2I> path = new();
		Vector2I step = goal;
		path.Add(step);

		while (step != start)
		{
			step = cameFrom[step];
			path.Add(step);
		}

		path.Reverse();
		return path;
	}

	public static Vector2I WorldToCell(Vector2 worldPosition)
	{
		int x = Mathf.RoundToInt((worldPosition.X - HalfTile) / TileSize);
		int y = Mathf.RoundToInt((worldPosition.Y - HalfTile) / TileSize);
		return new Vector2I(x, y);
	}

	public static Vector2 CellToWorld(Vector2I cell)
	{
		return new Vector2(HalfTile + (cell.X * TileSize), HalfTile + (cell.Y * TileSize));
	}

	public static Vector2I GetClosestWalkableCell(Vector2I cell)
	{
		if (IsWalkable(cell))
		{
			return cell;
		}

		Queue<Vector2I> queue = new();
		HashSet<Vector2I> visited = new() { cell };
		queue.Enqueue(cell);

		while (queue.Count > 0)
		{
			Vector2I current = queue.Dequeue();
			foreach (Vector2I direction in Directions)
			{
				Vector2I next = current + direction;
				if (!visited.Add(next))
				{
					continue;
				}

				if (IsWalkable(next))
				{
					return next;
				}

				if (IsInside(next))
				{
					queue.Enqueue(next);
				}
			}
		}

		return InvalidCell;
	}

	private static IEnumerable<Vector2I> GetNeighbors(Vector2I cell)
	{
		foreach (Vector2I direction in Directions)
		{
			Vector2I next = cell + direction;
			if (IsWalkable(next))
			{
				yield return next;
			}
		}
	}

	private static bool IsWalkable(Vector2I cell)
	{
		return IsInside(cell) && MazeRows[cell.Y][cell.X] != '#';
	}

	private static bool IsInside(Vector2I cell)
	{
		return cell.X >= 0 && cell.X < Width && cell.Y >= 0 && cell.Y < Height;
	}

	private static int Heuristic(Vector2I from, Vector2I to)
	{
		return Mathf.Abs(from.X - to.X) + Mathf.Abs(from.Y - to.Y);
	}
}
