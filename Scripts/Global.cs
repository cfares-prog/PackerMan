using Godot;
using System;

public partial class Global : Node
{
    [Signal]
    public delegate void ScoreChangedSigEventHandler(int newScore);
    [Signal]
    public delegate void PackerHitSigEventHandler();
    [Signal]
    public delegate void PowerUpSigEventHandler();
    [Signal]
    public delegate void GhostFleeSigEventHandler();
    [Signal]
    public delegate void GhostChaseSigEventHandler();

    
    public int Score { get; private set; }

	public override void _Ready() {
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
		Score = 0;
        EmitSignal(SignalName.PackerHitSig);
    }

}
