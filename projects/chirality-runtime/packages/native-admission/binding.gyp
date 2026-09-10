{
  "targets": [{
    "target_name": "chirality_native_admission",
    "sources": ["src/addon.cc"],
    "defines": ["NAPI_VERSION=6"],
    "cflags_cc": ["-std=c++20"],
    "conditions": [["OS=='mac'", {
      "defines": ["CHIRALITY_DARWIN_ONLY=1"],
      "xcode_settings": {
        "CLANG_CXX_LANGUAGE_STANDARD": "c++20",
        "MACOSX_DEPLOYMENT_TARGET": "15.0"
      }
    }]]
  }]
}
