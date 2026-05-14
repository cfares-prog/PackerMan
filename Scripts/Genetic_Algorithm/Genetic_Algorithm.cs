using System;
using System.Collections.Generic;
using System.Text.Json;
using Godot;

public class GeneticAlgorithm<T>
{
    public List<DNA<T>> Population { get; private set; }
    public int Generation { get; private set; }
    public float BestFitness { get; private set; }
    public T[] BestGenes { get; private set; }

    public float MutationRate;
    
    private List<DNA<T>> newPopulation;
    private Random random;
    private int dnaSize;
    private Func<T> getRandomGene;
    private Func<float> fitnessFunction;

    private const string SavePath = "user://ga_checkpoint.json";

    // Data transfer object
    public class SaveData
    {
        public int Generation { get; set; }
        public List<DNA<T>> Population { get; set; }
    }

    public GeneticAlgorithm(int populationSize, int dnaSize, Random random, Func<T> getRandomGene, Func<float> fitnessFunction, float mutationRate = 0.01f)
    {
        Generation = 1;
        MutationRate = mutationRate;
        Population = new List<DNA<T>>(populationSize);
        newPopulation = new List<DNA<T>>(populationSize);
        this.random = random;
        this.dnaSize = dnaSize;
        this.getRandomGene = getRandomGene;
        this.fitnessFunction = fitnessFunction;

        BestGenes = new T[dnaSize];

        for (int i = 0; i < populationSize; i++)
        {
            Population.Add(new DNA<T>(dnaSize, random, getRandomGene, fitnessFunction, shouldInitGenes: true));
        }
    }

    public void SaveToDisk()
    {
        int genNum = this.Generation + 1;
        foreach ( var dna in this.Population)
        {
            dna.Fitness = fitnessFunction();
        }
        
        var data = new SaveData
        {
            Generation = genNum,
            Population = this.Population 
        };

        var options = new JsonSerializerOptions { WriteIndented = true, IncludeFields = true };
        string jsonString = JsonSerializer.Serialize(data, options);

        using var file = FileAccess.Open(SavePath, FileAccess.ModeFlags.Write);
        if (file != null)
        {
            file.StoreString(jsonString);
            GD.Print($"Generation {Generation} saved to {SavePath}");
        }
    }

    public bool LoadFromDisk()
    {
        if (!FileAccess.FileExists(SavePath))
        {
            GD.PrintErr("Save file does not exist.");
            return false;
        }

        try
        {
            using var file = FileAccess.Open(SavePath, FileAccess.ModeFlags.Read);
            string jsonString = file.GetAsText();

            var options = new JsonSerializerOptions { IncludeFields = true };
            var loadedData = JsonSerializer.Deserialize<SaveData>(jsonString, options);

            if (loadedData == null || loadedData.Population == null)
            {
                GD.PrintErr("Failed to parse GA JSON data.");
                return false;
            }
        
            this.Generation = loadedData.Generation;
            this.Population = loadedData.Population;

            foreach (var dna in this.Population)
            {
                dna.RestoreDependencies(this.random, this.getRandomGene, this.fitnessFunction);
            }

            GD.Print($"Successfully resumed GA at Generation {Generation}.");
            return true;
        }
        catch (Exception e)
        {
            GD.PrintErr($"Exception while loading GA state: {e.Message}");
            return false;
        }
    }

    public void NewGeneration()
    {
        if (Population.Count <= 0) return;

        newPopulation.Clear();

        for (int i = 0; i < Population.Count; i++)
        {
            DNA<T> parent1 = ChooseParent();
            DNA<T> parent2 = ChooseParent();

            DNA<T> child = parent1.Crossover(parent2);
            child.Mutate(MutationRate);

            newPopulation.Add(child);
        }

        var tmpList = Population;
        Population = newPopulation;
        newPopulation = tmpList;

        Generation++;
    }

    private DNA<T> ChooseParent()
    {
        float fitness = fitnessFunction();
        double randomNumber = random.NextDouble() * fitness;
        double cumulativeSum = 0;

        for (int i = 0; i < Population.Count; i++)
        {
            cumulativeSum += Population[i].Fitness;
            if (cumulativeSum >= randomNumber)
            {
                return Population[i];
            }
        }

        return Population[random.Next(Population.Count)];
    }
}
