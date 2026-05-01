using Godot;
using System;

public partial class GeneticAlgorithm : Node
{
    [Export] public PackerMan packer;
    [Export] public bool aiHasControl = true;
    
    [Export] public int populationSize = 50;
    [Export] public int genomeLength = 300; 
    [Export] public float moveDelay = 0.2f;
    [Export] public float mutationRate = 0.02f;

    private GeneticAlgorithm<int> ga;
    private Random random = new Random();
    
    private int currentIndividualIndex = 0;
    private int currentGeneIndex = 0;
    private float timer = 0;
    
    private Vector2 startPosition;

    public override void _Ready()
    {
        if (packer == null) return;
        
        startPosition = packer.GlobalPosition;

        if (aiHasControl)
        {
            packer.disablePlayerControl();

            ga = new GeneticAlgorithm<int>(
                populationSize,
                genomeLength,
                random,
                GetRandomDirection,
                CalculateFitness,
                elitism: 3,
                mutationRate: mutationRate
            );
        }
    }

    public override void _PhysicsProcess(double delta)
    {
        if (!aiHasControl || ga == null) return;

        timer += (float)delta;

        if (timer >= moveDelay)
        {
            timer = 0;
            ExecuteNextMove();
        }
    }

    private void ExecuteNextMove()
    {
        var currentDNA = ga.Population[currentIndividualIndex];

        if (currentGeneIndex < currentDNA.Genes.Length)
        {
            int move = currentDNA.Genes[currentGeneIndex];
            
            switch (move)
            {
                case 0: packer.goUp(); break;
                case 1: packer.goDown(); break;
                case 2: packer.goLeft(); break;
                case 3: packer.goRight(); break;
            }
            currentGeneIndex++;
        }
        else
        {
            NextIndividual();
        }
    }

    private void NextIndividual()
    {
        currentGeneIndex = 0;
        currentIndividualIndex++;

        packer.GlobalPosition = startPosition;

        if (currentIndividualIndex >= ga.Population.Count)
        {
            currentIndividualIndex = 0;
            ga.NewGeneration();
            GD.Print($"Generation {ga.Generation} started. Best Fitness: {ga.BestFitness}");
        }
    }

    private int GetRandomDirection() => random.Next(4);

    private float CalculateFitness(int index)
    {

        float distanceTravelled = packer.GlobalPosition.DistanceTo(startPosition);
        return distanceTravelled; 
    }
}
