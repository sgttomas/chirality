import Foundation
import ApplicationServices
let pid=pid_t(Int32(CommandLine.arguments[1])!)
let app=AXUIElementCreateApplication(pid)
func value(_ element: AXUIElement,_ name:String)->CFTypeRef? { var v:CFTypeRef?; let err=AXUIElementCopyAttributeValue(element,name as CFString,&v); return err == .success ? v : nil }
print("trusted",AXIsProcessTrusted())
let windows=value(app,kAXWindowsAttribute) as? [AXUIElement] ?? []
for w in windows {
 let title=value(w,kAXTitleAttribute) as? String ?? "";let doc=value(w,kAXDocumentAttribute) as? String ?? ""
 print(String(data:try! JSONSerialization.data(withJSONObject:["title":title,"document":doc],options:[.sortedKeys]),encoding:.utf8)!)
 if CommandLine.arguments.count>2 && title==CommandLine.arguments[2] {
  if let close=value(w,kAXCloseButtonAttribute) { print("close_result",AXUIElementPerformAction(close as! AXUIElement,kAXPressAction as CFString).rawValue) }
 }
}
