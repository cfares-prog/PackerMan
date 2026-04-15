using Godot;
using System;

public partial class UserInterface : Control
{
	private Label timeComp;
	private Label scoreComp;
	private int _time;
	
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		timeComp= GetNode<Label>("GridContainer/Time");
		scoreComp= GetNode<Label>("GridContainer/Score");
		
        // Connect to the global signal
        var gameManager = GetNode<Global>("/root/Global");
        gameManager.ScoreChanged += UpdateScore;
        scoreComp.Text = $"Score: {gameManager.Score}";

		base._Ready();
	}

	private void TimerIter()
	{
        _time++;
        
        // Calculate minutes and seconds
        int minutes = _time / 60;
        int seconds = _time % 60;

        // Update the label text with "MM:SS" formatting
        timeComp.Text = string.Format("{0:00}:{1:00}", minutes, seconds);
	}
    private void UpdateScore(int newScore)
    {
        scoreComp.Text = $"Score: {newScore}";
    }
}
