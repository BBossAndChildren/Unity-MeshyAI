using System;
using UnityEngine;

namespace CareerExperience
{
    // One resource is written by the build profile; game rules are shared.
    public static class CareerSuiteMode
    {
        [Serializable] public sealed class Settings
        {
            public bool integrationOnly;
            public string buildId,officeDirectScenePath,officeTenScenePath;
        }
        static Settings settings;
        static bool loaded,managed;
        static Settings Current
        {
            get
            {
                if(!loaded)
                {
                    loaded=true;var resource=Resources.Load<TextAsset>("career-suite-settings");
                    managed=resource!=null;settings=resource==null?new Settings():JsonUtility.FromJson<Settings>(resource.text);
                }
                return settings;
            }
        }
        public static bool Managed { get { var ignored=Current;return managed; } }
        public static bool IntegrationOnly=>Current.integrationOnly;
        public static string BuildId(string fallback)=>string.IsNullOrEmpty(Current.buildId)?fallback:Current.buildId;
        public static string DirectScene=>string.IsNullOrEmpty(Current.officeDirectScenePath)?"Assets/Scenes/OfficeAssistantDirect.unity":Current.officeDirectScenePath;
        public static string TenScene=>string.IsNullOrEmpty(Current.officeTenScenePath)?"Assets/Scenes/OfficeTen.unity":Current.officeTenScenePath;
        public static bool IsOfficeScene(string path)=>path==DirectScene||path==TenScene;
    }
}
