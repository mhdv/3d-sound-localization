using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;


public class StartRecording : MonoBehaviour {

    public GameObject evenSystem;
    public GameObject leftTime;
    private int realTimeInt;
    private int setTimeInt;
    private int leftTimeInt;
    private bool properTime = true;
    private bool isRecording = false;
    private int recordTime = 5;
    private AudioClip recordedAudio;

    // Use this for initialization
    void Start () {
        realTimeInt = evenSystem.GetComponent<DisplayTime>().realTime;
        setTimeInt = evenSystem.GetComponent<StartTime>().realTime;
        leftTimeInt = setTimeInt - realTimeInt;
        if (leftTimeInt < 1)
        {
            leftTime.GetComponent<TextMeshProUGUI>().text = "BAD TIME SETTED";
            properTime = false;
        }
        else
            leftTime.GetComponent<TextMeshProUGUI>().text = ((leftTimeInt / 100)+1).ToString();
    }

    public void ResetState()
    {
        realTimeInt = evenSystem.GetComponent<DisplayTime>().realTime;
        setTimeInt = evenSystem.GetComponent<StartTime>().realTime;
        leftTimeInt = setTimeInt - realTimeInt;
        if (leftTimeInt < 1)
        {
            leftTime.GetComponent<TextMeshProUGUI>().text = "BAD TIME SETTED";
            properTime = false;
        }
        else
            leftTime.GetComponent<TextMeshProUGUI>().text = ((leftTimeInt / 100) + 1).ToString();
    }
	
	// Update is called once per frame
	void Update () {
        if (properTime)
        {
            realTimeInt = evenSystem.GetComponent<DisplayTime>().realTime;
            setTimeInt = evenSystem.GetComponent<StartTime>().realTime;
            leftTimeInt = setTimeInt - realTimeInt;
            if (leftTimeInt < 1)
            {
                if (!isRecording && leftTime.GetComponent<TextMeshProUGUI>().text != "DONE")
                {
                    recordedAudio = Microphone.Start(null, false, recordTime, 44100);
                    isRecording = true;
                }
                leftTime.GetComponent<TextMeshProUGUI>().text = (recordTime + leftTimeInt/100).ToString();
                if (recordTime + leftTimeInt/100 < 1)
                {
                    leftTime.GetComponent<TextMeshProUGUI>().text = "DONE";
                    SavWav.Save("wavfile.wav", recordedAudio);
                }
            }
            else
                leftTime.GetComponent<TextMeshProUGUI>().text = ((leftTimeInt / 100) + 1).ToString();
        }
        else
        {
            realTimeInt = evenSystem.GetComponent<DisplayTime>().realTime;
            setTimeInt = evenSystem.GetComponent<StartTime>().realTime;
            leftTimeInt = setTimeInt - realTimeInt;
            if (leftTimeInt < 1)
            {
                leftTime.GetComponent<TextMeshProUGUI>().text = "BAD TIME SETTED";
                properTime = false;
            }
            else
                properTime = true;
        }
    }
}
