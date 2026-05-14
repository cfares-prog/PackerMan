using Godot;
using System;

public partial class UserInterface : Control
{
    private Global gameManager;
	private Label timeComp;
	private Label scoreComp;
	
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		timeComp= GetNode<Label>("GridContainer/Time");
		scoreComp= GetNode<Label>("GridContainer/Score");
		
        // Connect to the global signal
        gameManager = GetNode<Global>("/root/Global");
        gameManager.ScoreChangedSig += UpdateScore;
        gameManager.PackerHitSig += ResetGame;

        scoreComp.Text = $"Score: {gameManager.Score}";

		base._Ready();
	}

	private void TimerIter()
	{
        gameManager.time++;
        gameManager.AddScore(1);
        int minutes = gameManager.time / 60;
        int seconds = gameManager.time % 60;

        timeComp.Text = string.Format("Time: {0:00}:{1:00}", minutes, seconds);
	}
    private void UpdateScore(int newScore)
    {
        scoreComp.Text = $"Score: {newScore}";
    }

    private void ResetGame()
    {
        gameManager.ScoreChangedSig -= UpdateScore;
        gameManager.PackerHitSig -= ResetGame;
    }
}
