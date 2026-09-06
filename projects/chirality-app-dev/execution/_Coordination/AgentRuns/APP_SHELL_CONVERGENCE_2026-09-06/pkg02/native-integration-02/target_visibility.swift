import Foundation
import AppKit
import CoreGraphics
let target=CGPoint(x:900,y:639)
let windows=CGWindowListCopyWindowInfo([.optionOnScreenOnly,.excludeDesktopElements],kCGNullWindowID) as? [[String:Any]] ?? []
let hit=windows.first { w in guard let b=w[kCGWindowBounds as String] as? [String:Double] else{return false};return (w[kCGWindowLayer as String] as? Int)==0 && CGRect(x:b["X"]!,y:b["Y"]!,width:b["Width"]!,height:b["Height"]!).contains(target) }
let owned:Int32=41768
print("frontmostIsOwned",NSWorkspace.shared.frontmostApplication?.processIdentifier==owned)
print("targetTopmostIsOwned",(hit?[kCGWindowOwnerPID as String] as? Int32)==owned)
print("targetTopmostIsFinder",(hit?[kCGWindowOwnerPID as String] as? Int32)==NSRunningApplication.runningApplications(withBundleIdentifier:"com.apple.finder").first?.processIdentifier)
