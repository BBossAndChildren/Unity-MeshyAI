using System;
using System.Linq;
using UnityEngine;
using UnityEngine.Rendering;

namespace CareerExperience
{
    // Actual existing 3D product rendered into the camera-owned UI viewfinder.
    // No mesh/material clone, palette tint or model texture replacement occurs.
    public sealed class PilotPhoto : IDisposable
    {
        Camera preview;
        RenderTexture target;
        public Texture Viewfinder=>target;
        public string Error { get; private set; }
        public bool Render(PilotDefinition career,Camera original,Vector3 overviewPosition,float fov,float horizontal,float lighting)
        {
            if(SystemInfo.graphicsDeviceType==GraphicsDeviceType.Null){Error="그래픽 장치가 없어 사진 미리보기를 만들 수 없습니다.";return false;}
            var subject=UnityEngine.Object.FindObjectsByType<Transform>(FindObjectsSortMode.None).FirstOrDefault(t=>t.name==career.photoSubject?.nodeName);
            var table=UnityEngine.Object.FindObjectsByType<Transform>(FindObjectsSortMode.None).FirstOrDefault(t=>t.name==career.objects[0].nodeName);
            if(subject==null||table==null||original==null){Error="촬영 대상 연결을 확인하지 못했습니다.";return false;}
            var pieces=subject.GetComponentsInChildren<Renderer>();if(pieces.Length==0){Error="촬영 대상의 메시가 없습니다.";return false;}
            if(preview==null)
            {
                var go=new GameObject("PilotPhotoViewfinder");UnityEngine.Object.DontDestroyOnLoad(go);preview=go.AddComponent<Camera>();preview.enabled=false;
                target=new RenderTexture(320,180,24,RenderTextureFormat.ARGB32){name="Camera work UI preview",useMipMap=false,autoGenerateMips=false};target.Create();
            }
            Bounds bounds=pieces[0].bounds;foreach(var piece in pieces)bounds.Encapsulate(piece.bounds);
            preview.CopyFrom(original);preview.enabled=false;preview.targetTexture=target;preview.rect=new Rect(0,0,1,1);preview.aspect=320f/180;
            preview.orthographic=false;preview.fieldOfView=fov;preview.nearClipPlane=.01f;preview.farClipPlane=100;preview.clearFlags=CameraClearFlags.SolidColor;preview.backgroundColor=new Color(.06f,.08f,.09f,1);
            var direction=(overviewPosition-bounds.center).normalized;float radius=Mathf.Max(.05f,bounds.extents.magnitude);float distance=radius/Mathf.Sin(35*.5f*Mathf.Deg2Rad)*1.4f;
            Quaternion rotation=Quaternion.LookRotation(-direction);Vector3 centre=bounds.center+(rotation*Vector3.right)*horizontal*radius*2;
            preview.transform.SetPositionAndRotation(centre+direction*distance,rotation);
            var renderers=UnityEngine.Object.FindObjectsByType<Renderer>(FindObjectsSortMode.None);var flags=renderers.Select(r=>r.enabled).ToArray();
            var lights=UnityEngine.Object.FindObjectsByType<Light>(FindObjectsSortMode.None);var intensities=lights.Select(l=>l.intensity).ToArray();
            try
            {
                foreach(var renderer in renderers)renderer.enabled=renderer.transform.IsChildOf(subject)||renderer.transform.IsChildOf(table);
                for(int i=0;i<lights.Length;i++)lights[i].intensity=intensities[i]*Mathf.Clamp(lighting,.1f,2);
                preview.Render();Error=null;return true;
            }
            catch(Exception e){Error="사진 미리보기 오류: "+e.Message;return false;}
            finally
            {
                for(int i=0;i<renderers.Length;i++)if(renderers[i]!=null)renderers[i].enabled=flags[i];
                for(int i=0;i<lights.Length;i++)if(lights[i]!=null)lights[i].intensity=intensities[i];
            }
        }
        public byte[] Capture()
        {
            if(target==null)return null;var previous=RenderTexture.active;Texture2D image=null;
            try{RenderTexture.active=target;image=new Texture2D(target.width,target.height,TextureFormat.RGB24,false);image.ReadPixels(new Rect(0,0,target.width,target.height),0,0);image.Apply();return image.EncodeToPNG();}
            finally{RenderTexture.active=previous;if(image!=null)UnityEngine.Object.Destroy(image);}
        }
        public void Dispose()
        {
            if(target!=null){target.Release();UnityEngine.Object.Destroy(target);target=null;}
            if(preview!=null){UnityEngine.Object.Destroy(preview.gameObject);preview=null;}
        }
    }
}
