import Foundation
import AppKit
import ApplicationServices
let target="/private/tmp/chirality-native-shell-02gzaapq/Chirality Shell Evidence.app"
guard let dock=NSRunningApplication.runningApplications(withBundleIdentifier:"com.apple.dock").first else {fatalError("Dock absent")}
func val(_ e:AXUIElement,_ key:String)->CFTypeRef? {var v:CFTypeRef?;return AXUIElementCopyAttributeValue(e,key as CFString,&v) == .success ? v : nil}
let ax=AXUIElementCreateApplication(dock.processIdentifier)
func find(_ e:AXUIElement,_ depth:Int)->AXUIElement? {if depth>3{return nil};let raw=val(e,kAXURLAttribute);let url=(raw as? URL)?.path ?? (raw as? String).flatMap{URL(string:$0)?.path};if url == target{return e};for c in val(e,kAXChildrenAttribute) as? [AXUIElement] ?? [] {if let hit=find(c,depth+1){return hit}};return nil}
guard let item=find(ax,0) else {print("Exact owned Dock item not found by AXURL; no other item metadata emitted");exit(2)}
print("Matched exact owned Dock URL",target)
let status=AXUIElementPerformAction(item,"AXShowMenu" as CFString);print("showMenu",status.rawValue)
Thread.sleep(forTimeInterval:0.4)
var rows=[[String:String]]()
func read(_ e:AXUIElement,_ depth:Int){if depth>5{return};rows.append(["title":val(e,kAXTitleAttribute) as? String ?? "","role":val(e,kAXRoleAttribute) as? String ?? ""]);for c in val(e,kAXChildrenAttribute) as? [AXUIElement] ?? [] {read(c,depth+1)}}
// Menu is read only from the matched application's Dock element.
read(item,0);print(String(data:try JSONSerialization.data(withJSONObject:rows,options:[.prettyPrinted,.sortedKeys]),encoding:.utf8)!)
