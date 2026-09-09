{
  "targets": [{
    "target_name": "chirality_native_admission",
    "sources": ["src/addon.cc"],
    "cflags_cc": ["-std=c++20"],
    "conditions": [["OS=='mac'", { "defines": ["CHIRALITY_DARWIN_ONLY=1"] }]]
  }]
}
