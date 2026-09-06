import Foundation
import AppKit
import ApplicationServices
let name="Drop Fixture"
guard let finder=NSRunningApplication.runningApplications(withBundleIdentifier:"com.apple.finder").first else {fatalError("Finder absent")}
func val(_ e:AXUIElement,_ key:String)->CFTypeRef? {var v:CFTypeRef?;return AXUIElementCopyAttributeValue(e,key as CFString,&v) == .success ? v : nil}
let ax=AXUIElementCreateApplication(finder.processIdentifier)
let windows=val(ax,kAXWindowsAttribute) as? [AXUIElement] ?? []
guard let w=windows.first(where:{val($0,kAXTitleAttribute) as? String == name}) else {fatalError("Owned fixture window absent")}
func point(_ v:CFTypeRef?)->[Double]? {guard let v=v,CFGetTypeID(v)==AXValueGetTypeID() else{return nil};var p=CGPoint.zero;if AXValueGetValue(v as! AXValue,.cgPoint,&p){return [p.x,p.y]};return nil}
var rows=[[String:Any]]()
func walk(_ e:AXUIElement,_ depth:Int){if depth>10{return};let title=val(e,kAXTitleAttribute) as? String ?? "", desc=val(e,kAXDescriptionAttribute) as? String ?? "", value=val(e,kAXValueAttribute) as? String ?? "",role=val(e,kAXRoleAttribute) as? String ?? ""
// Only the known fixture window is traversed. It has no sidebar and only one inert folder.
var row:[String:Any]=["depth":depth,"role":role,"title":title,"description":desc,"value":value];row["position"]=point(val(e,kAXPositionAttribute));rows.append(row)
for c in val(e,kAXChildrenAttribute) as? [AXUIElement] ?? [] {walk(c,depth+1)}}
walk(w,0);print(String(data:try JSONSerialization.data(withJSONObject:rows,options:[.prettyPrinted,.sortedKeys]),encoding:.utf8)!)
