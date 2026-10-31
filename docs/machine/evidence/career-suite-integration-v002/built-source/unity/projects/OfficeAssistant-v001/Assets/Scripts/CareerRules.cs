using System;
using System.Collections.Generic;
using System.Linq;

namespace CareerExperience
{
    // Reusable predicates. Scenario values belong to data, never to these rules.
    public static class CareerRules
    {
        public static bool Dialogue(IEnumerable<string> required, ISet<string> known, bool acknowledged)
            => acknowledged && required.All(known.Contains);
        public static bool Inspection(string actual, string expected) => actual == expected;
        public static bool Sequence(bool[] prerequisites) => prerequisites.All(p => p);
        public static bool Classification(string selected, string expected) => selected == expected;
    }

    [Serializable] public sealed class OfficeData
    {
        public int schema_version;
        public string scenario_id, occupation_id, request_id, document_id, document_title;
        public string initial_date, expected_date, expected_folder;
        public int base_copies, changed_copies;
        public string[] required_slots, folders;
        public float print_seconds;
    }
    public enum OfficeStage { request_pending, request_confirmed, document_saved, printing, print_ready, filed, complete }
    [Serializable] public sealed class DocumentRevision
    {
        public int revision;
        public string title, date;
        public bool saved;
    }
    [Serializable] public sealed class OfficeSnapshot
    {
        public string state, message;
        public int requestRevision, confirmedRequestRevision, documentRevision, savedRevision;
        public int expectedCopies, printCompletions, printedCopies, printedDocumentRevision, printedRequestRevision, run;
        public bool paused, changed, complete;
        public string date, title, printedDocumentId, folder;
    }

