using System;
using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class StartTime : MonoBehaviour {
    
    public GameObject timeObject;
    private TextMeshProUGUI tmptext;
    private string[] splitTime;
    public int realTime;

    // Use this for initialization
    void Start () {
        tmptext = timeObject.GetComponent<TextMeshProUGUI>();
        splitTime = tmptext.text.Split(':');
    }
	
    void updateTime()
    {
        tmptext.text = splitTime[0] + ":" + splitTime[1] + ":" + splitTime[2];
        realTime = Int32.Parse(splitTime[0]) * 60 * 60 * 100
                    + Int32.Parse(splitTime[1]) * 60 * 100
                    + Int32.Parse(splitTime[2].Split('.')[0]) * 100;
    }

    public void plusHour()
    {
        int hour = Int32.Parse(splitTime[0]);
        if (hour == 23)
            hour = 0;
        else
            ++hour;
        if(hour < 10)
            splitTime[0] = "0" + hour.ToString();
        else
            splitTime[0] = hour.ToString();
        updateTime();
    }
    public void minusHour()
    {
        int hour = Int32.Parse(splitTime[0]);
        if (hour == 0)
            hour = 23;
        else
            --hour;
        if (hour < 10)
            splitTime[0] = "0" + hour.ToString();
        else
            splitTime[0] = hour.ToString();
        updateTime();
    }

    public void plusMinutes()
    {
        int hour = Int32.Parse(splitTime[1]);
        if (hour == 59)
            hour = 0;
        else
            ++hour;
        if (hour < 10)
            splitTime[1] = "0" + hour.ToString();
        else
            splitTime[1] = hour.ToString();
        updateTime();
    }
    public void minusMinutes()
    {
        int hour = Int32.Parse(splitTime[1]);
        if (hour == 0)
            hour = 59;
        else
            --hour;
        if (hour < 10)
            splitTime[1] = "0" + hour.ToString();
        else
            splitTime[1] = hour.ToString();
        updateTime();
    }

    public void plusSeconds()
    {
        int hour = Int32.Parse(splitTime[2]);
        if (hour == 59)
            hour = 0;
        else
            ++hour;
        if (hour < 10)
            splitTime[2] = "0" + hour.ToString();
        else
            splitTime[2] = hour.ToString();
        updateTime();
    }
    public void minusSeconds()
    {
        int hour = Int32.Parse(splitTime[2]);
        if (hour == 0)
            hour = 59;
        else
            --hour;
        if (hour < 10)
            splitTime[2] = "0" + hour.ToString();
        else
            splitTime[2] = hour.ToString();
        updateTime();
    }
}
