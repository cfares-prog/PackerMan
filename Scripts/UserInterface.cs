using Godot;
using System;

public partial class UserInterface : Control
{
    private Global gameManager;
	private Label timeComp;
	private Label scoreComp;
	private Label lifeComp;
	private int _time;
	
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		timeComp= GetNode<Label>("GridContainer/Time");
		scoreComp= GetNode<Label>("GridContainer/Score");
		lifeComp= GetNode<Label>("GridContainer/Life");
		
        // Connect to the global signal
        gameManager = GetNode<Global>("/root/Global");
        gameManager.ScoreChangedSig += UpdateScore;
		gameManager.LifeLostSig += UpdateLife;

        scoreComp.Text = $"Score: {gameManager.Score}";
        lifeComp.Text = $"Life: {gameManager.Life}";

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
    private void UpdateLife(int newLife)
    {
		if (gameManager.Life < 1)
		{
        	lifeComp.Text = $"Life: Dead";
			return;
		}
        lifeComp.Text = $"Life: {newLife}";
    }
}
