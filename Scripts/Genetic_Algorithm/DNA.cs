using System;
using System.Text.Json.Serialization;

public class DNA<T>
{
    [JsonInclude]
	public T[] Genes { get; set; }

    [JsonInclude]
	public float Fitness { get; set; }

	private Random random;
	private Func<T> getRandomGene;
	private Func<float> fitnessFunction;

    public DNA() {}

	public DNA(int size, Random random, Func<T> getRandomGene, Func<float> fitnessFunction, bool shouldInitGenes = true)
	{
		Genes = new T[size];
		this.random = random;
		this.getRandomGene = getRandomGene;
		this.fitnessFunction = fitnessFunction;

		if (shouldInitGenes)
		{
			for (int i = 0; i < Genes.Length; i++)
			{
				Genes[i] = getRandomGene();
			}
		}
	}

    public void RestoreDependencies(Random rng, Func<T> geneFunc, Func<float> fitnessFunc)
    {
        this.random = rng;
        this.getRandomGene = geneFunc;
        this.fitnessFunction = fitnessFunc;
    }

	public float CalculateFitness()
	{
		Fitness = fitnessFunction();
		return Fitness;
	}

	public DNA<T> Crossover(DNA<T> otherParent)
	{
		DNA<T> child = new DNA<T>(Genes.Length, random, getRandomGene, fitnessFunction, shouldInitGenes: false);

		for (int i = 0; i < Genes.Length; i++)
		{
			child.Genes[i] = random.NextDouble() < 0.5 ? Genes[i] : otherParent.Genes[i];
		}

		return child;
	}

	public void Mutate(float mutationRate)
	{
		for (int i = 0; i < Genes.Length; i++)
		{
			if (random.NextDouble() < mutationRate)
			{
				Genes[i] = getRandomGene();
			}
		}
	}
}
