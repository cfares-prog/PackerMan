using Godot;
using System;

public partial class Global : Node
{
    [Signal]
    public delegate void ScoreChangedEventHandler(int newScore);

	public int CoinScore { get; private set; } =  50;
	public int PelletScore { get; private set; } = 1000;
    public int Score { get; private set; } = 0;

    public void AddScore(int amount)
    {
        Score += amount;
        EmitSignal(SignalName.ScoreChanged, Score);
    }

}
