using Godot;
using System;

public partial class UserInterface : Control
{
    private Global gameManager;
	private Label timeComp;
	private Label scoreComp;
	private int _time;
	
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		timeComp= GetNode<Label>("GridContainer/Time");
		scoreComp= GetNode<Label>("GridContainer/Score");
		
        // Connect to the global signal
        gameManager = GetNode<Global>("/root/Global");
        gameManager.ScoreChangedSig += UpdateScore;

        scoreComp.Text = $"Score: {gameManager.Score}";

		base._Ready();
	}

	private void TimerIter()
	{
        _time++;
        int minutes = _time / 60;
        int seconds = _time % 60;

        timeComp.Text = string.Format("Time: {0:00}:{1:00}", minutes, seconds);
	}
    private void UpdateScore(int newScore)
    {
        scoreComp.Text = $"Score: {newScore}";
    }
}
