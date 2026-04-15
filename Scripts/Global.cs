using Godot;
using System;

public partial class Global : Node
{
    [Signal]
    public delegate void ScoreChangedSigEventHandler(int newScore);
    [Signal]
    public delegate void LifeLostSigEventHandler(int curLife);
    [Signal]
    public delegate void PowerUpSigEventHandler();
    [Signal]
    public delegate void GhostFleeSigEventHandler();
    [Signal]
    public delegate void GhostChaseSigEventHandler();


	public int Life;
	public int CoinScore { get; private set; }
	public int PelletScore { get; private set; }
    public int Score { get; private set; }

	public override void _Ready() {
		Life = 3;
		CoinScore =  50;
		PelletScore = 1000;
		Score = 0;
		base._Ready();
	}
    public void AddScore(int amount)
    {
        Score += amount;
        EmitSignal(SignalName.ScoreChangedSig, Score);
    }
    public void PowerUp()
    {
        EmitSignal(SignalName.PowerUpSig);
    }
    public void ScareGhost()
    {
        EmitSignal(SignalName.GhostFleeSig);
    }
    public void CalmGhost()
    {
        EmitSignal(SignalName.GhostChaseSig);
    }
    public void UpdateLife()
    {
		Life= Life < 1 ? 0 : Life - 1;
		// GD.Print(Life);
        EmitSignal(SignalName.LifeLostSig, Life);
    }

}
