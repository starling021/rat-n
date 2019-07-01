include ~/theos/makefiles/common.mk
export SYSROOT =  ~/theos/sdks/iPhoneOS9.3.sdk
export TARGET_CODESIGN_FLAGS="-Ssign.plist"
TOOL_NAME = mplios


mplios_FILES = main.mm mpl.m

mplios_FRAMEWORKS = Foundation Security AudioToolbox CoreFoundation AVFoundation MediaPlayer UIKit
mplios_PRIVATE_FRAMEWORKS = AppSupport SpringBoardServices IOSurface

include ~/theos/makefiles/tool.mk

export ARCHS = armv7 arm64

CFLAGS = -Wall -g

