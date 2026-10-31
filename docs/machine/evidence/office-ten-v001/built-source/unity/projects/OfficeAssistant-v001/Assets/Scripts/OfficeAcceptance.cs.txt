using System;
using System.Collections.Generic;

namespace CareerExperience
{
    [Serializable] public sealed class AcceptanceCase { public string name, status, evidence; }
    [Serializable] public sealed class AcceptanceReport { public int schema_version = 3; public string scope = "Actual C# state machine execution; UI/input requires separate runtime checks"; public List<AcceptanceCase> cases = new List<AcceptanceCase>(); public int passed, failed; }
    public static class OfficeAcceptance
    {
        static void Require(bool ok, string message) { if (!ok) throw new Exception(message); }
        static void Confirm(OfficeSession s) { foreach (string slot in s.Data.required_slots) Require(s.Ask(slot), slot); Require(s.Confirm(true), "confirmation"); }
        static void Save(OfficeSession s) { Require(s.Edit(s.Data.document_title, s.Data.expected_date), "edit"); Require(s.Save(), "save"); }
        static void Print(OfficeSession s) { Require(s.Print(s.Data.document_id, s.SavedRevision, s.ExpectedCopies), "print"); s.Tick(s.Data.print_seconds + .1f); }
        static void Finish(OfficeSession s) { Require(s.File(s.Data.expected_folder), "file"); Require(s.Handoff(s.Data.document_title, s.Data.expected_date, s.ExpectedCopies, s.Data.expected_folder, true), "handoff"); }
        public static AcceptanceReport Run(OfficeData data)
        {
            var report = new AcceptanceReport();
            Action<string, Action<OfficeSession>> test = (name, run) => {
                try { var s = new OfficeSession(data); run(s); report.cases.Add(new AcceptanceCase { name = name, status = "pass", evidence = "Assertions executed against OfficeSession" }); report.passed++; }
                catch (Exception e) { report.cases.Add(new AcceptanceCase { name = name, status = "fail", evidence = e.Message }); report.failed++; }
            };
            test("base_success_2_copies", s => { Confirm(s); Save(s); Print(s); Require(s.Stage == OfficeStage.print_ready, "print ready"); Require(!s.Handoff(data.document_title, data.expected_date, 2, data.expected_folder, true), "must file first"); Finish(s); Require(s.Stage == OfficeStage.complete && s.PrintCompletions == 1 && s.PrintedCopies == 2, "complete snapshot"); });
            test("missing_request_slots_and_ack", s => { Require(!s.Confirm(true), "missing slots"); s.Ask("copies"); Require(!s.Confirm(true), "two slots missing"); s.Ask("document_id"); s.Ask("folder"); Require(!s.Confirm(false), "missing ack"); Require(s.Confirm(true), "confirmed"); });
            test("date_and_title_error_and_unsaved_revision", s => { Confirm(s); Require(!s.Save(), "initial wrong date"); s.Edit("팀 회의자료 초안", data.expected_date); Require(!s.Save(), "wrong title"); s.Edit(data.document_title, data.expected_date); Require(!s.Print(data.document_id, s.DocumentRevision, 2), "unsaved must not print"); Require(s.Save(), "correct save"); });
            test("wrong_copies_file_and_stale_document", s => { Confirm(s); Save(s); Require(!s.Print(data.document_id, s.SavedRevision, 1), "wrong copies"); Require(!s.Print("DOC-OLD", s.SavedRevision, 2), "wrong file"); Require(!s.Print(data.document_id, 1, 2), "stale revision"); Require(s.Stage == OfficeStage.document_saved && s.PrintCompletions == 0, "no mutation"); Print(s); });
            test("wrong_classification_and_handoff", s => { Confirm(s); Save(s); Print(s); Require(!s.File("인사자료"), "wrong folder"); Require(s.Stage == OfficeStage.print_ready && s.Folder == null, "no filing"); s.File(data.expected_folder); Require(!s.Handoff(data.document_title, data.initial_date, 2, data.expected_folder, true), "wrong handoff date"); Require(!s.Handoff(data.document_title, data.expected_date, 2, data.expected_folder, false), "receiver ack required"); Require(s.Handoff(data.document_title, data.expected_date, 2, data.expected_folder, true), "retry"); });
            test("sequence_violation_and_wrong_object", s => { Require(!s.SelectObject("copier"), "copier locked"); Require(!s.SelectObject("cabinet"), "cabinet locked"); Require(!s.File(data.expected_folder), "file locked"); Require(!s.Print(data.document_id, 1, 2), "print locked"); Require(s.Stage == OfficeStage.request_pending, "unchanged"); });
            test("request_change_3_copies_reconfirmation", s => { s.Reset(true); Confirm(s); Save(s); Require(s.RequestRevision == 2 && s.ConfirmedRequestRevision == 0 && s.ExpectedCopies == 3, "revision invalidated"); Require(!s.Print(data.document_id, s.SavedRevision, 3), "reconfirm required"); Confirm(s); Require(s.Stage == OfficeStage.document_saved, "saved doc retained"); Require(!s.Print(data.document_id, s.SavedRevision, 2), "old copies"); Print(s); Finish(s); Require(s.PrintedCopies == 3 && s.PrintedRequestRevision == 2, "latest request"); });
            test("printing_duplicate_and_pause", s => { Confirm(s); Save(s); s.Print(data.document_id, s.SavedRevision, 2); Require(!s.Print(data.document_id, s.SavedRevision, 2), "duplicate"); s.TogglePause(); s.Tick(99); Require(s.Stage == OfficeStage.printing && s.PrintCompletions == 0, "pause freezes"); s.TogglePause(); s.Tick(data.print_seconds); s.Tick(99); Require(s.PrintCompletions == 1, "one completion"); });
            test("completed_reclick_is_idempotent", s => { Confirm(s); Save(s); Print(s); Finish(s); Require(!s.Print(data.document_id, s.SavedRevision, 2), "completed print"); Require(!s.File(data.expected_folder), "completed file"); Require(!s.Handoff(data.document_title, data.expected_date, 2, data.expected_folder, true), "completed handoff"); Require(s.Stage == OfficeStage.complete && s.PrintCompletions == 1, "stable completion"); });
            test("reset_during_print_and_after_complete", s => { Confirm(s); Save(s); s.Print(data.document_id, s.SavedRevision, 2); int run = s.Run; s.Reset(false); s.Tick(99); Require(s.Stage == OfficeStage.request_pending && s.Run == run + 1 && s.PrintCompletions == 0 && s.PrintedCopies == 0 && s.History.Count == 1 && s.KnownSlots.Count == 0 && s.SavedRevision == 1 && !s.Paused, "reset clears state"); Confirm(s); Save(s); Print(s); Finish(s); s.Reset(true); Require(s.Stage == OfficeStage.request_pending && s.RequestRevision == 1 && !s.Changed && s.ExpectedCopies == 2, "reset changed path"); });
            return report;
        }
    }
}
