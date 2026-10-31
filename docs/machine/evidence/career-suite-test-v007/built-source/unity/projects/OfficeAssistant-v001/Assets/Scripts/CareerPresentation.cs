using System;
using System.Runtime.InteropServices;
using UnityEngine;

namespace CareerExperience
{
    public static class CareerPresentation
    {
        [Serializable] sealed class Options { public string backgroundColor; }
        [DllImport("__Internal")] static extern void CareerPresentationState(string json);
        static bool configured;
        static Color background;
        static string hex;
        static Camera clearCamera;
        public static Color Background(Color fallback)=>configured?background:fallback;
        public static void Receive(string json)
        {
            Options options=null;try{options=JsonUtility.FromJson<Options>(json);}catch{}
            string value=options?.backgroundColor;bool valid=value!=null&&value.Length==7&&value[0]=='#';
            if(valid)for(int i=1;i<value.Length;i++)if(!Uri.IsHexDigit(value[i]))valid=false;
            if(valid&&ColorUtility.TryParseHtmlString(value,out Color color)){configured=true;background=color;hex=value.ToUpperInvariant();Apply();}
            string response=PilotLedger.Json(PilotLedger.D("accepted",valid,"backgroundColor",hex,"error",valid?null:"INVALID_BACKGROUND_COLOR"));
#if UNITY_WEBGL && !UNITY_EDITOR
            CareerPresentationState(response);
#endif
        }
        public static void Apply()
        {
            if(!configured)return;
            if(clearCamera==null)
            {
                var go=new GameObject("CareerPresentationBackground");UnityEngine.Object.DontDestroyOnLoad(go);clearCamera=go.AddComponent<Camera>();
                clearCamera.cullingMask=0;clearCamera.depth=-10000;clearCamera.rect=new Rect(0,0,1,1);clearCamera.nearClipPlane=.01f;clearCamera.farClipPlane=1;
            }
            clearCamera.backgroundColor=background;clearCamera.clearFlags=CameraClearFlags.SolidColor;
            var main=Camera.main;if(main!=null){main.backgroundColor=background;main.clearFlags=CameraClearFlags.SolidColor;}
        }
    }
}
