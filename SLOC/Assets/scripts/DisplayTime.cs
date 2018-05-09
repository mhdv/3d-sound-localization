using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using System;

public class DisplayTime : MonoBehaviour {

    private string time;
    private string[] preciseTime;
    public GameObject timeObject;
    private TextMeshProUGUI tmptext;
    public int realTime = 0;
    float nextTime = 0;
    float interval = 0.01f;

    public IEnumerator getTime()
    {
        WWW url = new WWW("http://mhdv.pl/date.php");
        yield return url;
        time = url.text;
        time = time.Remove(time.Length - 4);
    }

	// Use this for initialization
	void Start () {
        StartCoroutine(getTime());
        tmptext = timeObject.GetComponent<TextMeshProUGUI>();
    }

    private string realTimeToString() {
        string tmp = "";
        if ((realTime / (60 * 60 * 100)) < 10)
            tmp += "0" + (realTime / (60 * 60 * 100)).ToString() + ":";
        else
            tmp += (realTime / (60 * 60 * 100)).ToString() + ":";
        if ((realTime / (60 * 100) % (60)) < 10)
            tmp += "0" + (realTime / (60 * 100) % (60)).ToString() + ":";
        else
            tmp += (realTime / (60 * 100) % (60)).ToString() + ":";
        if (((realTime % (60 * 100)) / 100) < 10)
            tmp += "0" + ((realTime % (60 * 100)) / 100).ToString();
        else
            tmp += ((realTime % (60 * 100)) / 100).ToString();
        /*if (((realTime % (60 * 100)) / 100) < 10)
            return (realTime / (60 * 60 * 100)).ToString()
                    + ":" + (realTime / (60 * 100) % (60)).ToString()
                    + ":0" + ((realTime % (60 * 100)) / 100).ToString();
        else
            return (realTime / (60 * 60 * 100)).ToString()
                    + ":" + (realTime / (60 * 100) % (60)).ToString()
                    + ":" + ((realTime % (60 * 100)) / 100).ToString();*/
        return tmp;
    }

    // Update is called once per frame
    void Update()
    {
        if (Time.time >= nextTime)
        {
            if (nextTime < 1)
            {
                preciseTime = time.Split(':');
                realTime = Int32.Parse(preciseTime[0]) * 60 * 60 * 100
                    + Int32.Parse(preciseTime[1]) * 60 * 100
                    + Int32.Parse(preciseTime[2].Split('.')[0]) * 100
                    + Int32.Parse(preciseTime[2].Split('.')[1]);
            }
            Debug.Log(realTime);
            tmptext.text = realTimeToString();
            nextTime += interval;
            realTime += 1;
        }
    }
}
