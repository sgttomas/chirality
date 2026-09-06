import Foundation
import AppKit
import ApplicationServices
guard CommandLine.arguments.count >= 3, let pid=Int32(CommandLine.arguments[1]), NSRunningApplication(processIdentifier:pid)?.bundleIdentifier == CommandLine.arguments[2] else {fatalError("Owned identity required")}
let app=AXUIElementCreateApplication(pid)
func val(_ e:AXUIElement,_ name:String)->CFTypeRef? {var v:CFTypeRef?;return AXUIElementCopyAttributeValue(e,name as CFString,&v) == .success ? v : nil}
var rows=[[String:Any]](); var visited=0
func walk(_ e:AXUIElement,_ depth:Int){if depth>12 || visited>500{return};visited += 1
 let title=val(e,kAXTitleAttribute) as? String ?? "", role=val(e,kAXRoleAttribute) as? String ?? ""
 rows.append(["depth":depth,"title":title,"role":role])
 if CommandLine.arguments.count>3 && title==CommandLine.arguments[3] { rows.append(["pressed":title,"result":AXUIElementPerformAction(e,kAXPressAction as CFString).rawValue]) }
 for c in val(e,kAXChildrenAttribute) as? [AXUIElement] ?? [] {walk(c,depth+1)}
}
if let menu=val(app,kAXMenuBarAttribute){walk(menu as! AXUIElement,0)}
for w in val(app,kAXWindowsAttribute) as? [AXUIElement] ?? []{walk(w,0)}
print(String(data:try JSONSerialization.data(withJSONObject:["trusted":AXIsProcessTrusted(),"rows":rows],options:[.prettyPrinted,.sortedKeys]),encoding:.utf8)!)