    // Pure C# state machine: shared by the actual player and deterministic acceptance cases.
    public sealed class OfficeSession
    {
        public readonly OfficeData Data;
        public OfficeStage Stage { get; private set; }
        public int RequestRevision { get; private set; }
        public int ConfirmedRequestRevision { get; private set; }
        public int DocumentRevision { get; private set; }
        public int SavedRevision { get; private set; }
        public int ExpectedCopies { get; private set; }
        public int PrintCompletions { get; private set; }
        public int PrintedCopies { get; private set; }
        public int PrintedDocumentRevision { get; private set; }
        public int PrintedRequestRevision { get; private set; }
        public int Run { get; private set; }
        public bool Paused { get; private set; }
        public bool ChangePractice { get; private set; }
        public bool Changed { get; private set; }
        public string Date { get; private set; }
        public string Title { get; private set; }
        public string PrintedDocumentId { get; private set; }
        public string Folder { get; private set; }
        public string Message { get; private set; }
        public float PrintProgress => Stage == OfficeStage.printing ? elapsed / Data.print_seconds : PrintCompletions > 0 ? 1 : 0;
        public readonly HashSet<string> KnownSlots = new HashSet<string>();
        public readonly List<DocumentRevision> History = new List<DocumentRevision>();
        public readonly List<string> Events = new List<string>();
        float elapsed;
        public OfficeSession(OfficeData data) { Data = data; Reset(false); }
        bool Tell(string message, bool success = false) { Message = message; Events.Add(Stage + ": " + message); return success; }
        bool Writable() => !Paused && Stage != OfficeStage.complete;
        bool Guard(bool allowed, string error)
        {
            if (!Writable()) return Tell(Paused ? "일시정지 중입니다. 계속하기를 선택하세요." : "이미 인계가 완료되었습니다. 새 연습은 전체 초기화로 시작하세요.");
            return allowed || Tell(error);
        }
        public void Reset(bool changePractice)
        {
            Run++; Stage = OfficeStage.request_pending; RequestRevision = 1; ConfirmedRequestRevision = 0;
            DocumentRevision = SavedRevision = 1; ExpectedCopies = Data.base_copies;
            Title = Data.document_title; Date = Data.initial_date; Folder = PrintedDocumentId = null;
            PrintCompletions = PrintedCopies = PrintedDocumentRevision = PrintedRequestRevision = 0;
            Paused = Changed = false; ChangePractice = changePractice; elapsed = 0;
            KnownSlots.Clear(); History.Clear(); Events.Clear();
            History.Add(new DocumentRevision { revision = 1, title = Title, date = Date, saved = true });
            Tell("동료: 회의자료 출력을 부탁드려요. 모니터에서 빠진 요청을 먼저 확인하세요.");
        }
        public void TogglePause() { Paused = !Paused; Tell(Paused ? "일시정지 — 출력 진행도 함께 멈췄습니다." : "연습을 계속합니다."); }
        public string ExpectedObject => Stage <= OfficeStage.document_saved ? "monitor" : Stage <= OfficeStage.printing ? "copier" : "cabinet";
        public bool SelectObject(string id)
        {
            bool monitor = id == "monitor" && Stage <= OfficeStage.document_saved;
            bool copier = id == "copier" && (Stage == OfficeStage.document_saved || Stage == OfficeStage.printing);
            bool cabinet = id == "cabinet" && (Stage == OfficeStage.print_ready || Stage == OfficeStage.filed);
            return Guard(monitor || copier || cabinet, "순서 안내: 요청 확인·날짜 수정 저장 → 복합기 출력 → 수납장 보관·인계 순서입니다.");
        }
        public bool Ask(string slot)
        {
            if (!Guard(Stage == OfficeStage.request_pending, "현재 요청은 확인되었습니다.")) return false;
            if (!Data.required_slots.Contains(slot)) return Tell("필요한 자료·부수·보관처를 질문하세요.");
            KnownSlots.Add(slot);
            return Tell(slot == "document_id" ? "동료: " + Data.document_id + " ‘" + Data.document_title + "’입니다. 회의일은 " + Data.expected_date + "이에요."
                : slot == "copies" ? "동료: " + ExpectedCopies + "부 부탁드려요."
                : "동료: ‘" + Data.expected_folder + "’ 칸에 보관하고 결과도 알려주세요.", true);
        }
        public bool Confirm(bool acknowledgement)
        {
            if (!Guard(Stage == OfficeStage.request_pending, "이미 확인한 요청입니다.")) return false;
            if (!CareerRules.Dialogue(Data.required_slots, KnownSlots, acknowledgement))
                return Tell("자료·부수·보관처를 모두 질문한 뒤 요약하고 동료의 확인을 받으세요.");
            ConfirmedRequestRevision = RequestRevision;
            Stage = SavedRevision == DocumentRevision && Date == Data.expected_date && Title == Data.document_title
                ? OfficeStage.document_saved : OfficeStage.request_confirmed;
            return Tell("동료: 네, 요청 요약이 맞아요. " + ExpectedCopies + "부, " + Data.expected_date + ", " + Data.expected_folder + " 칸입니다.", true);
        }
        public bool Edit(string title, string date)
        {
            if (!Guard(Stage == OfficeStage.request_confirmed || Stage == OfficeStage.document_saved, "모니터에서 요청 확인을 먼저 마치세요. 출력 후에는 편집할 수 없습니다.")) return false;
            if (Title == title && Date == date) return Tell("이미 같은 내용입니다. 수정 후 저장 여부를 확인하세요.");
            Title = title; Date = date; DocumentRevision++; Stage = OfficeStage.request_confirmed;
            History.Add(new DocumentRevision { revision = DocumentRevision, title = Title, date = Date });
            return Tell("문서 r" + DocumentRevision + " 편집 중 — 아직 저장되지 않았습니다.", true);
        }
        public bool Save()
        {
            if (!Guard(Stage == OfficeStage.request_confirmed, "요청 확인 후 날짜를 수정하고 저장하세요.")) return false;
            if (!CareerRules.Inspection(Title, Data.document_title)) return Tell("제목이 요청과 다릅니다. 제목을 유지하고 날짜 오류를 확인하세요.");
            if (!CareerRules.Inspection(Date, Data.expected_date)) return Tell("날짜 오류: 요청의 " + Data.expected_date + "과 문서 날짜를 비교해 수정하세요.");
            SavedRevision = DocumentRevision;
            History[History.Count - 1].saved = true;
            Stage = OfficeStage.document_saved;
            if (ChangePractice && !Changed)
            {
                Changed = true; RequestRevision++; ExpectedCopies = Data.changed_copies;
                ConfirmedRequestRevision = 0; KnownSlots.Clear(); Stage = OfficeStage.request_pending;
                return Tell("동료의 변경 요청: " + ExpectedCopies + "부로 바꿔 주세요. 요청 r" + RequestRevision + "을 모니터에서 다시 확인하세요.", true);
            }
            return Tell("최신 문서 r" + SavedRevision + " 저장 완료. 복합기에서 문서와 부수를 선택하세요.", true);
        }
        public bool Print(string documentId, int revision, int copies)
        {
            if (!Guard(Stage == OfficeStage.document_saved, Stage == OfficeStage.printing ? "출력 중입니다. 중복 출력하지 않습니다." : "요청 재확인과 최신 문서 저장을 먼저 마치세요.")) return false;
            if (!CareerRules.Sequence(new[] { ConfirmedRequestRevision == RequestRevision, SavedRevision == DocumentRevision })) return Tell("요청 또는 문서가 바뀌었습니다. 모니터에서 최신 내용을 확인·저장하세요.");
            if (documentId != Data.document_id || revision != SavedRevision) return Tell("문서 오류: 요청의 자료 ID와 최신 저장 revision을 선택하세요.");
            if (copies != ExpectedCopies) return Tell("부수 오류: 확인된 최신 요청은 " + ExpectedCopies + "부입니다. 출력 전에 부수를 맞추세요.");
            if (Date != Data.expected_date || Title != Data.document_title) return Tell("날짜·제목을 수정하고 저장하세요.");
            PrintedDocumentId = documentId; PrintedDocumentRevision = revision; PrintedRequestRevision = RequestRevision; PrintedCopies = copies;
            elapsed = 0; Stage = OfficeStage.printing;
            return Tell("출력 중… 완료될 때까지 기다려 주세요.", true);
        }
        public void Tick(float deltaSeconds)
        {
            if (Paused || Stage != OfficeStage.printing || deltaSeconds <= 0) return;
            elapsed += deltaSeconds;
            if (elapsed < Data.print_seconds) return;
            Stage = OfficeStage.print_ready; PrintCompletions++;
            Tell("출력 " + PrintedCopies + "부 완료. 뒤쪽 수납장의 회의자료 칸에 보관하세요.", true);
        }
        public bool File(string folder)
        {
            if (!Guard(Stage == OfficeStage.print_ready, "출력 완료 후 수납장에 보관하세요. 이미 보관했다면 인계를 마치세요.")) return false;
            if (!CareerRules.Classification(folder, Data.expected_folder)) return Tell("분류 오류: 회의자료는 ‘" + Data.expected_folder + "’ 칸에 보관합니다. 다른 칸에는 확정하지 않았습니다.");
            Folder = folder; Stage = OfficeStage.filed;
            return Tell("보관 완료. 제목·날짜·부수·보관처를 동료에게 요약해 인계하세요.", true);
        }
        public bool Handoff(string title, string date, int copies, string folder, bool acknowledgement)
        {
            if (!Guard(Stage == OfficeStage.filed, "보관 후 동료에게 인계해야 완료됩니다.")) return false;
            if (!CareerRules.Sequence(new[] { title == Data.document_title, date == Data.expected_date, copies == ExpectedCopies, folder == Data.expected_folder, acknowledgement,
                PrintedDocumentId == Data.document_id, PrintedDocumentRevision == DocumentRevision, PrintedRequestRevision == RequestRevision, PrintedCopies == ExpectedCopies }))
                return Tell("인계 내용이 빠졌거나 요청과 다릅니다. 제목·회의일·부수·보관 칸을 확인하고 상대 확인을 받으세요.");
            Stage = OfficeStage.complete;
            return Tell("동료: 요청한 자료와 보관 위치를 확인했어요. 감사합니다! 요청 확인과 정확한 인계를 마쳤습니다.", true);
        }
        public OfficeSnapshot Snapshot() => new OfficeSnapshot {
            state = Stage.ToString(), message = Message, requestRevision = RequestRevision, confirmedRequestRevision = ConfirmedRequestRevision,
            documentRevision = DocumentRevision, savedRevision = SavedRevision, expectedCopies = ExpectedCopies, printCompletions = PrintCompletions,
            printedCopies = PrintedCopies, printedDocumentRevision = PrintedDocumentRevision, printedRequestRevision = PrintedRequestRevision,
            run = Run, paused = Paused, changed = Changed, complete = Stage == OfficeStage.complete, date = Date, title = Title, printedDocumentId = PrintedDocumentId, folder = Folder
        };
    }
}
