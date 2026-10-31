using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace CareerExperience
{
    // Audio is a presentation side channel. It never publishes a business event,
    // consumes a process sequence, changes a draft or contributes to assessment.
    public static class CareerAudio
    {
        [DllImport("__Internal")] static extern void CareerAudioCue(string json);
        public static Action<string> Observer;
        static Dictionary<string,object> current;
        static string run;
        static bool retired,paused,resetPending;
        static readonly Dictionary<string,DateTime> cooldowns=new Dictionary<string,DateTime>();
        static readonly Dictionary<string,int> sheets=new Dictionary<string,int>();
        static readonly HashSet<string> loops=new HashSet<string>();
        public static string CurrentRun=>retired?null:run;
        static string Text(Dictionary<string,object> d,string key)=>d!=null&&d.TryGetValue(key,out object v)?v as string:null;
                static int Priority(string clip,string operation)=>clip=="mission_done"?90:clip=="validation"?80:clip=="hint"?60:operation=="loop_start"||operation=="loop_stop"?10:clip=="ui_click"||clip=="ui_focus"||clip=="field_edit"||clip=="keyboard"||clip=="writing"||clip=="slider_tick"?20:50;
        static void Send(string kind,string clip,string operation="play",string loop=null,string eventId=null,string step=null,string obj=null)
        {
            if(current==null)return;
            string json=PilotLedger.Json(PilotLedger.D("cueId",eventId==null?PilotLedger.NewId("audio-"):eventId+":"+kind+":"+clip,"cueKey",clip,"clipKey",clip,"scope",current,"kind",kind,"operation",operation,"loopId",loop,"stepId",step,"objectId",obj,"priority",Priority(clip,operation)));
            Observer?.Invoke(json);
#if UNITY_WEBGL && !UNITY_EDITOR
            CareerAudioCue(json);
#endif
        }
        public static void Play(string expectedRun,string key,string kind="action",string step=null,string obj=null,int cooldownMs=0)
        {
            if(retired||paused||run!=expectedRun||current==null||string.IsNullOrEmpty(key))return;
            string gate=kind+"|"+key;var now=DateTime.UtcNow;
            if(cooldownMs>0&&cooldowns.TryGetValue(gate,out DateTime until)&&now<until)return;
            if(cooldownMs>0)cooldowns[gate]=now.AddMilliseconds(cooldownMs);
            Send(kind,key,step:step,obj:obj);
        }
        public static void Cancel(string expectedRun,string kind="hidden",string clip=null)
        {
            if(retired||run!=expectedRun||current==null)return;
            loops.Clear();Send(kind,clip,"cancel");
        }
        public static void Loop(string expectedRun,string id,bool start,string key="printer_run")
        {
            if(retired||run!=expectedRun||current==null)return;
            if(start){if(paused||!loops.Add(id))return;Send("run",key,"loop_start",id);}
            else if(loops.Remove(id))Send("stop",key,"loop_stop",id);
        }
        public static void Printing(string expectedRun,string id,bool running,bool isPaused,int produced,bool audible=true)
        {
            if(retired||run!=expectedRun||current==null)return;
            bool first=!sheets.ContainsKey(id);if(first&&!running&&produced==0)return;if(first)sheets[id]=0;
            bool wasLoop=loops.Contains(id);
            if(running&&!isPaused&&!paused&&audible){if(first)Play(expectedRun,"printer_start");Loop(expectedRun,id,true);}
            else Loop(expectedRun,id,false);
            int old=sheets[id];sheets[id]=Math.Max(old,produced);
            if(!isPaused&&!paused&&audible)for(int i=old;i<produced;i++)Play(expectedRun,"printer_sheet","sheet");
            if(!running&&wasLoop&&audible)Play(expectedRun,"printer_stop");
        }
        public static void Edit(string expectedRun,string control,string surfaceKind,string objectName="")
        {
            string key=control.StartsWith("field")?(objectName.Contains("모니터")||objectName.Contains("노트북")||objectName.Contains("컴퓨터")?"keyboard":objectName.Contains("메모")||objectName.Contains("보드")||objectName.Contains("칠판")?"writing":"field_edit"):control.StartsWith("question")||control.StartsWith("observe")||control.StartsWith("finding")?"toggle":control.StartsWith("slider")||control.StartsWith("value")?"slider_tick":"card_move";
            Play(expectedRun,key,"edit",cooldownMs:control.StartsWith("field")?180:90);
        }
        public static bool Assembly(string kind)=>kind=="assembly"||kind=="assemble";
        public static void Event(Dictionary<string,object> e,string surfaceKind=null,string objectName=null,bool editsAlreadySounded=false)
        {
            string type=Text(e,"type"),incoming=Text(e,"scenarioRunId"),action=Text(e,"action"),id=Text(e,"eventId"),step=Text(e,"stepId"),obj=Text(e,"objectId");
            if(type=="scenario.started")
            {
                current=PilotLedger.D("sessionId",Text(e,"sessionId"),"experienceId",Text(e,"experienceId"),"scenarioRunId",incoming,"scenarioId",Text(e,"scenarioId"),"scenarioVersion",Text(e,"scenarioVersion"),"roomId",Text(e,"roomId"));
                run=incoming;retired=paused=false;cooldowns.Clear();sheets.Clear();loops.Clear();Send("start",null,"cancel",eventId:id);
                if(resetPending){resetPending=false;Play(run,"reset");}return;
            }
            if(current==null||incoming!=run||retired)return;
            if(type=="scenario.paused"){Cancel(run,"pause","pause");paused=true;return;}
            if(type=="scenario.resumed"){paused=false;Send("resume","resume",eventId:id);return;}
            bool cabinet=obj=="cabinet"||(objectName??"").Contains("수납")||(objectName??"").Contains("캐비닛")||(objectName??"").Contains("서랍");
            if(type=="interaction.closed"){Cancel(run,"close",cabinet?"drawer_close":"view_close");return;}
            if(type=="scene.exited"){Cancel(run,"scene");return;}
            if(type=="scenario.reset"||type=="experience.ended")
            {
                bool reset=type=="scenario.reset";resetPending=reset;Cancel(run,reset?"reset":"ended",reset?null:"exit");retired=true;return;
            }
            if(type=="request.changed"){Cancel(run,"request_change");Play(run,"request_change");return;}
            if(paused)return;
            string clip=null;
            switch(type)
            {
                case "object.selected":clip="object_select";break;
                case "interaction.opened":clip="view_open";if(cabinet)Play(run,"drawer_open");if((objectName??"").Contains("전화"))Play(run,"phone_pick");if((objectName??"").Contains("무전"))Play(run,"radio");break;
                case "interaction.validation_failed":clip="validation";break;
                case "interaction.retry_requested":clip="retry";break;
                case "guidance.presented":clip="hint";break;
                case "scenario.completed":Cancel(run,"complete");clip="mission_done";break;
                case "interaction.completed":
                    clip=surfaceKind=="photo"?"shutter":surfaceKind=="timer"?"timer_done":action=="file"?"file_place":action=="handoff"?"handoff_send":action=="save"||surfaceKind=="form"?"save":"step_done";break;
                case "interaction.progress":
                    if(action=="edit_field"&&!editsAlreadySounded)Play(run,obj=="monitor"?"keyboard":"field_edit","edit",cooldownMs:180);
                    if(action=="place_item")Play(run,"file_place");
                    break;
            }
            if(clip!=null)Send(type,clip,eventId:id,step:step,obj:obj);
        }
    }
}
