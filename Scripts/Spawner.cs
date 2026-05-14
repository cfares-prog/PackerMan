using Godot;
using System;

public partial class Spawner : Node2D
{
    // Drag your scene in the inspector or load it
    [Export]
    public PackedScene AgentScene;
	[Export]
	public int populationCount= 10;

    public override void _Ready()
    {
        SpawnPopulation(populationCount);
    }

    private void SpawnPopulation(int count)
    {
        for (int i = 0; i < count; i++)
        {
            var agent = AgentScene.Instantiate<Node2D>();
            
            // Optional: random position
            agent.Position = new Vector2(
                (float)GD.RandRange(0, 800),
                (float)GD.RandRange(0, 600)
            );

            AddChild(agent);
        }
    }
}